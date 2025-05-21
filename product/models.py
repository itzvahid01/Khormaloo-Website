from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    class ProductType(models.TextChoices):
        family = 'خانوادگی','خانوادگی'
        business = 'عمده' , 'عمده'
        discuobt = 'تخفیفی','تخفیفی'
    product_type = models.CharField(choices=ProductType,null=True,blank=True,default='family')
    price = models.IntegerField()
    weight = models.IntegerField()
    img = models.ImageField(upload_to='')
    def __str__(self):
        return f'{self.name} | {self.weight} گرم | {self.price}هزارتومان | {self.pk} کد'