# Instalacion
1. Ejecutar el comando: pip install -r requirements.txt 
2. Crear el archivo .env en la carpeta booking_project con el siguiente contenido:
SECRET_KET = Una cadena ramdom
3. Ejecutar la migracion para crear los modelos: python manage.py migrate
4. Cargar los datos iniciales:
    python manage.py loaddata room_facility.json

