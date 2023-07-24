from django.contrib import admin
from .models import Message,Cart,Product,Orders
# Register your models here.
admin.site.register(Message)
admin.site.register(Cart)
admin.site.register(Product)

admin.site.register(Orders)