from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=100)
    quantity=models.IntegerField()
    total_copies = models.PositiveIntegerField(default=0,blank=True,null=True)
    available_copies = models.PositiveIntegerField(default=0,blank=True,null=True)
    price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        default=0.00,
        blank=True,
        null=True
        )
    status = models.BooleanField(default=True,blank=True,null=True)
    publisher = models.CharField(max_length=150,blank=True,null=True)
    
    class Meta:
    
        db_table="Book_Details"
    
    def __str__(self):
        return self.title
    
class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(null=True,blank=False)
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default='librarian')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering=['email']
        db_table="Librarian_Information"

    def __str__(self):
        return self.email