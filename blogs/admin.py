from django.contrib import admin
from . models import Category, Blog, About, SocialLink, MyWeb, Comment

# pre generated slug from the title field
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # display in admin the categories 
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, requests):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
        

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
admin.site.register(MyWeb)
admin.site.register(Comment)

