import streamlit as st
import math
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
    a,b,c = st.columns(3)
    with a:
        wye_a = st.number_input("Wye a",value=1)
    with b:
        wye_b = st.number_input("Wye b",value=1)
    with c:
        wye_c = st.number_input("Wye c",value=1)
    a0, b0, c0 = st.columns(3)
    with a0:
        st.write("D_a : "+format(wye2del(wye_a, wye_b, wye_c), ".3e") + " Ω")
    with b0:
        st.write("D_a : "+format(wye2del(wye_b, wye_c, wye_a), ".3e") + " Ω")
    with c0:
        st.write("D_a : "+format(wye2del(wye_c, wye_a, wye_b), ".3e") + " Ω")
    st.markdown("***")
    e, f, g = st.columns(3)
    with e:
        del_a = st.number_input("Del a", value=1)
    with f:
        del_b = st.number_input("Del b", value=1)
    with g:
        del_c = st.number_input("Del c", value=1)
    e1, f1, g1 = st.columns(3)
    with e1:
        st.write("Y_a : "+format(del2wye(del_a, del_b, del_c), ".3e") + " Ω")
    with f1:
        st.write("Y_b : "+format(del2wye(del_b, del_c, del_a), ".3e") + " Ω")
    with g1:
        st.write("Y_c : "+format(del2wye(del_c, del_a, del_b), ".3e") + " Ω")
