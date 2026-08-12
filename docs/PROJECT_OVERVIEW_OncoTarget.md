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
