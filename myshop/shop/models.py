from django.contrib.auth.models import User
from django.db import models



class TimeStampMixin(models.Model):
    """
    Класс-примесь, который добавляет моделям временные метки.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name="Обновлено")

    class Meta:
        abstract = True


class Products(TimeStampMixin, models.Model):
    name = models.CharField(verbose_name="Наименоваие", max_length=100)
    description = models.CharField(verbose_name="Описание", max_length=500)
    count = models.IntegerField(verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return str(self.name)


class Cart(TimeStampMixin, models.Model):
    product_id = models.ForeignKey(
        to=Products,
        verbose_name="Товар",
        on_delete=models.PROTECT,
        related_name="products",
    )
    user = models.ForeignKey(
        to=User,
        verbose_name="Пользователь",
        on_delete=models.PROTECT
    )
    count = models.IntegerField(verbose_name="Количество")
    status = models.CharField(verbose_name="Статус заказа", max_length=50)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
