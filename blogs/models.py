from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # In Django Admin panel change the name of Categorys to Categories 
    class Meta: 
        verbose_name_plural = 'categories'

# Display the names of the fields added to Categories 
# directly linked to displaying the navigation categories 
    def __str__(self):
        return self.category_name
    

STATUS_CHOICES = (
    ("Draft", "Draft"), 
    ("Published", "Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if the user gets deleted then the blog posts will also be deleted 
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Display the names of the fields added to Categories 
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    
class About(models.Model):
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading
    
class SocialLink(models.Model): 
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform
    
class MyWeb(models.Model): 
    myname = models.CharField(max_length=25)
    mylink = models.URLField(max_length=100)

    class Meta: 
        verbose_name_plural = 'My Website'

    def __str__(self):
        return self.myname