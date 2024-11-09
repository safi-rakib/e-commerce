from django.shortcuts import render,redirect
from item.models import Catagory,Item
from itertools import zip_longest
from .forms import SignupForm
def index(request):
    items = Item.objects.filter(is_sold=False)
    catagory = Catagory.objects.all()
    next_items = items[7:30]  # Adjust this slice as needed
    paired_list = list(zip_longest(*[iter(next_items)] * 2))  # Pairs of items
    return render(request, 'index.html', {
        'catagory': catagory,
        'items': items,
        'paired_list': paired_list,
    })
def shop(request):
    return render(request,'shop.html')
def blog(request):
    return  render(request,'blog-list-sidebar-left.html')
def faq(request):
    return  render(request,'faq.html')
def privacy_policy(request):
    return render(request,'privacy-policy.html')
def my_account(request):
    return  render(request,'my-account.html')
# def login(request):
#     return   render(request,'login.html')
def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    return render(request,'cart.html')
def empty_cart(request):
    return  render(request,'empty-cart.html')
def wishlist(request):
    return render(request,'wishlist.html')
def compare(request):
    return render(request,'compare.html')
def about_us(request):
    return render(request,'about-us.html')
def contact_us(request):
    return render(request,'contact-us.html')
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/login/')
    else:
        form =SignupForm()
    return render(request,'signup.html',{
        'form' : form
    })
    
