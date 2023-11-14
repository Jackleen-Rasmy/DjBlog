from django.contrib import admin
from .models import Post, Category, Comments
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'tag_list']
    list_filter = ['title', 'category']
    search_fields = ['title']
    
    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    
    

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comments)


