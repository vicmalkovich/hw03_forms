from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('detail/<int:pk>/', views.details, name='detail'),
    path('<str:username>/<int:id>/', views.article, name='article'),
    path('group/<str:slug>/', views.group_posts),
    path('new/', views.new_post),
]
