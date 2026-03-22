from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from accounts.forms import CustomerRegistrationForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import Customer
# Create your views here.
def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            # form.save() handles password hashing and database insertion
            form.save()
            messages.success(request, "Registration Successful! Welcome to our Dairy.")
            return redirect('customer_register') # Redirect to your login page
        

    else:
        form = CustomerRegistrationForm()
        
    return render(request, 'customer_register.html', {'form': form})

def customer_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if not user.exists():
            messages.warning(request,'User not Found')
            return redirect('customer_login')
        user=authenticate(username=username,password=password)
        if not user:
            messages.warning(request,"Invalid username or Password")
            return redirect('customer_login')
        login(request,user)
        return redirect('home')
    return render(request,'customer_login.html')

def customer_logout(request):
    logout(request)
    return redirect('customer_login')
@login_required(login_url='customer_login')
def profile(request):
    addresses=Customer.objects.filter(user=request.user)
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            mobile_no=form.cleaned_data['mobile_no']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']
            customer=Customer(user=user,name=name,locality=locality,mobile_no=mobile_no,city=city,state=state,pincode=pincode)
            customer.save()
            messages.success(request,'Address saved succesfully')
            return redirect('profile')
        else:
            messages.warning(request,"Invalid data")
            return redirect('profile')
    else:
        form=ProfileForm()
    
    return render(request,'profile.html',{'form':form,'addresses':addresses})

def edit_address(request,pk):
    address=get_object_or_404(Customer,pk=pk,user=request.user)
    form=ProfileForm(instance=address)
    if request.method=='POST':
        form=ProfileForm(request.POST,instance=address)
        if form.is_valid():
            form.save()
            messages.success(request,'Address update succesfully')
            return redirect('profile')
        else:
            messages.warning(request,'Invalid data to update address')

    return render(request,'edit_address.html',{'form':form})

def delete_address(request,pk):
    address=get_object_or_404(Customer,pk=pk,user=request.user)
    address.delete()
    messages.success(request,'Address Delete succesfully')
    return redirect('profile')

def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'password changed succesfully')
            return redirect('profile')
        else:
            messages.warning(request,'something wrong or incorrect password')
    else:
        form=PasswordChangeForm(request.user)
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})
    return render(request,'change_password.html',{'form':form})