## $1: (A \Rightarrow B) \vee (B \Rightarrow A)$

$$
(\neg A \vee B) \vee (\neg B \vee A)\\
(\neg A \vee A) \vee (\neg B \vee B)\\
\neg \neg [(\neg A \vee A) \vee (\neg B \vee B)]\\
\neg [\neg (\neg A \vee A) \wedge \neg (\neg B \vee B)]\\
\neg [(A \wedge \neg A) \wedge (B \wedge \neg B)]\\
\neg (False \wedge False)\\
\neg False\\
True\\
$$

## $2: (A \Rightarrow B) \wedge (B \Rightarrow A) \equiv A \Leftrightarrow B$

$$
(\neg A \vee B) \wedge (\neg B \vee A)\\
\neg \neg (\neg A \vee B) \wedge \neg \neg (\neg B \vee A)\\
\neg (A \wedge \neg B) \wedge \neg (B \wedge \neg A)\\
$$

## $3: A \oplus B$

$$
(\neg A \wedge B) \vee (A \wedge \neg B)\\
\neg \neg [(\neg A \wedge B) \vee (A \wedge \neg B)]\\
\neg [\neg (\neg A \wedge B) \wedge \neg (A \wedge \neg B)]\\
\neg (A \Leftrightarrow B)\\
$$

## 4: 1-bit Adder

| A | B | C | S |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

$$
\Rightarrow C = A \wedge B\\
\Rightarrow S = A \oplus B\\
$$

