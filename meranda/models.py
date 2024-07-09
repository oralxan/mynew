from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category Name')
    description = models.TextField(verbose_name='Category Description')
    img = models.ImageField(upload_to='post/', verbose_name='Category Image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Healthy(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='healthies', verbose_name='Category')
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    hygiene = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Hygiene Tips')
    img = models.ImageField(upload_to='health_img/', verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Healthies'


class Sport(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sports', verbose_name='Category')
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    img = models.ImageField(upload_to='sports/', verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Sports'




class Design(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='designs', verbose_name='Category')
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    img = models.ImageField(upload_to='designs/', verbose_name='Image')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Designs'
