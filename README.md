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

### 🌐 Agrega interfaz HTML para mostrar partidos

Se ha añadido el archivo `index.html` que presenta una interfaz visual para consultar partidos en formato tabla.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Listado de Partidos</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f4f8;
      margin: 0;
      padding: 20px;
    }

    h1 {
      text-align: center;
      color: #333;
    }

    table {
      margin: 0 auto;
      width: 90%;
      border-collapse: collapse;
      background: white;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    th, td {
      padding: 12px;
      text-align: center;
      border-bottom: 1px solid #ddd;
    }

    th {
      background-color: #007BFF;
      color: white;
    }

    tr:hover {
      background-color: #f1f1f1;
    }
  </style>
</head>
<body>
  <h1>Listado de Partidos de Fútbol</h1>
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Fecha</th>
        <th>Equipo Local</th>
        <th>Equipo Visitante</th>
        <th>Goles Local</th>
        <th>Goles Visitante</th>
      </tr>
    </thead>
    <tbody id="tabla-body"></tbody>
  </table>

  <script>
    fetch('/partidos')
      .then(response => response.json())
      .then(data => {
        const tbody = document.getElementById('tabla-body');
        if (data.length === 0) {
          tbody.innerHTML = '<tr><td colspan="6">No hay datos disponibles</td></tr>';
        } else {
          data.forEach(p => {
            const fila = document.createElement('tr');
            fila.innerHTML = `
              <td>${p.id}</td>
              <td>${p.fecha}</td>
              <td>${p.equipo_local}</td>
              <td>${p.equipo_visitante}</td>
              <td>${p.goles_local}</td>
              <td>${p.goles_visitante}</td>
            `;
            tbody.appendChild(fila);
          });
        }
      })
      .catch(err => {
        console.error(err);
        document.getElementById('tabla-body').innerHTML =
          '<tr><td colspan="6" style="color:red;">Error al cargar los datos</td></tr>';
      });
  </script>
</body>
</html>
```

![image](https://github.com/user-attachments/assets/102dd56d-aaf3-4b87-81d6-1e9e800d7d63)

---

### 🖥️ Agrega backend en Flask para servir datos desde CSV

Se ha incorporado un pequeño servidor backend en Flask que expone un endpoint `/partidos` para servir los datos del archivo `partidos.csv` como JSON.

```python
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Ruta para leer el CSV y devolver datos JSON
@app.route('/partidos')
def partidos():
    try:
        # Leer archivo CSV (asegúrate que la ruta sea correcta)
        df = pd.read_csv('partidos.csv')

        # Reemplazar NaN por None para evitar errores en JSON
        df = df.where(pd.notnull(df), None)

        # Convertir DataFrame a lista de diccionarios para jsonify
        datos = df.to_dict(orient='records')

        return jsonify(datos)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
```

✅ Este backend permite que `index.html` obtenga dinámicamente los datos de los partidos para su visualización en tabla.

## KPIS

```python
import streamlit as st

def main():
    st.set_page_config(page_title="Dashboard de Fútbol", layout="wide")
    st.title("📊 Dashboard de Partidos de Fútbol")

    df = cargar_datos()

    # Mostrar tabla
    with st.expander("📋 Ver datos originales"):
        st.dataframe(df)

    # KPIs
    st.subheader("📌 Indicadores Clave (KPIs)")
    mostrar_kpis(df)

    # Gráficos
    st.subheader("📈 Goles por Equipo")
    graficar_goles_por_equipo(df)

    st.subheader("⚔️ Distribución de Resultados")
    grafico_resultados(df)

if __name__ == "__main__":
    main()
```

![image](https://github.com/user-attachments/assets/399c431d-3dcd-496e-b016-ad62fbec3221)
![image](https://github.com/user-attachments/assets/c9843135-6104-4453-b41e-a8d210c2cb12)

## Grafos


```python
# 📦 Instalar dependencias necesarias
!apt-get update
!apt-get install -y graphviz libgraphviz-dev
!pip install pygraphviz
!pip install requests pandas matplotlib seaborn networkx scikit-learn
statsmodels
# 📥 Cargar datos desde la API de football-data.org
import requests
import pandas as pd
import networkx as nx # Import the networkx library
from networkx.drawing.nx_agraph import graphviz_layout # Import
graphviz_layout
import matplotlib.pyplot as plt # Add this line to import matplotlib
API_TOKEN = "9b6fb9d028c84f48a2362feb2210d0f9"
HEADERS = {'X-Auth-Token': API_TOKEN}
BASE_URL = "https://api.football-data.org/v4/"
def obtener_partidos(competicion='PL', temporada=2023, limite=100):
url =
f"{BASE_URL}competitions/{competicion}/matches?season={temporada}"
response = requests.get(url, headers=HEADERS)
data = response.json()
partidos = data['matches'][:limite]
return pd.json_normalize(partidos)
df_partidos = obtener_partidos()
print("✅ Partidos descargados:", df_partidos.shape)
df_partidos[['utcDate', 'homeTeam.name', 'awayTeam.name',
'score.fullTime.home', 'score.fullTime.away']].head()
# 🔬 Modelo de regresión lineal (con datos simulados)
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
import seaborn as sns
df_modelo = df_partidos[[
'score.fullTime.home', 'score.fullTime.away',
'homeTeam.name', 'awayTeam.name'
]].copy()
np.random.seed(42)
df_modelo['HS'] = np.random.randint(5, 25, size=len(df_modelo))
df_modelo['AS'] = np.random.randint(5, 25, size=len(df_modelo))
df_modelo['Goles'] = df_modelo['score.fullTime.home'] +
df_modelo['score.fullTime.away']
df_modelo['Disparos'] = df_modelo['HS'] + df_modelo['AS']
df_modelo = df_modelo[['Goles', 'Disparos']].dropna()
print("\n✅ Datos del modelo:", df_modelo.shape)
print(df_modelo.head())
# 📈 Visualizar relación goles/disparos
sns.set(style="whitegrid")
sns.scatterplot(x="Disparos", y="Goles", data=df_modelo)
plt.title("Relación entre disparos y goles")
plt.xlabel("Disparos")
plt.ylabel("Goles")
plt.show()
# 📉 Entrenar modelo
X = df_modelo[["Disparos"]]
y = df_modelo["Goles"]
modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)
print(f"\n📊 Coeficiente (pendiente): {modelo.coef_[0]:.4f}")
print(f"📈 Intercepto: {modelo.intercept_:.4f}")
print(f"📉 R² Score: {r2_score(y, y_pred):.4f}")
# 📋 Statsmodels
X_sm = sm.add_constant(X)
modelo_sm = sm.OLS(y, X_sm).fit()
print(modelo_sm.summary())
# 📈 Gráfico con línea de regresión
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Disparos", y="Goles", data=df_modelo, label="Datos
reales")
plt.plot(df_modelo["Disparos"], y_pred, color="red", label="Regresión
lineal")
plt.title("Regresión lineal: Goles vs Disparos")
plt.xlabel("Disparos")
plt.ylabel("Goles")
plt.legend()
plt.show()
# 📊 Grafo completo de la Premier League (todos los equipos conectados)
def construir_grafo_completo(df):
G = nx.DiGraph()
for
, row in df.iterrows():
_
local = row['homeTeam.name']
visitante = row['awayTeam.name']
goles_local = row['score.fullTime.home']
goles_visitante = row['score.fullTime.away']
if pd.isna(goles_local) or pd.isna(goles_visitante):
continue
if goles_local > goles_visitante:
G.add_edge(local, visitante, weight=3)
elif goles_local < goles_visitante:
G.add_edge(visitante, local, weight=3)
else:
G.add_edge(local, visitante, weight=1)
G.add_edge(visitante, local, weight=1)
return G
# Construir y graficar
G_completo = construir_grafo_completo(df_partidos)
plt.figure(figsize=(15, 12))
pos = graphviz_layout(G_completo, prog='dot')
nx.draw(
G_completo, pos, with_labels=True,
node_color='skyblue', node_size=1600,
edge_color='gray', arrows=True, font_size=9, font_weight='bold'
)
edge_labels = nx.get_edge_attributes(G_completo, 'weight')
nx.draw_networkx_edge_labels(G_completo, pos, edge_labels=edge_labels,
font_color='darkred')
plt.title("🔗 Grafo completo de partidos de la Premier League",
fontsize=16)
plt.axis('off')
plt.show()
# 📊 Grafo reducido con los 7 mejores equipos
def construir_grafo_top7(df):
G = nx.DiGraph()
puntos = {}
# Calcular puntos por equipo
for
, row in df.iterrows():
_
local = row['homeTeam.name']
visitante = row['awayTeam.name']
goles_local = row['score.fullTime.home']
goles_visitante = row['score.fullTime.away']
if pd.isna(goles_local) or pd.isna(goles_visitante):
continue
if goles_local > goles_visitante:
puntos[local] = puntos.get(local, 0) + 3
elif goles_local < goles_visitante:
puntos[visitante] = puntos.get(visitante, 0) + 3
else:
puntos[local] = puntos.get(local, 0) + 1
puntos[visitante] = puntos.get(visitante, 0) + 1
# Seleccionar los 7 mejores
top7 = sorted(puntos.items(), key=lambda x: x[1], reverse=True)[:7]
equipos_top7 = set(e[0] for e in top7)
# Construir grafo solo con partidos entre ellos
for
, row in df.iterrows():
_
local = row['homeTeam.name']
visitante = row['awayTeam.name']
goles_local = row['score.fullTime.home']
goles_visitante = row['score.fullTime.away']
if (local not in equipos_top7) or (visitante not in
equipos_top7):
continue
if pd.isna(goles_local) or pd.isna(goles_visitante):
continue
if goles_local > goles_visitante:
G.add_edge(local, visitante, weight=3)
elif goles_local < goles_visitante:
G.add_edge(visitante, local, weight=3)
else:
G.add_edge(local, visitante, weight=1)
G.add_edge(visitante, local, weight=1)
return G, top7
# Crear grafo
G_top7, top7_lista = construir_grafo_top7(df_partidos)
# Mostrar los 7 mejores equipos
print("\n🏆 Top 7 equipos por puntos:")
for equipo, puntos in top7_lista:
print(f"{equipo}: {puntos} puntos")
# 🎨 Dibujar grafo de los 7 mejores
plt.figure(figsize=(12, 10))
pos = graphviz_layout(G_top7, prog='dot')
nx.draw(
G_top7, pos, with_labels=True,
node_color='gold', node_size=1600,
edge_color='gray', arrows=True, font_size=10, font_weight='bold'
)
edge_labels = nx.get_edge_attributes(G_top7, 'weight')
nx.draw_networkx_edge_labels(G_top7, pos, edge_labels=edge_labels,
font_color='black')
plt.title("🔝 Grafo entre los 7 mejores equipos de la Premier League",
fontsize=16)
plt.axis('off')
plt.show()
# 📊 Grafo de Liverpool con conexiones directas (más limpio y tipo
estrella)
def construir_grafo_estilo_estrella(df, equipo):
G = nx.DiGraph()
df_filtrado = df[(df['homeTeam.name'] == equipo) |
(df['awayTeam.name'] == equipo)]
for
_
, row in df_filtrado.iterrows():
local = row['homeTeam.name']
visitante = row['awayTeam.name']
goles_local = row['score.fullTime.home']
goles_visitante = row['score.fullTime.away']
if pd.isna(goles_local) or pd.isna(goles_visitante):
continue
if equipo in (local, visitante):
rival = visitante if local == equipo else local
if goles_local > goles_visitante and local == equipo:
G.add_edge(equipo, rival, weight=3)
elif goles_visitante > goles_local and visitante == equipo:
G.add_edge(equipo, rival, weight=3)
elif goles_local < goles_visitante and local == equipo:
G.add_edge(rival, equipo, weight=3)
elif goles_visitante < goles_local and visitante == equipo:
G.add_edge(rival, equipo, weight=3)
else:
G.add_edge(equipo, rival, weight=1)
G.add_edge(rival, equipo, weight=1)
return G
# Define the team name to focus on
equipo_focal = "Liverpool FC"
G_limpio = construir_grafo_estilo_estrella(df_partidos, equipo_focal)
print("\n")
# 🖼 Dibujar grafo estilo estrella
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G_limpio, k=0.8, seed=42) # Distribución limpia
tipo red
nx.draw(
G_limpio, pos, with_labels=True,
node_color='lightgreen', node_size=1500,
edge_color='gray', arrows=True, font_size=10, font_weight='bold'
)
edge_labels = nx.get_edge_attributes(G_limpio, 'weight')
nx.draw_networkx_edge_labels(G_limpio, pos, edge_labels=edge_labels,
font_color='red')
plt.title(f"Conexiones directas de {equipo_focal} con sus rivales",
fontsize=14)
plt.axis('off')
plt.show()
# 📐 Layout jerárquico ordenado (tipo estructura matemática)
plt.figure(figsize=(12, 10))
# Use graphviz_layout from networkx
# Ensure G_liverpool is defined - it seems G_limpio is the correct graph
# pos = graphviz_layout(G_liverpool, prog='dot')
pos = graphviz_layout(G_limpio, prog='dot')
nx.draw(
# Ensure G_liverpool is defined - it seems G_limpio is the correct
graph
# G_liverpool, pos, with_labels=True,
G_limpio, pos, with_labels=True,
node_size=1200, node_color='red', font_size=9,
edge_color='gray', arrows=True, font_weight='bold'
)
edge_labels = nx.get_edge_attributes(G_limpio, 'weight') # Use G_limpio
nx.draw_networkx_edge_labels(G_limpio, pos, edge_labels=edge_labels,
font_color='red') # Use G_limpio
print("\n")
plt.title(f"Partidos del {equipo_focal}"
, fontsize=14)
plt.axis('off')
plt.show()
# Mostrar tabla de puntos del Liverpool y sus rivales
# Ensure G_liverpool is defined - it seems G_limpio is the correct graph
# kpis_liverpool =
pd.DataFrame.from_dict(dict(G_liverpool.in_degree(weight='weight')),
orient='index', columns=['Puntos recibidos'])
kpis_equipo_focal =
pd.DataFrame.from_dict(dict(G_limpio.in_degree(weight='weight')),
orient='index', columns=['Puntos recibidos'])
print(f"\n🎯 KPI de puntos (solo {equipo_focal} y sus rivales):\n") # Use
equipo_focal
# print(kpis_liverpool.sort_values(by='Puntos recibidos',
ascending=False))
print(kpis_equipo_focal.sort_values(by='Puntos recibidos',
ascending=False))
```

<img width="781" alt="image" src="https://github.com/user-attachments/assets/1de02059-0ed3-4eb9-bdd6-04e628c89088" />
<img width="781" alt="image" src="https://github.com/user-attachments/assets/09016609-6ed5-4bef-b77c-9416960faedb" />
<img width="781" alt="image" src="https://github.com/user-attachments/assets/6fd4b1af-ccf9-4a00-82ee-047454aae3df" />
<img width="781" alt="image" src="https://github.com/user-attachments/assets/1656d155-8ecb-4fbb-9285-3aba8b2a85ca" />
<img width="781" alt="image" src="https://github.com/user-attachments/assets/6238bf9b-d09e-498a-bf67-eacc48abc5d7" />

## 🔧 Nota

Asegúrate de corregir la condición final para que sea:

```python
if __name__ == "__main__":
```

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
