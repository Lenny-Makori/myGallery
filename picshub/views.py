from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    image_display = Image.objects.all()


    return render(request, 'gallery/base.html', {"image_display": image_display})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"category": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})