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
Tiene que ser un usuario de Django, genera el token para el usuario.

**POST** http://127.0.0.1:8000/api/token/
```http
content-type: application/json

{
   "username":"",
   "password":""
}
```
### Buscar habitaciones
Realizar busqueda de habitaciones disponibles de acuerdo a un rango de fechas y cantidad de personas que se hospedaran. El formato de fecha es dd-mm-yyyy

**GET** http://127.0.0.1:8000/api/booking/search_rooms/?start_date/?end_date/?guests

Respuesta:

```json
{
  "data": [
    {
      "id": 1,
      "title": "Habitacion Individual",
      "description": "Esta habitación individual dispone de aire acondicionado, minibar y zona de estar.",
      "guests": 1,
      "beds": 1,
      "toilets": 1,
      "cost_per_night": 30.0,
      "facilities": [
        {
          "cod_facility": "aire-acon",
          "facility": "Aire acondicionado"
        },
        {
          "cod_facility": "balcon",
          "facility": "Balcon"
        },
        {
          "cod_facility": "bano-n",
          "facility": "Baño Normal"
        },
        {
          "cod_facility": "minibar",
          "facility": "Minibar"
        }
      ]
    }
  ],
  "error": null
}
```

### Realizar reserva 
Realiza la reserva de una habitacion

Peticion:

**POST** http://127.0.0.1:8000/api/booking/
```http
Authorization: Bearer <token>
content-type: application/json

{
    "start_date":"01-01-2022", //formato dd-mm-yyyy
    "end_date":"30-01-2022", //formato dd-mm-yyyy
    "guests":1,
    "room_id":2,
    "amount_paid":0,
    "state":"PEN",
    "payment_method":"EFEC"
}
```

### Registrar Factura 
Registro de la factura de la reserva

Peticion:

**POST** http://127.0.0.1:8000/api/invoice/
```http
Authorization: Bearer <token>
content-type: application/json

{
    "amount":154.23,
    "name":"Juan Perez",
    "nit":"1545454",
    "booking_id":2 // identificador de Reserva
}
```
### Obtener reserva 
**GET** http://127.0.0.1:8000/api/booking/?booking_id/

### Obtener reserva 
**GET** http://127.0.0.1:8000/api/invoice/?invoice_id/


En la carpeta **examples** existen ejemplo de como invocar los servicios rest

