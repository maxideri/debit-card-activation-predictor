# debit-card-activation-predictor
Modelo de boosting que a partir de los datos del usuario de una fintech predice si activaría la tarjeta de debito que ofrece la misma empresa

Para esto se estableció como base el rendimiento ROC_AUC de un modelo Naive Bayes, y en sucesivas etapas se fue optimizado un modelo LigthGBM:
- Primero se evaluó el rendimiento con los hiperperametros por defecto
- Luego se realizó una optimización bayesiana
- Sobre el modelo obtenido previamente, se realizó una feature selection de aquellas de mayor impacto como predictores, y se volvió a reentrenar el modelo.

Para interactuar con el predictor obtenido de una manera mas gráfica se puede usar el archivo streamlit.py. Para ejecutarlo hay que correr el siguiente comando:
streamlit run <path>/stream.py

Completando los campos correspondientes, nos dirá la probabilidad de que el usuario active o no la tarjeta de débito, la influencia de cada una de las features, y si el resultado es positivo, en cuanto dias desde la solicitudad de la tarjeta se haría la activación

![image](https://user-images.githubusercontent.com/77274340/154402920-4ea47d7b-b111-424a-bbaa-6b6f0c5bf4c8.png)
![image](https://user-images.githubusercontent.com/77274340/154402930-430c7d5e-c090-41db-9f2b-acac59785aa8.png)
![image](https://user-images.githubusercontent.com/77274340/154402963-184ab97d-b7e8-4a39-92c6-0bcb98f8b9ab.png)
![image](https://user-images.githubusercontent.com/77274340/154402977-afe44b8b-8ff8-49bf-adea-aded468fcafc.png)
![image](https://user-images.githubusercontent.com/77274340/154403009-ca001df2-ad93-48a3-9b52-82f1e332854a.png)
![image](https://user-images.githubusercontent.com/77274340/154403051-144a7187-0c73-4e8b-8044-655c901ddcb9.png)
![image](https://user-images.githubusercontent.com/77274340/154403075-5e421c07-581b-46c9-99ee-0d5c000d9667.png)
![image](https://user-images.githubusercontent.com/77274340/154403104-fdb1fc6b-1f5d-46ab-84c3-c8954192a531.png)
![image](https://user-images.githubusercontent.com/77274340/154403143-fd7284a2-4492-46b1-9cf3-b2ffb7f49938.png)
![image](https://user-images.githubusercontent.com/77274340/154403151-c4f0d77d-a91c-48fa-9e46-540b2f83d56f.png)
![image](https://user-images.githubusercontent.com/77274340/154403168-2155cd88-caad-40fc-8fd2-63dedbd82401.png)
![image](https://user-images.githubusercontent.com/77274340/154403212-a0594adc-605d-4318-8678-5cf45976cb18.png)
![image](https://user-images.githubusercontent.com/77274340/154403261-cc8cca0e-9c2c-4934-b606-52748ae95d85.png)
![image](https://user-images.githubusercontent.com/77274340/154403286-c168799f-0c7e-4836-92b1-823c8660cf77.png)
![image](https://user-images.githubusercontent.com/77274340/154403324-996ae8f4-1942-4106-b23f-8031a9822b0f.png)




