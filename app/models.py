from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    """Model to represent course categories."""
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    """Model to represent subcategories under a category."""
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='subcategories'
    )

    class Meta:
        verbose_name_plural = "SubCategories"
        unique_together = ('name', 'category')  # Ensures uniqueness within a category

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Course(models.Model):
    """Model to represent a course."""
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='courses'
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses'
    )
    image = models.ImageField(
        upload_to='courses/images/', 
        blank=True, 
        null=True
    )
    tutor_name = models.CharField(max_length=255)
    description = CKEditor5Field(config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
