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
git clone https://github.com/TU_USUARIO/proyecto_futbol.git
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

- Posesión por equipo
- Comparativa de goles
- xG por partido

---

# 🤝 Autores

- **Santiago Carvajal Fernández** – Líder de Proyecto, Backend & Despliegue
- **Matthew Espinosa** – DBA, Arquitectura y Soporte Técnico

---

# 📄 Licencia Educativa

Proyecto académico para la materia de **Bases de Datos III – ETITC Bogotá**, bajo fines educativos.
