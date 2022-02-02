import streamlit as st
import pickle
import numpy as np
import pandas as pd
import shap
import streamlit.components.v1 as components
import plotly.express as px

columnas = ['flag_seller', 'flag_credito', 'tpn_month', 'tpv_month',
    'tpn_billetera', 'tpn_seguros', 'tpn_ingresos', 'tpn_pagos_online',
    'tpn_pagos_commerce', 'dias_ult', 'flag_wallet', 'flag_seguros',
    'flag_ingresos', 'flag_pagos_online', 'flag_pagos_commerce',
    'LYLT_Bajo', 'LYLT_Medio', 'GEO_STATE_Baja California',
    'GEO_STATE_Baja California Sur', 'GEO_STATE_Campeche',
    'GEO_STATE_Chiapas', 'GEO_STATE_Chihuahua',
    'GEO_STATE_Ciudad de México', 'GEO_STATE_Coahuila de Zaragoza',
    'GEO_STATE_Colima', 'GEO_STATE_Durango',
    'GEO_STATE_Estado de México', 'GEO_STATE_Guanajuato',
    'GEO_STATE_Guerrero', 'GEO_STATE_Hidalgo', 'GEO_STATE_Jalisco',
    'GEO_STATE_Michoacán de Ocampo', 'GEO_STATE_Morelos',
    'GEO_STATE_Nayarit', 'GEO_STATE_Nuevo León', 'GEO_STATE_Oaxaca',
    'GEO_STATE_Puebla', 'GEO_STATE_Querétaro',
    'GEO_STATE_Quintana Roo', 'GEO_STATE_San Luis Potosí',
    'GEO_STATE_Sinaloa', 'GEO_STATE_Sonora', 'GEO_STATE_Tabasco',
    'GEO_STATE_Tamaulipas', 'GEO_STATE_Tlaxcala',
    'GEO_STATE_Veracruz de Ignacio de la Llave', 'GEO_STATE_Yucatán',
    'GEO_STATE_Zacatecas']

filtro = ['flag_seller', 'flag_credito', 'tpn_month', 'tpv_month',
    'tpn_billetera', 'tpn_ingresos', 'tpn_pagos_online',
    'tpn_pagos_commerce', 'dias_ult', 'LYLT_Bajo', 'LYLT_Medio',
    'GEO_STATE_Baja California', 'GEO_STATE_Baja California Sur',
    'GEO_STATE_Chiapas', 'GEO_STATE_Chihuahua',
    'GEO_STATE_Ciudad de México', 'GEO_STATE_Coahuila de Zaragoza',
    'GEO_STATE_Colima', 'GEO_STATE_Estado de México',
    'GEO_STATE_Guerrero', 'GEO_STATE_Hidalgo', 'GEO_STATE_Jalisco',
    'GEO_STATE_Michoacán de Ocampo', 'GEO_STATE_Nayarit',
    'GEO_STATE_Nuevo León', 'GEO_STATE_Oaxaca', 'GEO_STATE_Puebla',
    'GEO_STATE_Querétaro', 'GEO_STATE_Quintana Roo',
    'GEO_STATE_San Luis Potosí', 'GEO_STATE_Sinaloa',
    'GEO_STATE_Sonora', 'GEO_STATE_Tabasco', 'GEO_STATE_Tamaulipas',
    'GEO_STATE_Tlaxcala', 'GEO_STATE_Veracruz de Ignacio de la Llave',
    'GEO_STATE_Yucatán']


st.header('Predictor de activación de Tarjeta de Credito - Mexico')

col1, col2= st.columns(2)

with col1:

    tpn_ingresos = st.number_input('Cantidad ingresos de dinero en cuenta', step=1, max_value=900)

    tpn_month = st.number_input('Cantidad de operaciones', step=1, max_value=5000)

    tpn_pagos_commerce = st.number_input('Cantidad de pagos por e-commerce', step=1, max_value=300)

with col2:
    dias_ult = st.number_input('Cantidad de dias que pasaron desde la ultima transacción', step=1, max_value=200)

    tpn_billetera = st.number_input('Cantidad de operaciones usando la billtera virtual', step=1, max_value=2000)

    tpv_month = st.number_input('Monto de operaciones', step=1, max_value=5000000)

col21, col22, col23 = st.columns(3)
with col21:
    flag_seller = st.radio(
        "Es vendedor:",
        ('Si', 'No'))

    if flag_seller == 'Si':
        flag_seller =  1
    else:
        flag_seller = 0

with col22:
    lylt = st.radio(
        "Nivel de Loyalty:",
        ('Bajo', 'Medio', "Alto"))

    if lylt == 'Bajo':
        lylt_bajo =  1
        lylt_medio = 0
    elif lylt == "Medio":
        lylt_medio = 1
        lylt_bajo = 0
    else:
        lylt_bajo = 0
        lylt_medio = 0

with col23:
    flag_credito = st.radio(
        "Es tomador de credito:",
        ('Si', 'No'))

    if flag_credito == 'Si':
        flag_credito =  1
    else:
        flag_credito = 0

tpn_pagos_online = st.number_input('Cantidad de pagos online', step=1, max_value=800)

state = st.selectbox(
     'Estado de residencia del usuario:',
     ('Estado de México', 'Ciudad de México',
       'Veracruz de Ignacio de la Llave', 'Jalisco', 'Nuevo León',
       'Guanajuato', 'Puebla', 'Tamaulipas', 'Chihuahua', 'Baja California',
       'Quintana Roo', 'Coahuila de Zaragoza', 'Michoacán de Ocampo', 'Sonora',
       'Tabasco', 'Querétaro', 'Chiapas', 'Hidalgo', 'Oaxaca', 'Sinaloa',
       'Yucatán', 'Guerrero', 'Morelos', 'San Luis Potosí', 'Durango',
       'Campeche', 'Baja California Sur', 'Aguascalientes', 'Tlaxcala',
       'Colima', 'Nayarit', 'Zacatecas'))

if st.button('Evaluar'):
    
    estado = "GEO_STATE_" + state

    df = pd.DataFrame([np.zeros(48)], columns=columnas)
    
    df['flag_seller'] = flag_seller
    df['flag_credito'] = flag_credito
    df['tpn_month'] = tpn_month
    df['tpv_month'] = tpv_month
    df['tpn_billetera'] = tpn_billetera
    df['tpn_ingresos'] = tpn_ingresos
    df['tpn_pagos_online'] = tpn_pagos_online
    df['tpn_pagos_commerce'] = tpn_pagos_commerce
    df['dias_ult'] = dias_ult
    df['LYLT_Bajo'] = lylt_bajo
    df['LYLT_Medio'] = lylt_medio
    try:
        df[estado] = 1
    except:
        pass

    def calcular_prob(df):
        clf_filtered = pickle.load(open("model_final.sav", 'rb'))
        pred = clf_filtered.predict(df)[0]
        score = np.round(clf_filtered.predict_proba(df),2)
        prob = np.round(100*score[0][pred])

        if pred == 0:
            st.warning(f'El usuario NO va a activar la tarjeta debito con una probabilidad del {prob}%')
        else:
            st.success(f'El usuario va a activar la tarjeta debito con una probabilidad del {prob}%')
        return pred
        

    def st_shap(plot, height=None):    
        shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
        components.html(shap_html, height=height)

    def cuanto_tiempo(df):
        clf_acti = pickle.load(open("clf_acti.sav", 'rb'))
        one_pred = clf_acti.predict_proba(df.iloc[0].values.reshape(1, -1))
        fig_days = px.bar(x = ["0-60", "60-180", "+60"], y = one_pred[0], 
                title="Dias a activar la tarjeta de débito",
                width=750, height=400, text = np.round(one_pred[0],2), color=one_pred[0], color_continuous_scale=px.colors.sequential.Bluered)
        fig_days.update_layout(xaxis_title = 'Dias', yaxis_title = 'Probabilidad', coloraxis_colorbar=dict(title="%"))
        st.plotly_chart(fig_days)  

    
    r = calcular_prob(df[filtro])

    explainer = pickle.load(open("explainer.sav", 'rb'))
    st_shap(shap.force_plot(explainer.expected_value[1], explainer.shap_values(df[filtro])[1][0,:], df[filtro].iloc[0,:], link="logit"))

    if r == 1:
        cuanto_tiempo(df)