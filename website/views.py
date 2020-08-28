from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Post, BlogComment

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email

        send_mail(
            'Message from ' + message_name,  # subject
            message,  # message
            message_email,  # from email
            ['makeawvish@gmail.com'],  # to email
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_email = request.POST['your-email']
        appointment_type = request.POST['appointment-type']
        appointment_date = request.POST['appointment-date']
        appointment_time = request.POST['appointment-time']
        your_phone = request.POST['your-phone']

        # send an email

        appointment = "Name: " + your_name + "\nEmail: " + your_email + "\nPhone: "\
                      + your_phone + "\nDate: " + appointment_date + "\nTime: " + appointment_time
        send_mail(
            'Appointment request for ' + appointment_type,  # subject
            appointment,  # message
            your_email,  # from email
            ['makeawvish@gmail.com'],  # to email
        )
        return render(request, 'appointment.html', {'your_name': your_name, 'your_mail': your_email,
                                                    'your_phone': your_phone,
                                                    'appointment_type': appointment_type,
                                                    'appointment_time': appointment_time,
                                                    'appointment_date': appointment_date})
    else:
        return render(request, 'home.html', {})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})


def postComment(request):
    if request.method == 'POST':
        user_email = request.POST['user-email']
        comment_text = request.POST['comment-text']
        return render(request, 'article_details.html', {'user_email':user_email, 'comment_text ':comment_text })


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


