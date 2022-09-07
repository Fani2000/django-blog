from django.contrib import admin
from .models import Post,Author,Tag

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name","first_name","email_address"
    )
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('caption', )
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', )
    list_filter = ("author", 'tags', "date")
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)