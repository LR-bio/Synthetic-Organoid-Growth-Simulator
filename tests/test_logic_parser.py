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

    def test_invalid_gate_type():
        from core.logic_parser import LogicGate
        import pytest
        with pytest.raises(ValueError):
        LogicGate("FOO", ["A", "B"])

    def test_invalid_inputs_for_gate():
        from core.logic_parser import LogicGate
        import pytest
        with pytest.raises(ValueError):
            LogicGate("AND", [])
        with pytest.raises(ValueError):
            LogicGate("NOT", ["A", "B"])


if __name__ == "__main__":
    unittest.main()
