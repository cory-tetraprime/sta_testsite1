from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inside', views.inside, name='inside'),
    path('blog/<int:year>/<int:month>/<slug:slug>/', views.blog, name='blog')
]