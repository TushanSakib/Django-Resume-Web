from django.db import models

# Create your models here.

class About(models.Model):
    profile_img = models.ImageField(upload_to = 'upload/profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    career_obj = models.CharField(max_length=10000)
    facebook_link = models.CharField(max_length=100,null=True,blank=True)
    git_link = models.CharField(max_length=100,null=True,blank=True)
    linkedin_link = models.CharField(max_length=100,null=True,blank=True)
    twitter_link = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Education(models.Model):
    institute_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    passed_year = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.institute_name

class Interest(models.Model):
    description = models.TextField(max_length=20000)

class Reference(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    work_on = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Project(models.Model):
    title = models.CharField(max_length=100)
    github_link = models.CharField(max_length=1000)
    image = models.FileField(null=True,blank=True,upload_to='product/image/')

    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(Project,related_name='pro',on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='product/image/')
    



    
    


    

    
