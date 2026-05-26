# Linear Independence, Span, and Basis

These three concepts describe the structure of sets of vectors and underpin almost every idea in linear algebra.

---

## 1. Linear Combination

A **linear combination** of vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k$ is any expression of the form: $c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k$ where $c_1, \dots, c_k$ are real numbers called **coefficients**.

**Example.** In $\mathbb{R}^3$, let $\mathbf{v}_1 = (1, 0, 0)^T$, $\mathbf{v}_2 = (0, 1, 0)^T$. Then: $3\mathbf{v}_1 - 2\mathbf{v}_2 = (3, -2, 0)^T$ is a linear combination. Any vector of the form $(a, b, 0)^T$ is a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$.

---

## 2. Span

The **span** of a set of vectors $\lbrace\mathbf{v}_1, \dots, \mathbf{v}_k\rbrace$ is the set of **all possible** linear combinations:

$$
\mathrm{span}\lbrace\mathbf{v}_1, \dots, \mathbf{v}_k\rbrace
= \lbrace c_1 \mathbf{v}_1 + \cdots + c_k \mathbf{v}_k \mid c_i \in \mathbb{R} \rbrace
$$

Geometrically, span is the "reach" of a set of vectors.

**Examples:**

- $\mathrm{span}\lbrace(1,0)^T\rbrace$ is the $x$-axis in $\mathbb{R}^2$ — a line.
- $\mathrm{span}\lbrace(1,0)^T, (0,1)^T\rbrace$ is all of $\mathbb{R}^2$ — a plane.
- $\mathrm{span}\lbrace(1,0,0)^T, (0,1,0)^T\rbrace$ is the $xy$-plane in $\mathbb{R}^3$.

The span of any set of vectors is always a **subspace**: it contains $\mathbf{0}$, and is closed under addition and scalar multiplication.

---

## 3. Linear Independence

A set of vectors $\lbrace\mathbf{v}_1, \dots, \mathbf{v}_k\rbrace$ is **linearly independent** if the only way to write the zero vector as a linear combination is with all-zero coefficients:

$$
c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k = \mathbf{0} \quad \implies \quad c_1 = c_2 = \cdots = c_k = 0
$$

If there exists a non-trivial combination (not all coefficients zero) that equals $\mathbf{0}$, the set is **linearly dependent** — meaning at least one vector is redundant (expressible as a combination of the others).

**Example: dependent set.** $\mathbf{v}_1 = (1,2)^T$, $\mathbf{v}_2 = (2,4)^T$. Then $2\mathbf{v}_1 - \mathbf{v}_2 = \mathbf{0}$, so they are linearly dependent. $\mathbf{v}_2$ is just $2\mathbf{v}_1$ — no new direction.

**Example: independent set.** $\mathbf{v}_1 = (1,0)^T$, $\mathbf{v}_2 = (0,1)^T$. Then $c_1(1,0) + c_2(0,1) = (c_1, c_2) = (0,0)$ forces $c_1 = c_2 = 0$. ✓

**How to check:** try to solve $c_1 \mathbf{v}_1 + \cdots + c_k \mathbf{v}_k = \mathbf{0}$ for the coefficients. If the only solution is $c_1 = \cdots = c_k = 0$, the set is independent. A systematic matrix-based method for checking this will be introduced once Gaussian elimination is covered.

---

## 4. Basis

A **basis** for a vector space (or subspace) $V$ is a set of vectors that is:
1. **Linearly independent** — no redundancy.
2. **Spans** $V$ — every vector in $V$ can be written as a linear combination.

A basis is the minimal description of a space: it has exactly as many vectors as the space has "dimensions."

**Standard basis of $\mathbb{R}^n$:**

$$
\mathbf{e}_1 =
\begin{bmatrix}
1 \\
0 \\
\vdots \\
0
\end{bmatrix}
$$

$$
\mathbf{e}_2 =
\begin{bmatrix}
0 \\
1 \\
\vdots \\
0
\end{bmatrix}
$$

and so on, up to:

$$
\mathbf{e}_n =
\begin{bmatrix}
0 \\
0 \\
\vdots \\
1
\end{bmatrix}
$$

Any other basis for $\mathbb{R}^n$ also has exactly $n$ vectors.

**Non-uniqueness.** A space has infinitely many bases, but they all have the same number of vectors.

---

## 5. Dimension

The **dimension** of a vector space is the number of vectors in any of its bases: $\dim(V) = \text{number of vectors in a basis for } V$ This is well-defined: any two bases of $V$ have the same number of vectors.

**Examples:**

| Space | Dimension |
|---|---|
| $\mathbb{R}^n$ | $n$ |
| $xy$-plane in $\mathbb{R}^3$ | 2 |
| A line through the origin in $\mathbb{R}^3$ | 1 |
| $\lbrace\mathbf{0}\rbrace$ | 0 |

---

## 6. Coordinates

Once a basis $\lbrace\mathbf{b}_1, \dots, \mathbf{b}_n\rbrace$ is fixed, every vector $\mathbf{v}$ in the space has **unique coordinates** $(c_1, \dots, c_n)$ such that: $\mathbf{v} = c_1 \mathbf{b}_1 + \cdots + c_n \mathbf{b}_n$ Changing the basis changes the coordinates of vectors but not the vectors themselves — this is the idea behind change-of-basis matrices and eigenvector decompositions.

---

## 7. Use Cases in Machine Learning

**Feature redundancy.** If the columns of a feature matrix $X$ are linearly dependent, some features are exact linear combinations of others. The rank of $X$ is less than $n$, meaning the model has infinitely many equally-fit parameter vectors. Regularization or dimensionality reduction resolves this.

**Embedding dimension.** When training word embeddings or variational autoencoders, the embedding dimension $d$ is the number of basis directions you allow the representation to use. A $d$-dimensional embedding encodes at most $d$ independent factors of variation.

**Principal Component Analysis.** PCA finds the basis of $\mathbb{R}^n$ that best explains variance in data. The selected principal components form an orthonormal basis for the subspace of highest variance.

**Kernel methods.** The reproducing kernel Hilbert space (RKHS) used in SVMs is an infinite-dimensional vector space. Linear independence and span generalize to that setting.
