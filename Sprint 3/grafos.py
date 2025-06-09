# 📦 Instalar dependencias necesarias
!apt-get update
!apt-get install -y graphviz libgraphviz-dev
!pip install pygraphviz
!pip install requests pandas matplotlib seaborn networkx scikit-learn statsmodels

# 📥 Cargar datos desde la API de football-data.org
import requests
import pandas as pd
import networkx as nx # Import the networkx library
from networkx.drawing.nx_agraph import graphviz_layout # Import graphviz_layout
import matplotlib.pyplot as plt # Add this line to import matplotlib

API_TOKEN = "9b6fb9d028c84f48a2362feb2210d0f9"
HEADERS = {'X-Auth-Token': API_TOKEN}
BASE_URL = "https://api.football-data.org/v4/"

def obtener_partidos(competicion='PL', temporada=2023, limite=100):
    url = f"{BASE_URL}competitions/{competicion}/matches?season={temporada}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    partidos = data['matches'][:limite]
    return pd.json_normalize(partidos)

df_partidos = obtener_partidos()
print("✅ Partidos descargados:", df_partidos.shape)
df_partidos[['utcDate', 'homeTeam.name', 'awayTeam.name', 'score.fullTime.home', 'score.fullTime.away']].head()

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

df_modelo['Goles'] = df_modelo['score.fullTime.home'] + df_modelo['score.fullTime.away']
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
sns.scatterplot(x="Disparos", y="Goles", data=df_modelo, label="Datos reales")
plt.plot(df_modelo["Disparos"], y_pred, color="red", label="Regresión lineal")
plt.title("Regresión lineal: Goles vs Disparos")
plt.xlabel("Disparos")
plt.ylabel("Goles")
plt.legend()
plt.show()

# 📊 Grafo completo de la Premier League (todos los equipos conectados)
def construir_grafo_completo(df):
    G = nx.DiGraph()

    for _, row in df.iterrows():
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
nx.draw_networkx_edge_labels(G_completo, pos, edge_labels=edge_labels, font_color='darkred')

plt.title("🔗 Grafo completo de partidos de la Premier League", fontsize=16)
plt.axis('off')
plt.show()

# 📊 Grafo reducido con los 7 mejores equipos
def construir_grafo_top7(df):
    G = nx.DiGraph()
    puntos = {}

    # Calcular puntos por equipo
    for _, row in df.iterrows():
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
    for _, row in df.iterrows():
        local = row['homeTeam.name']
        visitante = row['awayTeam.name']
        goles_local = row['score.fullTime.home']
        goles_visitante = row['score.fullTime.away']

        if (local not in equipos_top7) or (visitante not in equipos_top7):
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
nx.draw_networkx_edge_labels(G_top7, pos, edge_labels=edge_labels, font_color='black')

plt.title("🔝 Grafo entre los 7 mejores equipos de la Premier League", fontsize=16)
plt.axis('off')
plt.show()

# 📊 Grafo de Liverpool con conexiones directas (más limpio y tipo estrella)
def construir_grafo_estilo_estrella(df, equipo):
    G = nx.DiGraph()
    df_filtrado = df[(df['homeTeam.name'] == equipo) | (df['awayTeam.name'] == equipo)]

    for _, row in df_filtrado.iterrows():
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

# 🖼️ Dibujar grafo estilo estrella
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G_limpio, k=0.8, seed=42)  # Distribución limpia tipo red

nx.draw(
    G_limpio, pos, with_labels=True,
    node_color='lightgreen', node_size=1500,
    edge_color='gray', arrows=True, font_size=10, font_weight='bold'
)
edge_labels = nx.get_edge_attributes(G_limpio, 'weight')
nx.draw_networkx_edge_labels(G_limpio, pos, edge_labels=edge_labels, font_color='red')

plt.title(f"Conexiones directas de {equipo_focal} con sus rivales", fontsize=14)
plt.axis('off')
plt.show()

# 📐 Layout jerárquico ordenado (tipo estructura matemática)
plt.figure(figsize=(12, 10))
# Use graphviz_layout from networkx
# Ensure G_liverpool is defined - it seems G_limpio is the correct graph
# pos = graphviz_layout(G_liverpool, prog='dot')
pos = graphviz_layout(G_limpio, prog='dot')


nx.draw(
    # Ensure G_liverpool is defined - it seems G_limpio is the correct graph
    # G_liverpool, pos, with_labels=True,
    G_limpio, pos, with_labels=True,
    node_size=1200, node_color='red', font_size=9,
    edge_color='gray', arrows=True, font_weight='bold'
)
edge_labels = nx.get_edge_attributes(G_limpio, 'weight') # Use G_limpio
nx.draw_networkx_edge_labels(G_limpio, pos, edge_labels=edge_labels, font_color='red') # Use G_limpio

print("\n")

plt.title(f"Partidos del {equipo_focal}", fontsize=14)
plt.axis('off')
plt.show()

# Mostrar tabla de puntos del Liverpool y sus rivales
# Ensure G_liverpool is defined - it seems G_limpio is the correct graph
# kpis_liverpool = pd.DataFrame.from_dict(dict(G_liverpool.in_degree(weight='weight')), orient='index', columns=['Puntos recibidos'])
kpis_equipo_focal = pd.DataFrame.from_dict(dict(G_limpio.in_degree(weight='weight')), orient='index', columns=['Puntos recibidos'])
print(f"\n🎯 KPI de puntos (solo {equipo_focal} y sus rivales):\n") # Use equipo_focal
# print(kpis_liverpool.sort_values(by='Puntos recibidos', ascending=False))
print(kpis_equipo_focal.sort_values(by='Puntos recibidos', ascending=False))