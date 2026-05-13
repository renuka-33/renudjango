from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Product(models.Model):
    name = models.CharField(max_length=400)
    price = models.FloatField(max_length=10, default=0.0)
    image = models.ImageField(upload_to='products/', default='products/product-default.png')
    description=RichTextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, max_length=400)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={ 'pk' :self.pk, 'slug':self.slug})
    
    def save(self, *args,  **kwargs):
        value = self.name
        self.slug = slugify(value,allow_unicode=True)
        super().save(*args, **kwargs)

        def __str__(self):
            return '%s - %s' % (self.name, self.create_ats)

 
