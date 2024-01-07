from django.urls import path
from NewApp import views


urlpatterns =[
    path('homepage/',views.homepage,name="homepage"),
    path('product_page/',views.product_page,name="product_page"),
    path('product_filtered/<cat_name>/',views.product_filtered,name="product_filtered"),
    path('product_single/<int:proid>/',views.product_single,name="product_single"),
    path('about_page/',views.about_page,name="about_page"),
    path('contactus_page/',views.contactus_page,name="contactus_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('register_page/',views.register_page,name="register_page"),
    path('register_save/',views.register_save,name="register_save"),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cartdelete/<int:pro_id>/',views.cartdelete,name="cartdelete"),
    path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
    path('save_checkout/',views.save_checkout,name="save_checkout"),
    path('yourorder/',views.yourorder,name="yourorder"),
    path('profile_page/<int:userid>/',views.profile_page,name="profile_page"),
    path('edit_pfdetails/<int:pro_id>/',views.edit_pfdetails,name="edit_pfdetails"),
    path('paymentpage/',views.paymentpage,name="paymentpage")

]