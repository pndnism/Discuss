from django.contrib import admin

from .models import DiscussTheme, ThemeGenre

admin.site.register([DiscussTheme, ThemeGenre])