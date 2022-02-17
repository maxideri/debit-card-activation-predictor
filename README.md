# debit-card-activation-predictor
Modelo de boosting que a partir de los datos del usuario de una fintech predice si activaría la tarjeta de debito que ofrece la misma empresa

Para esto se estableció como base el rendimiento ROC_AUC de un modelo Naive Bayes, y en sucesivas etapas se fue optimizado un modelo LigthGBM:
- Primero se evaluó el rendimiento con los hiperperametros por defecto
- Luego se realizó una optimización bayesiana
- Sobre el modelo obtenido previamente, se realizó una feature selection de aquellas de mayor impacto como predictores, y se volvió a reentrenar el modelo.

Para interactuar con el predictor obtenido de una manera mas gráfica se puede usar el archivo streamlit.py. Para ejecutarlo hay que correr el siguiente comando:
streamlit run <path>/stream.py

Completando los campos correspondientes, nos dirá la probabilidad de que el usuario active o no la tarjeta de débito, la influencia de cada una de las features, y si el resultado es positivo, en cuanto dias desde la solicitudad de la tarjeta se haría la activación
