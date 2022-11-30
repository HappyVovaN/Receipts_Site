from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from receipts.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('short_name','full_name',  'amount',  'cost', 'category','id', 'shop', 'adress', 'time_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save product'))

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()