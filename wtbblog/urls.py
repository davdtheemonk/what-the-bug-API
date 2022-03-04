from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("posts/",views.PostList.as_view()),
    path("posts/api/v1/",views.getDataJson),
    path("posts/<int:pk>",views.PostDetails.as_view()),
    path("post/search/<int:pk>",views.get_Data),
    path('modules/',views.ModuleList.as_view()),
    path("modules/<int:pk>",views.ModulePost.as_view())
    
    ]
