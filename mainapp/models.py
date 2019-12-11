from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ['name']

    def __str__(self):
        return self.name

class ProductManufacturer(models.Model):
    name = models.CharField(verbose_name='Производитель', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    

    class Meta:
        verbose_name_plural = "Производители"
        verbose_name = "Производитель"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(ProductManufacturer, on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name='Товар', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)


    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
        ordering = ['category']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

