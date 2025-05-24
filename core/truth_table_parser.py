# core/truth_table_parser.py
import csv
from core.logic_parser import LogicCircuit

def parse_truth_table(filepath):
    with open(filepath) as f:
        reader = csv.DictReader(f)
        inputs = reader.fieldnames[:-1]  # all columns except output
        circuit = LogicCircuit()

        # Naive sum-of-products synthesis
        for row in reader:
            input_vals = [int(row[i]) for i in inputs]
            output_val = int(row['Output'])
            if output_val == 1:
                # For each row with output=1, create AND of inputs or NOT(inputs)
                and_inputs = []
                for var, val in zip(inputs, input_vals):
                    if val == 1:
                        and_inputs.append(var)
                    else:
                        # Create NOT gate on var
                        not_out = circuit.add_gate("NOT", [var])
                        and_inputs.append(not_out)
                # Now create OR gate combining these AND terms (simplified)
                # For demo, just add the AND gate
                circuit.add_gate("AND", and_inputs)
        return circuit



# Example:
from core.truth_table_parser import parse_truth_table

circuit = parse_truth_table("truth_table.csv")
for part in circuit.generate_genetic_circuit():
    print(part)


