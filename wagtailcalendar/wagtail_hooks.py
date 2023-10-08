from django.urls import path
from wagtail import hooks
from .views import index
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from django.urls import reverse

@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('calendar/', index, name='calendar'),
    ]

@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    return MenuItem('Calendar', reverse('calendar'), icon_name='date')