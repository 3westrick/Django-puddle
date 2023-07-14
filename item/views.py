from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def show(request, pk):
    item = get_object_or_404(Item, pk=pk)
    items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    # items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk).exclude(user=request.user)[:3]
    return render(request, 'item/show.html', {'item': item, 'items': items})


@login_required
def create(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item:show', pk=item.id)
    form = NewItemForm()
    return render(request, 'item/form.html', {'form': form,
                                              'title': 'Create Item'})


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('item:show', pk=item.id)
    form = EditItemForm(instance=item)
    return render(request, 'item/form.html', {'form': form,
                                              'title': 'Edit Item'})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    item.delete()
    return redirect('dashboard:index')


def browse(request):
    # query = request.GET['search']
    search = request.GET.get('search', '')
    cat_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    if cat_id:
        items = items.filter(Q(category=cat_id))

    if search:
        # items = items.filter(name__contains=query)
        items = items.filter(Q(name__icontains=search) | Q(description__icontains=search))

    return render(request, 'item/items.html', {
        'items': items,
        'categories': categories,
        'query': search,
        'cat_id': int(cat_id),
    })
