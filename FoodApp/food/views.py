from django.shortcuts import render,redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
@login_required
def index(request):
    item_list=Item.objects.all()
    return render(request,'food/index.html',{'item_list':item_list})

# class IndexClassView(ListView):
#     model=Item
#     template_name='food/index.html'
#     context_object_name='item_list'
    

@login_required
def details(request,item_id):
    item=Item.objects.get(pk=item_id)
    return render(request,'food/detail.html',{"item":item})

# class FoodDetail(DetailView):
#      model=Item
#      template_name='food/detail.html'
    
def delete_item(request,item_id):
    item=Item.objects.get(pk=item_id)
    item.delete()
    return redirect('index')

@login_required
def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'food/create.html',{'form':form})

def update_item(request,item_id):
    item=Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'food/create.html',{'form':form})