from django.shortcuts import render

from .models import Item


def item(request, item_id):
    return render(request, "items/item.html", {"item": Item.objects.get(id=item_id)})
