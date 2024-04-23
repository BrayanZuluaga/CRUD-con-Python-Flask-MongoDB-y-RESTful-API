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

### *Funciones Principales* 
**Sintaxis clara y legible:** Python se destaca por su sintaxis simple y legible, lo que facilita la escritura y comprensión del código.
**Multiparadigma:** Python admite programación imperativa, orientada a objetos y funcional, lo que proporciona flexibilidad en la forma de abordar problemas.
**Amplia biblioteca estándar:** Python incluye una amplia gama de módulos y bibliotecas estándar para realizar diversas tareas, desde manipulación de archivos hasta desarrollo web y análisis de datos.
**Portabilidad:** Python es compatible con la mayoría de las plataformas, incluidas Windows, macOS y Linux, lo que lo hace altamente portátil.
**Interpretado y dinámico:** Python no requiere un paso de compilación explícito, lo que acelera el desarrollo y la prueba de código.
### *Ventajas*
**Legibilidad:** Su sintaxis es clara facilita la escritura y lectura del código.

**Versatilidad:** Python se utiliza en una variedad de dominios, como desarrollo web, ciencia de datos, automatización e inteligencia artificial.

**Productividad:** Python permite desarrollar rápidamente aplicaciones debido a su sintaxis clara y a la amplia variedad de bibliotecas disponibles que contribuyen la comunidad de desarrolladores 

### *Desventajas* 
**Velocidad de Ejecución:** Python es más lento que lenguajes de programación compilados como C, C++ o Java debido a su naturaleza interpretada.

**Gestión de Memoria:** La gestión automática de memoria puede llevar a problemas de rendimiento en aplicaciones multihilo que requieren un uso intensivo de recursos.

### *Python VS Otros lenguajes*

**Python vs Java:** Python es más simple y fácil de aprender que Java, pero Java es más rápido y se utiliza ampliamente en aplicaciones empresariales.

**Python vs C++:** Python es más fácil de aprender y de usar, pero C++ ofrecer mayor control sobre el hardware y un mejor rendimiento en aplicaciones intensivas en recursos.
Python es más versátil y se utiliza ampliamente en áreas como la ciencia de datos y el aprendizaje automático, mientras que JavaScript es el lenguaje principal para el desarrollo web.


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

### **Replicación MongoDB (Deploy a Replica Set)**
Un Replica Set en MongoDB es un grupo de procesos mongod que mantienen el mismo conjunto de datos. Estos conjuntos replicados aseguran la redundancia y la alta disponibilidad de los datos.

  

## **Restful API**
REST (acrónimo de Representational State Transfer, que se traduce como “transferencia
de representación de estado”) es una arquitectura de software utilizada para crear servicios
web. Características y ventajas clave de REST:
Sin Estado (Stateless):

• La característica fundamental de REST es que no mantiene un estado interno. Esto
significa que, entre dos llamadas a un servicio REST, el servidor no retiene
información sobre el cliente.

• El cliente debe proporcionar su estado en cada petición. Por ejemplo, si un usuario
inicia sesión, debe enviar sus credenciales en cada solicitud posterior.
Simple y Uniforme:

• REST utiliza métodos estándar de HTTP (como GET, POST, PUT y DELETE) para
operar sobre recursos.

• La interfaz REST es simple y fácil de entender, lo que facilita su implementación y
uso.
Escalabilidad:

• Al no mantener un estado interno, los servicios REST son altamente escalables. No
requieren almacenar datos de sesión en memoria, lo que evita problemas de falta de
memoria en servidores con muchos clientes.

• Aunque puede ser tedioso pasar el estado en cada llamada, esta desventaja se
compensa con la escalabilidad.
Compartir Recursos y Datos:

• REST permite compartir recursos y datos entre diferentes dispositivos y
aplicaciones de manera eficiente.

• Utiliza el protocolo HTTP para obtener y generar datos en formatos específicos,
como XML y JSON.

 API (acrónimo de Interfaz de Programación de Aplicaciones) es un conjunto de
definiciones y protocolos que permiten la comunicación entre dos aplicaciones de software.
Puntos clave sobre las API:
Definición y Propósito:

• Una API establece cómo un módulo de software se comunica o interactúa con otro
para cumplir una o muchas funciones.

• Es como un puente que facilita la transferencia de datos y funcionalidades entre
aplicaciones.

• Aunque no son visibles para los usuarios finales, las API son los circuitos internos
que conectan y hacen funcionar herramientas.
Funciones y Utilidad:

• Las API pueden tener una o varias funciones, incluso llegar a ser auténticos kits de
herramientas.
Ejemplos prácticos incluyen:

• Iniciar sesión en una aplicación usando tu cuenta de Facebook.

• Publicar resultados de un juego en Twitter.

• Recibir notificaciones en tu dispositivo.

• Pueden ser privadas, abiertas para partners o públicas para cualquier desarrollador.
Tipos de API:

• API Remotas: Acceso a servicios en puntos diferentes.

• API Locales: Comunicación dentro de un mismo ambiente o dispositivo.

• API Públicas: Cualquier desarrollador puede interactuar con ellas.

• API Privadas: Uso restringido a una empresa o grupo específico.

API RESTful (Transferencia de Estado Representacional) es una interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet. 

Los principios clave de REST incluyen:

**Interfaz Uniforme:** Una forma consistente de interactuar con los recursos.

**Cliente-Servidor:** Separación de responsabilidades entre clientes y servidores.

**Sin Estado:** Cada solicitud del cliente al servidor debe contener toda la información necesaria para comprender y procesar la solicitud.

**Posibilidad de Caché:** Las respuestas se pueden almacenar en caché para mejorar el rendimiento.

**Sistema en Capas:** Jerarquía de capas (por ejemplo, equilibradores de carga, pasarelas) que manejan diferentes aspectos de la solicitud.

**Código a Demanda:** Función opcional donde el servidor puede enviar código ejecutable (por ejemplo, JavaScript) al cliente.

Una API RESTful proporciona una forma segura y estandarizada para que diferentes sistemas se comuniquen a través de Internet, siguiendo estos principios e instrucciones. 

## **POSTMAN**

Postman es una herramienta de colaboración y desarrollo que permite a los desarrolladores interactuar y probar el funcionamiento de servicios web y aplicaciones. proporcionando una interfaz gráfica intuitiva y fácil de usar para enviar solicitudes a servidores web y recibir las respuestas correspondientes
Este entorno ofrece una GUI que facilita a los desarrolladores el envío de solicitudes HTTP y HTTPS a una API y a gestionar las respuestas recibidas.

Las principales características y funcionalidades de Postman son:

Envío de solicitudes. Permite enviar solicitudes GET, POST, PUT, DELETE y otros métodos HTTP a una API especificando los parámetros, encabezados y cuerpo de la solicitud.
Gestión de entornos. Facilita la configuración para diferentes entornos (por ejemplo, desarrollo, prueba, producción) y el cambio sencillo entre ellos (para realizar pruebas y desarrollo en diferentes contextos).
Colecciones de solicitudes. Agrupa las solicitudes relacionadas en colecciones, lo que facilita la organización y ejecución de pruebas automatizadas.
Pruebas automatizadas. Es ideal para crear y ejecutar pruebas automatizadas para verificar el comportamiento de una API (detectar errores e incrementar la calidad del software).
Documentación de API. Genera de forma automatizada, documentación detallada de la API a partir de las solicitudes y respuestas realizadas, lo que facilita su comprensión y uso por parte de otros desarrolladores.

Ventajas de usar Postman

Facilidad a la hora de trabajar al disponer de una interfaz gráfica de usuario intuitiva, sencilla y personalizable.
Amplia compatibilidad con numerosas tecnologías y protocolos web, como por ejemplo; HTTP, HTTPS, REST, SOAP, GraphQL… (lo que permite interaccionar con diversos tipos de API sin complicaciones o problemas).
Ofrece una amplia gama de funcionalidades para diseñar, probar y documentar APIs, siendo probablemente la solución más completa del mercado para gestionar el ciclo de vida completo de desarrollo de APIs.
Fomenta y facilita la colaboración entre los miembros del equipo de desarrollo (con opciones interesantes como compartir colecciones de solicitudes con otros desarrolladores).

# **Metodologia** 

### *Relación Python con MongoDB Atlas y MongoDB en el equipo*
**1.Interfaz de usuario de MongoDB Atlas:** Aunque no se requiere Python directamente para crear una cuenta en MongoDB Atlas, Python puede ser utilizado para interactuar con la base de datos MongoDB creada en Atlas, por ejemplo, si se utiliza la biblioteca **“pymongo”**, se puede conectar a la base de datos y realizar operaciones CRUD.

**Ejemplo:**

from pymongo import MongoClient

**Conexión a la base de datos en MongoDB Atlas**
client = MongoClient("mongodb+srv://<usuario>:<contraseña>@<cluster>/<basededatos>?retryWrites=true&w=majority")

**Seleccionar la base de datos**
db = client["mi_base_de_datos"]

**Listar todas las colecciones en la base de datos**
colecciones = db.list_collection_names()
for coleccion in colecciones:
    print(coleccion)

**2.Línea de comandos (CLI) con MongoDB Shell:** Aunque MongoDB Shell no está escrito con Python, una vez que se establece conexión con MongoDB Atlas a través de la CLI, Python puede usar se para automatizar tareas, procesar datos recuperados de la base de datos, o incluso para interactuar con el CLI mediante la ejecución de comandos utilizando el módulo **“subprocess”**

**Ejemplo:**

$ mongosh

*use mi_nueva_base_de_datos*

*switched to db mi_nueva_base_de_datos*

> db.mi_coleccion.insertOne({ "nombre": "Ejemplo" })

**3.MongoDB Compass:** Al igual que con MongoDB Shell, MongoDB Compass no está escrito en Python, pero puede utilizarse para interactuar con MongoDB Atlas. Sin embargo, Python puede integrarse con MongoDB Compass para realizar análisis de datos más avanzados o para automatizar tareas utilizando la API de MongoDB Compass y la biblioteca **“pymongo”**.

**Ejemplo:**

Para este proceso se debe a ver hecho la instalación correcta de MongoDB Compass, para crear una nueva base de datos utilizando la interfaz grafica se deben realizar los siguientes pasos:

**1.** Se abre MongoDB Compass y se selecciona "Conectar a MongoDB".

**2.** Se ingresa la cadena de conexión de tu clúster de Atlas.

**3.** Una vez conectado, haz clic en el botón "Crear base de datos" y se sigue los pasos para crear una nueva base de datos.

### *Relación de Python con la instalación de Flask*
**Creación del entorno virtual:** Python proporciona la capacidad de crear y gestionar entornos virtuales utilizando el módulo **“venv”**. Esto permite que las dependencias de un proyecto, como Flask y sus extensiones, se mantengan separadas del sistema global de Python, lo que facilita la gestión de las versiones de las bibliotecas y evita conflictos entre proyectos.
**Ejemplo:**
Para este proceso se debe a ver hecho la instalación correcta Flask y sus dependencias, por lo tanto, se deben realizar los siguientes pasos:
**1.** Crear un nuevo directorio para tu proyecto y navegar a él en la línea de comandos.
**2.** Crear un entorno virtual utilizando **“venv”**

**Ejemplo:**
$ mkdir mi_proyecto
$ cd mi_proyecto
$ python3 -m venv .venv
$ source .venv/bin/activate  **Para activar el entorno virtual en Linux/Mac**

**Instalación de Flask y sus dependencias:** Una vez creado el entorno virtual, Python se utiliza para instalar Flask y sus dependencias, como Werkzeug, Jinja, MarkupSafe. Esto se hace a través del gestor de paquetes de Python.

**Desarrollo del proyecto Flask:** Una vez instalado, Python es el lenguaje principal utilizado para desarrollar el proyecto CRUD con Flask. Python se utiliza para escribir las vistas, definir las rutas URL, interactuar con la base de datos (por ejemplo, utilizando **“pymongo”** para operaciones CRUD en MongoDB), procesar formularios, manejar solicitudes y respuestas HTTP.

Por ende, Python juega un papel fundamental en todo el proceso de la creación del CRUD, desde la interacción con MongoDB Atlas y MongoDB en el equipo, hasta la instalación y desarrollo del proyecto utilizando Flask. Su versatilidad y facilidad de uso lo convierte en una excelente opción para el desarrollo del proyecto web (CRUD) y trabajar con base de datos.


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

##  **Instalacion de Flask en su version Python**
  
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

 ## **Funcipnalidad Codigo**

 ### **Archivo Database.py**

**Este codigo se utiliza para establecer la conexion con la base de datos de Mongo**

 **Importa las librerias y archivos necesarios desde Mongo y Certifi**
 
	  from pymongo import MongoClient
	  
	  import certifi

**URI de conexión a la base de datos MongoDB**

	MONGO_URI = 'mongodb+srv://bbrayandavid2001:15kspzD2UQ1H6rdb@cluster0.sagniom.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'ca = certifi.where()

**Función para establecer una conexión con la base de datos MongoDB que nos retorna el objeto db que representa la base de datos "db_app_users"**
	
 	def dbConnection():

    	try:
     
**Se crea un cliente MongoClient con la URI de conexión y el archivo de certificados TLS**    

		client = MongoClient(MONGO_URI, tlsCAFile=ca)  
  
**Seleccionamos la base de datos "db_app_users"**   

		db = client["db_app_users"]

**Codigo para manejar posibles errores de conexión**
    
		except ConnectionError:
    
		print('Error de conexión con la base de datos')

**Retorna el objeto de la base de datos**
    
	    return db

 ## **Replicacion MongoDB Atlas**
MongoDB Atlas en su versión gratuita no permite realizar la desactivacion de la base de datos para hacer la replicacion
https://www.mongodb.com/developer/products/atlas/data-api-postman/


## **Bibliografia**
### *Python*
https://aws.amazon.com/es/what-is/python/

https://www.python.org/

https://keepcoding.io/blog/ventajas-y-desventajas-de-python/

https://profile.es/blog/python/#:~:text=A%20diferencia%20de%20otros%20lenguajes,de%20objetos%20(din%C3%A1micamente%20tipado).

### *Flask*
https://pypi.org/project/Flask/

https://wsgi.readthedocs.io/en/latest/what.html

https://flask.palletsprojects.com/en/3.0.x/installation/

### *MongoDB Atlas*
https://www.mongodb.com/es/atlas

https://www.mongodb.com/es/atlas/database

https://www.mongodb.com/es/basics/create-database

https://www.freecodecamp.org/espanol/news/tutorial-de-mongodb-atlas-como-empezar/

https://www.gyata.ai/es/mongodb/mongodb-atlas-login/

https://www.mongodb.com/docs/mongodb-shell/run-commands/

https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/mongodb-commands/

https://www.gyata.ai/es/mongodb/mongodb-shell-commands/

### *Postman*
https://formadoresit.es/que-es-postman-cuales-son-sus-principales-ventajas/

