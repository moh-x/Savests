from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import View
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.apps import apps

# from .forms import SendEmailForm
# from .actions import send_email

User = apps.get_model('users', 'User')


def email_page(request):
    if request.method == 'POST':
        email_body = request.POST.get('email')

        if email_body is not None:
            email_list_dict = list(User.objects.values(
                'email').filter(is_active=True))

            email_list = []

            for i in email_list_dict:
                email = i.get('email')
                email_list.append(email)

            send_mail('Subject goes here', email_body,
                      'no-reply@authapplication.com', email_list, fail_silently=False)
            return HttpResponse("Mail sent to: "+",".join(email_list))

    return render(request, 'admin/users/email_page.html')


# class SendEmailView(View):
#     template_name = 'users/user/send_email.html'
#     form_class = SendEmailForm
#     success_url = reverse_lazy('admin:users_user_changelist')

#     def form_valid(self, form):
#         users = form.cleaned_data['users']
#         subject = form.cleaned_data['subject']
#         message = form.cleaned_data['message']
#         sender = "admin@sv.ng"
#         print("hi")
#         send_mail(subject, message, sender, users)
#         user_message = '{0} users emailed successfully!'.format(
#             form.cleaned_data['users'].count())
#         message.success(self.request, user_message)
#         return super(SendEmailView, self).form_valid(form)


# def get(self, request, *args, **kwargs):
#     addresses = kwargs
#     context = {'addresses': addresses}
#     return render(request, self.template_name, context)

# def post(self, request, *args, **kwargs):

#     if form.is_valid():
#         return redirect('users/user/chang_list.html')

#     return render(request, self.template_name, context=self.get.context)
