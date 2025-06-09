# ⚽⚽⚽ Sistema de Análisis Deportivo Automatizado ⚽⚽⚽

Este proyecto consiste en una API REST desarrollada en Flask que consume datos de fútbol
desde [football-data.org](https://www.football-data.org/), 
los almacena en una base de datos relacional PostgreSQL y 
genera visualizaciones interactivas para análisis de rendimiento deportivo o eso creemos que hace.

---

# 📌 Objetivos del Proyecto 📌

- Automatizar la recolección de datos de partidos y equipos.
- Almacenar la información en una base de datos estructurada.
- Exponer endpoints útiles para la consulta de métricas.
- Visualizar indicadores como posesión, goles, tarjetas y xG.
- Desplegar todo en una instancia EC2 de AWS.

---

## 🧰 Tecnologías Usadas 🧰

| Herramienta       | Descripción                          |
|-------------------|--------------------------------------|
| Python 3.10       | Lenguaje principal                   |
| Flask             | Framework para API REST              |
| PostgreSQL        | Base de datos relacional             |
| SQLAlchemy        | ORM para conexión BD                 |
| football-data.org | API pública de fútbol europeo        |
| Seaborn / Plotly  | Visualización de datos               |
| AWS EC2           | Servidor de despliegue               |
| Docker            | Contenedor para backend              |

---

## 🚀 Estructura del Proyecto 🚀

```
proyecto_futbol/
├── app.py                  # API Flask principal
├── db.py                   # Conexión a base de datos
├── visual.py               # Visualizaciones y gráficos
├── utils/
│   ├── api_service.py      # Funciones para consumir API
│   └── db_utils.py         # Funciones para insertar datos
├── .env.example            # Variables de entorno
├── requirements.txt        # Dependencias
├── Dockerfile              # Imagen Docker
└── img/                    # Diagramas PNG
```

---

# ⚙️ Cómo Ejecutar el Proyecto

# 🔧 1. Clona el repositorio

```bash
copiar el link del proyecto
cd proyecto_futbol
```

# 🧪 2. Crea un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🔐 3. Configura tu archivo `.env`

Copia el ejemplo y reemplaza tu token:

```bash
cp .env.example .env
# Edita y agrega tu API_TOKEN
```

# ▶️ 4. Ejecuta la API

```bash
python app.py
```

Visita `http://localhost:5000/` para ver la API en acción.

---

# 📊 Visualización

Desde `visual.py` puedes generar gráficos como:

- 📈 Posesión por equipo
- ⚽ Comparativa de goles por fecha
- 📊 xG por partido
- 🟨 Tarjetas amarillas y rojas por equipo

---

## 👥 Usuarios del Sistema

| Rol                  | Permisos principales                                                   |
|----------------------|------------------------------------------------------------------------|
| Administrador        | Acceso completo: scripts, API, BD                                      |
| Analista Deportivo   | Consultas avanzadas, filtros por ligas, descarga de gráficos           |
| Tester               | Validación de integridad, pruebas de endpoints                         |
| Usuario Final        | Solo lectura de métricas y visualizaciones                             |
| Docente Evaluador    | Acceso a documentación, revisión de funcionalidad                      |

---

## 🗂 Diagramas y Documentación

- Modelo Entidad-Relación (ERD)
- BPMN del flujo de datos
- Diagrama de Clases
- Diagrama de Despliegue
- WBS del proyecto

Todos están disponibles en el directorio `img/` o dentro del informe técnico.

---

## 🔌 Integración con API externa

Se implementó un módulo llamado `api_service.py` encargado de conectarse a la API pública de football-data.org. A través de este componente se automatiza la descarga de datos relacionados con competiciones, equipos, jugadores y resultados. Se garantiza que las llamadas se realicen con autenticación y manejo de errores básicos.

---

## 🗃️ Estructura y carga de la base de datos

La base de datos está construida en PostgreSQL, estructurada con SQLAlchemy. Se definieron modelos para equipos, partidos, estadísticas por equipo y por partido. Además, se creó un script inicial `init_db.py` que permite cargar datos históricos base automáticamente desde la API.

---

## 🔐 Seguridad básica con token de acceso

Para proteger los endpoints, se agregó un middleware que valida la presencia y validez de un token antes de aceptar peticiones. El token se gestiona a través del archivo `.env`, evitando exposición directa del API key.

---

## 📈 Visualización de tarjetas por equipo

Se implementó una visualización que permite analizar la cantidad de tarjetas amarillas y rojas por equipo. Esta métrica está disponible en formato gráfico de barras y puede filtrarse por liga o temporada, permitiendo un análisis disciplinario.

---

## 🌐 Endpoint de partidos con filtros

Se desarrolló el endpoint `/matches` que acepta parámetros como fecha, nombre del equipo o competencia. Esto facilita a los usuarios consultar partidos específicos según el criterio deseado.

---

## 📦 Dockerización del entorno

Se configuró el archivo `Dockerfile` para contenedores y `docker-compose.yml` para levantar simultáneamente el backend y la base de datos PostgreSQL en entornos locales o de producción. Esto simplifica la instalación del sistema.

---

## 📄 Documentación con Swagger

Gracias al uso de `flasgger`, se implementó una documentación visual accesible desde el navegador. Esta interfaz facilita la prueba y comprensión de todos los endpoints expuestos por la API.

---

## 🧪 Pruebas unitarias básicas

Se agregaron pruebas para verificar la conectividad de la API, la correcta inserción de datos y el comportamiento del sistema ante errores comunes. Estas pruebas están escritas usando `unittest` y `pytest`.

---

## 🧹 Limpieza y normalización de datos

Antes de guardar la información extraída, se normalizan nombres, formatos de fecha y estructuras de estadísticas. Esto asegura la integridad de los datos almacenados y facilita futuras consultas y análisis.

---

### 🚀 Inicializa la estructura base del proyecto

| Tarea                   | Detalle                                   |
|------------------------|-------------------------------------------|
| Implementación          | Inicializa la estructura base del proyecto. |
| Módulo afectado         | Backend/API/Visualizaciones               |
| Documentación vinculada | Incluida en el README                     |

---

### 🐛 Conecta y prueba la base de datos PostgreSQL

- Se creó el componente relacionado a: **conecta y prueba la base de datos PostgreSQL**
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

---

### ✨ Define modelos fundamentales para representar partidos y equipos

Este cambio representa un avance en la consolidación de la funcionalidad.  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

---

### 🛠️ Crea el primer endpoint funcional expuesto vía Flask

Crea el primer endpoint funcional expuesto vía Flask, implementado de acuerdo a la estructura técnica definida en fases anteriores.

---

### 📦 Integra contenedores con Docker para entorno reproducible

| Tarea                   | Detalle                                   |
|------------------------|-------------------------------------------|
| Implementación          | Integra contenedores con Docker para entorno reproducible. |
| Módulo afectado         | Backend/API/Visualizaciones               |
| Documentación vinculada | Incluida en el README                     |

---

### 🧪 Corrige errores de conexión y configuración

- Se creó el componente relacionado a: **corrige errores de conexión y configuración**
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

---

### 📄 Agrega autenticación segura mediante JWT

Este cambio representa un avance en la consolidación de la funcionalidad.  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

---

### 🎯 Patrón de diseño: Factory Method

El patrón Factory Method es un patrón creacional que permite crear objetos sin especificar la clase exacta del objeto que se va a crear. En lugar de instanciar clases directamente con new o Clase(), se delega la creación a una “fábrica” que encapsula esa lógica. Esto permite mayor flexibilidad y escalabilidad.

## 🧩 Aplicación en el proyecto

Actualmente, el proyecto utiliza SQLAlchemy. El Repository Pattern encaja perfectamente para centralizar operaciones CRUD (Create, Read, Update, Delete) sobre entidades como equipos, partidos, estadísticas, etc.

**🗂 Archivo sugerido:** `utils/api_factory.py`

```python
from utils.api_service import MatchesAPI, TeamsAPI, CompetitionsAPI

class APIFactory:
    @staticmethod
    def create_api(service_name: str, token: str):
        if service_name == "matches":
            return MatchesAPI(token)
        elif service_name == "teams":
            return TeamsAPI(token)
        elif service_name == "competitions":
            return CompetitionsAPI(token)
        else:
            raise ValueError("Servicio no reconocido.")
```

**✅ Uso práctico (app.py o controllers/etl_controller.py):**

```python
from utils.api_factory import APIFactory

api = APIFactory.create_api("matches", api_token)
partidos = api.obtener_partidos()
```

✅ Beneficios

Flexibilidad: Permite cambiar o agregar nuevos servicios sin modificar el código principal.

Escalabilidad: Puedes agregar APIs como PlayersAPI o SeasonsAPI sin alterar el flujo general.

Desacoplamiento: El controlador no necesita conocer cómo se construye cada servicio.

---

### 🗃️ Patrón de diseño: Repository Pattern

El Repository Pattern (Patrón de Repositorio) es un patrón de diseño que encapsula la lógica de acceso a datos, proporcionando una interfaz limpia entre la lógica de negocio y la base de datos. Permite trabajar con objetos de dominio sin preocuparse por los detalles de persistencia (ORM, SQL, etc.).

## 🧩 Aplicación en el proyecto

Actualmente, el proyecto utiliza SQLAlchemy. El Repository Pattern encaja perfectamente para centralizar operaciones CRUD (Create, Read, Update, Delete) sobre entidades como equipos, partidos, estadísticas, etc.

**📄 `repositories/match_repository.py`**

```python
from models import Match
from db import get_db

class MatchRepository:
    def __init__(self, session=None):
        self.session = session or get_db()

    def save(self, match_obj):
        self.session.add(match_obj)
        self.session.commit()

    def get_by_id(self, match_id):
        return self.session.query(Match).filter_by(id=match_id).first()

    def get_all(self):
        return self.session.query(Match).all()
```

**📄 `repositories/team_repository.py`**

```python
from models import Team
from db import get_db

class TeamRepository:
    def __init__(self, session=None):
        self.session = session or get_db()

    def save(self, team_obj):
        self.session.add(team_obj)
        self.session.commit()

    def get_by_name(self, name):
        return self.session.query(Team).filter_by(name=name).first()

    def get_all(self):
        return self.session.query(Team).all()
```

**🧪 Ejemplo:**

```python
from repositories.match_repository import MatchRepository
from models import Match

repo = MatchRepository()
nuevo_partido = Match(id=123, goles_local=2, goles_visitante=1)
repo.save(nuevo_partido)

todos = repo.get_all()
```

✅ Beneficios 

Abstracción del ORM: Puedes cambiar de SQLAlchemy a raw SQL o a otra BD sin tocar la lógica de negocio.

Reutilización y pruebas unitarias más fáciles

Centralización: Todas las consultas SQL están en un lugar consistente.

---

### 🔌 Patrón de diseño: Adapter Pattern

El Adapter Pattern permite que dos interfaces incompatibles trabajen juntas. En otras palabras, convierte la interfaz de una clase en otra que el sistema espera.

En el contexto del proyecto, este patrón se aplica para transformar el JSON crudo que retorna football-data.org en objetos compatibles con tus modelos SQLAlchemy (por ejemplo: Match, Team, Competition).

## 🧩 Aplicación en el proyecto

La API externa entrega estructuras complejas o con nombres diferentes a los de los modelos. Se necesita un adaptador que:

Extraiga los datos relevantes.

Cambie los nombres de campos si es necesario.

Estructure un objeto de dominio (por ejemplo, una instancia de Match).

**📄 `adapters/match_adapter.py`**

```python
from models import Match

class MatchAdapter:
    @staticmethod
    def from_api(data):
        return Match(
            id=data["id"],
            fecha=data["utcDate"],
            id_equipo_local=data["homeTeam"]["id"],
            id_equipo_visitante=data["awayTeam"]["id"],
            goles_local=data["score"]["fullTime"]["home"],
            goles_visitante=data["score"]["fullTime"]["away"]
        )
```

**📄 `adapters/team_adapter.py`**

```python
from models import Team

class TeamAdapter:
    @staticmethod
    def from_api(data):
        return Team(
            id=data["id"],
            nombre=data["name"],
            pais=data["area"]["name"],
            fundacion=data.get("founded", None)
        )
```

**🧪 Ejemplo:**

```python
from adapters.match_adapter import MatchAdapter
from repositories.match_repository import MatchRepository

response_json = {
    "id": 456,
    "utcDate": "2023-08-15",
    "homeTeam": {"id": 10},
    "awayTeam": {"id": 20},
    "score": {"fullTime": {"home": 2, "away": 1}}
}

match_obj = MatchAdapter.from_api(response_json)
MatchRepository().save(match_obj)

✅ Beneficios 

Aislamiento: Si cambia el formato de la API, solo debes modificar los adaptadores.

Consistencia: Todos los datos que entran al sistema cumplen con tu estructura interna.

Escalabilidad: Puedes crear adaptadores para Players, Events, Standings, etc.

### ♻️ Patrón de diseño: Singleton

El patrón Singleton garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella. Es especialmente útil cuando se necesita compartir un recurso único, como una conexión a base de datos.

## 🧩 Aplicación en el proyecto

El proyecto en Flask necesita acceder a la base de datos PostgreSQL a través de SQLAlchemy. En vez de crear múltiples sesiones, se puede usar el patrón Singleton para que todos los módulos compartan una única instancia del motor de conexión o sesión.

**📄 `db.py`**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DBConnectionSingleton:
    _engine = None
    _Session = None

    @classmethod
    def initialize(cls):
        if cls._engine is None:
            DATABASE_URL = os.getenv("DATABASE_URL")
            cls._engine = create_engine(DATABASE_URL)
            cls._Session = sessionmaker(bind=cls._engine)

    @classmethod
    def get_session(cls):
        if cls._Session is None:
            cls.initialize()
        return cls._Session()
```

**🧪 Ejemplo de uso:**

```python
from db import DBConnectionSingleton

session = DBConnectionSingleton.get_session()
resultados = session.query(Equipo).all()
```

✅ Beneficios 

Evita múltiples conexiones simultáneas innecesarias.

Asegura eficiencia y control de recursos cuando se usan ORM pesados como SQLAlchemy.

Facilita las pruebas: puedes mockear el get_session().

---

### 👀 Patrón de diseño: Observer Pattern

El Observer Pattern permite definir un mecanismo de suscripción para que múltiples objetos se mantengan informados sobre cambios en otro objeto. Es decir, cuando el "sujeto observado" cambia, notifica automáticamente a todos sus “observadores”.

## 🧩 Aplicación en el proyecto

En el sistema, se puede usar este patrón para que los módulos de visualización (como visual.py) se actualicen automáticamente cada vez que se inserten nuevos datos en la base de datos (por ejemplo: nuevos partidos).

Este patrón también es útil si se desea automatizar la generación de gráficos o actualizaciones de dashboards cuando hay nuevas inserciones por ETL.

**📄 `observers/subject.py`**

```python
class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_all(self, data):
        for observer in self._observers:
            observer.update(data)
```

**📄 `observers/visual_observer.py`**

```python
from visual import generar_grafico_tarjetas, generar_grafico_goles

class VisualObserver:
    def update(self, data):
        print("🔄 Datos actualizados. Generando visualizaciones...")
        generar_grafico_tarjetas(data)
        generar_grafico_goles(data)
```

**🧪 Ejemplo:**

```python
from observers.subject import Subject
from observers.visual_observer import VisualObserver
from repositories.match_repository import MatchRepository

subject = Subject()
subject.subscribe(VisualObserver())

nuevo_partido = {...}
MatchRepository().save(nuevo_partido)

subject.notify_all([nuevo_partido])
```

✅ Beneficios 

Automatización: Visualizaciones se actualizan sin intervención manual.

Desacoplamiento: visual.py no depende de db_utils o api_service.

Escalabilidad: Puedes suscribir otros observadores como EmailAlert, Logger, etc.

### 🏁 Conclusión de los patrones de diseño
Se implementaron los 5 patrones de diseño aplicados al dominio de fútbol y análisis deportivo, lo cual mejora la calidad arquitectónica, mantenibilidad y escalabilidad del sistema.

## Aplicación de los patrones de diseño en el proyecto
![image](https://github.com/user-attachments/assets/e338b87c-df4c-4fa1-9325-977ad2554a87)

### 🔧 Configura la documentación interactiva con Swagger.

Configura la documentación interactiva con Swagger. implementado de acuerdo a la estructura técnica definida en fases anteriores.  


### 📊 Genera visualización de goles mediante gráficos.

| Tarea                     | Detalle                                   |
|---------------------------|-------------------------------------------|
| Implementación            | Genera visualización de goles mediante gráficos.                                   |
| Módulo afectado           | Backend/API/Visualizaciones               |
| Documentación vinculada   | Incluida en el README                     |

### 🧰 Crea visualización de posesión de balón.

- Se creó el componente relacionado a: **crea visualización de posesión de balón.**  
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

### 🧠 Automatiza las visualizaciones con el patrón Observer.

Este cambio representa un avance en la consolidación de la funcionalidad automatiza las visualizaciones con el patrón observer..  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

### ⚙️ Refactoriza el código para una arquitectura más clara.

Refactoriza el código para una arquitectura más clara. implementado de acuerdo a la estructura técnica definida en fases anteriores.  


### 🔐 Implementa repositorios para desacoplar la lógica de datos.

| Tarea                     | Detalle                                   |
|---------------------------|-------------------------------------------|
| Implementación            | Implementa repositorios para desacoplar la lógica de datos.                                   |
| Módulo afectado           | Backend/API/Visualizaciones               |
| Documentación vinculada   | Incluida en el README                     |

### ♻️ Agrega validaciones para asegurar entradas válidas.

- Se creó el componente relacionado a: **agrega validaciones para asegurar entradas válidas.**  
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

### 💾 Actualiza dependencias críticas del proyecto.

Este cambio representa un avance en la consolidación de la funcionalidad actualiza dependencias críticas del proyecto..  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

### ✅ Aplica patrón Singleton en el módulo de conexión a BD.

Se aplico el patrón Singleton en el módulo de conexión a BD. implementado de acuerdo a la estructura técnica definida en fases anteriores.  


### 🗃️ Documenta proceso de despliegue en servidores EC2.

- Se creó el componente relacionado a: **documenta proceso de despliegue en servidores ec2.**  
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

### 🧱 Corrige bugs menores relacionados con formato de fechas.

Este cambio representa un avance en la consolidación de la funcionalidad corrige bugs menores relacionados con formato de fechas..  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

### 🔍 Consolida patrones de diseño en la arquitectura general.

Consolida patrones de diseño en la arquitectura general. implementado de acuerdo a la estructura técnica definida en fases anteriores.  

### 🚀 Implementa cliente para consumir datos desde football-data.org.

| Tarea                     | Detalle                                   |
|---------------------------|-------------------------------------------|
| Implementación            | Implementa cliente para consumir datos desde football-data.org.                                   |
| Módulo afectado           | Backend/API/Visualizaciones               |
| Documentación vinculada   | Incluida en el README                     |

### 🐛 Construye clases API para partidos y equipos.

- Se creó el componente relacionado a: **construye clases api para partidos y equipos.**  
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

### ✨ Implementa patrón Factory Method para instanciar servicios.

Este cambio representa un avance en la consolidación de la funcionalidad implementa patrón factory method para instanciar servicios..  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

### 🛠️ Integra patrón Adapter para convertir datos externos.

Integra patrón Adapter para convertir datos externos. implementado de acuerdo a la estructura técnica definida en fases anteriores.  

### 📦 Crea script ETL para automatizar extracción y carga.

| Tarea                     | Detalle                                   |
|---------------------------|-------------------------------------------|
| Implementación            | Crea script ETL para automatizar extracción y carga.                                   |
| Módulo afectado           | Backend/API/Visualizaciones               |
| Documentación vinculada   | Incluida en el README                     |

### 🧪 Ejecuta pruebas de integración sobre el sistema.

- Se creó el componente relacionado a: **ejecuta pruebas de integración sobre el sistema.**  
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

### 📄 Desarrolla pruebas visuales con datos simulados.

Este cambio representa un avance en la consolidación de la funcionalidad desarrolla pruebas visuales con datos simulados..  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

### 🔧 Agrega diagrama entidad-relación (ERD).

Diagrama entidad-relación (ERD). implementado de acuerdo a la estructura técnica definida en fases anteriores.  

![image](https://github.com/user-attachments/assets/9f4695f9-e354-44ff-9d78-fa7ad124c68a)


### 📊 Describe el modelo dimensional en estrella.

| Tarea                     | Detalle                                   |
|---------------------------|-------------------------------------------|
| Implementación            | Describe en README el modelo dimensional en estrella.                                   |
| Módulo afectado           | Backend/API/Visualizaciones               |
| Documentación vinculada   | Incluida en el README                     |

### 🧰 Integra visualización con notificaciones automáticas.

- Se creó el componente relacionado a: **integra visualización con notificaciones automáticas.**  
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

### 🧠 Resuelve inconsistencias con claves foráneas duplicadas.

Este cambio representa un avance en la consolidación de la funcionalidad resuelve inconsistencias con claves foráneas duplicadas..  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

### ⚙️ Depura el sistema y elimina trazas de depuración.

Depura el sistema y elimina trazas de depuración. implementado de acuerdo a la estructura técnica definida en fases anteriores.  


### 🔐 Automatiza generación de gráficos desde inserciones ETL.

| Tarea                     | Detalle                                   |
|---------------------------|-------------------------------------------|
| Implementación            | Automatiza generación de gráficos desde inserciones ETL.                                   |
| Módulo afectado           | Backend/API/Visualizaciones               |
| Documentación vinculada   | Incluida en el README                     |

### ♻️ Redacta sección detallada de patrones en la documentación.

- Se creó el componente relacionado a: **redacta sección detallada de patrones en la documentación.**  
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

### 💾 Crea visualización de tarjetas por equipo y liga.

Este cambio representa un avance en la consolidación de la funcionalidad crea visualización de tarjetas por equipo y liga..  
Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

### ✅ Agrega endpoint para estadísticas globales.

Agrega endpoint para estadísticas globales. implementado de acuerdo a la estructura técnica definida en fases anteriores.  


### 📈 Permite exportar métricas en formato CSV.

| Tarea                     | Detalle                                   |
|---------------------------|-------------------------------------------|
| Implementación            | Permite exportar métricas en formato CSV.                                   |
| Módulo afectado           | Backend/API/Visualizaciones               |
| Documentación vinculada   | Incluida en el README                     |

### 🗃️ Resuelve problemas con codificación de caracteres.

- Se creó el componente relacionado a: **resuelve problemas con codificación de caracteres.**  
- Se integró con otros módulos existentes  
- Se verificó que el comportamiento fuera coherente con la arquitectura esperada  

### ⭐ Modelo dimensional en estrella

> Basado en la API de fútbol **football-data.org**, se construyó un modelo dimensional en estrella enfocado en el análisis de partidos.
> Se desarrolló asegurando compatibilidad con los estándares ya definidos dentro del sistema.

![image](https://github.com/user-attachments/assets/e57bcbce-c692-469f-94ef-a6130bf7bbae)

### 🔍 Incorpora imagen resumen de patrones de diseño aplicados.

Incorpora imagen resumen de patrones de diseño aplicados. implementado de acuerdo a la estructura técnica definida en fases anteriores.  

## 👥 Roles y Autores

| Nombre                  | Rol                        |
|-------------------------|----------------------------|
| Santiago Carvajal       | Backend, Visualización     |
| Matthew Espinosa        | ETL, Arquitectura BD       |

# 📄 Licencia Educativa

Proyecto académico para la materia de **Bases de Datos III – ETITC Bogotá**, bajo fines educativos.
