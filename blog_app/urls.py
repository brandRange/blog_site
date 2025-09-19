from django.urls import path
from .views import post_list, post_details

urlpatterns = [
    path("",post_list, name="home"),
    path("post/<int:pk>/", post_details, name="post_detail")
]