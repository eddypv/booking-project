## Instalacion
- Crear el archivo .env en la carpeta booking_project con el siguiente contenido:

SECRET_KET = Una cadena secreta 

- Ejecutar el comando: 
```sh
pip install -r requirements.txt 
python manage.py migrate
python manage.py loaddata room_facility.json
python manage.py loaddata rooms.json
```
## Documentacion
### Autenticacion
La autenticacion es con Json Web Token utilizando el sistema de usuario de Django.

## Servicios
### Inicio de Sesion
Tiene que ser un usuario de Django.

**POST** http://127.0.0.1:8000/api/token/
```http
content-type: application/json

{
   "username":"",
   "password":""
}
```


