# M7-L4-ClavesPrimariasCRUD-Parte2
Educativo y de Aprendizaje Personal

---
## Tabla de Contenidos
- [Tecnologías](#Tecnologías)
- [Configuración Inicial](#configuración-Inicial)
- [Creación del Modelo](#creación-del-modelo)
- [Creación de Vistas](#creación-de-vistas)

---
# Tecnologías
- Django: Framework web en Python.
- SQLite:
--- 
# Configuración Inicial 
1. Entorno virtual 
    ```bash 
    python -m venv venv

2. Activar el entorno virtual
    ```bash 
    venv\Scripts\activate

3. Instalar Django
    ```bash 
    pip install django 
    pip install djangorestframework==3.15.2
    pip install drf-spectacular==0.28.0
    
4. Actulizamos el pip 
    ```bash
    python.exe -m pip install --upgrade pip

5. Crear el proyecto de django crud
    ```bash 
    django-admin startproject crud

6. Guardamos dependencias
    ```bash
    pip freeze > requirements.txt

7. Ingresamos al proyecto 
    ```bash 
    cd crud

9. Creamos la aplicacion llamada app1, app2, docs
    ```bash     
    python manage.py startapp app1
    python manage.py startapp app2
    python manage.py startapp docs

10. Configuración de crud/settings.py 
    ```bash 
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'app1',
    'app2',
    'docs',
    ]
    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }

11. Hacemos las migraciones correspondientes
    ```bash
    python manage.py makemigrations
    python manage.py migrate




# Creación del Modelo 

14. en app1/models.py
    ```bash
   from django.db import models

    class Author(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)

        def __str__(self):
            return f"{self.first_name} {self.last_name}"

15. Creamos el serializer.py en app1/serializer.py
    ```bash
    from rest_framework import serializers
    from .models import Author

    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = '__all__'

16. app2/views.py
    ```bash
    from rest_framework import viewsets
    from .models import Author
    from .serializers import AuthorSerializer

    # Create your views here.
    class AuthorViewSet(viewsets.ModelViewSet):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer

17. en app2/models.py
    ```bash
    from django.db import models
    from app1.models import Author

    class Book(models.Model):
        title = models.CharField(max_length=200)
        publication_date = models.DateField()
        author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

        def __str__(self):
            return self.title

18. app2/serializers.py
    ```bash
    from rest_framework import serializers
    from .models import Book

    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = '__all__'
19. app2/views.py
    ```bash 
    from rest_framework import viewsets
    from .models import Book
    from .serializers import BookSerializer

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

20. docs/urls.py
    ```bash 
    from django.urls import path
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

    # Definición de las rutas para la generación y visualización de la documentación de la API
    urlpatterns = [
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
21. Ejecuta las migraciones para aplicar estos cambios a la base de datos:
    ```bash 
    python manage.py makemigrations
    python manage.py migrate

22. Navegar en las rutas http://127.0.0.1:8000/api/redoc/   http://127.0.0.1:8000/api/swagger-ui/  http://127.0.0.1:8000/api/schema/ este último descarga un archivo