# Matrices

A **matrix** is a rectangular array of numbers arranged in rows and columns.

For example:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

This matrix has 2 rows and 3 columns.

Matrices extend the idea of vectors: a vector is a list of numbers, and a matrix is a table of numbers.

---

## 1. Notation and Dimensions

A matrix with $m$ rows and $n$ columns is called an **$m \times n$ matrix**.

We write: $A \in \mathbb{R}^{m \times n}$ The element in row $i$ and column $j$ is written as: $A_{ij}$ or sometimes as: $a_{ij}$ For example, for:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

we have:

$$
A_{11} = 1, \quad A_{12} = 2, \quad A_{13} = 3
$$

$$
A_{21} = 4, \quad A_{22} = 5, \quad A_{23} = 6
$$

The first index is the row, and the second index is the column.

---

## 2. Relation to Vectors

A vector is a special case of a matrix.

A **column vector** is an $n \times 1$ matrix:

$$
\mathbf{v} =
\begin{bmatrix}
v_1 \\
v_2 \\
\vdots \\
v_n
\end{bmatrix}
\in \mathbb{R}^{n \times 1}
$$

A **row vector** is a $1 \times n$ matrix:

$$
\mathbf{v}^T =
\begin{bmatrix}
v_1 & v_2 & \cdots & v_n
\end{bmatrix}
\in \mathbb{R}^{1 \times n}
$$

---

## 3. Matrix Addition

Two matrices of the **same dimensions** can be added.

If $A$ and $B$ are both $m \times n$, then:

$$
(A + B)_{ij} = A_{ij} + B_{ij}
$$

We add element by element.

For example:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

$$
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
$$

Then:

$$
A + B =
\begin{bmatrix}
6 & 8 \\
10 & 12
\end{bmatrix}
$$

---

## 4. Scalar Multiplication

A matrix can be multiplied by a scalar.

If $c$ is a number and $A$ is an $m \times n$ matrix, then:

$$
(cA)_{ij} = c \cdot A_{ij}
$$

We multiply every element by $c$.

For example:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

Then:

$$
3A =
\begin{bmatrix}
3 & 6 \\
9 & 12
\end{bmatrix}
$$

---

## 5. Matrix Multiplication

Two matrices can be multiplied if the number of columns in the first equals the number of rows in the second.

If $A \in \mathbb{R}^{m \times k}$ and $B \in \mathbb{R}^{k \times n}$, then the product: $C = AB \in \mathbb{R}^{m \times n}$ The element $C_{ij}$ is computed as: $C_{ij} = \sum_{l=1}^{k} A_{il} B_{lj}$ That means: take row $i$ of $A$ and column $j$ of $B$, multiply them component by component, and sum the results.

For example:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

$$
B =
\begin{bmatrix}
5 & 6 \\
7 & 8
\end{bmatrix}
$$

The element at row 1, column 1 is: $1 \cdot 5 + 2 \cdot 7 = 5 + 14 = 19$ The element at row 1, column 2 is: $1 \cdot 6 + 2 \cdot 8 = 6 + 16 = 22$ The element at row 2, column 1 is: $3 \cdot 5 + 4 \cdot 7 = 15 + 28 = 43$ The element at row 2, column 2 is: $3 \cdot 6 + 4 \cdot 8 = 18 + 32 = 50$.

So:

$$
AB =
\begin{bmatrix}
19 & 22 \\
43 & 50
\end{bmatrix}
$$

---

## 6. Matrix Multiplication Is Not Commutative

In ordinary arithmetic, $ab = ba$.

For matrices, this is **not true in general**: $AB \neq BA$ For example:

$$
A =
\begin{bmatrix}
1 & 2 \\
0 & 1
\end{bmatrix}
$$

$$
B =
\begin{bmatrix}
1 & 0 \\
3 & 1
\end{bmatrix}
$$

Then:

$$
AB =
\begin{bmatrix}
7 & 2 \\
3 & 1
\end{bmatrix}
$$

but:

$$
BA =
\begin{bmatrix}
1 & 2 \\
3 & 7
\end{bmatrix}
$$

The results are different.

---

## 7. Matrix-Vector Multiplication

A special important case is multiplying a matrix by a vector.

If:

$$
A \in \mathbb{R}^{m \times n}
$$

and:

$$
\mathbf{x} \in \mathbb{R}^n
$$

then:

$$
A\mathbf{x} \in \mathbb{R}^m
$$

The result is a new vector.

The $i$-th component of $A\mathbf{x}$ is:

$$
(A\mathbf{x})_i = \sum_{j=1}^{n} A_{ij} x_j
$$

For example:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

$$
\mathbf{x} =
\begin{bmatrix}
5 \\
6
\end{bmatrix}
$$

Then:

$$
A\mathbf{x} =
\begin{bmatrix}
1 \cdot 5 + 2 \cdot 6 \\
3 \cdot 5 + 4 \cdot 6
\end{bmatrix}
$$

So:

$$
A\mathbf{x} =
\begin{bmatrix}
17 \\
39
\end{bmatrix}
$$

Matrix-vector multiplication is the core operation in linear algebra: it takes a vector as input and produces a new vector as output.

---

## 8. Transpose

The **transpose** of a matrix $A$ is written as $A^T$.

It is obtained by swapping rows and columns.

If $A \in \mathbb{R}^{m \times n}$, then $A^T \in \mathbb{R}^{n \times m}$.

The elements satisfy:

$$
(A^T)_{ij} = A_{ji}
$$

For example:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
$$

Then:

$$
A^T =
\begin{bmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{bmatrix}
$$

An important property: $(AB)^T = B^T A^T$ The order reverses.

---

## 9. Square Matrix

A matrix with equal numbers of rows and columns is called a **square matrix**.

If $A \in \mathbb{R}^{n \times n}$, then $A$ is $n \times n$ square.

Square matrices are especially important because they can represent transformations that map $\mathbb{R}^n$ back to $\mathbb{R}^n$.

---

## 10. Identity Matrix

The **identity matrix** $I$ is the square matrix with 1s on the diagonal and 0s everywhere else.

For $n = 2$:

$$
I_2 =
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$

For $n = 3$:

$$
I_3 =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Multiplying any matrix by the identity matrix leaves it unchanged: $AI = A \quad \text{and} \quad IA = A$ And for any vector: $I\mathbf{v} = \mathbf{v}$ The identity matrix plays the role of the number 1 in matrix arithmetic.

---

## 11. Inverse Matrix

For some square matrices, there exists an **inverse matrix** $A^{-1}$ such that: $A A^{-1} = I \quad \text{and} \quad A^{-1} A = I$ Not every square matrix has an inverse.

If the inverse exists, the matrix is called **invertible** or **non-singular**.

If the inverse does not exist, the matrix is called **singular**.

The inverse is useful for solving systems of equations: $A\mathbf{x} = \mathbf{b}$ If $A^{-1}$ exists, then:

$$
\mathbf{x} = A^{-1}\mathbf{b}
$$

---

## 12. Zero Matrix

The **zero matrix** has every entry equal to zero:

$$
\mathbf{0} =
\begin{bmatrix}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0
\end{bmatrix}
$$

Adding the zero matrix to any matrix leaves it unchanged: $A + \mathbf{0} = A$ It plays the role of the number $0$ in matrix arithmetic.

---

## 13. Diagonal Matrix

A **diagonal matrix** is a square matrix where all entries outside the main diagonal are zero:

$$
D =
\begin{bmatrix}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_n
\end{bmatrix}
$$

It is often written compactly as $D = \mathrm{diag}(d_1, d_2, \dots, d_n)$.

Multiplying a vector by $D$ scales each coordinate independently:

$$
D\mathbf{x} =
\begin{bmatrix}
d_1 x_1 \\
d_2 x_2 \\
\vdots \\
d_n x_n
\end{bmatrix}
$$

The identity matrix is a special diagonal matrix with all $d_i = 1$.

Diagonal matrices appear in many places:
- In **scaling transformations**: stretching or compressing each axis independently.
- In decompositions of matrices (covered in later sections).

---

## 14. Symmetric Matrix

A matrix $A$ is **symmetric** if it equals its own transpose:

$$
A = A^T
$$

Equivalently, entry $(i, j)$ equals entry $(j, i)$ for all $i, j$:

$$
A_{ij} = A_{ji}
$$

For example:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
2 & 5 & 4 \\
3 & 4 & 6
\end{bmatrix}
$$

is symmetric because it looks the same when reflected across the main diagonal.

**Where symmetric matrices arise:**

A **covariance matrix** (used in PCA and statistics) is always symmetric: $\Sigma_{ij} = \mathrm{Cov}(x_i, x_j) = \mathrm{Cov}(x_j, x_i) = \Sigma_{ji}$

A **Gram matrix** $G = A^T A$ is always symmetric: $G^T = (A^T A)^T = A^T (A^T)^T = A^T A = G$

---

## 15. Skew-Symmetric Matrix

A matrix $A$ is **skew-symmetric** (also called **antisymmetric**) if it equals the negative of its own transpose:

$$
A^T = -A
$$

Equivalently, every entry satisfies:

$$
A_{ij} = -A_{ji}
$$

This forces all **diagonal entries to be zero**, because $A_{ii} = -A_{ii}$ implies $A_{ii} = 0$.

**Example** ($3 \times 3$):

$$
A =
\begin{bmatrix}
0 & -3 & 2 \\
3 & 0 & -1 \\
-2 & 1 & 0
\end{bmatrix}
$$

Check:

$$
A^T =
\begin{bmatrix}
0 & 3 & -2 \\
-3 & 0 & 1 \\
2 & -1 & 0
\end{bmatrix}
= -A
$$

**Key properties:**

- All diagonal entries are zero.
- All eigenvalues are purely imaginary (or zero) — never real and nonzero.
- The determinant of an odd-sized skew-symmetric matrix is always zero.
- If $A$ is skew-symmetric, then $\mathbf{x}^T A \mathbf{x} = 0$ for all $\mathbf{x}$.

**Symmetric + skew-symmetric decomposition.**

Any square matrix $M$ can be uniquely split into a symmetric part and a skew-symmetric part:

$$
M = \underbrace{\frac{M + M^T}{2}}_{\text{symmetric}} + \underbrace{\frac{M - M^T}{2}}_{\text{skew-symmetric}}
$$

**Connection to cross products.**

In 3D, the cross product $\mathbf{a} \times \mathbf{b}$ can be written as matrix-vector multiplication using the skew-symmetric matrix of $\mathbf{a}$:

$$
[\mathbf{a}]_\times =
\begin{bmatrix}
0 & -a_3 & a_2 \\
a_3 & 0 & -a_1 \\
-a_2 & a_1 & 0
\end{bmatrix}
$$

Then:

$$
\mathbf{a} \times \mathbf{b} = [\mathbf{a}]_\times \mathbf{b}
$$

**Where skew-symmetric matrices appear:**

In **robotics and 3D graphics**, skew-symmetric matrices encode angular velocity and rotation generators. The matrix exponential of a skew-symmetric matrix is a rotation matrix.

The Lie algebra is:

$$
\mathfrak{so}(3)
$$

The corresponding rotation group is:

$$
\mathrm{SO}(3)
$$

In **physics**, the electromagnetic field tensor is skew-symmetric.

In **optimization**, gradient flows on manifolds use skew-symmetric updates to stay on the manifold. One example is Riemannian gradient descent on $\mathrm{SO}(n)$.

---

## 16. Orthogonal Matrix

A square matrix $Q$ is **orthogonal** if its transpose equals its inverse:

$$
Q^T Q = I
$$

and:

$$
Q Q^T = I
$$

Equivalently:

$$
Q^{-1} = Q^T
$$

The columns of $Q$ form an **orthonormal** set: every column has length 1, and any two distinct columns are perpendicular.

Orthogonal matrices preserve lengths: $\lvert Q\mathbf{v} \rvert = \lvert \mathbf{v} \rvert$ and angles: $(Q\mathbf{u}) \cdot (Q\mathbf{v}) = \mathbf{u} \cdot \mathbf{v}$ They represent **rotations** and **reflections** — rigid transformations that do not stretch or squash space.

**Examples:**

The $2 \times 2$ rotation matrix is orthogonal:

$$
R_\theta =
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
$$

because:

$$
R_\theta^T =
\begin{bmatrix}
\cos\theta & \sin\theta \\
-\sin\theta & \cos\theta
\end{bmatrix}
$$

Then:

$$
R_\theta^T R_\theta =
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$

So $R_\theta^T R_\theta = I$.

Orthogonal matrices appear in QR decomposition, SVD, and PCA — all covered in later sections.

---

## 17. Trace

The **trace** of a square matrix $A \in \mathbb{R}^{n \times n}$ is the sum of its diagonal entries:

$$
\mathrm{tr}(A) = \sum_{i=1}^{n} A_{ii}
$$

Equivalently:

$$
\mathrm{tr}(A) = A_{11} + A_{22} + \cdots + A_{nn}
$$

**Example:**

$$
A =
\begin{bmatrix}
3 & 1 & 0 \\
2 & 5 & 4 \\
-1 & 0 & 2
\end{bmatrix}
$$

Then:

$$
\mathrm{tr}(A) = 3 + 5 + 2 = 10
$$

**Key properties:**

- **Linearity:** $\mathrm{tr}(A + B) = \mathrm{tr}(A) + \mathrm{tr}(B)$ and $\mathrm{tr}(cA) = c\,\mathrm{tr}(A)$.
- **Cyclic permutation:** $\mathrm{tr}(ABC) = \mathrm{tr}(BCA) = \mathrm{tr}(CAB)$ (order rotates, but does not fully commute).
- **Transpose:** $\mathrm{tr}(A^T) = \mathrm{tr}(A)$.

**The trace trick.**

The cyclic property makes the trace useful for rewriting scalar expressions involving matrices. Since a scalar equals its own trace:

$$
\mathbf{x}^T A \mathbf{x} = \mathrm{tr}(\mathbf{x}^T A \mathbf{x}) = \mathrm{tr}(A \mathbf{x} \mathbf{x}^T)
$$

This is used extensively in deriving matrix gradients and expectations.

**Where trace appears in ML:**

- **Frobenius norm:** $\lVert A \rVert_F^2 = \mathrm{tr}(A^T A)$ — square root of this is the matrix analogue of vector length.
- **Variance of random projections:** when $\mathbf{x} \sim \mathcal{N}(\mathbf{0}, \Sigma)$, $\mathbb{E}[\lVert \mathbf{x} \rVert^2] = \mathrm{tr}(\Sigma)$.
- **Hutchinson's estimator:** the trace of a large matrix can be estimated cheaply without forming it explicitly: $\mathrm{tr}(A) \approx \frac{1}{K}\sum_{k=1}^K \mathbf{z}_k^T A \mathbf{z}_k$ with random vectors $\mathbf{z}_k$.

---

## 18. Summary

A **matrix** is a rectangular array of numbers: $A \in \mathbb{R}^{m \times n}$ The key operations are:

**Addition** (same dimensions): add element by element.

**Scalar multiplication**: multiply every element by the scalar.

**Matrix multiplication** ($m \times k$ times $k \times n$ gives $m \times n$): $C_{ij} = \sum_{l=1}^{k} A_{il} B_{lj}$ **Transpose**: swap rows and columns, $(A^T)_{ij} = A_{ji}$.

**Trace** (square matrices): $\mathrm{tr}(A) = \sum_i A_{ii}$, equals sum of eigenvalues.

**Determinant** (square matrices, covered in full in the next section): $\det(A) = 0$ iff $A$ is singular.

Special matrix types:

| Name | Definition | Key property |
|---|---|---|
| Zero matrix $\mathbf{0}$ | all entries 0 | additive identity |
| Identity matrix $I$ | diagonal 1s | $AI = IA = A$ |
| Diagonal matrix $D$ | non-zero only on diagonal | scales each axis independently |
| Symmetric matrix | $A = A^T$ | symmetric about main diagonal |
| Skew-symmetric matrix | $A^T = -A$ | zero diagonal, imaginary eigenvalues |
| Orthogonal matrix $Q$ | $Q^T Q = I$ | preserves lengths and angles |
| Invertible matrix | $\det(A) \neq 0$ | $A^{-1}$ exists, $AA^{-1} = I$ |
| Singular matrix | $\det(A) = 0$ | no inverse |

The next section covers the **determinant** in full — how to calculate it for any size matrix, what it means geometrically, and how it connects to invertibility and eigenvalues.
