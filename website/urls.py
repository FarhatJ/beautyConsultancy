from django.urls import path
from . import views
from .views import BlogView, PostDetailView, category_detail

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('appointment.html', views.appointment, name="appointment"),
    path('blog.html', BlogView.as_view(), name="blog"),
    # path('results/$', search, name="search"),
    path('article/<int:pk>', PostDetailView.as_view(), name="article-detail"),
    path(r'^category-detail/(?P<slug>[-\w]+)/$', category_detail, name="category_detail"),
    # API to post a comment
    path('postComment', views.postComment, name="postComment"),

]
