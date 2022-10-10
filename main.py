import streamlit as st
import math
import pandas as pd

#pylint:disable=E0001
rhos ={
"Cu": 1.68*10**(-8),
"Ag": 1.59*10**(-8),
"Au": 2.21*10**(-8),
"Al": 2.65*10**(-8),
"Fe": 1*10**(-7),
"Pt":10.6*10**(-8)

}# [Ohm* meter]

C_temp_R ={
"Cu" : 0.00393,
"Au" : 0.0034,
"Fe" : 0.005,
"Al" : 0.0039,
"Ag" : 0.0038,
"Pt": 0.00392
}#

#element sign, m, mm^2, T as celcius return [Ohm]
def resistance(e, l, A,T): return rhos[e] * l /A *10**6 * (1+C_temp_R[e]*(T-20))


def wye2del(a, b, c): return (a * b + b * c + c * a) / a


def del2wye(a, b, c): return b * c / (a + b + c)




opts = [
    "Delta Wye Transformation",
    "Conductor Resistance Calculation",
    "Power Calculation",
    "Test of Multi input"
]

main_selector = st.selectbox(label="Select Calculator", options=opts)
if main_selector == "Conductor Resistance Calculation":
    st.markdown("***")
    st.markdown("# Conductor Resistance Calculation")
    a,b,c,d,e = st.columns(5)
    with a:
        area_cond = st.number_input("Cross-sectional area [mm^2}",value = 100)
    with b:
        length = st.number_input("Length of Conductor [m]",100)
    with c:
        element = st.selectbox(label="Element of conductor [Ωm]",options=rhos)
    with d:
        temperature = st.number_input(label= "Temperature of conductor [℃]",value = 25)
    with e:
        st.write("Result : "+ format(resistance(element, length, area_cond,temperature),".3e")+"Ω")
elif main_selector == "Delta Wye Transformation":
    st.markdown("***")
    st.write("### Wye-Delta Transformation")
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
elif main_selector == "Power Calculation":
    st.write("***")
    st.write("# Single phase")
    a,b,c,d = st.columns(4)
    with a :
        voltage_single = st.number_input(label="Voltage [V]", value= 110)
    with b :
        current_single = st.number_input(label="Current [A]",value= 0)
    with c :
        pf_single = st.number_input(label="Power Factor", value= 1.00)
    with d :
        st.write("Result : ")
        st.write(format(voltage_single*current_single*pf_single,".3e")+ " [W]")
        st.write(format(voltage_single*current_single*pf_single/1000,",.1f")+ " [kW]")
        st.write(format(voltage_single*current_single*pf_single/1000/1.34102,",.1f")+ " [hp]")
    st.write("***")
    st.write("# Three Phase (Symmetrical Circuit")
    e, f, g, h = st.columns(4)
    with e:
        voltage_three_s = st.number_input(label="Voltage (line to line, V)", value= 480)
    with f:
        current_three_s = st.number_input(label="Current (line, A)",value= 100)
    with g:
        pf_three_s = st.number_input(label="Power Factor",value = 0.85)
    with h:
        st.write("Result : ")
        st.write(format(3 ** .5 * voltage_three_s * current_three_s * pf_three_s, ".3e") + " [W]")
        st.write(format(3 ** .5 * voltage_three_s * current_three_s * pf_three_s/ 1000, ",.1f") + " [kW]")
        st.write(format(3 ** .5 * voltage_three_s * current_three_s * pf_three_s/ 1000 / 1.34102, ",.1f") + " [hp]")
elif main_selector == "Test of Multi input":
    x,y,z = st.columns([3,2,1])
    with x :
        x1 = st.number_input("x1")
        x2 = st.number_input("x2")
        x3 = st.number_input("x3")
    with y :
        temp_radio = st.radio("Select",["x1@@@@@@@@@@@@@@@","x2","x3"])
    with z :
        st.write(temp_radio)

