from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item


def index(request):
    query = request.GET.get('query', '')
    sort_by = request.GET.get('sort_by', 'id')
    items = Item.objects.filter(name__icontains=query).order_by(sort_by)
    return render(request, 'index.html', {'items': items})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()

    return render(request, 'CRUD_app/add_item.html', {'form': form})





def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Updated this line
    else:
        form = ItemForm(instance=item)

    return render(request, 'CRUD_app/edit_item.html', {'form': form, 'item': item})



def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('index')

def item_list(request):
    sort_by = request.GET.get('sort_by', 'id')  
    keyword = request.GET.get('keyword', '')  
    
    items = Item.objects.all().order_by(sort_by)
    
    if keyword.isdigit():
        items = items.filter(id=keyword)
    elif keyword:
        items = items.filter(name__icontains=keyword)

    return render(request, 'CRUD_app/item_list.html', {'items': items})



def remove_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('item_list')




