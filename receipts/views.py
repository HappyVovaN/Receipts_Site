from django.shortcuts import render
from .models import Product
from django.views.generic import CreateView, UpdateView, ListView
from receipts.forms import ProductForm
from django.urls import reverse_lazy
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

# Create your views here.
from .handle_receipts import handle_uploaded_file

def receipts(request):
    context = {
        'cont': 'в целом страница основная'
    }
    return render(request, 'receipts/index.html', context)


def receipts_in(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('templates/receipts/upload.html')
    else:
        form = UploadFileForm()
    return render(request, 'receipts/upload.html', {'form': form})


def all_receipts(request):
    products_list = Product.objects.order_by('time_date')
    context = {
        'cont': products_list
    }
    return render(request, 'receipts/index.html', context)


def statistic(request):
    context = {
        'cont': 'здесь выводим статистику'
    }
    return render(request, 'receipts/index.html', context)


class Products_ALL(ListView):
    model = Product
    template_name = 'receipts/product_list.html'

    def get_context_data(self, **kwargs):
        mydata = Product.objects.all().values()
        context = {'products': mydata, 'name': 'All products'}
        print(context)
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ('short_name', 'full_name', 'amount', 'cost', 'category', 'id', 'shop', 'adress', 'time_date')
    success_url = reverse_lazy('')
    success_message = 'Added'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'receipts/product_update_form.html'
