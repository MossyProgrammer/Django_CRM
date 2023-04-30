from django.db import models

class assigned_record(models.Model):
    date_added = models.DateTimeField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 2)
    zip = models.CharField(max_length=10)
    assigned_to = models.CharField(max_length = 100)
    notes = models.TextField()
    
    def __str__(self):
        return(f"{self.first_name } {self.last_name}")

    