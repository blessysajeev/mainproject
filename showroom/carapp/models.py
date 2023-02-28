from django.db import models

class Vehicles(models.Model):
    name=models.CharField(max_length=250,unique=True)
    #slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=True)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    image1=models.ImageField(upload_to='product',blank=True)
    image2=models.ImageField(upload_to='product',blank=True)
    image3=models.ImageField(upload_to='product',blank=True)
    image4=models.ImageField(upload_to='product',blank=True)
    image5=models.ImageField(upload_to='product',blank=True)
    image6=models.ImageField(upload_to='product',blank=True)
    #stock=models.CharField(max_length=250,default="null")
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='Vehicle'
        verbose_name_plural='Vehicles'

    def _str_(self):
        return '{}'.format(self.name)


class customer(models.Model):
    username = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100,unique=True)
    last_name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100, unique=True)
    Contact = models.BigIntegerField(default=0)
    password = models.CharField(max_length=250)
    
    class Meta:
        ordering=('username',)
        verbose_name='customer'
        verbose_name_plural='customers'

    def _str_(self):
        return '{}'.format(self.username)

class test_drive(models.Model):
   
    
    username = models.ForeignKey(customer, null=True, on_delete=models.CASCADE,related_name="name")
    venue = models.CharField(max_length=100,null=True)
    carmodel = models.CharField(max_length=100,null=True)
    Contact = models.BigIntegerField(default=0)
    Email = models.EmailField(max_length=100,unique=True)
    testdate = models.DateField(null=True, auto_now_add=False)
    testtime = models.TimeField(null=True, blank=True)


    class Meta:
        ordering=('carmodel',)
        verbose_name='test_drive'
        verbose_name_plural='test_drive'

    def _str_(self):
        return '{}'.format(self.carmodel)
    def __str__(self):
        return self.username.username
# Create your models here.
