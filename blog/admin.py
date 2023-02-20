from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *
from . import models



# class CustomMPTTModelAdmin(MPTTModelAdmin):
#     # specify pixel amount for this ModelAdmin only:
#     mptt_level_indent = 50

admin.site.register(models.Category, MPTTModelAdmin)
# admin.site.register(models.Tag)
# admin.site.register(models.Post)
# admin.site.register(models.Recipe)
admin.site.register(models.Comment)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name')
#     prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'id')
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prep_time', 'cook_time', 'post')