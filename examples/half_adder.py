# examples/half_adder.py
from core.logic_parser import LogicCircuit
from core.visualize import draw_logic_circuit

circuit = LogicCircuit()
a = "A"
b = "B"
sum_out = circuit.add_gate("XOR", [a, b])
carry_out = circuit.add_gate("AND", [a, b])

bio_parts = circuit.generate_genetic_circuit()
print("Generated Genetic Circuit:")
for part in bio_parts:
    print(part)

print("\nExport to GenBank:")
print(circuit.export_to_genbank())

draw_logic_circuit(circuit)

from core.sbol_export import export_sbol

filename = export_sbol(circuit)
print(f"SBOL file saved as {filename}")
