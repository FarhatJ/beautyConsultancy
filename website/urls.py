from django.urls import path
from . import views
from .views import BlogView, ArticleDetailView, CategoryView

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('appointment.html', views.appointment, name="appointment"),
    path('blog.html', BlogView.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('category/<str:cats>/', CategoryView, name="category"),
    # API to post a comment
    path('postComment', views.postComment, name="postComment"),

]
