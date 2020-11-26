from django.contrib import admin

from .models import Post, Comments


class CommentsInlineAdmin(admin.StackedInline):
    model = Comments
    extra = 2
    fields = ['comment_text']


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'image', 'pub_date']
    inlines = [CommentsInlineAdmin]
    list_filter = ['pub_date']


admin.site.register(Post, PostAdmin)

