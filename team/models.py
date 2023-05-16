from django.db import models

# Create your models here.
#THIS IS servises's model 
class service(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class whyus(models.Model):
    nomber=models.IntegerField()
    title=models.CharField(max_length=100)
    data=models.CharField(max_length=300)
    def __str__(self):
        return self.title
    
class Pricing(models.Model):
    title=models.CharField(max_length=100)
    pricing=models.IntegerField()
    def __str__(self):
        return self.title


class TextOffPricing(models.Model):
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    li = models.CharField(max_length=200)


class Team(models.Model):
    name_surname=models.CharField(max_length=200)
    speciality=models.CharField(max_length=200)
    img=models.ImageField(upload_to="media")
    def __str__(self):
        return self.name_surname
    

class Question(models.Model):
    question=models.CharField(max_length=1500)
    response=models.CharField(max_length=1200)

    def __str__(self):
        return self.question
    

    #portfolio 
class   Portfolio(models.Model):
    title=models.CharField(max_length=30)
    img=models.ImageField(upload_to='media')
    tip=models.CharField(max_length=100)
    def __str__(self):
        return self.title

