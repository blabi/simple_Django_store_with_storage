from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from store_app.forms import AddCategoryModelForm, AddProductModelForm, SearchCategoryProductForm
from store_app.models import Category, Product, VAT


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request=request, template_name="categories.html", context={
            "categories": categories
        })


class CategoryView(View):
    def get(self, request, slug: str):
        category = Category.objects.get(slug=slug)
        products = Product.objects.filter(categories=category).order_by('name')
        return render(request, template_name="category.html", context={
            "products": products,
            "category": category,
        })


class ProductView(View):
    def get(self, request, product_id: int):
        product = Product.objects.get(pk=product_id)
        gross = (product.price * product.get_vat_display()) + product.price
        vat_disp = product.get_vat_display()*100
        return render(request, template_name="product.html", context={
            "product": product,
            'gross': gross,
            'vat_disp': vat_disp,
        })
        

class AddCategoryModelFormView(View):

    def get(self, request):
        form = AddCategoryModelForm()
        return render(request, 'addCategory.html', {"form": form})

    def post(self, request):
        form = AddCategoryModelForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('categories')
        return render(request, "addCategory.html", {'form': form})


class UpdateCategoryView(UpdateView):

    model = Category
    template_name = 'editCategory.html'
    form_class = AddCategoryModelForm
    success_url = reverse_lazy('categories')


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request=request, template_name="products.html", context={
            "products": products
        })


class AddProductModelFormView(View):

    def get(self, request):
        form = AddProductModelForm()
        return render(request, 'addProduct.html', {"form": form})

    def post(self, request):
        form = AddProductModelForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('products')
        return render(request, "addProduct.html", {'form': form, 'categories': categories_id})


class UpdateProductView(UpdateView):

    model = Product
    template_name = 'editProduct.html'
    form_class = AddProductModelForm
    success_url = reverse_lazy('products')


class SearchCategoryProductView(View):

    def get(self, request):
        form = SearchCategoryProductForm()
        return render(request, 'searchCategoriesProducts.html', {'form': form})

    def post(self, request):
        form = SearchCategoryProductForm(request.POST)
        if form.is_valid():
            category_product = form.cleaned_data['category_product']
            categories = Category.objects.filter(category_name__icontains=category_product).order_by('category_name')
            products = Product.objects.filter(name__icontains=category_product).order_by('name')

            return render(request, 'searchCategoriesProducts.html', {"categories": categories, "products": products, 'form':form})
        return render(request, 'searchCategoriesProducts.html', {'form': form})


class HomeView(View):
    
    def get(self, request):
        return render(request, template_name='home.html')
        