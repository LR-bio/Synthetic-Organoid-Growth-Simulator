### BioLogic: A Synthetic Biology Logic Compiler
# Converts Boolean logic circuits into synthetic gene circuits using repressors/promoters

# core/logic_parser.py
class LogicGate:
    def __init__(self, gate_type, inputs):
        self.gate_type = gate_type.upper()
        self.inputs = inputs  # List of input gate names or signals
        self.output = None

    def __repr__(self):
        return f"{self.gate_type}({', '.join(self.inputs)}) -> {self.output}"


class LogicCircuit:
    def __init__(self):
        self.gates = []
        self.output_count = 0
        self.variables = set()

    def add_gate(self, gate_type, inputs):
        gate = LogicGate(gate_type, inputs)
        gate.output = f"OUT_{self.output_count}"
        self.output_count += 1
        self.gates.append(gate)
        self.variables.update(inputs)
        return gate.output

    def generate_genetic_circuit(self):
        circuit = []
        for gate in self.gates:
            part = self._translate_gate_to_genetic_parts(gate)
            circuit.append(part)
        return circuit

    def _translate_gate_to_genetic_parts(self, gate):
        if gate.gate_type == "AND":
            return f"Promoter({gate.inputs[0]})-Repressor({gate.inputs[1]})-Reporter({gate.output})"
        elif gate.gate_type == "OR":
            return f"Promoter({gate.inputs[0]})+Promoter({gate.inputs[1]}) -> Reporter({gate.output})"
        elif gate.gate_type == "NOT":
            return f"Repressor({gate.inputs[0]}) inhibits Reporter({gate.output})"
        elif gate.gate_type == "NAND":
            return f"Promoter({gate.inputs[0]})-Repressor({gate.inputs[1]})-Repressor(NOT)-Reporter({gate.output})"
        elif gate.gate_type == "XOR":
            return f"Complex XOR circuit built from NOT, AND, OR parts to produce {gate.output}"
        else:
            return f"Unsupported gate type: {gate.gate_type}"

    def export_to_genbank(self):
        content = "LOCUS       SYNBIO_LOGIC        300 bp    DNA     SYN       UNK
"
        for i, gate in enumerate(self.gates):
            content += f"FEATURES             gate_{i}           {gate.gate_type}({','.join(gate.inputs)}) -> {gate.output}\n"
        return content


# core/visualize.py
import networkx as nx
import matplotlib.pyplot as plt

def draw_logic_circuit(circuit):
    G = nx.DiGraph()
    for gate in circuit.gates:
        for input_node in gate.inputs:
            G.add_edge(input_node, gate.output, label=gate.gate_type)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Logic Circuit Diagram")
    plt.show()


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

# README.md
"""
# BioLogic

**BioLogic** is a compiler that transforms Boolean logic circuits into synthetic biology representations using repressors, activators, and promoters.

## Features
- Parse and represent logic gates
- Translate to synthetic biology parts
- Visualize logic network as a graph
- Export logic gates as a GenBank-style text

## Example: Half Adder
```python
circuit = LogicCircuit()
sum_out = circuit.add_gate("XOR", ["A", "B"])
carry_out = circuit.add_gate("AND", ["A", "B"])
print(circuit.generate_genetic_circuit())
print(circuit.export_to_genbank())
```

## Future Features
- Export to full SBOL XML
- Support biological simulation with synthetic kinetics
- Drag-and-drop GUI design interface

## License
MIT License
"""

# requirements.txt
matplotlib
networkx
