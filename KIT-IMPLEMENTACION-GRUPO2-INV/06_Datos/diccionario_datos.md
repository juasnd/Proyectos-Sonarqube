# Diccionario de datos

- `participant_id`: código anónimo P01...Pn.
- `treatment`: `control` o `experimental`.
- `experience_block`: `bajo` o `alto`.
- `included`: 1 incluido, 0 excluido.
- `requirements_count`: requisitos entregados.
- `total_words`: palabras del artefacto.
- `ambiguity_defects_consensus`: defectos aceptados tras consenso.
- `defect_free_requirements`: requisitos sin defectos léxicos.
- `completion_score`: funcionalidades esperadas cubiertas, 0-10.
- `time_minutes`: minutos efectivos.
- `difficulty_1_5`: dificultad percibida.
- `deviation_flag`: 1 si existió una desviación relevante.

Variables derivadas:
- `ambiguity_density_100 = ambiguity_defects_consensus / total_words * 100`
- `defect_free_pct = defect_free_requirements / requirements_count * 100`
