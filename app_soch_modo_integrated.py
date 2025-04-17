
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("nisoplus_goals_combined.csv")

st.set_page_config(page_title="НИСО+ Интеграция СОЧ и МОДО", layout="wide")
st.title("🎯 НИСО+: Интеграция внутреннего (СОЧ) и внешнего (МОДО) оценивания")

st.markdown("### 📊 Фильтрация по уровню системы")

# Фильтрация
year = st.selectbox("Учебный год", sorted(df["Учебный год"].unique()))
df = df[df["Учебный год"] == year]

region = st.selectbox("Область", sorted(df["Область"].unique()))
df = df[df["Область"] == region]

district = st.selectbox("Район", sorted(df["Район"].unique()))
df = df[df["Район"] == district]

school = st.selectbox("Школа", sorted(df["Школа"].unique()))
df = df[df["Школа"] == school]

grade = st.selectbox("Класс", sorted(df["Класс"].unique()))
df = df[df["Класс"] == grade]

goal = st.selectbox("Цель обучения", sorted(df["Цель обучения"].unique()))
df_goal = df[df["Цель обучения"] == goal]

# Визуализация
st.markdown("### 📈 Сравнение СОЧ и МОДО по ученикам")
fig = px.bar(df_goal, x="Ученик", y=["СОЧ (%)", "МОДО (%)"], barmode="group",
             title=f"Цель обучения: {goal}", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

# Таблица с аналитикой
st.markdown("### 📋 Аналитика и обратная связь по ученикам")
styled = df_goal[["Ученик", "СОЧ (%)", "МОДО (%)", "Отклонение", "Аналитика", "Обратная связь"]].sort_values("СОЧ (%)", ascending=False)
styled_display = styled.style.background_gradient(cmap="RdYlGn_r", subset=["Отклонение"])
st.dataframe(styled_display, use_container_width=True)
