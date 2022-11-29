# Salva a un amigo
## Clonar repositorio

Para clonar el repositorio ejecutamos los siguiente comandos en Git bash
```
$ git init
$ git clone https://github.com/YOUR-USERNAME/pet_adoption_api.git
```

## Crear entorno virtual

Para crear nuestro entorno virtual ejecutamos el siguiente comando en nuestra terminal.

***Para nuestro caso es Windows, para el caso de Mac o Linux puedes encontrar como hacerlo [aqui.](https://www.programaenpython.com/miscelanea/crear-entornos-virtuales-en-python/)***

```
python -m venv adoption-env
```
luego para activar el entorno ejecutamos
```
.\adoption-env\Scripts\activate
```
## Instalación librerias requeridas

Para instalar todas las librerias basta con ejecutar el siguiente codigo en la terminal, el cual instala nuestro archivo [requirements.txt](https://github.com/Juanma1023/pet_adoption_api/blob/main/requirements.txt)

```
pip install -r requirements.txt
```

## Crear y conectar la base de datos

Para crear nuestra base de datos debemos de tener instalado [PostgreSQL](https://www.postgresql.org/) en nuestro dispositivo. Procedemos a ejecutar el siguiente comando en un archivo SQL
```
CREATE DATABASE mascotas_adopcion WITH OWNER = postgres ENCODING = 'UTF8' CONNECTION LIMIT = -1;
```
Luego de creada nuestra base de datos, procedemos con la conexion. Para lograr una correcta conexion debemos crear un archivo cuyo nombre sera ***.env*** con la siguiente informacion:

```
DB_NAME = mascotas_adopcion
DB_USER = USER_POSTGRES
DB_PASS = PASSWORD
DB_HOST = localhost
DB_PORT = 5432
```

Para completar nuestra base de datos y agregar nuestra tablas, ejecutamos el siguiente codigo en nuestra terminal con ubicacion en el entorno virtual.

```
python
from app.v1.scripts.create_tables import create_tables
create_tables()
```

## Uvicorn

Utilizaremos [Uvicorn](https://www.uvicorn.org/) para convertir nuestro espacio en un servidor y para poder usar nuestra API REST. Ejecutamos el siguiente codigo para activarlo.

```
uvicorn main:app --reload
```
Buscamos en nuestro navegador web ***http://localhost:8000/docs*** para utilizar nuestra api.
