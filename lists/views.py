from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    items = request.session.get('items', [])

    if request.method == 'POST':
        new_item = request.POST.get('item_text', '')
        if new_item:
            items.append(new_item)
            request.session['items'] = items

    return render(request, 'home.html', {'items': items})
