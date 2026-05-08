Armería Medieval API

Es una API REST desarrollada con Python y Flask inspirada en un sistema de carrito de compras medieval.
Permite gestionar un inventario de objetos como armaduras, espadas y escudos.

La aplicación implementa operaciones CRUD básicas y documentación automática mediante Swagger/OpenAPI.

Características:
Listado de productos
Inventario/carrito en memoria
Agregar objetos al inventario
Eliminar objetos
Calcular valor total
Documentación automática con Swagger
API RESTful
Persistencia en memoria (sin base de datos)

Tecnologías utilizadas:
Python 
Flask
Flasgger
Swagger/OpenAPI

Instalación
1. Clonar repositorio
git clone TU_URL_DEL_REPOSITORIO

2. Entrar al proyecto
cd nombre-del-proyecto

3. Instalar dependencias
pip install flask
pip install flasgger

Ejecutar aplicación
python app.py

Servidor:
http://127.0.0.1:5000

La documentación interactiva se encuentra en:

http://127.0.0.1:5000/apidocs

Desde allí es posible:

visualizar endpoints
probar requests
ver respuestas
analizar parámetros

 Endpoints
 Obtener productos
GET /products

 Ver inventario
GET /art

 Agregar objeto
POST /art
Body JSON
{
  "id": 1
}

Eliminar objeto
DELETE /art/{id}

Ejemplo:

DELETE /art/1

Vaciar inventario
DELETE /art

Calcular total
GET /art/total

Arquitectura

La aplicación sigue una arquitectura backend basada en APIs REST:

Cliente → HTTP Request → Flask API → JSON Response

Los datos se almacenan temporalmente en memoria mediante listas de Python.
