from django.db.models import query
from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, serializers, viewsets, request, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.filters import OrderingFilter
from django_filters import FilterSet, RangeFilter, CharFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.core.mail import send_mail
from tour.settings import EMAIL_HOST_USER
import locale
locale.setlocale(locale.LC_ALL, 'vi_VN')



class IsOwnerUserProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, user_obj):
        return user_obj.id == request.user.id

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user_obj):
        return user_obj.user_id == request.user.id

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView,generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'update':
            return [permissions.IsAuthenticated() and IsOwnerUserProfile()]
        
        return [permissions.AllowAny()]

class RegisterUserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = RegisterUserSerializer
    parser_classes = [MultiPartParser, ]

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


def filter_by_desid(queryset, name, value):
    values = value.split(',')
    return queryset.filter(destination__id__in=values)

def filter_by_cateid(queryset, name, value):
    values = value.split(',')
    return queryset.filter(category_tour__id__in=values)

class ToursFilterSet(FilterSet):
    price = RangeFilter()
    destination_ids = CharFilter(method=filter_by_desid)
    category_ids = CharFilter(method=filter_by_cateid)
   
    class Meta:
        model = Tours
        fields = {
            'destination__name': ['icontains'],
            'start_date': ['iexact'],
            'traffic': ['icontains']
        }


class ToursViewSet(viewsets.ViewSet, generics.ListAPIView,generics.UpdateAPIView):
    queryset = Tours.objects.filter(status=True).order_by('-date_add')
    serializer_class = ListToursSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    ordering_fields = ['price','views','date_add']
    filter_class = ToursFilterSet


class ToursDetailViewSet(viewsets.ViewSet, generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Tours.objects.filter(status=True)
    serializer_class = ToursDetailSerializer


class ListNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(status=True).order_by('-date_add')
    serializer_class = RecentNewsSerializer
    odering_fields = ['date_add','views']


class NewsDetailViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView):
    queryset = News.objects.filter(status=True)
    serializer_class = NewsSerializer


class CommentViewSet(viewsets.ModelViewSet,generics.RetrieveAPIView,generics.CreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentPostSerializer

    def create(self, request, *args, **kwargs):
        if request.data["user"] == request.user.id:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            return Response(status=403)

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated()]


class RatingViewSet(viewsets.ViewSet,generics.CreateAPIView,generics.DestroyAPIView,generics.UpdateAPIView):
    queryset = RatingTour.objects.all()
    serializer_class = RatingPostSerializer

    def create(self, request, *args, **kwargs):
        if request.data["user"] == request.user.id:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            return Response(status=403)

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated() and IsOwner()]


class LikeViewSet(viewsets.ViewSet,generics.RetrieveDestroyAPIView,generics.ListAPIView,generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePostSerializer

    def create(self, request, *args, **kwargs):
        if request.data["user"] == request.user.id:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            return Response(status=403)
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        
        return [permissions.IsAuthenticated() and IsOwner()]


class LocationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer


class CategoryTourViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = CategoryTour.objects.all()
    serializer_class = CategoryTourSerializer


class OrderTourViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = OrderTour.objects.all()
    serializer_class = OrderTourSerializer

    def create(self, request, *args, **kwargs):
        if request.data["user"] == request.user.id:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            return Response(status=403)

    def get_permissions(self):
        return [permissions.IsAuthenticated() and IsOwner()]


class RegisterTourViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = OrderTour.objects.all()
    serializer_class = RegisterTourSerializer

    def get_permissions(self):
        return [permissions.IsAuthenticated() and IsOwner()]


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsAdminUser])
def getSum(request):
    day = request.query_params.get('day')
    month = request.query_params.get('month')
    year_from = request.query_params.get('year_from')
    year_to = request.query_params.get('year_to')


    if day is not None and month is not None:
        query = OrderTour.objects.filter(date_add__day=day, date_add__month=month, date_add__year=year_from).aggregate(Sum('total'))['total__sum']
        results = query if query else 0
        return Response({'data':results})

    if day is None and month is None and year_to is None:
        results= {}
        for i in range(1,13):
            total = OrderTour.objects.filter(date_add__month=i, date_add__year=year_from).aggregate(Sum('total'))['total__sum']
            results[i] = total if total else 0
        return Response(results)

    if year_to is not None:
        results= {}
        for i in range(int(year_from),int(year_to) + 1):
            total = OrderTour.objects.filter(date_add__year=i).aggregate(Sum('total'))['total__sum']
            results[i] = total if total else 0
        return Response(results)

@api_view(['POST'])
def sendEmail(request):
    total = locale.currency(request.data['total'], grouping=True)
    msg = 'Chào {},\nBạn đã đặt thành công {} với {} người lớn và {} trẻ em, tổng cộng {}\nCảm ơn bạn đã tin tưởng và sử dụng dịch vụ của chúng tôi!'.format(request.data['user_name'],request.data['tour_name'],request.data['adult'],request.data['children'],total)
    send_mail("Hóa đơn đặt Tour", msg, EMAIL_HOST_USER, [request.data['email']], fail_silently=False)
    return Response({'msg':'mail sent'})