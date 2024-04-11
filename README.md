# **CRUD-con-Python-Flask-MongoDB-y-RESTful-API**
Implementación de un CRUD con Python, Flask, MongoDB (en Replicación) y RESTful API.
## Integrantes
Cristian Camilo Ocampo Bravo, 
Felipe Jimenez Londoño, 
Luisa Fernanda Andrade, 
Brayan David Zuluaga Cardenas.
# **Marco Teorico**

## **Python**
### *¿Qué es Python?*
Python es un lenguaje de programación versátil y poderoso que permite trabajar de  manera rapida e integrar sistemas de manera más efectiva. Es conocido por su sintaxis clara y legible, ya que facilita la escritura y el  mantenimiento del codigo.
## **Flask**
Flask es un framework de aplicación web de carácter minimalista desarrollado en Python que se basa en las especificaciones WSGI (web server Gateway interface o en español la interface de entrada para servidores web), una especificación que describe la manera en que los servidores web y las aplicaciones web se comunican entre si y como las aplicaciones web pueden ser encadenadas para procesar una petición.

El framework Flask está diseñado para que iniciar un proyecto sea rápido y fácil, con la habilidad de escalar a aplicaciones más complejas, Flask también ofrece sugerencias, pero no requiere ni enforza dependencias para funcionar, permitiendo que los desarrolladores elijan las herramientas y librerías que deseen usar dando al equipo libertad total de trabajar con este framework.



## **Mongo DB Atlas**
MongoDB Atlas es una plataforma integrada de servicios de datos en la nube que acelera y simplifica la forma de construccion con datos. Aspectos de MongoDB Atlas:

**Modelo de documentos:** El modelo de documentos de MongoDB permite almacenar datos en estructuras ricas y anidadas, lo que facilita la organización y consulta de datos debido a su rendimiento y escalabilidad.

**API de consulta unificada:** La API de consulta unificada es la forma más natural de trabajar con datos en cualquier formato. Atlas amplía la flexibilidad y facilidad de uso de MongoDB para crear búsquedas de texto completo, análisis en tiempo real y experiencias basadas en eventos.

**Seguridad y confianza:** Atlas ofrece una base sólida con seguridad de datos incorporada y opciones de recuperación. Se pueden ejecutar aplicaciones en cualquier parte del mundo gracias a la presencia global y multi-nube de Atlas.

**Servicios de datos integrados:** MongoDB Atlas proporciona una variedad de servicios de datos integrados, como búsqueda, búsqueda vectorial, gráficos y más. Estos servicios ayudan a construir aplicaciones de manera más rápida y eficiente.

Para crear una base de datos en la nube, se puede realizar utilizando la *interfaz de usuario de Atlas*, la *CLI*, el *Operador de Kubernetes* o un *proveedor de recursos de Infraestructura* como Código (IaC).

***Comandos más importantes y más utilizados en la línea de comandos (CLI) con MongoDB Shell (mongosh):***

  **Información general:**
  
  *db.help():* Muestra todos los comandos disponibles en MongoDB.
  
  *mongo --version:* Muestra la versión de MongoDB que se esta utilizando.
  
  **Comandos para bases de datos:**
  
  *show dbs:* Lista todas las bases de datos disponibles.
  
  *use DATABASE_NAME:* Cambia a una base de datos específica.
  
  *db:* Muestra la base de datos actualmente seleccionada.
  
  db.dropDatabase(): Elimina la base de datos actualmente seleccionada.
  
  **Comandos para colecciones:**
  
  *db.createCollection(Name, Options):* Crea una colección con opciones personalizadas.
  
  *show collections:* Enumera todas las colecciones disponibles.
  
  *collectionName.drop():* Elimina una colección específica.
  
  **Administración de usuarios:**
  
  Para gestionar usuarios, se pueden utilizar comandos como *db.createUser()* y *db.updateUser()*.
  
  **Añadir y gestionar documentos:**
  
  *db.nombre_coleccion.insert(document):* Inserta un nuevo documento en una colección.
  
  *db.nombre_coleccion.find():* Recupera documentos de una colección.
  
  *db.nombre_coleccion.update(criterio, nuevo_valor):* Actualiza documentos dentro de una colección.
  
  **Agrupar y clasificar:**
  
  Se pueden utilizar comandos como *db.nombre_coleccion.aggregate()* para realizar operaciones de agregación y clasificación.
  
  **Comandos relevantes para la seguridad:**
  
  Para configurar autenticación y roles, se pueden utilizar comandos como *db.createUser()* y *db.grantRolesToUser()*.
  
  **Diagnóstico y seguimiento:**
  
  *db.stats():* Proporciona estadísticas sobre la base de datos actual.
  
  *db.serverStatus():* Muestra información sobre el estado del servidor.
  

## **Restful API**
API RESTful (Transferencia de Estado Representacional) es una interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet. 

Los principios clave de REST incluyen:

**Interfaz Uniforme:** Una forma consistente de interactuar con los recursos.

**Cliente-Servidor:** Separación de responsabilidades entre clientes y servidores.

**Sin Estado:** Cada solicitud del cliente al servidor debe contener toda la información necesaria para comprender y procesar la solicitud.

**Posibilidad de Caché:** Las respuestas se pueden almacenar en caché para mejorar el rendimiento.

**Sistema en Capas:** Jerarquía de capas (por ejemplo, equilibradores de carga, pasarelas) que manejan diferentes aspectos de la solicitud.

**Código a Demanda:** Función opcional donde el servidor puede enviar código ejecutable (por ejemplo, JavaScript) al cliente.

Una API RESTful proporciona una forma segura y estandarizada para que diferentes sistemas se comuniquen a través de Internet, siguiendo estos principios e instrucciones. 


# **Metodologia** 

## **Crear Cuenta Mongo DB Atlas o Activar MongoDB en el Equipo**
Para realizar la creacion de una cuenta en MongoDB Atlas, hay varias opciones:

*1. Interfaz de usurio de MongoDB Atlas:*

  Acceder a la página de registro de MongoDB Atlas.
  
  Completa los detalles necesarios, como tu nombre, correo electrónico y contraseña.
  
  Haz clic en “Registrarse” o “Comenzar gratis”. ¡Listo! Tu cuenta está creada y puedes empezar a trabajar con MongoDB Atlas.
  
*2. Linea de comandos (CLI) con MongoDB Shell (mongosh):* 

  Asegúrate de tener acceso al clúster de MongoDB que deseas usar.
  
  Agrega tu dirección IP a la lista de acceso de IP para tu proyecto de Atlas.
  
  Asegúrate de tener un usuario de base de datos en el clúster.
  
  Instala MongoDB Shell en tu máquina.
  
  Abre una terminal y ejecuta el comando mongosh para conectarte al clúster de MongoDB Atlas.
  
  Una vez conectado, puedes crear una base de datos usando comandos en la CLI.

*3. MongoDB Compass:* 

  Descarga e instala MongoDB Compass.
  
  Abre Compass y selecciona “Conectar a MongoDB”.
  
  Ingresa la cadena de conexión de tu clúster de Atlas.
  
  Una vez conectado, puedes crear una base de datos desde la interfaz gráfica de Compass.

## **Crear Base de Datos Mongo DB Atlas**
Para crear una base de datos en MongoDB Atlas, Existen diferentes formas de realizarlo. Se puede utilizar la interfaz de usuario de MongoDB Atlas, la línea de comandos (CLI) o MongoDB Compass (la interfaz gráfica de MongoDB), a cntinuacion se explica como realizarlo con cada uno de los anteriores:

*1. Interfaz de usurio de MongoDB Atlas:*

  Acceder a tu cuenta de MongoDB Atlas.

  Desde la página de tu clúster, haz clic en “Explorar Colecciones”.

  Si aún no tienes bases de datos en este clúster, verás la opción para crear una base de datos haciendo clic en “Agregar mis propios datos”.

  Ingresa un nombre para la base de datos y la colección, luego haz clic en “Crear” y la base de datos está creada y disponible para su uso

*2. Linea de comandos (CLI) con MongoDB Shell (mongosh):* 

  Asegúrate de tener acceso al clúster de MongoDB que deseas usar.
  
  Agrega tu dirección IP a la lista de acceso de IP para tu proyecto de Atlas.
  
  Asegúrate de tener un usuario de base de datos en el clúster.
  
  Instala MongoDB Shell en tu máquina.
  
  Abre una terminal y ejecuta el comando mongosh para conectarte al clúster de MongoDB Atlas.
  
  Una vez conectado, se puede crear una base de datos usando comandos en la CLI.

  *3. MongoDB Compass:* 

  Descarga e instala MongoDB Compass.
  
  Abre Compass y selecciona “Conectar a MongoDB”.
  
  Ingresa la cadena de conexión de tu clúster de Atlas.
  
  Una vez conectado, se puede crear una base de datos desde la interfaz gráfica de Compass.

  **Instalacion de Flask en su version Python**
  
Flask siendo un framework para la elaboracion de proyectos se utilizara como la base del Crud a desarrollar.

Para la elaboracion de este CRUD se planea utilizar la version 3,12,3 de python, por lo cual se utilizara la version actual de Flask la cual soporta las versiones de Python desde la 3,8 en adelante. Para utilizar este framework se deben de instalar tambien varias dependencias, siendo estas: 
    • Werkzeug: Implementa WSGI, la interfaz estándar para la conexión entre servidores y clientes en Python.
    • Jinja: Un lenguaje plantilla para el renderizado de paginas que la aplicación muestra.
    • MarkupSafe: Acompaña a Jinja, permite escapar entradas no confiables para evitar los ataques de injeccion.
    • ItsDangerous: pone señales de seguridad en los datos para asegurar su integridad. Esto se utiliza para proteger las cookies de Flask
    • Click: Un framework para la escritura de lineas de comandos de aplicación. Provee los comandos “Flask” y permite añadir comandos de control personalizados
    • Blinker: Provee el soporte para el sistema de señales de Flask.
    
Estas dependencias son instaladas automáticamente junto con el framework flask puesto que son necesarias para su uso adecuado pero se deben de notar como requisitos para su funcionamiento.
Entornos virtuales:

Flask recomienda el uso de entornos virtuales para manejar las dependencias del proyecto tanto en desarrollo como en producción, para la creacion de estos entornos se utilizara el modulo veny de Python que es el recomendado por Flask.

Para la creacion de este entorno se siguen los siguientes pasos:
    • Crear una carpeta para el proyecto y una carpeta .veny dentro de esta
    • En la consola de comandos escribir el siguiente codigo:
      $ mkdir myproject
      $ cd myproject
      $ python3 -m venv .venv
    • Una vez el entorno se ha creado este se activa con el siguiente codigo:
      $ . .venv/bin/activate

**Instalar Flask:**
Para instalar Flask se debe de activar el entorno virtual creado e ingresar el siguiente codigo:
	$ pip install Flask


## **Bibliografia**
### *Python*
https://aws.amazon.com/es/what-is/python/

### *Flask*
https://pypi.org/project/Flask/

https://wsgi.readthedocs.io/en/latest/what.html

### *MongoDB Atlas*
https://www.mongodb.com/es/atlas

https://www.mongodb.com/es/atlas/database

https://www.mongodb.com/es/basics/create-database

https://www.freecodecamp.org/espanol/news/tutorial-de-mongodb-atlas-como-empezar/

https://www.gyata.ai/es/mongodb/mongodb-atlas-login/

https://www.mongodb.com/docs/mongodb-shell/run-commands/

https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/mongodb-commands/

https://www.gyata.ai/es/mongodb/mongodb-shell-commands/

