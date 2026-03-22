from django.db import models
from django.contrib.auth.models import User
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

    