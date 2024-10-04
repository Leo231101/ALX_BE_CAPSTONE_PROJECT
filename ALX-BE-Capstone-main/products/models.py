from django.db import models

# Model representing a product category
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    # String representation of the category (for admin interface or debugging)
    def __str__(self):
        return self.name

# Model representing a product
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    # String representation of the category (for admin interface or debugging)
    def __str__(self):
        return self.name

# Model representing a product image
class ProductImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
