from django.db import models

class Post(models.Model):
    title = models.CharField("Заголовок записи", max_length=50)
    content = models.TextField("Контент записи", max_length=2000)
    name = models.CharField("Имя пользователя", max_length=50)
    date = models.DateField("Дата публикации")
    img = models.ImageField("Изображение", upload_to='image/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title},{self.name}'