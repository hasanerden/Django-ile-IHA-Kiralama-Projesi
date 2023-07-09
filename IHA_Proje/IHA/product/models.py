from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
     
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)    
     
    def get_unique_slug_cat(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug_cat()
        return super(Category, self).save(*args, **kwargs)  
    
    class Meta:
        ordering = ['-id'] 
     
    def __str__(self):
        return self.name
    
    
class Airvehicles(models.Model):
    brand = models.CharField(max_length=40,verbose_name="Marka")
    model = models.CharField(max_length=40,verbose_name="Model")
    weight = models.IntegerField(verbose_name="Ağırlık")
    image = models.ImageField(upload_to="iha",verbose_name="Resim Upload")
    description = RichTextField(verbose_name="Açıklama")
    is_active = models.BooleanField(default=False,verbose_name="Durum (Aktif/Pasif)")
    #slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False,verbose_name="Link")   
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False) 
    #slug = models.SlugField(unique=True, editable=False, max_length=130)
    category = models.ManyToManyField(Category,blank=True,verbose_name="Kategori")             #tablo ilişkisi -> çok ka çok
    #category = models.ForeignKey(Category,default=6,on_delete=models.CASCADE)                  #tablo ilişkisi -> bire çok   
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.brand)
    #     super().save(*args, **kwargs)  
    
    
    def get_unique_slug(self):
        marka=self.brand.replace('ı', 'i')
        vmodel=self.model.replace('ı', 'i')
        slug = slugify(marka + " " + vmodel)
        unique_slug = slug
        counter = 1
        while Airvehicles.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Airvehicles, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('iha_update', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('iha_delete', kwargs={'slug': self.slug})




    
    def __str__(self):
        return self.brand
