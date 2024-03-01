from django.urls import path
from root import views

urlpatterns = [
    path('', views.root_homepage, name='root_homepage'),
    path('signup', views.SignupView.as_view(), name='signup'),
]