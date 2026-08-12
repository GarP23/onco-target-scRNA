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
