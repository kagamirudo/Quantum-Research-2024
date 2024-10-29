# I can do classical logic in Quantum Computer. 

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
