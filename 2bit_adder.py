# Import the Libraries
from qiskit import *
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Make the Adder into a 4 Wire Circuit
adder = QuantumRegister(4)
adder = QuantumCircuit(adder, name='adder')
adder.barrier(range(4))
adder.ccx(0,1,3)
adder.cx(0,1)
adder.ccx(1,2,3)
adder.cx(1,2)
adder.cx(0,1)
adder.barrier(range(0,4))
myAdder = adder.to_instruction()

in_bit = 7
out_bit = 3
test = 2048

qc = QuantumCircuit(in_bit, out_bit)
qc.h(i for i in range(0, 4))
qc.barrier(range(in_bit))
qc.append(myAdder, [0, 2, 4, 5])
qc.append(myAdder, [1, 3, 5, 6])
qc.barrier(range(in_bit))
for x in range(out_bit):
    qc.measure((in_bit - out_bit) + x, x)

qc.draw(output="mpl",filename="circuit.png")
qc = qc.decompose()

backend_sim = Aer.get_backend('qasm_simulator')
job_sim = backend_sim.run(qc, shots=test)
# job_sim = execute(qc,backend_sim,shots=2048) # Cannot run

counts = job_sim.result().get_counts()
total_counts = sum(counts.values())
probs = {key: value / total_counts for key, value in counts.items()}
fig = plot_histogram(probs, title="Quantum")
fig.savefig("quan_result.png")

truth_table = {'000': 1, '001': 2, '010': 3, '011': 4, 
               '100': 3, '101': 2, '110': 1}
fig = plot_histogram(truth_table, color='orange'
                     , title="Truth Table")
fig.savefig("actual_result.png")
