# Classical Logic on a Quantum Computer: Exploring the Basics with IBM's Quantum Computing Platform

Quantum computing may sound like the realm of high-level quantum mechanics and futuristic possibilities, 
but one of its fascinating aspects is that it can also handle **classical logic operations** - the same kind 
of operations that run on traditional computers. By running classical logic on quantum hardware, researchers 
can better understand the transition between classical and quantum realms, and developers can explore the 
power of quantum systems with tasks that feel more familiar. 

In this blog, we'll dive into how classical logic operates on quantum computers using **IBM's Quantum Computing platform**. IBM provides an accessible, visual way to work with quantum circuits, so let's explore how you can 
leverage this platform to implement classical operations, such as AND, OR, and NOT, on a quantum computer.

### Why Run Classical Logic on a Quantum Computer?

Quantum computers are known for their ability to handle superposition, entanglement, and parallelism. However, it’s essential to understand that these systems can still implement **classical logic gates** as well, like AND, OR, and NOT, which are the foundational building blocks of traditional computing. Using classical logic on quantum computers has several practical applications:

1. **Testing and Calibration**: Running classical algorithms on quantum hardware is a valuable way to test the system’s accuracy and reliability, allowing developers to benchmark performance.
   
2. **Quantum-Classical Hybrid Models**: Many practical quantum algorithms combine classical logic with quantum operations. Classical gates on a quantum computer let us switch back and forth as needed.

3. **Learning Tool**: For beginners, starting with classical logic helps develop intuition for how quantum gates operate, preparing them to understand more complex quantum algorithms later on.

### Classical Gates on IBM Quantum’s Circuit Composer

IBM's **Quantum Circuit Composer** is a fantastic tool for experimenting with both classical and quantum logic gates. It offers a visual interface to build circuits, drag-and-drop gates, and run simulations on actual quantum hardware. Here’s how to set up a few classical gates on IBM’s quantum platform and observe their outputs.

### Implementing Classical Logic Gates with Qubits

In classical computing, gates manipulate bits—values that are either 0 or 1. In IBM’s Quantum Composer, we can simulate classical gates by manipulating **qubits** in specific ways. Let’s start with some basic classical gates: NOT, AND, and OR. 

#### 1. The NOT Gate

The **NOT gate** in classical computing flips a bit: it changes 0 to 1 and 1 to 0. The quantum equivalent of a NOT gate is the **X gate** in IBM’s Quantum Composer.

- **Setting it up on IBM's platform**: 
- Open a new circuit in IBM's Quantum Composer.
- Drag an **X gate** onto your qubit, which initializes at $$|0\rangle$$.
- Run the circuit and observe the output in the histogram.

When you apply the X gate to a qubit initialized in $$|0\rangle$$, it flips the qubit to $$|1\rangle$$, just like a classical NOT operation. Similarly, applying the X gate to a qubit in $$|1\rangle$$ flips it to $$|0\rangle$$.

#### 2. The AND Gate

The **AND gate** in classical computing outputs 1 only if both inputs are 1. To simulate this on a quantum computer, we use **two qubits** and apply a combination of **X gates** and a **CCNOT (Toffoli) gate**.

- **Setting it up on IBM's platform**:
- Initialize two qubits in the $$|0\rangle$$ state.
- Apply an **X gate** to one or both qubits to represent your inputs (for example, apply X to both to represent input 1 and 1).
- Place a **CCNOT gate** (Controlled-Controlled-NOT gate) with these two qubits as controls and a third qubit as the target.
- Run the circuit and view the output.

The third qubit (the target) will be in the $$|1\rangle$$ state only when both inputs are 1, simulating the AND gate’s behavior.

#### 3. The OR Gate

The **OR gate** outputs 1 if at least one of the inputs is 1. To simulate this, we use two qubits and the **CNOT (Controlled-NOT) gate**.

- **Setting it up on IBM's platform**:
- Start with two qubits in the $$|0\rangle$$ state.
- Apply **X gates** to one or both qubits to represent your inputs.
- Apply **CNOT gates** to control a third qubit based on these inputs.

The third qubit will be in $$|1\rangle$$ if either of the first two qubits is 1, just like an OR gate in classical logic.

### Example Circuit on IBM Quantum Composer

Let's put all of this together in a practical example. Suppose you want to create a circuit that applies a classical AND and OR operation to two input bits and shows the results.

1. **Set up the input qubits**: Initialize two qubits for your inputs. Set their states to $$|0\rangle$$ or $$|1\rangle$$ by applying an X gate if you want them in the 1 state.

2. **Construct the AND gate**:
   - Use two input qubits as control and apply a **CCNOT gate** with a third qubit as the target.
   - This third qubit will represent the output of the AND gate.

3. **Construct the OR gate**:
   - Apply CNOT gates to control a fourth qubit based on the first two inputs.
   - This fourth qubit will represent the output of the OR gate.

4. **Run the circuit and observe results**:
   - Run the circuit and check the output histogram to see the resulting states of your AND and OR qubits.

### Practical Applications of Classical Logic on Quantum Systems

Running classical logic gates on a quantum computer isn’t just an interesting experiment; it has real-world applications:

- **Verification and Testing**: By running familiar classical operations, researchers can verify the fidelity and error rates of quantum gates, an essential step for improving quantum computers’ accuracy.
  
- **Quantum Simulations**: Certain hybrid algorithms blend classical and quantum steps. In these cases, classical gates simulated on qubits play a role in managing the flow and decision-making of quantum computations.

- **Educational Purposes**: For those new to quantum computing, IBM’s platform offers an approachable way to visualize and understand quantum operations by starting with familiar classical gates.

### Conclusion

Quantum computers, while built on fundamentally different principles, can indeed perform classical logic just like a traditional computer. Using IBM’s Quantum Computing platform, we can visualize and experiment with how classical gates operate within a quantum circuit, making it an excellent tool for beginners and experts alike. Classical logic on quantum computers isn’t just a theoretical exercise - it provides practical benefits, from testing system accuracy to bridging the gap between classical and quantum computing.

As we explore classical logic on quantum platforms, we gain insights into the seamless blending of classical and quantum processes. This capability is a big step towards realizing the full power of quantum computing, enabling us to unlock hybrid algorithms and solve complex problems in ways never before possible.


### 1: $$(A \Rightarrow B) \vee (B \Rightarrow A)$$

$$ 
\begin{split}
    (\neg A \vee B) &\vee (\neg B \vee A)\\\\
    (\neg A \vee A) &\vee (\neg B \vee B)\\\\
    \neg \neg [(\neg A \vee A) &\vee (\neg B \vee B)]\\\\
    \neg [\neg (\neg A \vee A) &\wedge \neg (\neg B \vee B)]\\\\
    \neg [(A \wedge \neg A) &\wedge (B \wedge \neg B)]\\\\
    \neg (False &\wedge False)\\\\
    \neg& False\\\\
    &True
\end{split}
$$

### 2: $$(A \Rightarrow B) \wedge (B \Rightarrow A) \equiv A \Leftrightarrow B$$

$$
\begin{split}
    (\neg A \vee B) &\wedge (\neg B \vee A)\\\\
    \neg \neg (\neg A \vee B) &\wedge \neg \neg (\neg B \vee A)\\\\
    \neg (A \wedge \neg B) &\wedge \neg (B \wedge \neg A)
\end{split}
$$

### 3: $$A \oplus B$$

$$
\begin{split}
    (\neg A \wedge B) &\vee (A \wedge \neg B)\\\\
    \neg \neg [(\neg A \wedge B) &\vee (A \wedge \neg B)]\\\\
    \neg [\neg (\neg A \wedge B) &\wedge \neg (A \wedge \neg B)]\\\\
    \neg (A &\Leftrightarrow B)
    \end{split}
$$

### 4: 1-bit Adder

<div align="center">
<style>
table {
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 60%;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    }
thead {
    border-bottom: 1px solid #ddd;
    }
tbody {
    text-align: center;
    }
</style>
<table>
  <thead>
    <tr>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>S</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

$$
\begin{split}
    \Rightarrow C &= A \wedge B\\\\
    \Rightarrow S &= A \oplus B
\end{split}
$$
