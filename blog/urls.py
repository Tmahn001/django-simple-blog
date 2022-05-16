from . import views
from django.urls import path
from .views import ContactDetail

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('/contact', ContactDetail.as_view(), name='contact_detail')
] 
