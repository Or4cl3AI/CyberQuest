```python
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.extensions import Initialize
from qiskit.ignis.verification import marginal_counts
from qiskit.quantum_info import random_statevector

class QuantumAlgorithm:
    def __init__(self):
        self.simulator = Aer.get_backend('qasm_simulator')

    def create_circuit(self, num_qubits):
        return QuantumCircuit(num_qubits)

    def apply_gate(self, circuit, gate, qubit):
        if gate.lower() == 'h':
            circuit.h(qubit)
        elif gate.lower() == 'x':
            circuit.x(qubit)
        elif gate.lower() == 'y':
            circuit.y(qubit)
        elif gate.lower() == 'z':
            circuit.z(qubit)
        else:
            raise ValueError("Invalid gate specified")

    def measure(self, circuit, qubit, cbit):
        circuit.measure(qubit, cbit)

    def run_circuit(self, circuit):
        job = execute(circuit, self.simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(circuit)
        return counts

quantumAlgorithms = QuantumAlgorithm()
```