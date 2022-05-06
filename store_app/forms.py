from django import forms
from django.core.exceptions import ValidationError

from store_app.models import Category, Product


class AddCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'slug']


class AddProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['categories']


class SearchCategoryProductForm(forms.Form):
    category_product = forms.CharField()

