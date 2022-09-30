import streamlit as st
import pandas as pd

view = [100,200,400,800]
sview = pd.series(view)
st.write("# Mark-up level 1")
st.write("## Mark-up level 2")
st.bar_chart(view)
st.bar_chart(sview)
