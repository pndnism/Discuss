from django.contrib import admin

from .models import DiscussSide, DiscussTheme, ThemeGenre, User, DiscussionComment

admin.site.register([DiscussTheme, ThemeGenre, DiscussSide, User, DiscussionComment])