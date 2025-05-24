# core/sbol_export.py
import sbol2

def export_sbol(circuit, filename="circuit.xml"):
    doc = sbol2.Document()
    for i, gate in enumerate(circuit.gates):
        comp = sbol2.ComponentDefinition(f"gate_{i}", sbol2.BIOPAX_DNA)
        comp.name = f"{gate.gate_type} Gate"
        comp.description = f"Inputs: {gate.inputs}, Output: {gate.output}"
        doc.addComponentDefinition(comp)
    doc.write(filename)
    return filename
