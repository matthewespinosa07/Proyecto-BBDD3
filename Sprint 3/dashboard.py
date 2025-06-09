import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------
# FUNCIONES
# -------------------------------

def cargar_datos():
    df = pd.read_csv('partidos.csv')

    # Convertir fecha a datetime
    df['fecha'] = pd.to_datetime(df['fecha'])

    # KPIs adicionales
    df['resultado'] = df.apply(lambda row: 'Victoria Local' if row['goles_local'] > row['goles_visitante']
                               else 'Victoria Visitante' if row['goles_local'] < row['goles_visitante']
                               else 'Empate', axis=1)
    
    return df

def mostrar_kpis(df):
    total_partidos = len(df)
    total_goles = df['goles_local'].sum() + df['goles_visitante'].sum()
    promedio_goles = round(total_goles / total_partidos, 2)

    st.metric("📊 Total de Partidos", total_partidos)
    st.metric("⚽ Goles Totales", total_goles)
    st.metric("📈 Promedio de Goles por Partido", promedio_goles)

def graficar_goles_por_equipo(df):
    goles_local = df.groupby('equipo_local')['goles_local'].sum()
    goles_visitante = df.groupby('equipo_visitante')['goles_visitante'].sum()

    goles_totales = goles_local.add(goles_visitante, fill_value=0).sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 4))
    goles_totales.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Goles Totales por Equipo')
    ax.set_ylabel('Goles')
    st.pyplot(fig)

def grafico_resultados(df):
    resultado_counts = df['resultado'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(resultado_counts, labels=resultado_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# -------------------------------
# INTERFAZ STREAMLIT
# -------------------------------

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