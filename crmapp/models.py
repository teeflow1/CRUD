from django.db import models

class School(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    date_created = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    mobile = models.CharField(max_length=14)
    
    def __str(self):
        return (f"{self.first_name} {self.last_name}")
