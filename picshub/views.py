from django.shortcuts import render
from .models import Image, categories, location

# Create your views here.
def index(request):
    image_display = Image.objects.all()


    return render(request, 'gallery/image_view.html', {"image_display": image_display})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"category": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})

def categories(request, category_id):
    category_pictures = categories.objects.get(id=category_id)
    category_images = Image.objects.get(category=category_pictures)

    return render(request, 'gallery/category.html',{"category_images": category_images})

def filter_location(request,image_id):
    try:
        location = location.get_location()
        location_photos = Image.objects.filter(location=image_id)
    except DoesNotExist:
        raise Http404()
        return render(request,'photos/photos_detail.html',{"located_photos":located_photos,"locations":location})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gallery/image.html", {"image":image})