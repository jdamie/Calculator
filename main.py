import streamlit as st
import math
"""
a, b, c = st.columns(3)
with a :
    a = st.number_input("a")
with b:
    b = st.number_input("b")
with c:
    st.text(format(a+b,'.2f'))
"""

def wye2del(a,b,c): return (a*b+b*c+c*a)/a
def del2wye(a,b,c): return b*c/(a+b+c)

opts = [
    "Delta Wye Transformation",
    "Conductor Resistance Calculation",
    "Power Calculator"
    ]

a, b, c = st.columns(3)
with a : st.write("Clip Board")
with b : clip_board = st.text("touch to copy--->")
with c : st.button("Copy")
main_selector = st.selectbox(label="Select Calculator",options = opts)

if main_selector == "Delta Wye Transformation" :
    st.markdown("***")
    a,b,c,d = st.columns(4)
    with a:
        wye_a = st.number_input("Wye a",value=1)
    with b:
        wye_b = st.number_input("Wye b",value=1)
    with c:
        wye_c = st.number_input("Wye c",value=1)
    with d:
        st.write("D_a : "+format(wye2del(wye_a, wye_b, wye_c), ".3e") + " Ω")
        st.write("D_a : "+format(wye2del(wye_b, wye_c, wye_a), ".3e") + " Ω")
        st.write("D_a : "+format(wye2del(wye_c, wye_a, wye_b), ".3e") + " Ω")
    st.markdown("***")
    e, f, g, h = st.columns(4)
    with e:
        del_a = st.number_input("Del a", value=1)
    with f:
        del_b = st.number_input("Del b", value=1)
    with g:
        del_c = st.number_input("Del c", value=1)
    with h:
        st.write("Y_a : "+format(del2wye(del_a, del_b, del_c), ".3e") + " Ω")
        st.write("Y_b : "+format(del2wye(del_b, del_c, del_a), ".3e") + " Ω")
        st.write("Y_c : "+format(del2wye(del_c, del_a, del_b), ".3e") + " Ω")
