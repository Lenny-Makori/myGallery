from django.contrib import admin
from .models import categories, location, Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('image_category',)

# Register your models here.
admin.site.register(categories)
admin.site.register(location)
admin.site.register(Image, ImageAdmin)
