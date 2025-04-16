### 🧪 Quantum Value Frequency Estimator

This code constructs a **quantum circuit** to estimate the frequency of values stored in a classical list using quantum parallelism. It simulates storing values in quantum memory indexed by a pointer register, and measures the frequency of each value by only observing the value qubits.

---

### 📌 Problem Overview

Giving a list `L` of integers. The goal is to simulate encoding these integers into a quantum circuit such that each index of `L` maps to its corresponding value, and by measuring the value qubits, you retrieve a frequency histogram akin to a classical counter.

However, **since the number of indices may not fill the entire quantum address space (i.e., `2^n` for `n` index qubits)**, the quantum state will include *extra states* that act as **placeholders**, and default to value `0`.

---

### 🧮 Parameters and Initialization

```python
L = [1, 6, 5, 3, 1, 1, 3, 4, 1, 5]
```

- `n_index = ceil(log2(len(L)))`: Minimum number of qubits needed to uniquely index all elements in `L`.
- `n_val = ceil(log2(max(L)+1))`: Number of qubits needed to represent all possible values in `L`.

```python
qc = QuantumCircuit(n_index + n_val, n_val)
```

- A quantum circuit is created with `n_index` qubits for addressing and `n_val` qubits to store values. Only `n_val` qubits are measured.

---

### 🌀 Step-by-Step Circuit Description

#### **1. Create Uniform Superposition of Indices**

```python
for i in idx_qubits:
    qc.h(i)
```

- Apply Hadamard gates to index qubits, creating a superposition over all possible indices (`0` to `2^n_index - 1`).

#### **2. Encode Classical Values**

```python
for idx, val in enumerate(L):
```

For each entry in `L`:

- Flip index qubits to match binary representation of `idx` (control condition).
- Apply multi-controlled X gates to flip `val_qubits` accordingly if value bit is `1`.
- Uncompute (revert) the control index qubits to restore original state.

This step encodes the classical list into the quantum memory (as if a RAM module stores values at addresses).

#### **3. Barrier and Measurement**

```python
qc.barrier(range(n_val, n_index + n_val))
for i in range(n_index, n_index + n_val):
    qc.measure(i, i - n_index)
```

- A barrier is inserted to separate encoding from measurement.
- Only value qubits (specifically `val_qubits`) are measured.

#### **4. Simulation and Frequency Conversion**

- Run the simulation on `qasm_simulator` with 2048 shots.
- Convert output binary strings to decimal and calculate percentages.

---

### ⚠️ Important Note on Padding

Because the number of index qubits defines a full space of `2^n_index` possible states, the input list `L` may not fully occupy all these index values.  

**Unoccupied indices default to a value of `0`,** making them act as padding. This can cause some frequency to appear at `0` even if `0` was not explicitly in `L`.

---

### 📊 Output Format

```python
{0: '35.69% 000', 1: '25.83% 001', 3: '13.13% 011', 4: '6.64% 100', 5: '12.89% 101', 6: '5.81% 110'}
```

Each entry maps:
- Decimal value → frequency percentage and binary bitstring.

---