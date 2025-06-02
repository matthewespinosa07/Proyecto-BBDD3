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

# 🤝 Autores

- **Santiago Carvajal Fernández** – Líder de Proyecto, Backend & Despliegue
- **Matthew Espinosa** – DBA, Arquitectura y Soporte Técnico

---

# 📄 Licencia Educativa

Proyecto académico para la materia de **Bases de Datos III – ETITC Bogotá**, bajo fines educativos.
