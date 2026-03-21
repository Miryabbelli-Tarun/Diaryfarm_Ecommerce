from django.shortcuts import get_object_or_404, render
from django.views import View

from app.models import Product

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

class CategoryView(View):
    def get(self,request,val):
        products=Product.objects.filter(category=val)
        return render(request,'app/category.html',locals())

def product_details(request,pk):
    product=get_object_or_404(Product,pk=pk)
    context={
        'product':product
    }
    return render(request,'app/product_details.html',context)


