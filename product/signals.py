from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from .models import Product
from khormaloo.settings import BASE_DIR
@receiver(pre_delete,sender=Product)
def delete_product_files(sender,instance,**kwargs):
    dir_img = os.path.join(BASE_DIR,instance.img.path)
    os.remove(dir_img)