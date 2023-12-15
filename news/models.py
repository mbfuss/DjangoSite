from audioop import reverse
from django.db import models


class Articles(models.Model): 
    title = models.CharField('Название', max_length = 50) # max 250 символов
    anons = models.CharField('Анонс', max_length = 250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и время публикации')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})