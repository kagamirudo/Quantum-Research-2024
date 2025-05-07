# LMSR\_Q Algorithm Analysis Summary

This document consolidates all analysis and proofs for the Lexicographically Minimal String Rotation (LMSR\_Q) quantum algorithms discussed:

---

## 1. Original Grover‑Filter Algorithm

* **Structure**:

  1. Prepare index register of $n_1=\lceil\log_2 n\rceil$ qubits in uniform superposition.
  2. Repeat for each character position (up to $r$ rounds):

     * Phase‑oracle marks indices whose rotation’s current symbol equals the minimal symbol.
     * Diffuser inverts about the mean on the index register.
     * Increment index by +1 mod $n$ (using full-matrix `inc_modM_gate`).
     * Measure and classically filter remaining candidates.
  3. Stop when one index remains or characters exhausted.

* **Costs** per round using full-matrix increment + Diagonal oracle:

  * Grover body: $Θ(m_k^{3/2})$ gates.
  * Increment: $Θ(m_k^2)$ gates.
  * Classical filter: $Θ(m_k)$.

* **Complexity**:

  | Case    | Time     | Qubits      |
  | ------- | -------- | ----------- |
  | Best    | $Θ(n^2)$ | $Θ(\log n)$ |
  | Average | $Θ(n^2)$ | $Θ(\log n)$ |
  | Worst   | $Θ(n^3)$ | $Θ(\log n)$ |

---

## 2. Ripple‐Increment Optimization

* **Replacement**: simple ripple-carry adder `inc_simple(n_qubits)`

  ```python
  qc.x(0)
  for j in range(1, n_qubits):
      qc.mcx(list(range(j)), j)
  ```
* **Cost**: $Θ(n_1)$ gates per increment.
* **Effect**: per-round increment drops from $Θ(n^2)$ to $Θ(n)$.

---

## 3. OR-Tree Phase Oracle Optimization

* **Components**:

  1. One flag qubit per marked index: equality test circuits.
  2. OR-tree merging flags into a root ancilla via Toffolis.
  3. Phase kick on root, then uncompute.
* **Depth**: $Θ(n_1 + \log M)$.
* **Qubits**: $n_1 + 2M - 1$.

---

## 4. Combined Optimized Algorithm

* **Per-Round Cost** using ripple-inc + OR-tree oracle:

  * Grover body: $Θ(\sqrt{m_k}\,\log m_k)$.
  * Increment: $Θ(\log m_k)$.
  * Classical filter: $Θ(m_k)$.

* **Complexities**:

  | Case    | Time         | Qubits      |
  | ------- | ------------ | ----------- |
  | Best    | $Θ(n)$       | $Θ(\log n)$ |
  | Average | $Θ(n\log n)$ | $Θ(\log n)$ |
  | Worst   | $Θ(n^{5/2})$ | $Θ(\log n)$ |

---

## 5. QRAM‑Powered Coherent Dür–Høyer Algorithm

* **Eliminates** per‑round measure & increment steps.
* **Registers**: two index registers (|i>,|r>) each $Θ(\log n)$ qubits + work ancilla.
* **Comparator**:

  * **Binary-search**: $Θ(\log n)$ depth.
  * **Hash-assisted**: amortized $Θ(1)$ depth (worst-case $Θ(\log n)$).
* **Iterations**: $Θ(\sqrt n)$ of {compare-phase, diffusion}.
* **Measurement**: single final read on |r>.

### 5.1 Runtime & Space

| Variant              | Avg. Time     | Worst Time    | Qubits          |
| -------------------- | ------------- | ------------- | --------------- |
| QRAM + binary-search | $Θ(√n\log n)$ | $Θ(√n\log n)$ | $n + Θ(\log n)$ |
| QRAM + hashing       | $Θ(√n)$       | $Θ(√n\log n)$ | $n + Θ(\log n)$ |

---

## 6. Relationship to Original Filtering Loop

* The filter‑measure‑increment subroutine is equivalent to **amplitude amplification** split into measured chunks.
* Coherent Dür–Høyer reassembles these chunks into a single pass, yielding quadratic speed-up.

## 7. Pseudocode

```pseudo
procedure QuantumMinRotation_QRAM(L,n):
  allocate |r>=|0>, |i>=superposition, work ancilla
  K=ceil((pi/4)*sqrt(n))
  for t in 1..K:
    phase-kick if Rot(i)<Rot(r) via comparator
    diffuse on |i>
  swap |i>,|r>
  measure |r>
  return result
```

---

## 8. Proof Sketches

* **Worst-case** (no filter): $Θ(n^{5/2})$ with ripple-inc, $Θ(n^3)$ with full-matrix inc.
* **Average-case** (random string): $Θ(n)$ for filtered version, $Θ(√n\log n)$ or $Θ(√n)$ for QRAM version.
* **Space**: always $Θ(\log n)$ work qubits (plus $n$ QRAM cells).
