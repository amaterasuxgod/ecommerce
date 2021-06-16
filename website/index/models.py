from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from account.models import UserBase

class Category(MPTTModel):
    name = models.CharField(verbose_name=_("Category Name"),help_text=_('Required and unique'),max_length=255,unique=True)
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta: 
        order_insertion_by = ["name"]

    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    
    def get_absolute_url(self):
        return reverse("index:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(verbose_name=_("Product Name"), help_text=_("Required"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")
    
    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)


    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")
    

    def __str__(self):
        return self.name

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(verbose_name=_("title"), help_text=_("Required"), max_length=255)
    description = models.TextField(verbose_name=_("description"), help_text=_("Not required"), blank=True)
    product_is_featured = models.BooleanField(verbose_name='Product featured', default=False)
    slug = models.SlugField(max_length=255)
    is_available = models.BooleanField(verbose_name='Product availability', default=True)
    regular_price = models.FloatField(verbose_name=_("Regular price"), help_text=_("Максимально 10 цифр"))
    discount_price = models.FloatField(verbose_name=_("Discount price"), help_text=_("Максимально 10 цифр"))
    is_active = models.BooleanField(verbose_name=_("Product visibility"), help_text=_("Change product visibility"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now_add=True)
    

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    
    def get_absolute_url(self):
        return reverse("index:product_detail", args=[self.slug])
    
    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_spec")
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(verbose_name=_("value"), help_text=_("Product specification value (maximum of 1000 words)"), max_length=1000)

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

        def __str__(self):
            return self.value


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(verbose_name='image', help_text=_("Upload a product image"), default="images/keyboard.png", upload_to="images/")
    alt_text = models.CharField(verbose_name=_("Alturnative text"), help_text=_("Please add alturnative text"), max_length=255)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comment")
    user = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' % (self.product.title, self.user)    

