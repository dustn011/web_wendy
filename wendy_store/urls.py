from django.urls import path
from . import views


urlpatterns = [
    path('detail/<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
         ]

