import streamlit as st
import math


def wye2del(a, b, c): return (a * b + b * c + c * a) / a


def del2wye(a, b, c): return b * c / (a + b + c)




opts = [
    "Delta Wye Transformation",
    "Conductor Resistance Calculation",
    "Power Calculator"
]
main_selector = st.selectbox(label="Select Calculator", options=opts)

if main_selector == "Delta Wye Transformation":
    st.markdown("***")
    st.write("### Why-Delta Transformation")
    a, b, c = st.columns(3)
    with a:
        wye_a = st.number_input("Wye a", value=1)
    with b:
        wye_b = st.number_input("Wye b", value=1)
    with c:
        wye_c = st.number_input("Wye c", value=1)
    a0, b0, c0 = st.columns(3)
    if wye_a <= 0 or wye_b <= 0 or wye_c <= 0:
        st.write("Numbers must be positive!!")
    else:
        with a0:
            st.write("Delta_a : " + format(wye2del(wye_a, wye_b, wye_c), ".3e") + " Ω")
        with b0:
            st.write("Delta_b : " + format(wye2del(wye_b, wye_c, wye_a), ".3e") + " Ω")
        with c0:
            st.write("Delta_c : " + format(wye2del(wye_c, wye_a, wye_b), ".3e") + " Ω")
    st.markdown("***")
    st.write("### Delta-Wye Transformation")
    e, f, g = st.columns(3)
    with e:
        del_a = st.number_input("Del a", value=1)
    with f:
        del_b = st.number_input("Del b", value=1)
    with g:
        del_c = st.number_input("Del c", value=1)
    e1, f1, g1 = st.columns(3)
    if del_a < 0 or del_b < 0 or del_c < 0:
        st.write("Numbers must be positive!!")
    else:
        with e1:
            st.write("Wye_a : " + format(del2wye(del_a, del_b, del_c), ".3e") + " Ω")
        with f1:
            st.write("Wye_b : " + format(del2wye(del_b, del_c, del_a), ".3e") + " Ω")
        with g1:
            st.write("Wye_c : " + format(del2wye(del_c, del_a, del_b), ".3e") + " Ω")
    st.write("***")
    st.write("### Delta Connected Resistance Calculation")
    h, i, j, k = st.columns(4)
    with h:
        st.image("Delta.png")
    with i:
        xi = st.number_input("Rab", value=1.5)
    with j:
        yi = st.number_input("Rbc", value=1.5)
    with k:
        zi = st.number_input("Rca", value=2.0)
    h1, i1, j1, k1 = st.columns(4)

    def f1(x, y, z):
        return (x + y - z) / 2, (z + x - y) / 2, (y + z - x) / 2


    def f2(A, B, C):
        return (A * B + B * C + C * A) / A, (A * B + B * C + C * A) / B, (A * B + B * C + C * A) / C


    def convtr(x, y, z):
        return f2(*f1(x, y, z))

    temp = [xi,yi,zi]
    if max(temp) >= sum(temp) - max(temp) : st.write("Invalid input. inputs must be triangula.")

    else:
        temp = convtr(*temp)
        with h1:
            st.write("Result :    ")
        with i1:
            st.write("Ra = " + format(temp[0], ".3e") + "Ohm")
        with j1:
            st.write("Rb = " + format(temp[1], ".3e") + "Ohm")
        with k1:
            st.write("Rc = " + format(temp[2], ".3e") + "Ohm")
