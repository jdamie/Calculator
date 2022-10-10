import streamlit as st


tab1 , tab2, tab3 = st.tabs(["Power Calc","Conductor Resisteance Calc", "Wye-Delta Trans"])

with tab1:
    sel_object_power = st.selectbox("Calculate this",["Power(W,kW,hp)", "Voltage", "Ampere","Power Factor"])

    if sel_object_power == "Power(W,kW,hp)":
        t1s1_voltage = st.number_input("Voltage [V]",key="t1s1V",value=480.0, min_value=0.0, step = 5.0)
        t1s1_ampere = st.number_input("Current [A]", key="t1s1A",value=100.0, min_value=0.0,step = 0.5)
        t1s1_pf = st.number_input("Power Factor", key="t1s1pf",value=0.8,min_value=0.0, max_value = 1.0, step=0.01)
        st.write("### Results")
        st.write("# "+format(t1s1_voltage*t1s1_ampere*t1s1_pf,",.1f")+ " [W]")
        st.write("# " + format(t1s1_voltage * t1s1_ampere * t1s1_pf/ 1000 , ",.1f") +" [kW]")
        st.write("# " + format(t1s1_voltage * t1s1_ampere * t1s1_pf/ 1000 / 1.34102, ",.1f")+" [hp]")