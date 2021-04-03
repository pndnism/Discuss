from django.contrib import admin

from .models import DiscussSide, DiscussTheme, ThemeGenre

admin.site.register([DiscussTheme, ThemeGenre, DiscussSide])