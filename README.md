# booking-tour-django

use `python manage.py runserver` to run server at http://127.0.0.1:8000/

## Basic CRUD API
### Get all tour
METHOD `GET` - URL `/api/tour/`

### Get all news
METHOD `GET` - URL `/api/news/`

### Crate new review of tour
METHOD `POST` - URL `/api/review/` - Param: `{"user": id_user, "content": "text of content", "tour": id_tour}`

### Add like from user 
METHOD `POST` - URL `/api/like/` - Param: `{"user": id_user, "news": id_news}`

### Create new comment from user 
METHOD `POST` - URL `/api/comment/` - Param: `{"user": id_user, "content": "text of content", "news": id_news}`

### Add rating for tour 
METHOD `POST` - URL `/api/rating/` - Param: `{"user": id_user, "star": number_of_star, "tour": id_tour}`

### Get list comment of 1 news
METHOD `GET` - URL `/api/all-comment/<id_news>`

### Get list like of 1 news
METHOD `GET` - URL `/api/all-like/<id_news>`

### Get list review of 1 tour
METHOD `GET` - URL `/api/all-review/<id_tour>`

### Get list rating of 1 tour
METHOD `GET` - URL `/api/all-rating/<id_tour>`
