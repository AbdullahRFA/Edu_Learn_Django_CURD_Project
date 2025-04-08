# Course_app/apps.py

from django.apps import AppConfig

class CourseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Course_app'

    def ready(self):
        import Course_app.signals  # ✅ Import signals here