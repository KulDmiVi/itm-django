from django.db import models


class TimeStampMixin(models.Model):
    """
    Класс-примесь, который добавляет моделям временные метки.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name="Обновлено")
    class Meta:
        abstract = True


class Clients(TimeStampMixin, models.Model):
    name = models.CharField(verbose_name="Имя", max_length=500)
    address = models.CharField(verbose_name="Адрес", max_length=500)
    phone = models.CharField(verbose_name="Контактный телефон", max_length=50)

    def __str__(self):
        return str(self.name)


class Products(TimeStampMixin, models.Model):
    name = models.CharField(verbose_name="Наименоваие", max_length=100)
    description = models.CharField(verbose_name="Описание", max_length=500)
    count = models.CharField(verbose_name="Количество", max_length=50)
    def __str__(self):
        return str(self.name)


