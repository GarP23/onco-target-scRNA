import streamlit as st
import pandas as pd
import numpy as np
import os

# Configuración de página
st.set_page_config(
    page_title="OncoTarget Mining Dashboard",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 BioProject OncoTarget Mining Dashboard (Multi-Cohort)")
st.markdown("Plataforma interactiva para la predicción de resistencia inmunológica sobre 'Basura Genómica' pública.")

# Pestañas
tab1, tab2 = st.tabs(["📊 Análisis de Cohorte Base (PRJEB108071)", "🌐 Comparativa Multi-BioProject"])

with tab1:
    st.header("Evaluación de Riesgo Transversal - PRJEB108071")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Muestras por Perfil Inmunológico")
        df_prj = pd.DataFrame({
            "Perfil": ["Respuesta Moderada", "Baja / Inmunosupresora (Alto Riesgo)"],
            "Muestras": [32, 14],
            "Porcentaje (%)": [69.57, 30.43]
        })
        st.dataframe(df_prj, use_container_width=True)
        st.bar_chart(df_prj.set_index("Perfil")["Muestras"])
        
    with col2:
        st.subheader("Target Discovery — Ejes de Evasión")
        if os.path.exists("onco_targets_priorizados_evasion.csv"):
            df_targets = pd.read_csv("onco_targets_priorizados_evasion.csv")
            st.dataframe(df_targets, use_container_width=True)
        else:
            df_targets_dummy = pd.DataFrame({
                "Target": ["CD274 (PD-L1)", "PDCD1 (PD-1)", "TIGIT", "HAVCR2 (TIM-3)"],
                "Delta_Expresion": [0.042990, -0.209052, -0.229288, -0.503626]
            })
            st.dataframe(df_targets_dummy, use_container_width=True)

with tab2:
    st.header("Matriz Consolidada Multi-BioProject")
    if os.path.exists("mineria_multi_bioproject_resumen.csv"):
        df_multi = pd.read_csv("mineria_multi_bioproject_resumen.csv")
        st.dataframe(df_multi, use_container_width=True)
        st.bar_chart(df_multi.set_index("BioProject")["Pct_Alto_Riesgo (%)"])
    else:
        df_multi_dummy = pd.DataFrame({
            "BioProject": ["PRJEB108071", "PRJNA720232", "PRJNA588993"],
            "Fuente": ["Local / ENA", "ENA / NCBI SRA", "ENA / NCBI SRA"],
            "Total_Muestras": [46, 6, 3],
            "Muestras_Inmunosupresoras": [14, 1, 0],
            "Pct_Alto_Riesgo (%)": [30.43, 16.67, 0.0]
        })
        st.dataframe(df_multi_dummy, use_container_width=True)
        st.bar_chart(df_multi_dummy.set_index("BioProject")["Pct_Alto_Riesgo (%)"])