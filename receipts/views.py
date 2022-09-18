from django.shortcuts import render
from .models import Product
from django.views.generic import CreateView
from django.views.generic import UpdateView
from receipts.forms import ProductForm
from django.urls import reverse_lazy

# Create your views here.

def receipts(request):
    context={
        'cont':'в целом страница основная'
    }
    return render(request,'receipts/index.html',context)

def receipts_in(request):
    context={
        'cont':'пишем сюда свои чеки или закидываем'
    }
    return render(request,'receipts/index.html',context)

def all_receipts(request):
    products_list=Product.objects.order_by('time_date')
    context={
        'cont':products_list
    }
    return render(request,'receipts/index.html',context)

def statistic(reques):

    context={
        'cont':'здесь выводим статистику'
    }
    return render(request,'receipts/index.html',context)


class ProductCreateView(CreateView):
    model = Product
    fields = ('short_name','full_name',  'amount',  'cost', 'category','id', 'shop', 'adress', 'time_date')
    success_url = reverse_lazy('test')
    success_message='Adde'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'receipts/product_update_form.html'