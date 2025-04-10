from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  
    
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    ceated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-ceated_at']
    
    def __str__(self):
        return self.cars_count
      
    
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    model = models.CharField(max_length=100)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, null=True, blank=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.model
    