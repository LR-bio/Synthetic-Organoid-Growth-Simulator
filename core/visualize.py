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
