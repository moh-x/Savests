from django.shortcuts import redirect, render

# from .forms import SendEmailForm


# sv004
def demote(modeladmin, request, queryset):
    queryset.update(level='J')


def promote(modeladmin, request, queryset):
    queryset.update(level='S')


# def send_email(modeladmin, request, queryset):
#     form = SendEmailForm(initial={'users': queryset})
#     return render(request, 'admin/users/send_email.html', {'form': form})


# names = ['Bob', 'Kieran', 'Wale', 'Joe', 'Sue', 'Millian',
#          'Ivan', 'Zoe', 'Dwayne', 'Esther', 'Jane', 'Peju', 'Tola', ]

# for i in range(0, 40):
#     User.objects.create_user(email=f"sv{i}@email.com",
#                              password='dinosaurs', username=f"svuser{i}",
#                              name=f"{names[random.randint(0, len(names)-1)]} {names[random.randint(0, len(names)-1)]}",
#                              date_joined=timezone.now() - timedelta(days=random.randint(0, 100)))
