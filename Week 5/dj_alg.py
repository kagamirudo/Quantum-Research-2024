from qiskit import *
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram


def imply_logic():
    num = 6
    qubits = range(num)
    logic = QuantumRegister(num)
    logic = QuantumCircuit(logic, name="imply")
    logic.x(0)
    logic.ccx(0, 1, 2)
    logic.x([0, 1])
    logic.ccx(0, 1, 3)
    logic.x(1)
    logic.ccx(2, 3, 4)
    logic.x(4)
    logic.barrier(qubits)
    # For y
    logic.cx(4, 5)
    # Reverse
    logic.barrier(qubits)
    logic.x(0)
    logic.ccx(0, 1, 2)
    logic.x([0, 1])
    logic.ccx(0, 1, 3)
    logic.x(1)
    logic.ccx(2, 3, 4)
    logic.x(4)
    return logic.to_instruction()


def left_right_logic():
    num = 6
    qubits = range(num)
    logic = QuantumRegister(num)
    logic = QuantumCircuit(logic, name="left_right")
    logic.x(1)
    logic.ccx(0, 1, 3)
    logic.x([0, 1, 3])
    logic.ccx(0, 1, 2)
    logic.x([0, 2])
    logic.ccx(2, 3, 4)
    logic.barrier(qubits)
    # For y
    logic.cx(4, 5)
    # Reverse
    logic.barrier(qubits)
    logic.ccx(2, 3, 4)
    logic.x([0, 2])
    logic.ccx(0, 1, 2)
    logic.x([0, 1, 3])
    logic.ccx(0, 1, 3)
    logic.x(1)
    return logic.to_instruction()


def xor_logic():
    num = 3
    qubits = range(num)
    logic = QuantumRegister(num)
    logic = QuantumCircuit(logic, name="xor")
    logic.cx(0, 1)
    logic.barrier(qubits)
    # For y
    logic.cx(1, 2)
    logic.barrier(qubits)
    # Reverse
    logic.cx(0, 1)
    return logic.to_instruction()


def dj_algo(f, num_qubits, input, name, out_y=0):
    y = num_qubits + 1
    classical_bits = input + 1 if out_y == 1 else input
    qc = QuantumCircuit(y, classical_bits)
    qc.h(range(input))
    qc.x(y - 1)
    qc.h(y - 1)
    qc.barrier(range(y))
    qc.append(f, range(y))
    qc.barrier(range(y))
    qc.h(range(input))
    qc.measure(range(input), range(input))
    if out_y == 1:
        qc.barrier(range(y))
        qc.measure(y - 1, input)
    qc.draw(output="mpl", filename=name)
    qc = qc.decompose()
    return qc


def analyse(qc, test, name):
    backend_sim = Aer.get_backend("qasm_simulator")
    job_sim = backend_sim.run(qc, shots=test)
    counts = job_sim.result().get_counts()
    total_counts = sum(counts.values())
    probs = {key: value / total_counts for key, value in counts.items()}
    fig = plot_histogram(probs, title="Quantum")
    fig.savefig(name + "_quan_chart")


def process_imply(test, y_out=0):
    name = "imply_logic"
    f = imply_logic()
    qc = dj_algo(f, 5, 2, name, y_out)
    analyse(qc, test, name)


def process_left_right(test, y_out=0):
    name = "left_right_logic"
    f = left_right_logic()
    qc = dj_algo(f, 5, 2, name, y_out)
    analyse(qc, test, name)


def process_xor(test, y_out=0):
    name = "xor_logic"
    f = xor_logic()
    qc = dj_algo(f, 2, 2, name, y_out)
    analyse(qc, test, name)


if __name__ == "__main__":
    test = 2048
    y_out = 0
    process_imply(test, y_out)
    process_left_right(test, y_out)
    process_xor(test, y_out)
