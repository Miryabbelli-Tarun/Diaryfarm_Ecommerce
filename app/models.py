from django.db import models
from django.contrib.auth.models import User

from accounts.models import Customer
# Create your models here.
category_choices=[
    ('Curd','Curd'),
    ('Milk','Milk'),
    ('Lassi','Lassi'),
    ('Milkshake','Milkshake'),
    ('Panner','Panner'),
    ('Ghee','Ghee'),
    ('Cheese','Cheese'),
    ('Ice-creams','Ice-creams')
]



class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=category_choices,max_length=10)
    product_image=models.ImageField(upload_to='products')

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __property__(self):
        return self.quantity * self.product.discount_price
