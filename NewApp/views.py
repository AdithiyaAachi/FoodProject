import razorpay
from django.shortcuts import render,redirect
from NewApp.models import contactdb,RegisterDb,CartDb,Checkoutdb
from Backend.models import CategoryDb,ProductDb
from django.contrib import messages

# Create your views here.
def homepage(request):
    cat = CategoryDb.objects.all()
    if request.session.has_key('Username'):
        print("****************true" + request.session['Username'] +request.session['Password'])
        username = request.session['Username']
        pwd = request.session['Password']
        mydata = RegisterDb.objects.filter(Username=username,Password=pwd).values()[0]
        return render(request,"Home.html",{'cat':cat,'mydata':mydata})

    else:
        return render(request,"Home.html",{'cat':cat})


def product_page(request):
    pro = ProductDb.objects.all()
    return render(request,"Products.html",{'pro':pro})


def product_filtered(request,cat_name):
    data = ProductDb.objects.filter(Category_Name=cat_name)
    return render(request,"Products_Filtered.html",{'data':data})


def product_single(request,proid):
    data = ProductDb.objects.get(id=proid)
    return render(request,"SingleProduct.html",{'data':data})


def about_page(request):
    return render(request,"About.html")


def contactus_page(request):
    return render(request,"Contact.html")


def save_contact(request):
    if request.method=="POST":
        fna=request.POST.get('first_name')
        lna= request.POST.get('last_name')
        addr = request.POST.get('address')
        email= request.POST.get('email')
        city = request.POST.get('city')
        count = request.POST.get('country')
        tele = request.POST.get('tel')
        obj=contactdb(FirstName=fna,LastName=lna,Address=addr,EmailId=email,City=city,Country=count,Telephone=tele)
        obj.save()
        messages.success(request, "Contact save successfully....!")
        return redirect(contactus_page)


def register_page(request):
    return render(request,"Register.html")


def register_save(request):
    if request.method=="POST":
        na=request.POST.get('name')
        mob=request.POST.get('mobile')
        em=request.POST.get('email')
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        obj=RegisterDb(Name=na,Mobile=mob,Email=em,Username=un,Password=pwd)
        obj.save()
        messages.success(request, "Register save successfully....!")
        return redirect(register_page)


def UserLogin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if RegisterDb.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username'] = un
            request.session['Password'] = pwd
            messages.success(request, "Welcome")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password....!")
            return redirect(register_page)
    return redirect(register_page)


def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(register_page)


def cart_page(request):
    data = CartDb.objects.filter(UserName=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price+i.TotalPrice
    return render(request,"Cart.html",{'data':data, 'total_price':total_price})


def save_cart(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pname=request.POST.get('pname')
        quty= request.POST.get('quantity')
        tprice = request.POST.get('tprice')
        descp= request.POST.get('description')
        obj=CartDb(UserName=uname,ProductName=pname,Quantity=quty,TotalPrice=tprice,Description=descp)
        obj.save()
        messages.success(request, "Cart save successfully....!")
        return redirect(cart_page)


def cartdelete(request,pro_id):
    pro=CartDb.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request, "Delete successfully....!")
    return redirect(cart_page)


def checkoutpage(request):
    data = CartDb.objects.filter(UserName=request.session['Username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request,"Checkout.html",{'data':data,'total_price':total_price})


def save_checkout(request):
    if request.method=="POST":
        fn=request.POST.get('fname')
        ln= request.POST.get('lname')
        ema = request.POST.get('email')
        add = request.POST.get('addr')
        city = request.POST.get('city')
        count = request.POST.get('country')
        tel = request.POST.get('tele')
        obj=Checkoutdb(FirstName=fn,LastName=ln,EmailId=ema,Address=add,City=city,Country=count,Telephone=tel)
        obj.save()
        messages.success(request, "Checkout save successfully....!")
        return redirect(checkoutpage)


def yourorder(request):
    messages.success(request, "Place order has been success....!")
    return redirect(homepage)


def profile_page(request,userid):
    mydata = RegisterDb.objects.get(id=userid)
    return render(request,"Profile.html",{'mydata':mydata})


def edit_pfdetails(request,pro_id):
    data=RegisterDb.objects.get(id=pro_id)
    messages.success(request, "edit details successfully....!")
    return render(request,"Profile.html",{'data':data})


def paymentpage(request):
    if request.method == "GET":
        data = CartDb.objects.filter(UserName=request.session['Username'])
        amount = 0
        for i in data:
            amount = amount + i.TotalPrice
        order_currency="INR"
        client = razorpay.Client(auth=('rzp_test_W3mMQR6ikpp5sy','awCOQKU5dv7qZ8HXmymxqf96'))
        payment=client.order.create({'amount':amount*100,'currency':order_currency,'payment_capture':'1'})
        return render(
            request,
            "payment.html",
            {
                "razorpay_key": 'rzp_test_W3mMQR6ikpp5sy',
                "payment": payment,
            },
        )
    return render(request,"payment.html")
