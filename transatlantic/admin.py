from django.contrib import admin
from transatlantic.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'views')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'likes', 'views')
	

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
