from qiskit import *
from qiskit_aer import Aer


# Define the oracle for marking the minimum element
def oracle(n_qubits, marked_index):
    qc = QuantumCircuit(n_qubits)
    # Mark the specific state (e.g., |marked_index>)
    for i, bit in enumerate(reversed(f"{marked_index:0{n_qubits}b}")):
        if bit == "0":
            qc.x(i)
    qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
    for i, bit in enumerate(reversed(f"{marked_index:0{n_qubits}b}")):
        if bit == "0":
            qc.x(i)
    return qc.to_gate(label="Oracle")


# Define the diffuser (Grover's operator)
def diffuser(n_qubits):
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    qc.x(range(n_qubits))
    qc.h(n_qubits - 1)
    qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
    qc.h(n_qubits - 1)
    qc.x(range(n_qubits))
    qc.h(range(n_qubits))
    return qc.to_gate(label="Diffuser")


# Main simulation
def quantum_minimum_search(n_qubits, marked_index):
    # Initialize quantum circuit
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))  # Create equal superposition

    # Oracle and diffuser gates
    oracle_gate = oracle(n_qubits, marked_index)
    diffuser_gate = diffuser(n_qubits)

    # Apply Grover iterations
    iterations = int((3.14 / 4) * (2 ** (n_qubits / 2)))
    for _ in range(iterations):
        qc.append(oracle_gate, range(n_qubits))
        qc.append(diffuser_gate, range(n_qubits))

    # Measure the result
    qc.measure(range(n_qubits), range(n_qubits))
    return qc


if __name__ == "__main__":
    # Parameters
    n_qubits = 3  # Number of qubits (searching among 2^n_qubits elements)
    marked_index = 1  # Minimum value's index
    # Generate the circuit and simulate
    qc = quantum_minimum_search(n_qubits, marked_index).decompose()
    simulator = Aer.get_backend("qasm_simulator")
    job_sim = simulator.run(qc, shots=2048)
    counts = job_sim.result().get_counts()
    total_counts = sum(counts.values())
    # Print the result
    print("Measurement counts:", counts)
