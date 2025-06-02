# Proyecto-BBDD3
# Proyecto para la clase de Base de Datos
# Realizado por : Matthew Espinosa y Santiago Carvajal

---

# ⚽ Sistema de Análisis Deportivo Automatizado ⚽⚽⚽

Este proyecto consiste en una API REST desarrollada en Flask que consume datos de fútbol desde 
[football-data.org](https://www.football-data.org/), los almacena en una base de datos relacional PostgreSQL y 
genera visualizaciones interactivas para análisis de rendimiento deportivo o eso creemos que hizo.

---

## 📌 Objetivos del Proyecto

- Automatizar la recolección de datos de partidos y equipos.
- Almacenar la información en una base de datos estructurada.
- Exponer endpoints útiles para la consulta de métricas.
- Visualizar indicadores como posesión, goles, tarjetas y xG.
- Desplegar todo en una instancia EC2 de AWS.

---

## 🧰 Tecnologías Usadas

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

## 🚀 Estructura del Proyecto

