from django.db import models
from django.contrib.auth import get_user_model
import uuid

User=get_user_model()  
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  #User (admin) FK
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    def __str__(self):
        return self.title

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    quantity=models.IntegerField()
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)  
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.IntegerField()
    prod_id=models.CharField(max_length=200)
    def __str__(self):
        return self.user.username

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    adress=models.CharField(max_length=300)
    quantity=models.IntegerField()
    phone=models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    order_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username