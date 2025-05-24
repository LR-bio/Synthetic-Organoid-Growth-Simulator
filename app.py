# app.py
import streamlit as st
from core.logic_parser import LogicCircuit, LogicGate
from core.visualize import draw_logic_circuit
import matplotlib.pyplot as plt

st.title("BioLogic Circuit Designer")

if 'circuit' not in st.session_state:
    st.session_state.circuit = LogicCircuit()

gate_type = st.selectbox("Select Gate Type", ["AND", "OR", "NOT", "NAND", "XOR"])
inputs = st.text_input("Enter inputs (comma separated)")

if st.button("Add Gate"):
    input_list = [x.strip() for x in inputs.split(",") if x.strip()]
    try:
        st.session_state.circuit.add_gate(gate_type, input_list)
        st.success(f"Added {gate_type} gate with inputs {input_list}")
    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Show Circuit"):
    circuit = st.session_state.circuit
    bio_parts = circuit.generate_genetic_circuit()
    st.write("Genetic Circuit Parts:")
    for part in bio_parts:
        st.write(part)

    fig, ax = plt.subplots()
    draw_logic_circuit(circuit)
    st.pyplot(fig)
