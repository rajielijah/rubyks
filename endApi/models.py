from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  
from  django.db.models.signals import post_save
import uuid



GENDER_CHOICES  = (
       ('M', 'Male'),
       ('F', 'Female')
   )

CATEGORY = (
    ('fashion', 'Fashion'),
    ('electronics', 'Electronics'),
    ('furniture', 'Furniture')
)



class Post(models.Model):
    product_name = models.CharField(max_length=200)
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    product_description = models.CharField(max_length=400)
    category  = models.CharField(max_length=190, choices=CATEGORY)
    product_details = models.TextField()
    price = models.CharField(max_length=100) 
    posted_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'feedupload', null=True, blank=True)
    id =  models.UUIDField(default=uuid.uuid4, blank=False, primary_key=True)


    def __str__(self):
        return self.product_name


class Profile(models.Model):
    avatar = models.ImageField(null=False)
    company_name = models.CharField(max_length=100)
    name  = models.CharField(max_length=300)
    phone  = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=11)
    location  = models.CharField(max_length=40)
    state = models.CharField (max_length=200)
    email  = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined  = models.DateTimeField(auto_now_add=True)
    bio  = models.CharField(max_length=300, null=True, blank=False)
    gender  = models.CharField(max_length=10, choices=GENDER_CHOICES)
    id =  models.UUIDField(default=uuid.uuid4, blank=False, primary_key=True)
    
    def __str__(self):
        return self.name
    

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()