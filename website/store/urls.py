from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("home",views.home,name="home"),
    path("gallery",views.gallery,name="gallery"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("cart",views.cart,name="cart"),
    path("product/<str:product_id>",views.product,name="product"),
    path("delete/<str:product_id>",views.delete,name="delete"),
    path("cart/<str:product_id>",views.addToCart,name="addToCart"),
    path("checkout",views.checkout,name="checkout"),
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("signout",views.signout,name="signout"),
    path("goodbye",views.GoodBye,name="GoodBye"),
]
