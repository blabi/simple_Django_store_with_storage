from django import forms
from django.core.exceptions import ValidationError

from store_app.models import Category, Product


class AddCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'slug']
        
        labels = {
            'category_name': 'Nazwa kategorii'
        }


class AddProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['categories']
        
        labels = {'name': 'Nazwa produktu',
            'description': 'Opis',
            'price': 'Cena',
            'stock': 'Stan',
            'categories': 'Kategorie',
            }


class SearchCategoryProductForm(forms.Form):
    category_product = forms.CharField()

