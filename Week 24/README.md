# README: Quantum Index Search & Increment

This project demonstrates a quantum subroutine for locating marked values in a classical list and cycling through their indices, as a stepping stone toward a full quantum minimum-finding algorithm (Dürr & Høyer).

---

## Problem Overview

Given a list of \(M\) classical values:

```python
L = [1, 3, 1, 4, 1, 6]
```

we wish to:

1. **Search** for all positions \(i\) where \(L[i] == \text{target}\).
2. **Increment** each found index by 1 (mod \(M\)), wrapping the last position back to zero.
3. **Iterate** this process until a single index remains with high probability.
4. **Backtrack** from the final index by undoing the increments to recover the original position.

In future work, we will replace the classical `targets` list with the Dürr & Høyer quantum minimum-finding oracle [1].

---

## Prerequisites

- Python 3.8+
- Qiskit Terra ≥ 0.24
- NumPy, Matplotlib

Install dependencies with:

```bash
pip install qiskit numpy matplotlib
```

---

## Key Components

### 1. Preprocessing

```python
import math
from math import ceil, log2

n = ceil(log2(len(L)))         # qubits to index 0..M-1
if count_targets / 2**n == 0.5:
    n += 1                     # avoid the M/N = 1/2 dead zone
N = 2**n
L_pad = L + [None]*(N - len(L))
```
- Compute the number of index qubits \(n\) and pad `L` to length \(N = 2^n\).
- Detect and avoid the case where exactly half the basis states would be marked.

### 2. Oracle Construction

```python
from qiskit.circuit.library import UnitaryGate
import numpy as np

diag = [
    -1 if (i in candidates and L_pad[i] == target) else +1
    for i in range(N)
]
oracle = UnitaryGate(np.diag(diag), label="Oracle")
```
- On the **first** pass, `candidates = []`, so all positions with `L_pad[i] == target` are marked.  
- On subsequent passes, only indices in `candidates` carry a \(-1\) phase.

### 3. Diffusion Operator (Grover)

```python
from qiskit import QuantumCircuit

def diffuser(n_qubits):
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits)); qc.x(range(n_qubits))
    qc.h(n_qubits - 1)
    qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
    qc.h(n_qubits - 1)
    qc.x(range(n_qubits)); qc.h(range(n_qubits))
    return qc.to_gate(label="Diffuser")
```
- Implements the reflection about the mean on an \(n\)-qubit register.

### 4. Increment Gate

```python
from qiskit.circuit.library import UnitaryGate

def inc_modM_gate(n_qubits, M):
    N = 2**n_qubits
    P = np.eye(N, dtype=complex)
    for i in range(M):
        P[i, i] = 0
        P[(i + 1) % M, i] = 1
    return UnitaryGate(P, label=f"inc_mod{M}")
```
- A single-unitary permutation mapping \(|i\rangle → |(i+1) mod M\rangle\), leaving \(|i≥M⟩\) unchanged.

### 5. Optimal Grover Iterations

```python
import math

def optimal_grover_iterations(N: int, M: int) -> int:
    """
    Compute k ≈ ⌊(π/4) √(N/M)⌋ iterations to maximize success probability.
    """
    return math.floor((math.pi / 4) * math.sqrt(N / M))
```
- Choose \(k\) based on the ratio \(M/N\), where \(M\) is the current number of marked states.

### 6. Circuit Assembly & Execution

```python
from qiskit import Aer, transpile, execute

# Build one Grover+increment round:
def build_round_circuit(n, oracle, diffuse, inc_modM, k):
    qc = QuantumCircuit(n, n)
    qc.h(range(n))
    for _ in range(k):
        qc.append(oracle,   range(n))
        qc.append(diffuse,  range(n))
        qc.append(inc_modM, range(n))
    qc.measure(range(n), range(n))
    return qc

# Run and extract candidate indices:
backend = Aer.get_backend('qasm_simulator')
qc_round = build_round_circuit(...)
qc_t      = transpile(qc_round, backend)
counts    = execute(qc_t, backend, shots=1024).result().get_counts()
candidates = [int(bs, 2) for bs in counts]
```
- Execute each round “coherently” then measure once to get the surviving indices.

### 7. Backtracking the Start Index

```python
def recover_start_index(final_index: int, k: int, M: int) -> int:
    """Compute original index before k increments mod M."""
    return (final_index - k) % M
```
- Undo \(k\) increments to recover the original list position.

---

## Current Status & Next Steps

- **Implemented**: Iterative Grover + modular increment using a classical `targets` list.  
- **Next**: Integrate the full quantum minimum-finding algorithm of Dürr & Høyer [1], replacing the `targets` hack.  
- **Goal**: Achieve an end-to-end quantum circuit that finds the minimum element’s index in \(L\) with high probability.

---

## References

1. Dürr, C. & Høyer, P. _A quantum algorithm for finding the minimum_. Lecture Notes in Computer Science, Vol. 1509, pp. 362–371 (1999).

2. Grover, L. K. _A fast quantum mechanical algorithm for database search_. _STOC_ ’96, pp. 212–219 (1996).

**Author:** Gary Pham  
**Date:** April 2025

