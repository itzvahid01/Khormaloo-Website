from django.shortcuts import render
from product.models import *
# Create your views here.
def home(request):
    discount = Product.objects.filter(product_type='تخفیفی')
    home = Product.objects.filter(product_type='خانوادگی')
    company = Product.objects.filter(product_type='عمده')
    context = {'discount' : discount,'home':home,'company':company}
    return render(request,'home.html',context)