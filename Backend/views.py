from django.shortcuts import render,redirect
from Backend.models import CategoryDb,ProductDb
from NewApp.models import contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def indexpage(request):
    return render(request,"Index.html")
def categorypage(request):
    return render(request,"Add Category.html")
def save_category(request):
    if request.method=="POST":
        cn=request.POST.get('cname')
        des= request.POST.get('desriptn')
        img=request.FILES['image']
        obj=CategoryDb(CategoryName=cn,Description=des,CategoryImage=img)
        obj.save()
        messages.success(request, "Category save successfully....!")
        return redirect(categorypage)

def display_category(request):
    data=CategoryDb.objects.all()
    return render(request,"Display Category.html",{'data':data})
def edit_category(request,cat_id):
    category=CategoryDb.objects.get(id=cat_id)
    return render(request,"Edit Category.html",{'category':category})
def update_category(request,dataid):
    if request.method=="POST":
        cna=request.POST.get('cname')
        desc= request.POST.get('desriptn')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=dataid).CategoryImage
        CategoryDb.objects.filter(id=dataid).update(CategoryName=cna,Description=desc,CategoryImage=file)
        messages.success(request, "Product update successfully....!")
        return redirect(display_category)
def remv_category(request,dataid):
    rem=CategoryDb.objects.filter(id=dataid)
    rem.delete()
    messages.success(request, "Category remove successfully....!")
    return redirect(display_category)
def productpage(request):
    category=CategoryDb.objects.all()
    return render(request,"Add Product.html",{'category':category})
def save_product(request):
    if request.method=="POST":
        na=request.POST.get('cat')
        pna= request.POST.get('pname')
        des= request.POST.get('description')
        price= request.POST.get('price')
        imge=request.FILES['pimage']
        obj=ProductDb(Category_Name=na,ProductName=pna,Description=des,Price=price,ProductImage=imge)
        obj.save()
        messages.success(request, "Product save successfully....!")
        return redirect(productpage)
def display_products(request):
    pro=ProductDb.objects.all()
    return render(request,"Display Product.html",{'pro':pro})
def edit_product(request,pro_id):
    cat=CategoryDb.objects.all()
    product=ProductDb.objects.get(id=pro_id)
    messages.success(request, "Product edit successfully....!")
    return render(request,"Edit Product.html",{'cat':cat,'product':product})
def Update_product(request,dataid):
    if request.method == "POST":
        cna= request.POST.get('cat')
        pn= request.POST.get('pname')
        des = request.POST.get('desriptn')
        price= request.POST.get('price')
        try:
            img = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=dataid).ProductImage
        ProductDb.objects.filter(id=dataid).update(Category_Name=cna,ProductName=pn,Description=des,Price=price,ProductImage=file)
        messages.success(request, "Update product successfully....!")
        return redirect(display_products)
def rem_product(request,dataid):
    rem = ProductDb.objects.filter(id=dataid)
    rem.delete()
    messages.success(request, "Remove product successfully....!")
    return redirect(display_products)
def adminlogin(request):
    return render(request,"AdminLogin.html")
def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(indexpage)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully....!")
    return redirect(adminlogin)

def display_contact(request):
    data = contactdb.objects.all()
    messages.success(request, "Display contact successfully....!")
    return render(request,"Display Contact.html",{'data':data})
def delete_contact(request,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_contact)