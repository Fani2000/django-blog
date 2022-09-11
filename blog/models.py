from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField( max_length=100)  
    last_name = models.CharField( max_length=100)  
    email_address = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption 
    


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField( max_length=200)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True) # Ensure that when you delete the author then the field is set to null
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.title} - {self.author}"

