from django.urls import path

# from users.views import SendEmailView
from . import views

app_name = 'users'
urlpatterns = [
    path('email_page/', views.email_page, name='email_page')
    # path('email/', SendEmailView.as_view(), name='email'),
]
