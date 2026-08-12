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
