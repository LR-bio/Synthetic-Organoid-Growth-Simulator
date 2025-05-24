# tests/test_logic_parser.py
import unittest
from core.logic_parser import LogicCircuit

class TestLogicCircuit(unittest.TestCase):
    def test_add_gate_and_output(self):
        circuit = LogicCircuit()
        out = circuit.add_gate("AND", ["A", "B"])
        self.assertTrue(out.startswith("OUT_"))
        self.assertEqual(len(circuit.gates), 1)

    def test_generate_genetic_circuit(self):
        circuit = LogicCircuit()
        circuit.add_gate("AND", ["A", "B"])
        parts = circuit.generate_genetic_circuit()
        self.assertIn("Promoter(A)", parts[0])

if __name__ == "__main__":
    unittest.main()
