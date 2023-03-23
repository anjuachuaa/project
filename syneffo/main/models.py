from django.db import models

# Create your models here.
class department(models.Model):
    dep_name=models.CharField(max_length=255)
    def __str(self):
        return self.dep_name
    


class batch(models.Model):
    batch_time=models.IntegerField()
    def __str(self):
        return self.batch_time
    

class student(models.Model):
    std_time=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dep=models.ForeignKey(department,default=0,on_delete=models.CASCADE)
    

    
    