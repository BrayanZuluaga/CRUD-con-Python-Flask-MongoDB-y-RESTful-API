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

***Los principios clave de REST incluyen:***

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

***Las principales características y funcionalidades de Postman son:***

Envío de solicitudes. Permite enviar solicitudes GET, POST, PUT, DELETE y otros métodos HTTP a una API especificando los parámetros, encabezados y cuerpo de la solicitud.
Gestión de entornos. Facilita la configuración para diferentes entornos (por ejemplo, desarrollo, prueba, producción) y el cambio sencillo entre ellos (para realizar pruebas y desarrollo en diferentes contextos).

Colecciones de solicitudes. Agrupa las solicitudes relacionadas en colecciones, lo que facilita la organización y ejecución de pruebas automatizadas.
Pruebas automatizadas. Es ideal para crear y ejecutar pruebas automatizadas para verificar el comportamiento de una API (detectar errores e incrementar la calidad del software).
Documentación de API. Genera de forma automatizada, documentación detallada de la API a partir de las solicitudes y respuestas realizadas, lo que facilita su comprensión y uso por parte de otros desarrolladores.

***Ventajas de usar Postman***

Facilidad a la hora de trabajar al disponer de una interfaz gráfica de usuario intuitiva, sencilla y personalizable.
Amplia compatibilidad con numerosas tecnologías y protocolos web, como por ejemplo; HTTP, HTTPS, REST, SOAP, GraphQL… (lo que permite interaccionar con diversos tipos de API sin complicaciones o problemas).

Ofrece una amplia gama de funcionalidades para diseñar, probar y documentar APIs, siendo probablemente la solución más completa del mercado para gestionar el ciclo de vida completo de desarrollo de APIs.

Fomenta y facilita la colaboración entre los miembros del equipo de desarrollo (con opciones interesantes como compartir colecciones de solicitudes con otros desarrolladores).


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

##  **Instalar Flask:**
Flask siendo un framework para la elaboracion de proyectos se utilizara como la base del Crud a desarrollar. Para la elaboracion de este CRUD se planea utilizar la version 3,12,3 de python, por lo cual se utilizara la version actual de Flask la cual soporta las versiones de Python desde la 3,8 en adelante. 

Para instalar Flask se debe de activar el entorno virtual creado e ingresar el siguiente codigo:

	$ pip install Flask

 ## **Instalar librerias pymongo y certifi**

**Pymongo** facilita la comunicación entre una aplicación Python y una base de datos MongoDB, permitiendo que la aplicación acceda y manipule los datos almacenados en MongoDB de manera eficiente.

**Certifi** proporciona un conjunto de certificados de raíz confiables para verificar la autenticidad de los certificados SSL/TLS al establecer conexiones seguras a través de Internet. 

Para instalar estas librerias se debe ejecutar un terminal y dentro del terminal, escribir lo siguiente, linea por line:

	pip install pymongo

  	pip install certifi


 # **Estructura del Proyecto**

 El proyecto esta constituido por la carpeta principal CRUD-con-Python-Flask-MongoDB-y-RESTful-API, dentro de esta se encuentan los archivos app.py, database.py, user.py, LICENSE, README.md y la carpeta templates que en su interior se encuentan los archivos index.html y views.html.

 ![Estructura CRUD-con-Python-Flask-MongoDB-y-RESTful-API](https://raw.githubusercontent.com/BrayanZuluaga/PeerToPeer/main/Captura.PNG)

 # **Funcipnalidad Codigo**

 ## **Archivo database.py**

**Este codigo se utiliza para establecer la conexion con la base de datos de Mongo**

 **Importa las librerias y archivos necesarios desde Mongo y Certifi**
 
	  from pymongo import MongoClient
	  
	  import certifi

**URI de conexión a la base de datos MongoDB**

	MONGO_URI = 'mongodb+srv://bbrayandavid2001:15kspzD2UQ1H6rdb@cluster0.sagniom.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'ca = certifi.where()

**Función para establecer una conexión con la base de datos MongoDB que nos retorna el objeto db que representa la base de datos "db_app_users"**
	
 	def dbConnection():

    	try:   

		client = MongoClient(MONGO_URI, tlsCAFile=ca)  

		db = client["db_app_users"]
    
		except ConnectionError:
    
		print('Error de conexión con la base de datos')
    
	    return db
 

## **Archivo app.py**

**Este codigo se utiliza para definir una aplicación Flask con varias rutas y funciones asociadas a esas rutas.**

 **Importa las librerias y archivos, las clases y funciones necesarias de Flask**
 
	from flask import Flask, render_template, request, Response, jsonify, redirect, url_for  
 
	import database as dbase  
 
	from user import Users 

**Establece la conexión con la base de datos**

	db = dbase.dbConnection() 

**Crea una instancia de la aplicación Flask**

	app = Flask(__name__)

**Rutas de la aplicación**

*Función para manejar la ruta principal de la aplicación.*

	@app.route('/')
	def home():

	    users = db['users']
	    usersReceived = users.find()
	    return render_template('index.html', users=usersReceived)

**Método GET para visualizar usuarios**

*Función para manejar la solicitud GET de visualización de usuarios.*

	@app.route('/viewU', methods=['GET'])
	def viewU():

	    users = db['users']
	    usersReceived = users.find()
	
	    if request.headers.get('Accept') == 'application/JSON':
	        user_data = []
	        for user in usersReceived:
	            user_data.append({
	                'name': user['name'],
	                'years': user['years'],
	                'cc': user['cc']
	            })
	        return jsonify(users=user_data)
	    else:
	        return render_template('views.html', users=usersReceived)

**Método POST y PUT para agregar usuarios**

*Función para agregar un nuevo usuario mediante POST o actualizar un usuario existente mediante PUT*

	@app.route('/users', methods=['POST', 'PUT'])
	def addUser():

	    users = db['users']
	    name = request.form['name']
	    cc = request.form['cc']
	    years = request.form['years']
	
	    if name and cc and years:
	        user = Users(name, cc, years)
	        users.insert_one(user.toDBCollection())
	        return redirect(url_for('home'))
	    else:
	        return notFound()

**Método DELETE para eliminar usuarios**

*Función para eliminar un usuario*

	@app.route('/delete/<string:user_name>', methods=['DELETE'])
	def delete(user_name):

	    users = db['users']
	    users.delete_one({'name': user_name})
	    return redirect(url_for('home'))

**Método POST y PUT para editar usuarios**

*Función para editar un usuario existente mediante POST o PUT.*

	@app.route('/edit/<string:user_name>', methods=['POST', 'PUT'])
	def edit(user_name):

	    users = db['users']
	    name = request.form['name']
	    cc = request.form['cc']
	    years = request.form['years']
	
	    if name and cc and years:
	        users.update_one({'name': user_name}, {'$set': {'name': name, 'cc': cc, 'years': years}})
	        return redirect(url_for('home'))
	    else:
	        return notFound()

**Manejador de errores 505 (Not Found)**

*Función para manejar el error 505 (Not Found)*

	@app.errorhandler(505)
	def notFound(error=None):
	
	    message = {
	        'message': 'Not Found ' + request.url,
	        'status': '505 Not Found'
	    }
	    response = jsonify(message)
	    response.status_code = 505
	    return response

**Función principal**

*Funcion para ejecutar la la aplicación en modo debug en el puerto 9000**
	
 	if __name__ == '__main__':
	app.run(debug=True, port=9000)  

## **Archivo user.py**

El codigo de este archivo, permite que encapsula los datos relacionados con un usuario y facilita su almacenamiento en MongoDB, convirtiéndolo en un formato adecuado para ser insertado en una colección de la base de datos MongoDB.

*Se define la clase Users*

	class Users:

*Funcion para inicializar objetos de la clase Users con tres atributos: name, cc y years. Estos atributos representan el nombre, la cédula y la edad del usuario respectivamente.*
	
 	def __init__(self, name, cc, years):
        self.name = name
        self.cc = cc
        self.years = years

*Funcion que permite delvolver un diccionario con tres claves (name, cc, years) y los valores correspondientes son los atributos del objeto de usuario.*

	def toDBCollection(self):
        return{
            'name': self.name,
            'cc': self.cc,
            'years': self.years
        }


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

