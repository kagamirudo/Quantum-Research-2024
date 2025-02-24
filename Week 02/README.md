# Lexicographically Minimal String Rotation (LMSR)

### Introduction

This blog explores **Lexicographically Minimal String Rotation (LMSR)**, a fundamental concept in string algorithms with important applications in data compression, bioinformatics, and pattern matching. The presentation is structured around three key questions:

1. **What is LMSR?**
2. **How do we compute it using classic algorithms (e.g., Booth’s Algorithm)?**
3. **Why is LMSR important? What are its applications?**

---

## 1. What is LMSR?

A **Lexicographically Minimal String Rotation (LMSR)** is the smallest possible rotation of a given string in lexicographic order. In simpler terms, lexicographic order is similar to the way words are sorted in a dictionary, where letters are compared one by one.

### Definition:
For a string `S`, rotating means cyclically shifting characters. Among all possible rotations of `S`, the LMSR is the rotation that appears first lexicographically.

### Example:
Let the string `S = "bca"`. The rotations of `S` are:

- `"bca"`
- `"cab"`
- `"abc"`

The lexicographically minimal rotation is `"abc"`, which comes before `"bca"` and `"cab"` in alphabetical order.

### What does “Lexicographic” Mean?
Lexicographic order is a generalization of the alphabetical order used in dictionaries. Comparisons are made character by character until a difference is found. For example:
- `"abc" < "abd"`
- `"car" < "cat"`

---

## 2. How Do We Compute LMSR?

### Knuth-Morris-Pratt (KMP) Algorithm:
KMP is a string-matching algorithm used to find the occurrence of a pattern (a smaller string) within a larger text. Its key strength lies in its ability to search for the pattern in **linear time** by avoiding unnecessary rechecking of previously matched characters. This is achieved through the use of a **prefix function** (sometimes called the failure function), which stores information about how the pattern matches itself.

#### How KMP Works:
1. **Preprocessing the Pattern**: The algorithm creates a **prefix table** for the pattern. This table records the lengths of the longest proper prefix of the pattern that is also a suffix up to each position in the pattern.
2. **Searching**: Using the prefix table, KMP efficiently shifts the pattern over the text without revisiting previously matched characters. This ensures that each character in the text is compared at most once.

#### Example:
If you are searching for the pattern `"ABABC"` in the text `"ABABDABABC"`, KMP will:
- Preprocess the pattern to create the prefix table.
- Compare the pattern to the text, skipping over parts of the text where a match is already known to have failed, based on the information in the prefix table.

#### Why is KMP Important?
KMP is useful in many real-world string matching problems because it has a time complexity of **O(n + m)**, where `n` is the length of the text and `m` is the length of the pattern. This is an improvement over the brute force approach, which has a time complexity of **O(n * m)**.

Though KMP itself is a string-matching algorithm, the **failure function** idea it uses is similar to Booth’s Algorithm for LMSR. Both algorithms employ a mechanism that allows efficient comparison of substrings without backtracking.

One of the most efficient ways to compute the LMSR is to use **Booth’s Algorithm**. This algorithm runs in linear time, making it optimal for large strings.

### Booth’s Algorithm:
Booth’s Algorithm computes the smallest lexicographical rotation of a string `S` by efficiently comparing all rotations without explicitly generating them. It uses a concatenation trick to avoid the need for multiple rotations. The string `S` is concatenated with itself (`S + S`), and the algorithm finds the lexicographically smallest substring of length equal to the original string.

#### Key Steps:
1. Concatenate the string `S` with itself.
2. Use a failure function (similar to the KMP algorithm) to find the starting index of the LMSR.
3. The rotation starting at this index is the lexicographically smallest rotation.

#### Example:
For `S = "bca"`, concatenating gives `S + S = "bcabca"`. Booth’s Algorithm will find that the lexicographically smallest rotation starts at index 2, corresponding to the rotation `"abc"`.

### Shiloach's Fast Canonization Algorithm:
This algorithm is used to find the canonical labeling of a graph, which involves rearranging the graph's vertex labels to obtain a unique, lexicographically minimal form. This is useful in graph isomorphism testing, where the goal is to determine if two graphs are structurally identical.

#### Key Concepts in Shiloach's Algorithm:
- Canonical Labeling: Assigning a unique, minimal lexicographic label to a graph so that isomorphic graphs (those that have the same structure) have the same label.
- Automorphism Group: A group that preserves the graph's structure (the rearrangements that leave the graph unchanged).
- Lexicographically Minimal Labeling: The labeling of the vertices and edges that produces the smallest possible adjacency matrix when considered as a string.
#### High-Level Approach
- Generating Permutations of the vertices.
- Computing Adjacency Matrices for each permutation.
- Finding the Lexicographically Minimal Adjacency Matrix.

---

## 3. Applications of LMSR

### Why do we care about finding the LMSR?
LMSR has several important applications in both theoretical computer science and practical domains. Some of these include:

1. **Data Compression**: LMSR is used in algorithms like the **Burrows-Wheeler Transform (BWT)**, which is a key part of modern compression tools such as bzip2. LMSR helps sort the rotations of the string to encode the data efficiently.
   
2. **String Matching**: LMSR can be used in **circular string matching**, where you must determine if one string is a rotation of another. This is common in DNA sequencing and pattern-matching algorithms in bioinformatics.

3. **Cryptography**: LMSR is useful in cryptographic protocols where patterns need to be compared or sorted lexicographically.

4. **Combinatorics**: In combinatorial optimization, the LMSR helps in solving problems related to string rotation symmetries and generating minimal representations of cyclic strings.

---

## Conclusion

This blog provides an overview of Lexicographically Minimal String Rotations (LMSR), with a focus on understanding its definition, how to compute it efficiently using Booth’s Algorithm, and why it is useful in various applications. By mastering LMSR, we gain insights into fundamental string operations with far-reaching implications in fields like compression, bioinformatics, and more.

---

## References

- **Booth, S. M. (1983)**, *Lexicographically least circular substrings*, Information Processing Letters.
- **Burrows-Wheeler Transform**, *Data Compression and LMSR*, SpringerLink: [Springer Article](https://link.springer.com/article/10.1007/s00224-023-10146-8#ref-CR21).

--- 

