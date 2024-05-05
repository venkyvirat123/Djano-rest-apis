from  django.urls import path
from . import views

urlpatterns=[
    path("blogpost/",views.listcreateserializer.as_view()),
    path("getdetails/<int:pk>/",views.RetrieveBlogView.as_view()),
    path("getlist",views.ListBlogView.as_view()),
    path("delete/<int:pk>",views.DeleteViewBlog.as_view())
]