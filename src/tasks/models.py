from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=80, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Tasks(models.Model):

    title = models.CharField(max_length=100, verbose_name='Задача')
    description = models.TextField(blank=True, null=True, verbose_name='Детали')
    task_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title

