from django.urls import path
from . import views
from .views import postDetails

app_name = "posts"

urlpatterns = [
    path('', views.postTest, name='posts'),
    path('<uuid:post_id>', postDetails, name='post-details'),
]