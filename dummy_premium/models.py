from django.db import models

class file(models.Model):
    documents = models.FileField() 
    aadhar = models.FileField()
    pencard = models.FileField()
    photo = models.FileField()   


# class dummy(models.Model):
#     dob=models.CharField(max_length=210)
#     tenure=models.IntegerField(default=0)
#     insurance_coverage=models.IntegerField()
#     mode = models.CharField(max_length=200)

    
# class company1(models.Model):
#     age = models.IntegerField(default=0,null=True)
#     tenure = models.IntegerField(blank=True,null=True)
#     value = models.FloatField(null=True)

# class company2(models.Model):
#     age = models.IntegerField(default=0,null=True)
#     tenure = models.IntegerField(blank=True,null=True)
#     value = models.FloatField(null=True)

# class company3(models.Model):
#     age = models.IntegerField(default=0,null=True)
#     tenure = models.IntegerField(blank=True,null=True)
#     value = models.FloatField(null=True)      

# class company4(models.Model):
#     age = models.IntegerField(default=0,null=True)
#     tenure = models.IntegerField(blank=True,null=True)
#     value = models.FloatField(null=True)     

       
   
