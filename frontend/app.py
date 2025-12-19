import streamlit as st
import requests
import pandas as pd

st.title("💪 Edzésnapló")

BACKEND_URL = "http://127.0.0.1:8000/workouts"

with st.sidebar:
    st.header("Új gyakorlat")
    ex = st.text_input("Gyakorlat neve")
    reps = st.number_input("Ismétlésszám", min_value=1, value=10)
    if st.button("Mentés"):
        requests.post(BACKEND_URL, json={"exercise": ex, "reps": reps})
        st.success("Hozzáadva!")

try:
    data = requests.get(BACKEND_URL).json()
    if data:
        df = pd.DataFrame(data)
        st.subheader("Mai edzésed")
        st.table(df[['exercise', 'reps']])
        
        st.subheader("Statisztika")
        st.bar_chart(df.set_index('exercise')['reps'])
except:
    st.error("A backend nem elérhető.")