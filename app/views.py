from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.db.models import Q
from accounts.models import Customer
from app.models import Cart, OrderPlaced, Product

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

def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)

    item_already_in_cart=Cart.objects.filter(user=user,product=product).exists()
    if item_already_in_cart:                                                #if already item existe increse quantity
        c=Cart.objects.get(user=user,product=product)
        c.quantity+=1
        c.save()
    else:                                                                    #add product to cart
        c=Cart(user=user,product=product)
        c.save()
    return redirect('/cart')
def show_cart(request):
    user=request.user
    carts=Cart.objects.filter(user=user)
    amount=0
    shipping_price=40
    totalamount=0
    if carts:
        for item in carts:
            tempamount=item.product.discount_price*item.quantity
            amount+=tempamount
        totalamount=amount+shipping_price
    return render(request,'app/add_to_cart.html',{'carts':carts,'totalamount':totalamount,'amount':amount})

def plus_cart(request,pid):
    user=request.user
    cart=Cart.objects.get(user=user,id=pid)
    cart.quantity+=1
    cart.save()
    return redirect('show_cart')

def minus_cart(request,pid):
    user=request.user
    cart=Cart.objects.get(user=user,id=pid)
    if cart.quantity>1:
        cart.quantity-=1
        cart.save()
    else:
        cart.delete()
    return redirect('show_cart')

def remove_from_cart(request,pid):
    user=request.user
    item=Cart.objects.get(user=user,id=pid)
    item.delete()
    return redirect('show_cart')

def checkout(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_items=Cart.objects.filter(user=user)
    amount=0
    totalamount=0
    shipping_amount=0
    if cart_items:
        for p in cart_items:
            tempamount=p.product.discount_price*p.quantity
            amount+=tempamount
    totalamount=amount+shipping_amount
    return render(request,'app/checkout.html',{'add':add,'cart_items':cart_items,'amount':amount,'totalamount':totalamount})

def payment_gateway(request):
    customer_id=request.GET.get('custid')
    totalamount=request.GET.get('totalamount')
    cust_id=get_object_or_404(Customer,id=customer_id)
    # print(totalamount,cust_id.id)
    context={
        'totalamount':totalamount,
        'custid':cust_id.id
    }
    return render(request,'app/payment_gateway.html',context)

def orderplaced(request):
    user=request.user
    #get address
    customer_id=request.GET.get('custid')
    customer=get_object_or_404(Customer,id=customer_id)
    #get all cart items
    cart_items=Cart.objects.filter(user=user)
    print(user,customer_id)
    if cart_items:
        for c in cart_items:
            order=OrderPlaced(
                user=user,
                customer=customer,
                product=c.product,
                quantity=c.quantity,
                status='Accepted'
            )
            order.save()
            c.delete()
    return redirect('orders')

def orders(request):
    user=request.user
    order_placed=OrderPlaced.objects.filter(user=user)
    return render(request,'app/orders.html',{'order_placed':order_placed})
            