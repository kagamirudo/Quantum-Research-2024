# Lexicographically Minimal String Rotation (LMSR_Q)

This report summarizes the design, optimizations, and complexity analyses for finding the lexicographically minimal rotation of a list $L$ of length $n$ using quantum algorithms. It covers:

- Original Grover-based filtering loop
- Increment-gate optimizations (ripple vs. full-unitary)
- Oracle optimizations (OR-tree phase oracle)
- Best, average, and worst-case complexity
- QRAM-powered coherent minimum-finding via Dür–Høyer

---

## 1. Problem Statement

Given a list $L$ of $n$ elements (e.g., symbols over an alphabet $\Sigma$), find the index $i^*$ such that the rotation
$$
  \text{Rot}_i = L[i:] + L[:i]
$$
is lexicographically minimal.

---

## 2. Original Quantum Filtering Algorithm (LMSR_Q)

### 2.1 Algorithm Structure
1. **Initialization**: Prepare $n_1=\lceil\log_2 n\rceil$ index qubits in uniform superposition.
2. **Grover Filtering Rounds** (at most one per character):
   - Build a phase–oracle marking indices whose current character matches the minimal symbol.
   - Apply Grover's diffusion on the index register.
   - **Increment** the quantum index by $+1$ mod $n$ (to advance to the next character position).
3. **Measurement** after each round; classical filtering shrinks the candidate set.
4. **Termination** when a unique index remains or all characters are compared.

### 2.2 Increment Gate (inc_modM)
- **Original**: built via a full $N\times N$ permutation matrix $N=2^{n_1}$, implemented as `UnitaryGate(P)`.  
  - **Cost**: $Θ(N^2)=Θ(n^2)$ gates.  
  - **Qubits**: $n_1$.

### 2.3 Oracle Gate
- **Plain Diagonal**: `Diagonal(diag)` over $N$ basis states (±1 phases).  
  - **Cost**: $Θ(N)$ two-qubit gates and single-qubit rotations.  
  - **Qubits**: $n_1$.

### 2.4 Complexity Summary
| Case    | Time         | Qubits      |
| ------- | ------------ | ----------- |
| Best    | $Θ(n)$       | $Θ(\log n)$ |
| Average | $Θ(n\log n)$ | $Θ(\log n)$ |
| Worst   | $Θ(n^{5/2})$ | $Θ(\log n)$ |

---

## 3. Increment Optimization: Ripple-Increment

Replace the dense `UnitaryGate` with a **ripple-carry** add‑one circuit:

```python
def inc_simple(n_qubits):
    qc = QuantumCircuit(n_qubits, name="inc")
    qc.x(0)
    for j in range(1, n_qubits):
        qc.mcx(list(range(j)), j)
    return qc.to_gate()
```

- **Cost**: $Θ(n_1)$ MCX/X gates (linear in qubit count).  
- **Qubits**: no ancilla.  
- **Effect on complexity**: reduces increment to $O(n)$ overall (once per round), improving average runtime.

---

## 4. Oracle Optimization: OR-Tree Phase Oracle

Trade ancilla qubits for depth by:
1. **Per-index comparators**: set one flag qubit per marked index $i$ if $|idx\>=|i\>$.  
2. **OR-tree**: binary-tree of Toffolis to combine flags into one root ancilla.  
3. **Phase-kick**: Z on the root.  
4. **Uncompute**: invert OR-tree and flags.

```python
oracle_gate = optimized_phase_oracle(n_1, marked_indices)
```
- **Depth**: $Θ(n_1 + \log M)$.  
- **Qubits**: $n_1 + 2M - 1$ ancilla (for $M$ marked items).

---

## 5. Combined Optimized LMSR_Q

- **Increment**: ripple-based $O(n_1)$ gate
- **Oracle**: OR-tree $O(n_1+\log M)$ depth
- **Grover body**: $k=O(1)$ iterations per round on average

| Case  | Rounds $r$  | Time         | Qubits      |
| ----- | ----------- | ------------ | ----------- |
| Best  | 1           | $Θ(n)$       | $Θ(\log n)$ |
| Avg   | $Θ(\log n)$ | $Θ(n\log n)$ | $Θ(\log n)$ |
| Worst | $Θ(n)$      | $Θ(n^{5/2})$ | $Θ(\log n)$ |

---

## 6. QRAM-Powered Coherent Minimum-Finding

Leverage QRAM to eliminate intermediate measurements and surpass the current published quantum bound of $O(n^{3/4})$:

1. **QRAM Storage**  
   Load the list $L$ of length $n$ into an ideal QRAM so that
   
   $$
     \lvert i\rangle\lvert 0\rangle
     \;\xrightarrow{\text{QRAM}}\;
     \lvert i\rangle\lvert L[i]\rangle
   $$
   
   which costs $O(1)$ time and uses $n$ memory cells.

2. **Quantum Comparator Oracle**  
   - **Binary-search version (no hashing):**  
     Find the first position where two rotations differ using $O(\log n)$ QRAM lookups and equality tests.  
   - **Hash-assisted version:**  
     Precompute rolling-hashes of all suffixes in QRAM so that comparing two rotations reduces to one hash-lookup (amortized $O(1)$) plus a final collision-check.

3. **Dür–Høyer Minimum-Finding**  
   Use the fully coherent algorithm of Dür & Høyer (1996) to find the minimal rotation index $i^*$ in one pass:  
   - **Registers**: index registers $\lvert r\rangle,\lvert i\rangle$ (each $\lceil\log_2 n\rceil$ qubits) and a small work register.  
   - **Iterations** ($\Theta(\sqrt{n})$ of):  
     1. **Comparator Oracle**: phase-kick $\lvert i\rangle\lvert r\rangle$ if $\mathrm{Rot}_i < \mathrm{Rot}_r$.  
     2. **Diffusion**: inversion-about-mean on $\lvert i\rangle$.  
   - **Swap & Final Measurement**: swap the roles of $\lvert i\rangle$ and $\lvert r\rangle$, then measure $\lvert r\rangle$ **once** to read out the answer.

4. **Runtime Comparison**  
   | Comparator            | Iterations        | Total Time                               | Qubit Usage                 |
   | --------------------- | ----------------- | ---------------------------------------- | --------------------------- |
   | **Classical best**    | —                 | $\Theta(n)$                              | $n$ classical cells (bits)  |
   | **No QRAM Grover**    | $\Theta(\sqrt n)$ | $\Theta(\sqrt n\cdot n)=\Theta(n^{3/2})$ | $O(\log n)$ work qubits     |
   | **Published quantum** | —                 | $\Theta(n^{3/4})$                        | -                           |
   | **QRAM + Bin-search** | $\Theta(\sqrt n)$ | $\Theta(\sqrt n\log n)$                  | $n$ QRAM + $O(\log n)$ work |
   | **QRAM + Hashing**    | $\Theta(\sqrt n)$ | $\Theta(\sqrt n)$                        | $n$ QRAM + $O(\log n)$ work |

   Our **QRAM + hashing** algorithm achieves a true quadratic speed-up $\Theta(\sqrt n)$, improving on the $O(n^{3/4})$ published bound.

5. **Qubits & Space**  
   - **QRAM cells**: $n$  
   - **Index & work registers**: $O(\log n)$ qubits

6. **Overall Worst-Case**  
- **Time**: $\Theta(\sqrt n\,\log n)$ (binary-search) or $\Theta(\sqrt n)$ (hashing, amortized)  
- **Space**: $n$ QRAM cells + $O(\log n)$ extra qubits  
- **Measurements**: 1 final readout of $|r⟩$

---

## 7. Dependencies & Usage

- Python 3.8+ with Qiskit Terra
- `QuantumCircuit`, `Diagonal`, `MCXGate`

```bash
pip install qiskit
```

- Use `LMSR_Q(L, print_qc=True)` to obtain the circuit and index.
- Note that can change between `ver=1` or `ver=2` to see different approach.

---

## License

MIT © Gary Pham

