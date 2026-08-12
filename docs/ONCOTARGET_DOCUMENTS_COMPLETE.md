
==========================================================================================
README_OncoTarget.txt
==========================================================================================

# 🧬 OncoTarget Mining

### Computational Mining of Public Transcriptomic Data for Immune-Evasion Candidate Prioritization

OncoTarget Mining is a computational pipeline that combines single-cell RNA sequencing (scRNA-seq), supervised machine learning, and public transcriptomic datasets to explore immune-response profiles and prioritize immune-evasion candidates.

## 🔬 Overview

The pipeline uses a PBMC 3k reference atlas to derive cytotoxic transcriptional signatures and train a Random Forest classifier. The resulting model is applied to independent public transcriptomic datasets retrieved from ENA / NCBI / SRA.

The project is designed as a reproducible proof-of-concept for transforming heterogeneous public transcriptomic data into computationally testable biological hypotheses.

## 🧠 Pipeline

```text
PBMC 3k scRNA-seq
        │
        ▼
Cytotoxicity signatures
NKG7 · GZMA · CCL5 · GNLY · PRF1
        │
        ▼
Random Forest Classifier
        │
        ▼
Public Transcriptomic Datasets
ENA / NCBI / SRA
        │
        ▼
Functional Stratification
        │
        ▼
Immune-Evasion Candidate Prioritization
        │
        ▼
CD274 / PD-L1
```

## 📊 Main Result

### PRJEB108071

The primary cohort contained 46 samples.

| Predicted profile | Samples | Percentage |
|---|---:|---:|
| Moderate Response | 32 | 69.57% |
| Low / Immunosuppressive | 14 | 30.43% |
| Total | 46 | 100% |

Among the evaluated immune-evasion candidates:

| Candidate | Δ Expression |
|---|---:|
| CD274 (PD-L1) | +0.042990 |
| PDCD1 | -0.209052 |
| TIGIT | -0.229288 |
| HAVCR2 | -0.503626 |

CD274 was the only candidate with a positive expression delta within the evaluated panel and was therefore computationally prioritized for downstream validation.

This is a computational prioritization, not a demonstration of causality, therapeutic efficacy, or clinical utility.

## 🛠️ Technologies

- Python
- Scanpy / AnnData
- Pandas / NumPy
- Scikit-learn
- Joblib
- ENA / NCBI / SRA resources
- Streamlit / interactive visualization components

## 📁 Repository Structure

```text
onco-target-scRNA/
│
├── 01_onco_target_analysis.ipynb
├── 01_fetch_genomic_metadata.py
├── onco_target_random_forest.joblib
├── model_features.json
├── top10_oncotarget_genes.json
├── onco_targets_priorizados_evasion.csv
├── mineria_multi_bioproject_resumen.csv
├── reporte_oncotargets_pbmc3k.csv
├── Informe_Tecnico_OncoTarget_Mining.md
├── requirements.txt
├── README.md
└── LICENSE
```

## 📚 Documentation

- [Project Overview](PROJECT_OVERVIEW.md)
- [Scientific / Executive Report](Informe_Tecnico_OncoTarget_Mining.md)

The Project Overview explains the questions, objectives, scope, results, limitations, and potential R&D relevance of the project.

## 🚀 Reproducibility

```bash
git clone https://github.com/GarP23/onco-target-scRNA.git
cd onco-target-scRNA
python -m venv .venv
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

The main analysis is documented in:

```text
01_onco_target_analysis.ipynb
```

## ⚠️ Scientific Scope

OncoTarget Mining is a computational research and data-mining project.

It does not provide medical diagnosis, patient prognosis, therapeutic recommendations, clinical biomarkers, or proof of causal biological mechanisms.

The results are intended to generate hypotheses that require independent computational and experimental validation.

## 👤 Author

GarP23

Repository:
https://github.com/GarP23/onco-target-scRNA

## 📜 License

MIT License



==========================================================================================
PROJECT_OVERVIEW_OncoTarget.txt
==========================================================================================

# OncoTarget Mining — Project Overview

## Ficha Ejecutiva: Preguntas, Objetivos, Alcance, Resultados y Potencial de I+D

> **Nota del autor**
>
> Este proyecto fue desarrollado desde una perspectiva de análisis de datos y bioinformática computacional. No se presenta como una herramienta médica ni como un sistema de diagnóstico. Su objetivo es demostrar cómo una pipeline reproducible puede integrar datos transcriptómicos públicos, aprendizaje automático y análisis computacional para generar hipótesis biológicas susceptibles de validación posterior.

---

# 1. ¿Qué es OncoTarget Mining?

OncoTarget Mining es una pipeline computacional orientada a la reutilización transversal de datos transcriptómicos públicos.

El proyecto combina:

- análisis de scRNA-seq;
- extracción de firmas transcriptómicas;
- aprendizaje automático supervisado;
- recuperación programática de datos públicos;
- estratificación de muestras;
- análisis de genes asociados a evasión inmune;
- priorización computacional de candidatos.

La idea central es utilizar información molecular ya disponible públicamente para realizar una primera fase de exploración antes de plantear análisis o experimentos adicionales.

---

# 2. ¿Qué problema intenta abordar?

Existe una gran cantidad de datasets transcriptómicos públicos generados para estudios independientes. Una dificultad práctica consiste en transformar ese volumen de información en señales comparables y preguntas concretas de investigación.

OncoTarget Mining explora un enfoque en el que:

```text
Datos públicos heterogéneos
        ↓
Representación funcional
        ↓
Modelo predictivo
        ↓
Estratificación
        ↓
Priorización de candidatos
        ↓
Hipótesis de investigación
```

El proyecto no pretende resolver por sí solo la validación biológica. Su propósito es reducir el espacio inicial de búsqueda y proporcionar una metodología reproducible para explorarlo.

---

# 3. ¿Qué preguntas responde?

## 3.1. Pregunta técnica

¿Es posible utilizar un modelo de Machine Learning entrenado a partir de datos scRNA-seq de referencia para clasificar perfiles transcriptómicos de muestras externas procedentes de repositorios públicos?

En este proyecto, se entrenó un Random Forest a partir de características derivadas del atlas PBMC 3k y posteriormente se aplicó sobre muestras independientes.

## 3.2. Pregunta biológica computacional

Dentro de las muestras clasificadas con un perfil de baja citotoxicidad / inmunosupresor, ¿cuál de los candidatos de evasión inmune evaluados presenta un comportamiento diferencial positivo respecto al grupo de respuesta moderada?

El panel evaluado incluyó:

- CD274
- PDCD1
- TIGIT
- HAVCR2

En la cohorte principal, CD274 fue el único candidato con delta de expresión positivo.

## 3.3. Pregunta de automatización

¿Cómo puede automatizarse la recuperación y análisis de datasets transcriptómicos públicos para evitar que la exploración dependa exclusivamente de procesos manuales?

La pipeline utiliza recursos públicos de ENA / NCBI / SRA y automatiza parte del flujo de recuperación, procesamiento e inferencia.

---

# 4. Objetivo principal

Desarrollar una infraestructura computacional reproducible que conecte:

```text
scRNA-seq
+
Machine Learning
+
Repositorios genómicos públicos
+
Análisis transcriptómico
=
Priorización computacional de candidatos
```

El objetivo concreto del proyecto no es demostrar una nueva terapia, sino demostrar la viabilidad de este flujo de análisis.

---

# 5. Objetivos secundarios

1. Derivar firmas transcriptómicas asociadas a actividad citotóxica.
2. Entrenar y serializar un modelo Random Forest.
3. Aplicar el modelo sobre muestras transcriptómicas independientes.
4. Estratificar muestras según el perfil predicho.
5. Comparar genes relacionados con evasión inmune.
6. Generar artefactos reproducibles en formatos CSV, JSON y Markdown.
7. Facilitar la exploración de los resultados mediante una interfaz interactiva.

---

# 6. Datos utilizados

## Referencia

Atlas PBMC 3k:

- 2.638 células
- 1.826 genes

## Firma funcional

El modelo utiliza genes asociados con actividad citotóxica, incluyendo:

- NKG7
- GZMA
- CCL5
- GNLY
- PRF1

## Cohorte principal

BioProject:

PRJEB108071

Número de muestras analizadas:

46

---

# 7. ¿Qué produjo realmente el proyecto?

## Estratificación

| Perfil predicho | Muestras | Porcentaje |
|---|---:|---:|
| Respuesta Moderada | 32 | 69.57% |
| Baja / Inmunosupresora | 14 | 30.43% |
| Total | 46 | 100.00% |

## Priorización

| Candidato | Delta de expresión |
|---|---:|
| CD274 | +0.042990 |
| PDCD1 | -0.209052 |
| TIGIT | -0.229288 |
| HAVCR2 | -0.503626 |

CD274 fue el único candidato del panel con delta positivo.

---

# 8. ¿Qué significa este resultado?

El resultado indica que, bajo el esquema analítico utilizado, CD274 fue el candidato que presentó el comportamiento diferencial positivo más claro dentro del panel evaluado en PRJEB108071.

Esto permite formular la siguiente hipótesis:

> CD274 / PD-L1 merece una investigación posterior como posible componente del perfil inmunosupresor identificado en esta cohorte.

No debe interpretarse como:

> "CD274 causa la inmunosupresión."

Ni como:

> "CD274 es una diana terapéutica validada."

La primera afirmación requeriría evidencia causal. La segunda requeriría validación preclínica y clínica.

---

# 9. Alcance

## Incluye

- Procesamiento de un atlas scRNA-seq de referencia.
- Construcción de características transcriptómicas.
- Entrenamiento de Random Forest.
- Serialización del modelo.
- Recuperación de información de repositorios públicos.
- Inferencia sobre cohortes independientes.
- Estratificación funcional.
- Comparación de candidatos de evasión inmune.
- Generación de resultados reproducibles.

## Fuera de alcance

- Diagnóstico médico.
- Pronóstico individual.
- Selección de tratamientos.
- Validación experimental.
- Ensayos clínicos.
- Demostración de causalidad.
- Desarrollo de un biomarcador clínico.
- Corrección exhaustiva de todos los posibles efectos de lote entre estudios.

---

# 10. ¿Qué preguntas de I+D puede ayudar a explorar?

### Reutilización de datos

¿Existen datasets públicos que contengan señales relacionadas con una pregunta biológica que originalmente no era el objetivo principal del estudio?

### Priorización

¿Qué candidatos merecen una investigación posterior antes de invertir recursos en validaciones más costosas?

### Estratificación

¿Existen subgrupos transcriptómicos dentro de una cohorte que puedan justificar una investigación diferenciada?

### Vigilancia de datasets

¿Puede automatizarse la búsqueda de nuevos estudios públicos relevantes para una hipótesis concreta?

### Comparación transversal

¿Una firma computacional produce señales similares cuando se aplica a cohortes independientes?

---

# 11. ¿Qué posible valor tiene desde una perspectiva de industria?

La aplicación industrial debe entenderse como un potencial de I+D, no como un producto clínico validado.

## 11.1. Reutilización de datos

Una organización puede explorar datos públicos antes de generar nuevos experimentos.

Potencialmente, esto puede ayudar a:

- identificar cohortes relevantes;
- encontrar señales previamente no exploradas;
- priorizar análisis;
- diseñar experimentos posteriores.

## 11.2. Priorización de investigación

Un pipeline de este tipo puede funcionar como una etapa inicial de filtrado.

```text
Muchos candidatos
       ↓
Screening computacional
       ↓
Menos candidatos
       ↓
Validación experimental
```

Este proyecto no cuantifica todavía cuánto dinero o tiempo se ahorraría.

## 11.3. Estratificación exploratoria

La clasificación computacional puede ayudar a identificar subconjuntos de muestras que merezcan un análisis diferenciado.

## 11.4. Automatización

La recuperación programática de información pública puede convertirse en una infraestructura reutilizable para análisis periódicos de nuevos datasets.

---

# 12. ¿Qué valor demuestra realmente el proyecto?

El principal resultado no es únicamente CD274.

El proyecto demuestra un flujo reproducible:

```text
Dataset de referencia
        ↓
Firma funcional
        ↓
Machine Learning
        ↓
Datos públicos externos
        ↓
Clasificación
        ↓
Priorización
        ↓
Hipótesis
```

CD274 representa el resultado principal obtenido en la cohorte analizada.

La arquitectura es el resultado metodológico más generalizable.

---

# 13. Limitaciones

1. El modelo depende de las características aprendidas a partir del atlas de referencia.
2. La transferencia hacia datasets externos puede introducir diferencias de distribución.
3. Los datasets públicos presentan heterogeneidad técnica y biológica.
4. El panel de candidatos evaluado es limitado.
5. Los deltas de expresión no demuestran causalidad.
6. El resultado de una cohorte no garantiza reproducibilidad en otras cohortes.
7. No se ha realizado validación experimental del candidato.

---

# 14. Próximos pasos

## Corto plazo

- Validar CD274 en cohortes adicionales.
- Ampliar el panel de candidatos.
- Incorporar métricas formales de rendimiento del clasificador.
- Mejorar la documentación de reproducibilidad.

## Medio plazo

- Incorporar corrección / modelado de efectos de lote.
- Automatizar el procesamiento de nuevas cohortes.
- Añadir análisis de rutas y redes.
- Comparar varios algoritmos de clasificación.

## Largo plazo

Construir una infraestructura de minería sistemática capaz de identificar y priorizar señales biológicas emergentes en nuevos datasets públicos.

---

# 15. Conclusión ejecutiva

OncoTarget Mining demuestra la viabilidad de utilizar datos transcriptómicos públicos y Machine Learning para generar hipótesis de investigación de manera reproducible.

En la cohorte PRJEB108071, 14 de 46 muestras (30.43%) fueron clasificadas como Baja / Inmunosupresora. Dentro del panel evaluado, CD274 presentó un delta positivo de +0.042990 y fue priorizado computacionalmente.

El proyecto debe entenderse como una plataforma de exploración y generación de hipótesis.

Su valor potencial para I+D está en conectar:

**datos públicos → análisis computacional → priorización → validación posterior.**

---

# 16. Nota de interpretación

Este documento no constituye asesoramiento médico, diagnóstico, pronóstico ni recomendación terapéutica.

Los resultados corresponden al análisis computacional realizado sobre las cohortes y características descritas en el proyecto y requieren validación independiente antes de cualquier interpretación clínica o aplicación experimental.



==========================================================================================
R&D_COMMERCIAL_PERSPECTIVE_OncoTarget.txt
==========================================================================================

# OncoTarget Mining — R&D / Commercial Perspective

## Documento de posicionamiento técnico y potencial de aplicación

> Este documento describe posibles usos de OncoTarget Mining desde una perspectiva de análisis de datos e I+D. Las aplicaciones descritas como "potenciales" no deben interpretarse como capacidades comerciales ya validadas ni como resultados clínicos.

---

# 1. ¿Qué problema intenta resolver?

En biotecnología y ciencias de la vida existe una gran cantidad de información transcriptómica disponible públicamente.

El reto no es únicamente disponer de datos, sino:

- localizar datasets relevantes;
- procesarlos;
- compararlos;
- identificar patrones;
- priorizar hipótesis;
- decidir qué merece una validación posterior.

OncoTarget Mining explora una solución computacional para esa primera fase.

---

# 2. Propuesta de valor

La propuesta conceptual es:

> Convertir datasets transcriptómicos públicos heterogéneos en señales y candidatos que puedan ser investigados posteriormente.

La arquitectura se puede resumir como:

```text
Public Data
    ↓
Automated Retrieval
    ↓
Functional Representation
    ↓
Machine Learning
    ↓
Sample Stratification
    ↓
Candidate Prioritization
    ↓
Research Hypothesis
```

---

# 3. ¿Qué preguntas de I+D puede ayudar a responder?

## Pregunta 1

¿Podemos reutilizar datasets públicos para explorar una pregunta que no era necesariamente el objetivo original del estudio?

**Potencial:** sí, mediante minería computacional y definición de firmas específicas.

## Pregunta 2

¿Podemos identificar subgrupos de muestras que merezcan una investigación específica?

**Potencial:** sí, mediante clasificación o estratificación basada en características transcriptómicas.

## Pregunta 3

¿Podemos reducir el número de candidatos que deben evaluarse experimentalmente?

**Potencial:** un screening computacional puede utilizarse como etapa previa a la validación experimental.

Importante: este proyecto no cuantifica todavía cuánto dinero o tiempo se ahorraría.

## Pregunta 4

¿Podemos reutilizar una firma computacional sobre múltiples cohortes?

La arquitectura está diseñada para esa reutilización.

La generalización a nuevas cohortes debe validarse individualmente.

## Pregunta 5

¿Podemos construir un sistema de vigilancia de nuevos datasets?

La recuperación programática desde repositorios públicos constituye una base para desarrollar una infraestructura de este tipo.

---

# 4. Posibles aplicaciones

## 4.1. Target Discovery Exploratorio

Una organización podría utilizar un sistema similar para priorizar genes o rutas que merezcan análisis adicional.

```text
Genome-wide / transcriptomic candidates
             ↓
Computational screening
             ↓
Prioritized candidates
             ↓
Experimental validation
```

En este proyecto, CD274 constituye un ejemplo de candidato priorizado.

## 4.2. Data Mining para I+D

La infraestructura podría utilizarse para buscar señales en datasets que ya existen.

Esto puede ser especialmente interesante cuando una pregunta de investigación cambia después de que los datos hayan sido publicados.

## 4.3. Cohort Stratification

El análisis computacional puede ayudar a dividir grandes conjuntos de muestras en perfiles funcionales.

Esto podría servir como etapa exploratoria para:

- análisis posteriores;
- selección de cohortes;
- generación de hipótesis;
- diseño experimental.

No equivale a una clasificación clínica de pacientes.

## 4.4. Scientific Intelligence

Una evolución del sistema podría utilizar datasets y publicaciones públicas para monitorizar:

- nuevas cohortes;
- nuevos biomarcadores;
- nuevas asociaciones moleculares;
- nuevas líneas de investigación.

Esto requeriría componentes adicionales que no forman parte de la implementación actual.

---

# 5. ¿Qué aporta frente a un análisis manual?

Un flujo manual puede verse así:

```text
Buscar estudio
    ↓
Descargar datos
    ↓
Procesarlos
    ↓
Explorarlos
    ↓
Comparar genes
    ↓
Repetir
```

Una infraestructura automatizada puede aproximarse a:

```text
Definir pregunta
    ↓
Buscar datasets
    ↓
Procesar
    ↓
Inferir
    ↓
Comparar
    ↓
Generar reporte
```

La ventaja potencial es la repetibilidad y escalabilidad del proceso, no una garantía de que todos los resultados sean correctos.

---

# 6. ¿Qué demuestra este proyecto?

El proyecto demuestra concretamente:

- integración de scRNA-seq y Machine Learning;
- entrenamiento de un Random Forest;
- serialización de un modelo;
- aplicación sobre datos externos;
- minería de recursos públicos;
- estratificación de una cohorte;
- priorización computacional de candidatos;
- generación de artefactos reproducibles.

En PRJEB108071:

- 46 muestras;
- 32 con Respuesta Moderada;
- 14 con perfil Baja / Inmunosupresora;
- 30.43% en el segundo grupo;
- CD274 como único candidato con delta positivo dentro del panel evaluado.

---

# 7. ¿Qué NO demuestra?

No demuestra:

- que CD274 sea causal;
- que PD-L1 sea necesariamente la mejor diana terapéutica;
- que el modelo sea clínicamente válido;
- que el sistema diagnostique pacientes;
- que exista eficacia terapéutica;
- que se produzca un ahorro económico cuantificado;
- que los resultados sean universalmente reproducibles.

Estas afirmaciones requerirían estudios adicionales.

---

# 8. ¿Cuál podría ser el producto futuro?

Una evolución conceptual podría ser una plataforma de:

## Public Transcriptomic Intelligence

Con módulos para:

1. búsqueda automática de datasets;
2. descarga de metadatos;
3. control de calidad;
4. procesamiento;
5. inferencia;
6. comparación entre cohortes;
7. ranking de candidatos;
8. generación automática de informes.

La versión actual debe considerarse un proof-of-concept, no un producto terminado.

---

# 9. Potencial para Biotech / Pharma

El proyecto puede servir como demostración de competencias en:

- bioinformática;
- data engineering científico;
- machine learning;
- análisis de datos ómicos;
- automatización;
- reproducibilidad;
- scientific computing;
- target prioritization.

Desde una perspectiva de industria, la pregunta más interesante no es:

> "¿Encontró una diana?"

sino:

> "¿Puede una infraestructura computacional reducir sistemáticamente el espacio de búsqueda de hipótesis antes de realizar experimentos?"

Ese es el potencial que debería explorarse en futuras versiones.

---

# 10. Modelo conceptual de valor

```text
Datos públicos
     │
     ▼
Menor barrera de acceso a información
     │
     ▼
Screening computacional
     │
     ▼
Priorización
     │
     ▼
Hipótesis
     │
     ▼
Validación experimental
     │
     ▼
Decisión de I+D
```

OncoTarget Mining ocupa principalmente las etapas de:

**datos → screening → priorización → hipótesis.**

Las etapas experimentales y clínicas están fuera del alcance actual.

---

# 11. Oportunidades futuras

### A. Escalabilidad

Aplicar el sistema a cientos o miles de datasets.

### B. Multi-omics

Incorporar transcriptómica, epigenómica, proteómica y mutaciones.

### C. Knowledge Graphs

Relacionar genes, enfermedades, estudios y mecanismos.

### D. Literature Mining

Conectar resultados computacionales con literatura científica.

### E. Automated Monitoring

Detectar automáticamente nuevos datasets relacionados con una hipótesis.

### F. Validation Layer

Añadir evidencia independiente antes de elevar un candidato en el ranking.

---

# 12. Posicionamiento recomendado

La descripción más segura y precisa sería:

> **OncoTarget Mining is a computational data-mining proof-of-concept for prioritizing biological hypotheses from public transcriptomic datasets.**

En español:

> **OncoTarget Mining es una prueba de concepto de minería computacional de datos transcriptómicos públicos orientada a priorizar hipótesis biológicas para investigación posterior.**

Esta formulación refleja mejor lo que actualmente demuestra el proyecto que expresiones como "plataforma de descubrimiento de fármacos" o "sistema de diagnóstico".

---

# 13. Conclusión

El principal valor potencial de OncoTarget Mining reside en la combinación de:

**datos públicos + automatización + Machine Learning + análisis transcriptómico + priorización.**

El resultado obtenido con CD274 demuestra que la arquitectura puede producir una hipótesis molecular concreta a partir de datos públicos.

El siguiente nivel de valor no sería simplemente encontrar más candidatos, sino demostrar que el proceso:

1. escala;
2. reproduce señales en cohortes independientes;
3. mejora la priorización respecto a estrategias simples;
4. genera candidatos que posteriormente se validan experimentalmente.

Ese sería el camino para transformar el proof-of-concept actual en una plataforma de I+D más robusta.



==========================================================================================
PAPER_EJECUTIVO_OncoTarget.txt
==========================================================================================

# OncoTarget Mining: Priorización Computacional de Candidatos de Evasión Inmune mediante Minería Transversal de Datos Transcriptómicos Públicos

## Paper Ejecutivo

---

## Resumen

### Antecedentes

La disponibilidad creciente de datos transcriptómicos públicos ofrece una oportunidad para reutilizar información molecular generada originalmente para objetivos experimentales distintos y explorar nuevas hipótesis biológicas. Sin embargo, la heterogeneidad entre estudios y la ausencia de anotaciones funcionales homogéneas dificultan su explotación sistemática para la investigación de mecanismos de evasión inmune.

### Objetivo

Desarrollar una pipeline computacional reproducible que combine análisis transcriptómico unicelular, aprendizaje automático supervisado y minería transversal de datasets públicos para estratificar perfiles funcionales de respuesta inmune y priorizar candidatos asociados a evasión inmunitaria.

### Métodos

Se utilizó un atlas de referencia PBMC 3k compuesto por 2.638 células y 1.826 genes para caracterizar firmas transcriptómicas asociadas a actividad citotóxica. El análisis empleó marcadores como NKG7, GZMA, CCL5, GNLY y PRF1. Sobre estas características se entrenó un clasificador Random Forest, posteriormente aplicado a muestras transcriptómicas independientes obtenidas de recursos públicos de ENA/NCBI/SRA.

La cohorte principal correspondió al BioProject PRJEB108071, con 46 muestras. Las muestras fueron estratificadas según el perfil funcional predicho y posteriormente se evaluaron genes relacionados con regulación y evasión inmune, incluyendo CD274, PDCD1, TIGIT y HAVCR2.

### Resultados

En PRJEB108071, 32 de 46 muestras (69.57%) fueron clasificadas como Respuesta Moderada, mientras que 14 muestras (30.43%) fueron clasificadas como Baja/Inmunosupresora.

Entre los genes evaluados, CD274 presentó un delta de expresión positivo de +0.042990. PDCD1, TIGIT y HAVCR2 presentaron deltas negativos de -0.209052, -0.229288 y -0.503626, respectivamente.

CD274 fue por tanto priorizado computacionalmente como el principal candidato dentro del panel evaluado.

### Conclusión

OncoTarget Mining demuestra la viabilidad de combinar firmas derivadas de scRNA-seq, clasificación mediante Random Forest y minería de datasets transcriptómicos públicos para generar hipótesis sobre mecanismos de evasión inmune. La priorización de CD274 en la cohorte PRJEB108071 constituye una hipótesis computacional que requiere validación independiente y experimental antes de cualquier interpretación causal o clínica.

---

# 1. Introducción

La caracterización de mecanismos de evasión inmune constituye un área relevante de investigación en biología tumoral. La respuesta inmunitaria depende de múltiples interacciones entre células, genes y señales moleculares, por lo que la interpretación de perfiles transcriptómicos puede proporcionar información útil para formular hipótesis sobre estados funcionales.

Los repositorios públicos de secuenciación contienen una gran cantidad de datos generados para estudios independientes. Estos datasets pueden contener señales relevantes para nuevas preguntas de investigación incluso cuando el objetivo original del estudio era diferente.

OncoTarget Mining explora una estrategia computacional para reutilizar estos datos mediante una arquitectura que conecta un atlas de referencia de scRNA-seq con aprendizaje automático y minería transversal de datasets públicos.

La hipótesis de trabajo es que una firma transcriptómica derivada de un atlas de referencia puede utilizarse para estratificar muestras independientes según perfiles funcionales de actividad citotóxica y, posteriormente, explorar genes relacionados con evasión inmune.

---

# 2. Materiales y Métodos

## 2.1. Diseño general

```text
PBMC 3k
   ↓
Procesamiento scRNA-seq
   ↓
Caracterización de firmas citotóxicas
   ↓
Random Forest
   ↓
Modelo predictivo
   ↓
Datasets públicos ENA / NCBI / SRA
   ↓
Predicción por muestra
   ↓
Estratificación funcional
   ↓
Comparación de genes de evasión inmune
   ↓
Priorización de candidatos
```

## 2.2. Atlas de referencia

Se utilizó un atlas PBMC 3k como referencia.

La matriz analizada contiene:

- 2.638 células;
- 1.826 genes.

El procesamiento se realizó utilizando herramientas del ecosistema Scanpy/AnnData.

## 2.3. Firma citotóxica

La caracterización funcional se apoyó en:

- NKG7
- GZMA
- CCL5
- GNLY
- PRF1

Estas características se utilizaron como base para construir las variables empleadas posteriormente por el modelo.

## 2.4. Modelo de Machine Learning

Se entrenó un clasificador Random Forest supervisado.

El modelo se utilizó para categorizar perfiles en:

- Alta Citotoxicidad;
- Respuesta Moderada;
- Baja / Inmunosupresora.

El modelo entrenado fue serializado para permitir su reutilización.

## 2.5. Datos públicos

La pipeline utiliza recursos públicos asociados con ENA, NCBI y SRA.

La cohorte principal fue PRJEB108071.

Número de muestras analizadas: 46.

## 2.6. Estratificación

| Perfil | n | % |
|---|---:|---:|
| Respuesta Moderada | 32 | 69.57 |
| Baja / Inmunosupresora | 14 | 30.43 |
| Total | 46 | 100.00 |

## 2.7. Priorización de candidatos

Se evaluó:

- CD274;
- PDCD1;
- TIGIT;
- HAVCR2.

| Candidato | Δ expresión |
|---|---:|
| CD274 | +0.042990 |
| PDCD1 | -0.209052 |
| TIGIT | -0.229288 |
| HAVCR2 | -0.503626 |

---

# 3. Resultados

## 3.1. Estratificación de la cohorte

El modelo clasificó 32 de 46 muestras como Respuesta Moderada y 14 de 46 como Baja/Inmunosupresora.

El segundo grupo representa el 30.43% de la cohorte.

## 3.2. Priorización de CD274

CD274 fue el único candidato del panel con un delta de expresión positivo:

Δ = +0.042990.

Los restantes genes mostraron valores negativos.

Por este criterio, CD274 fue priorizado como el principal candidato computacional identificado en la cohorte.

---

# 4. Discusión

El resultado principal demuestra una conexión entre una firma funcional derivada de scRNA-seq y la estratificación de muestras transcriptómicas independientes.

La identificación de un subconjunto de 14 muestras con perfil Baja/Inmunosupresora permite posteriormente comparar genes relacionados con regulación inmune.

Dentro del panel evaluado, CD274 presentó el comportamiento diferencial positivo.

Desde una perspectiva de generación de hipótesis, este resultado justifica considerar CD274 como candidato para investigaciones posteriores.

Sin embargo, el análisis no demuestra que CD274 sea responsable del fenotipo observado. El delta de expresión constituye una señal de priorización y no una prueba de causalidad.

---

# 5. Valor metodológico

La contribución general del proyecto consiste en demostrar un flujo que transforma:

```text
Datos públicos
     ↓
Características funcionales
     ↓
Machine Learning
     ↓
Estratificación
     ↓
Priorización
     ↓
Hipótesis
```

La arquitectura puede potencialmente reutilizarse para otras cohortes y otros paneles de genes.

---

# 6. Limitaciones

1. El modelo depende de las características aprendidas a partir del atlas de referencia.
2. La transferencia a datasets externos puede introducir diferencias de distribución.
3. Los datasets públicos presentan heterogeneidad técnica y biológica.
4. El panel de candidatos evaluado es limitado.
5. Los deltas de expresión no demuestran causalidad.
6. El resultado de una cohorte no garantiza reproducibilidad en otras cohortes.
7. No se ha realizado validación experimental del candidato.

---

# 7. Implicaciones para investigación futura

1. Validar CD274 en cohortes adicionales.
2. Ampliar el panel de candidatos.
3. Incorporar corrección de efectos de lote.
4. Evaluar el rendimiento del modelo mediante métricas formales.
5. Incorporar análisis de rutas.
6. Integrar otras capas ómicas.
7. Automatizar el análisis de nuevos datasets.

---

# 8. Conclusión

OncoTarget Mining proporciona una prueba de concepto para la minería computacional de datos transcriptómicos públicos.

En PRJEB108071, 14 de 46 muestras (30.43%) fueron clasificadas como Baja/Inmunosupresora.

Dentro del panel analizado, CD274 presentó un delta positivo de +0.042990 y fue priorizado computacionalmente.

El resultado más generalizable del proyecto es la arquitectura que conecta scRNA-seq, Machine Learning y minería de datos públicos para transformar datasets heterogéneos en hipótesis investigables.

---

# 9. Disponibilidad

Repositorio:

https://github.com/GarP23/onco-target-scRNA

El proyecto incluye código, modelo serializado, resultados tabulares y documentación técnica.

---

# 10. Declaración

Este trabajo es un estudio computacional exploratorio.

No constituye diagnóstico, pronóstico, recomendación terapéutica ni evidencia clínica.

La priorización de CD274 debe considerarse una hipótesis que requiere validación independiente y experimental.


