from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Education(models.Model):
    title = models.CharField(max_length=123)
    body = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='images/stat/')
    description = models.TextField()
    # skEditor .RichUploader

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey('Education', on_delete=models.CASCADE, related_name='edu_pages')
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/stat/')

    def __str__(self):
        return f'{self.title}'


class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    content = RichTextUploadingField(blank=True, null=True,verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True)
    exp = models.IntegerField(verbose_name='Опыт работы')
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/teacher/')

    def __str__(self):
        return self.full_name


class Ads(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название Объявления')
    description = models.TextField(blank=True, null= True, verbose_name='Описание')
    content = RichTextUploadingField(blank=True, null=True,verbose_name='Содержимое объявления')
    image = models.ImageField(upload_to='images/ads/')
    def __str__(self):
        return self.title

class Anons(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название Анонса')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/anons/')
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название курса')
    content = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/teacher/')

    def __str__(self):
        return self.title
