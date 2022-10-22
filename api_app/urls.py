from django.urls import path
from .views import Articles


urlpatterns = [
    path('article_details/', Articles.as_view()),
    path('article_details/<int:id>', Articles.as_view())

]
