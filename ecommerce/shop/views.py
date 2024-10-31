from django.contrib.auth.models import  User
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Category,Product
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages



# Create your views here.

def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)

def allproducts(request,p):                  #here p recieves the category id
    c=Category.objects.get(id=p)             # create a particular category objects uesing id
    p=Product.objects.filter(category=c)     # reads all products under a particular category object
    context={'cat':c , 'product':p}

    return render(request,'product.html',context)


def detail(request,p):
    k=Product.objects.get(id=p)
    context={'pro':k}
    return render(request,'detail.html',context)


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return messages("Passwords are not same")
        return redirect('shop:login')

    return render(request,'register.html')


def user_login(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']


        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
             messages.error(request,"Invalid")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:categories')


def add_product(request):
    if (request.method=="POST"):
        n = request.POST['n']
        pr = request.POST['pr']
        s = request.POST['s']
        d = request.POST['d']
        category_id = request.POST.get('ca')
        c = request.FILES['c']

        category = get_object_or_404(Category, id=category_id)
        p=Product.objects.create(name=n,price=pr,stock=s,desc=d,category=category,image=c)
        p.save()
        return redirect('shop:addproduct')


    return render(request,"add_product.html")


def add_category(request):
    if (request.method == "POST"):
        na = request.POST['na']
        d = request.POST['d']
        c = request.FILES['c']

        c=Category.objects.create(name=na,desc=d,image=c)
        c.save()
        return redirect('shop:addcategory')


    return render(request,'add_category.html')

def add_stock(request,p):
    product=Product.objects.get(id=p)


    if(request.method=="POST"):
        Product.stock=request.POST['n']
        product.save()
        return redirect('shop:categories')
    context={'pro':product}
    return render(request,'add_stock.html',context)
