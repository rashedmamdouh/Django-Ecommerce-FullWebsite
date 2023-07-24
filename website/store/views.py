from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth,User
from django.contrib import messages #dynmic messages
from .models import Message,Product,Cart,Orders

def home(request):
    user=request.user
    return render(request, 'index.html',{"user":user})

@login_required(login_url="signin")
def gallery(request):
    products=Product.objects.all()
    product_list=[]
    for product in products:
        product_list.append(product)
    print(product_list)
    return render(request, 'gallery.html',{"products":product_list})

def signup(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        username=request.POST["username"]
        password=request.POST["password"]
        user=User.objects.filter(username=username,password=password) 
        if user is None:
            user=User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname)
            user.save()  
            # Login the user Automaticlly
            user_login=auth.authenticate(username=username,password=password)
            auth.login(request,user_login)
            return redirect('home')
        else:
            messages.info(request,"User Exists")
    return render(request, 'sign_up.html')

def signin(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
             # Login the user Automaticlly
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid User")

            
    return render(request, 'sign_in.html')

@login_required(login_url="signin")
def signout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url="signin")
def about(request):
    return render(request,"about.html")

@login_required(login_url="signin")
def contact(request):
    if request.method=="POST":
        title=request.POST["title"]
        content=request.POST["content"]
        new_message=Message.objects.create(user=user,title=title,content=content)
        new_message.save()
    return render(request,"contact.html")

@login_required(login_url="signin")
def delete(request,product_id):
    product=Product.objects.get(id=product_id)
    cart=Cart.objects.get(product=product)
    cart.delete()
    return redirect('cart')  

def product(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request,"product.html",{"product":product})

def addToCart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(prod_id=product_id)
    except Cart.DoesNotExist:
        cart=None
    if cart is None:
        user=request.user
        new_cart=Cart.objects.create(user=user,product=product,quantity=1,prod_id=product_id)
        new_cart.save()
    else:
        cart.quantity=cart.quantity+1
        cart.save()
    return redirect("cart")

@login_required(login_url="signin")
def cart(request):
    user=request.user
    carts = Cart.objects.filter(user=user).all()
    products={}
    for cart in carts:
        products[cart.product]=cart.quantity
    if request.method=="POST":
        prod_id=request.POST.getlist("prod_id")
        quantity=request.POST.getlist("quantity")
        for i in range(len(prod_id)):
            cart=Cart.objects.get(prod_id=prod_id[i])
            cart.quantity=quantity[i]
            cart.save()
        return redirect("checkout")
    return render (request,"cart.html",{"products":products})


def checkout(request):
    user=request.user
    carts = Cart.objects.filter(user=user).all()
    products={}
    for cart in carts:
        products[cart.product]=cart.quantity
    if request.method=="POST":
        phone=request.POST['phone']
        adress=request.POST['address']
        for product,quantity in products.items():
            new_order=Orders.objects.create(adress=adress,phone=phone,user=user,product=product,quantity=quantity)
            new_order.save()
        for cart in carts:
            cart.delete()
        return redirect("GoodBye")
    return render (request,"checkout.html",{"products":products,"name":user.username})

def GoodBye(request):
    return render(request, "goodbye.html")





