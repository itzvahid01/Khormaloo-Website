from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
    def ready(self):
        # اطمینان حاصل کنید که سیگنال‌ها هنگام لود اپ ثبت می‌شوند
        import product.signals  # جایگزین your_app با نام اپ خود