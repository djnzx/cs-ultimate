# Null Space

The **null space** of a matrix $A$ is the set of all vectors that $A$ maps to the zero vector: $\mathcal{N}(A) = \lbrace\mathbf{x} \mid A\mathbf{x} = \mathbf{0}\rbrace$ It is also called the **kernel** of $A$, written $\ker(A)$.

The null space answers: **which inputs does this transformation destroy?**

---

## 1. The Null Space Is a Subspace

The null space is not just a collection of vectors — it is a **vector subspace** of $\mathbb{R}^n$.

It contains the zero vector: $A\mathbf{0} = \mathbf{0}$.

It is closed under addition: if $A\mathbf{u} = \mathbf{0}$ and $A\mathbf{v} = \mathbf{0}$, then $A(\mathbf{u} + \mathbf{v}) = \mathbf{0}$.

It is closed under scalar multiplication: if $A\mathbf{v} = \mathbf{0}$, then $A(c\mathbf{v}) = \mathbf{0}$.

The **dimension** of the null space is called the **nullity** of $A$.

---

## 2. Finding the Null Space via RREF

To find the null space of $A$, solve $A\mathbf{x} = \mathbf{0}$ using Gaussian elimination.

Form the augmented matrix $[A \mid \mathbf{0}]$ and row-reduce to RREF.

**Example.** Find the null space of:

$$
A =
\begin{bmatrix}
1 & 2 & 2 & 2 \\
2 & 4 & 6 & 8 \\
3 & 6 & 8 & 10
\end{bmatrix}
$$

Row-reduce $[A \mid \mathbf{0}]$:

$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$:

$$
\begin{bmatrix}
1 & 2 & 2 & 2 \\
0 & 0 & 2 & 4 \\
0 & 0 & 2 & 4
\end{bmatrix}
$$

$R_3 \leftarrow R_3 - R_2$, $R_2 \leftarrow \tfrac{1}{2}R_2$:

$$
\begin{bmatrix}
1 & 2 & 2 & 2 \\
0 & 0 & 1 & 2 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

$R_1 \leftarrow R_1 - 2R_2$:

$$
\text{RREF:} \quad
\begin{bmatrix}
1 & 2 & 0 & -2 \\
0 & 0 & 1 & 2 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

**Identify pivot and free variables:**

- Columns 1 and 3 have pivots → $x_1$ and $x_3$ are **pivot variables**.
- Columns 2 and 4 have no pivots → $x_2$ and $x_4$ are **free variables**.

Free variables can be anything. Set $x_2 = s$ and $x_4 = t$ (arbitrary real numbers).

**Back-substitute:**

From row 2: $x_3 = -2t$.

From row 1: $x_1 = -2s + 2t$.

So the general solution is:

$$
\mathbf{x} =
\begin{bmatrix}
-2s + 2t \\
s \\
-2t \\
t
\end{bmatrix}
$$

Equivalently:

$$
\mathbf{x} =
s\mathbf{v}_1 + t\mathbf{v}_2
$$

The **null space** is the span of these two vectors:

$$
\mathcal{N}(A) = \mathrm{span}\lbrace
\mathbf{v}_1,
\mathbf{v}_2
\rbrace
$$

where:

$$
\mathbf{v}_1 =
\begin{bmatrix}
-2 \\
1 \\
0 \\
0
\end{bmatrix}
$$

and:

$$
\mathbf{v}_2 =
\begin{bmatrix}
2 \\
0 \\
-2 \\
1
\end{bmatrix}
$$

This is a 2-dimensional subspace of $\mathbb{R}^4$.

---

## 3. Rank-Nullity Theorem

The **rank-nullity theorem** is a fundamental relationship between the rank of a matrix and the dimension of its null space.

For a matrix $A \in \mathbb{R}^{m \times n}$: $\mathrm{rank}(A) + \mathrm{nullity}(A) = n$ where:
- $\mathrm{rank}(A)$ = number of pivots = number of linearly independent columns.
- $\mathrm{nullity}(A)$ = dimension of $\mathcal{N}(A)$ = number of free variables.

**In the example above:**

$A$ is $3 \times 4$ ($n = 4$), has 2 pivots, so $\mathrm{rank}(A) = 2$.

Therefore: $\mathrm{nullity}(A) = 4 - 2 = 2$. ✓

**Intuition:** the $n$ dimensions of the input split into two groups — the $r = \mathrm{rank}(A)$ dimensions that the matrix "uses" (mapped to nonzero output), and the $n - r$ dimensions it collapses to zero.

---

## 4. Geometric Interpretation

A matrix $A$ is a linear transformation $\mathbb{R}^n \to \mathbb{R}^m$.

The null space is the set of input directions that get **collapsed** — mapped to zero.

If $\mathcal{N}(A) = \lbrace\mathbf{0}\rbrace$ (trivial null space, $\mathrm{nullity} = 0$), then $A$ is injective: different inputs give different outputs, nothing is lost.

If $\mathcal{N}(A)$ is non-trivial, then $A$ squashes a whole subspace of directions to zero. Information is lost — the transformation cannot be reversed.

---

## 5. Null Space and Invertibility

A square $n \times n$ matrix $A$ is invertible if and only if: $\mathcal{N}(A) = \lbrace\mathbf{0}\rbrace$ Equivalently:

$$
\mathrm{rank}(A) = n \quad \iff \quad \det(A) \neq 0 \quad \iff \quad \mathcal{N}(A) = \lbrace\mathbf{0}\rbrace
$$

These three conditions are all equivalent ways of saying the matrix is non-singular.

When $A$ is singular, $\det(A) = 0$, and there exist non-zero vectors $\mathbf{x}$ with $A\mathbf{x} = \mathbf{0}$. The null space is the set of all those vectors.

---

## 6. Solution Structure for $A\mathbf{x} = \mathbf{b}$

The null space explains the structure of all solutions to $A\mathbf{x} = \mathbf{b}$.

If $\mathbf{x}_p$ is any particular solution (so $A\mathbf{x}_p = \mathbf{b}$), then **every** solution has the form: $\mathbf{x} = \mathbf{x}_p + \mathbf{x}_n$ where $\mathbf{x}_n \in \mathcal{N}(A)$ is any vector in the null space.

**Why:** if $A\mathbf{x}_p = \mathbf{b}$ and $A\mathbf{x}_n = \mathbf{0}$, then:

$$
A(\mathbf{x}_p + \mathbf{x}_n) = A\mathbf{x}_p + A\mathbf{x}_n = \mathbf{b} + \mathbf{0} = \mathbf{b}
$$

So the set of all solutions is a "shifted copy" of the null space, centered at the particular solution.

| Null space | Solutions to $A\mathbf{x} = \mathbf{b}$ |
|---|---|
| $\lbrace\mathbf{0}\rbrace$ | Unique solution (if one exists) |
| 1-dimensional | Line of solutions |
| $k$-dimensional | $k$-dimensional affine subspace of solutions |

---

## 7. The Four Fundamental Subspaces

Every matrix $A \in \mathbb{R}^{m \times n}$ has four associated subspaces:

| Subspace | Definition | Lives in | Dimension |
|---|---|---|---|
| Column space $\mathcal{C}(A)$ | Span of columns of $A$ | $\mathbb{R}^m$ | $r$ |
| Null space $\mathcal{N}(A)$ | $\lbrace\mathbf{x} : A\mathbf{x} = \mathbf{0}\rbrace$ | $\mathbb{R}^n$ | $n - r$ |
| Row space $\mathcal{C}(A^T)$ | Span of rows of $A$ | $\mathbb{R}^n$ | $r$ |
| Left null space $\mathcal{N}(A^T)$ | $\lbrace\mathbf{y} : A^T\mathbf{y} = \mathbf{0}\rbrace$ | $\mathbb{R}^m$ | $m - r$ |

where $r = \mathrm{rank}(A)$.

These four subspaces have a deep orthogonality structure:

- The **null space** is perpendicular to the **row space** (both in $\mathbb{R}^n$).
- The **left null space** is perpendicular to the **column space** (both in $\mathbb{R}^m$).

The system $A\mathbf{x} = \mathbf{b}$ has a solution if and only if $\mathbf{b}$ is in the column space $\mathcal{C}(A)$.

---

## 8. Use Cases in Machine Learning

**Redundant features.** If the data matrix $X \in \mathbb{R}^{m \times n}$ has a non-trivial null space, then some features are linear combinations of others — they carry no independent information. The model has infinitely many equally good parameter settings, differing by vectors in $\mathcal{N}(X)$.

**Underdetermined systems.** In neural networks with more parameters than training examples, the normal equations are underdetermined: there are infinitely many parameter vectors that achieve zero training loss. They form an affine subspace, and the particular solution found depends on initialization and optimization dynamics.

**Regularization.** $L_2$ regularization (ridge regression) replaces: $X^T X \mathbf{\theta} = X^T \mathbf{y}$ with: $(X^T X + \lambda I)\mathbf{\theta} = X^T \mathbf{y}$ The added $\lambda I$ makes the matrix full rank even when $X^T X$ is singular — it shrinks the null space to $\lbrace\mathbf{0}\rbrace$ and produces a unique solution.

**PCA and SVD.** The null space of the data matrix corresponds to directions along which there is zero variance. PCA discards these directions, keeping only the column space of $X$ (the directions of actual variation).

---

## 9. Summary

The **null space** of $A$ is: $\mathcal{N}(A) = \lbrace\mathbf{x} : A\mathbf{x} = \mathbf{0}\rbrace$ Found by reducing $[A \mid \mathbf{0}]$ to RREF and expressing free variables as parameters.

**Rank-nullity theorem:** $\mathrm{rank}(A) + \mathrm{nullity}(A) = n$ **Connection to invertibility** (for square $A$): $A \text{ invertible} \iff \mathcal{N}(A) = \lbrace\mathbf{0}\rbrace \iff \det(A) \neq 0$ **Solution structure:**

$$
\lbrace\text{all solutions to } A\mathbf{x} = \mathbf{b}\rbrace = \mathbf{x}_p + \mathcal{N}(A)
$$
