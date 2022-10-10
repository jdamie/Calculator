import streamlit as st


tab1 , tab2, tab3, tab4 = st.tabs(["Power Calc", "Power Calc","Conductor Resisteance Calc", "Wye-Delta Trans"])

with tab1:
    sel_object_power = st.selectbox("Calculate this",["Ampere", "Power Factor", "Power(W,kW,hp)", "Voltage"])

    if sel_object_power == "Power(W,kW,hp)":
        t1s1_phase = st.radio("Phase",[1,3],key="t1s1ph")
        t1s1_voltage = st.number_input("Voltage [V]",key="t1s1V",value=480.0, min_value=0.0, step = 5.0)
        t1s1_ampere = st.number_input("Current [A]", key="t1s1A",value=100.0, min_value=0.0,step = 0.5)
        t1s1_pf = st.number_input("Power Factor", key="t1s1pf",value=1.0,min_value=0.0, max_value = 1.0, step=0.01)
        st.write("### Results")
        st.write("# "+format( t1s1_phase ** 0.5 * t1s1_voltage*t1s1_ampere*t1s1_pf,",.1f")+ " [W]")
        st.write("# " + format( t1s1_phase ** 0.5 * t1s1_voltage * t1s1_ampere * t1s1_pf/ 1000 , ",.1f") +" [kW]")
        st.write("# " + format( t1s1_phase ** 0.5 * t1s1_voltage * t1s1_ampere * t1s1_pf/ 1000 / 1.34102, ",.1f")+" [hp]")
    elif sel_object_power == "Voltage":
        t1s2_phase = st.radio("Phase",[1,3],key="t1s2ph")
        t1s2_unit_power = st.radio("Unit of power",["kW","hp"])
        t1s2_power = st.number_input("Wattage ["+t1s2_unit_power+"]", key="t1s2P", value=100.0, min_value=0.0, step=1.0)
        t1s2_ampere = st.number_input("Current [A]", key="t1s2A", value=100.0, min_value=0.0, step=0.5)
        t1s2_pf = st.number_input("Power Factor", key="t1s2pf", value=1.0, min_value=0.0, max_value=1.0, step=0.01)
        st.write("### Results")
        if t1s2_unit_power == "kW":
            st.write("# " + format(t1s2_power * 1000/ t1s2_phase ** 0.5 / t1s2_ampere / t1s2_pf, ",.1f") + " [V]")
        elif t1s2_unit_power == "hp":
            st.write("# " + format(t1s2_power * 1000 * 1 / 0.746 / t1s2_phase ** 0.5 / t1s2_ampere / t1s2_pf, ",.1f") + " [V]")
    elif sel_object_power == "Ampere":
        t1s3_phase = st.radio("Phase",[1,3],key="t1s3ph")
        t1s3_unit_power = t1s2_unit_power = st.radio("Unit of power",["kW","hp"],key="t1s3up")
        t1s3_power = st.number_input("Wattage [" + t1s3_unit_power + "]", key="t1s3P", value=100.0, min_value=0.0,
                                     step=5.0)
        t1s3_voltage = st.number_input("Voltage [V]", key="t1s3V", value=6600.0, min_value=0.0,
                                     step=5.0)
        t1s3_pf = st.number_input("Power Factor", key="t1s3pf",value=1.0,min_value=0.0, max_value = 1.0, step=0.01)
        st.write("### Results")
        if t1s2_unit_power == "kW":
            st.write("# " + format(t1s3_power * 1000 / t1s3_phase ** 0.5 / t1s3_voltage / t1s3_pf, ",.1f") + " [A]")
        elif t1s2_unit_power == "hp":
            st.write("# " + format(t1s3_power * 1000 * 1 / 0.746 / t1s3_phase ** 0.5 / t1s3_voltage / t1s3_pf, ",.1f") + " [A]")
