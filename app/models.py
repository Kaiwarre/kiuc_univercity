from django.db import models


class Education(models.Model):
    title = models.CharField(max_length=123)
    body = models.TextField()
    image = models.ImageField(upload_to='images/stat/')
    description = models.TextField()
    # skEditor .RichUploader

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey('Education', on_delete=models.CASCADE, related_name='edu_pages')
    body = models.TextField()
    # body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/stat/')

    def __str__(self):
        return f'{self.title}'


class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


