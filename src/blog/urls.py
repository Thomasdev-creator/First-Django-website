from django.urls import path
from .views import index, article

urlpatterns = [
    # On associe un chemi à notre vue dans views.py de blog
    path('', index, name="blog-index"),
    path('article-<str:numero_article>/', article, name="blog-article"),
]