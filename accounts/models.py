from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User , related_name = 'customer' , null = True , blank = True , on_delete = models.CASCADE)
    name = models.CharField(max_length=100 , null = True)
    phone = models.CharField(max_length=100 , null = True)
    email = models.CharField(max_length=100 , null = True)
    profile_pic = models.ImageField(default = "fiat.png " ,null = True , blank = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    
class Category(models.Model):
    category_name = models.CharField(max_length=100 , null = True)
    price_per_day = models.FloatField(max_length=10 , null = True)
    occupant_amount = models.CharField(max_length=100 , null = True)
    baggage_amount = models.CharField(max_length=100 , null = True)
    driver_age = models.FloatField(max_length=10 , null = True)
    Power = models.FloatField(max_length=10 , null = True)
    door_amount = models.FloatField(max_length=10 , null = True)
    acriss_code = models.CharField(max_length=100 , null = True)

    def __str__(self):
        return self.category_name

    


class Car(models.Model):
   
    name = models.CharField(max_length=100 , null = True)
    category = models.ForeignKey(Category , null=True, on_delete = models.SET_NULL )
    model_year = models.CharField(max_length=100 , null = True)
    description = models.CharField(max_length=100 , null = True , blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(null = True , blank = True)
    

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class City(models.Model):
    name = models.CharField(max_length=100 , null = True)

    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=100 , null = True)
    street = models.CharField(max_length=100 , null = True)
    post_code = models.CharField(max_length=100 , null = True)
    image = models.ImageField(null = True , blank = True)
    phone = models.CharField(max_length=100 , null = True)
    email = models.CharField(max_length=100 , null = True)
    link = models.URLField(max_length=200, null = True)
    city = models.ForeignKey(City , on_delete = models.CASCADE)

    def __str__(self):
        return self.name 

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Protection(models.Model):
    name = models.CharField(max_length = 100, null = True)
    price = models.FloatField(max_length=10 , null = True)
    description = models.CharField(max_length = 999, null = True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer = models.ForeignKey(Customer , null=True, on_delete = models.SET_NULL )
    car = models.ForeignKey(Car , null=True, on_delete = models.SET_NULL )

    city = models.ForeignKey(City , on_delete = models.CASCADE , related_name = "pickup_city")
    station = models.ForeignKey(Station , on_delete = models.CASCADE , related_name = "pickup_station")
    pickup_date = models.DateTimeField (null = True )
    
    

    city1 = models.ForeignKey(City , on_delete = models.CASCADE , related_name = "return_city" )
    station1 = models.ForeignKey(Station , on_delete = models.CASCADE , related_name = "return_station" )
    dropoff_date = models.DateTimeField (null = True )

    protection = models.ForeignKey(Protection , null=True, blank = False , on_delete = models.CASCADE )
   
    
    def __str__(self):
        return self.car.name

    def get_price(self):
        if (self.dropoff_date - self.pickup_date).days<1:
            return self.car.category.price_per_day + self.protection.price
        else:
            return (self.dropoff_date - self.pickup_date).days * (self.car.category.price_per_day) + (self.dropoff_date - self.pickup_date).days * (self.protection.price)
            