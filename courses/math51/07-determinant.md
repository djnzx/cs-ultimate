# Determinant

The **determinant** of a square matrix is a single number associated with the matrix.

It is written as $\det(A)$ or $\lvert A \rvert$.

The determinant answers two fundamental questions:

1. **Is the matrix invertible?** — $\det(A) = 0$ means no, $\det(A) \neq 0$ means yes.
2. **How does the matrix scale space?** — $\lvert \det(A) \rvert$ is the factor by which volumes are multiplied.

---

## 1. Geometric Meaning

A matrix $A$ is a linear transformation: it maps vectors to new vectors.

In 2D, consider the two column vectors of $A$:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

The columns are:

$$
\mathbf{u} =
\begin{bmatrix}
a \\
c
\end{bmatrix}
$$

and:

$$
\mathbf{v} =
\begin{bmatrix}
b \\
d
\end{bmatrix}
$$

These two columns form a parallelogram.

The determinant equals the **signed area** of that parallelogram: $\det(A) = \text{signed area of the parallelogram formed by the columns of } A$ In 3D, the determinant equals the **signed volume** of the parallelepiped formed by the three column vectors.

**Sign of the determinant:**

- $\det(A) > 0$: the transformation preserves orientation (like a rotation).
- $\det(A) < 0$: the transformation flips orientation (like a reflection).
- $\det(A) = 0$: the columns are linearly dependent — the parallelogram has collapsed to a line or a point, and the transformation squashes space into a lower dimension.

**Scale factor:**

If you apply $A$ to any region of space, its volume is multiplied by $\lvert \det(A) \rvert$: $\text{volume after} = \lvert \det(A) \rvert \cdot \text{volume before}$ So:
- $\lvert \det(A) \rvert = 1$: no volume change (rotation, reflection).
- $\lvert \det(A) \rvert > 1$: expansion.
- $\lvert \det(A) \rvert < 1$: compression.
- $\lvert \det(A) \rvert = 0$: complete collapse — the matrix is singular.

---

## 2. Determinant of a $2 \times 2$ Matrix

For:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

the determinant is:

$$
\det(A) = ad - bc
$$

**Why this formula:**

The columns are $\mathbf{u} = (a, c)$ and $\mathbf{v} = (b, d)$.

The area of the parallelogram they span equals:

$$
\lvert ad - bc \rvert
$$

The formula $ad - bc$ multiplies along the main diagonal and subtracts the product along the anti-diagonal.

**Example 1:**

$$
A =
\begin{bmatrix}
3 & 1 \\
2 & 4
\end{bmatrix}
$$

Then:

$$
\det(A) = 3 \cdot 4 - 1 \cdot 2 = 12 - 2 = 10
$$

The columns $(3, 2)$ and $(1, 4)$ form a parallelogram of area 10.

**Example 2 (singular matrix):**

$$
A =
\begin{bmatrix}
2 & 4 \\
1 & 2
\end{bmatrix}
$$

Then:

$$
\det(A) = 2 \cdot 2 - 4 \cdot 1 = 4 - 4 = 0
$$

The columns $(2, 1)$ and $(4, 2)$ are parallel — one is $2 \times$ the other — so the parallelogram has zero area.

**Inverse from the determinant:**

For a $2 \times 2$ matrix, the inverse can be written directly:

$$
A^{-1} = \frac{1}{ad - bc}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
$$

This formula only works when $\det(A) = ad - bc \neq 0$.

---

## 3. Determinant of a $3 \times 3$ Matrix

For:

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

### Cofactor expansion along the first row

$$
\det(A) = a_{11}\det(M_{11}) - a_{12}\det(M_{12}) + a_{13}\det(M_{13})
$$

Each $2 \times 2$ determinant is obtained by **deleting** the row and column of the corresponding entry.

For example:

$$
M_{11} =
\begin{bmatrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{bmatrix}
$$

$$
M_{12} =
\begin{bmatrix}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{bmatrix}
$$

$$
M_{13} =
\begin{bmatrix}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{bmatrix}
$$

The signs alternate: $+$, $-$, $+$.

Expanded fully:

$$
\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})
$$

### Rule of Sarrus (visual shortcut for $3 \times 3$)

Write the matrix and repeat the first two columns to the right:

$$
\begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{vmatrix}
$$

Repeat the first two columns:

$$
\begin{array}{cc}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{array}
$$

**Add** the products of the three **downward** diagonals:

$$
a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}
$$

**Subtract** the products of the three **upward** diagonals:

$$
a_{31}a_{22}a_{13} + a_{32}a_{23}a_{11} + a_{33}a_{21}a_{12}
$$

So:

$$
\det(A) = (a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}) - (a_{31}a_{22}a_{13} + a_{32}a_{23}a_{11} + a_{33}a_{21}a_{12})
$$

**Warning:** Sarrus's rule works only for $3 \times 3$ matrices. Do not apply it to larger matrices.

### Worked example

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

Cofactor expansion along row 1:

$$
M_{11} =
\begin{bmatrix}
5 & 6 \\
8 & 9
\end{bmatrix}
$$

$$
M_{12} =
\begin{bmatrix}
4 & 6 \\
7 & 9
\end{bmatrix}
$$

$$
M_{13} =
\begin{bmatrix}
4 & 5 \\
7 & 8
\end{bmatrix}
$$

$$
\det(A) = 1 \cdot \det(M_{11}) - 2 \cdot \det(M_{12}) + 3 \cdot \det(M_{13})
$$

$$
= 1 \cdot (45 - 48) - 2 \cdot (36 - 42) + 3 \cdot (32 - 35)
$$

$$
= 1 \cdot (-3) - 2 \cdot (-6) + 3 \cdot (-3)
$$

$$
= -3 + 12 - 9 = 0
$$

The determinant is zero, so this matrix is singular — the three rows are linearly dependent (row 3 = 2·row 2 − row 1).

---

## 4. Minors and Cofactors

These are the building blocks for computing determinants of any size.

The **$(i,j)$ minor** $M_{ij}$ is the determinant of the submatrix obtained by deleting row $i$ and column $j$.

$$
M_{ij} = \det(\text{submatrix after deleting row } i \text{ and column } j)
$$

The **$(i,j)$ cofactor** $C_{ij}$ attaches a sign:

$$
C_{ij} = (-1)^{i+j} M_{ij}
$$

The signs form a checkerboard pattern:

| | Column 1 | Column 2 | Column 3 | Column 4 |
|---|---|---|---|---|
| Row 1 | $+$ | $-$ | $+$ | $-$ |
| Row 2 | $-$ | $+$ | $-$ | $+$ |
| Row 3 | $+$ | $-$ | $+$ | $-$ |
| Row 4 | $-$ | $+$ | $-$ | $+$ |

---

## 5. Cofactor Expansion for $n \times n$ Matrices

For any square matrix of any size, expanding along **any row $i$**: $\det(A) = \sum_{j=1}^{n} a_{ij}\, C_{ij}$ Or expanding along **any column $j$**: $\det(A) = \sum_{i=1}^{n} a_{ij}\, C_{ij}$ Both give the same result.

**Choosing the best row or column:** pick the one with the most zeros, since each zero eliminates one term from the sum.

For example, if column 2 is $(0, 0, 5, 0)^T$, expand along column 2 and only one term survives.

**Computational cost:**

Cofactor expansion has cost $O(n!)$ — it is impractical for large matrices.

In practice, the **LU decomposition** is used instead, which computes the determinant in $O(n^3)$ by reducing the matrix to triangular form.

For a triangular matrix, the determinant is simply the product of the diagonal entries:

$$
\det\begin{bmatrix}
d_1 & * & * \\
0 & d_2 & * \\
0 & 0 & d_3
\end{bmatrix}
= d_1 \cdot d_2 \cdot d_3
$$

---

## 6. Properties of Determinants

These properties are useful for computing determinants without expanding every time.

**Multiplicativity:** $\det(AB) = \det(A) \cdot \det(B)$ **Transpose:** $\det(A^T) = \det(A)$ **Inverse:** $\det(A^{-1}) = \frac{1}{\det(A)}$ **Scalar multiplication** (for an $n \times n$ matrix): $\det(cA) = c^n \det(A)$ **Row operations:**

- Swapping two rows **negates** the determinant.
- Multiplying a row by scalar $c$ **multiplies** the determinant by $c$.
- Adding a multiple of one row to another row **leaves the determinant unchanged**.

**Repeated row:**

If two rows are identical: $\det(A) = 0$ because swapping those rows both negates the determinant and leaves the matrix unchanged — so the determinant must be its own negative, forcing it to zero.

**Triangular matrix:**

$$
\det\begin{bmatrix}
d_1 & * & \cdots & * \\
0 & d_2 & \cdots & * \\
\vdots & & \ddots & \vdots \\
0 & 0 & \cdots & d_n
\end{bmatrix}
= d_1 \cdot d_2 \cdots d_n
$$

The determinant is the product of the diagonal entries.

---

## 7. Determinant and Invertibility

A square matrix $A$ is **invertible** if and only if: $\det(A) \neq 0$ When $\det(A) = 0$:
- The columns of $A$ are linearly dependent.
- The transformation squashes space: some non-zero vectors map to $\mathbf{0}$.
- The equation $A\mathbf{x} = \mathbf{b}$ either has no solution or infinitely many solutions.
- No matrix inverse $A^{-1}$ exists.

When $\det(A) \neq 0$:
- The columns span the full space.
- The transformation is bijective.
- $A^{-1}$ exists and is unique.

---

## 8. Determinant and Eigenvalues

The determinant is closely related to eigenvalues — a concept covered in section 16.

Two key facts: (1) the determinant equals the product of all eigenvalues, so $\det(A) = 0$ if and only if at least one eigenvalue is zero; (2) the eigenvalues of $A$ are found by solving $\det(A - \lambda I) = 0$, called the characteristic equation. Both facts are developed fully in the eigenvectors section.

---

## 9. Determinant and the Cross Product

In 3D, the cross product of two vectors can be computed using a determinant.

For $\mathbf{a} = (a_1, a_2, a_3)$ and $\mathbf{b} = (b_1, b_2, b_3)$:

$$
\mathbf{a} \times \mathbf{b} = \det
\begin{bmatrix}
\mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{bmatrix}
$$

Expanding along the first row:

$$
\mathbf{a} \times \mathbf{b} = \mathbf{e}_1(a_2 b_3 - a_3 b_2) - \mathbf{e}_2(a_1 b_3 - a_3 b_1) + \mathbf{e}_3(a_1 b_2 - a_2 b_1)
$$

This is a useful mnemonic: the cross product formula is exactly cofactor expansion applied to this symbolic matrix.

---

## 10. Summary

The **determinant** is a single number $\det(A)$ associated with a square matrix.

**Geometric meaning:** $\lvert \det(A) \rvert$ is the volume scaling factor of the transformation; $\det(A) < 0$ indicates orientation flip.

**Calculation:**

| Matrix size | Method |
|---|---|
| $2 \times 2$ | $\det = ad - bc$ |
| $3 \times 3$ | Cofactor expansion or Sarrus's rule |
| $n \times n$ | Cofactor expansion (theoretical) or LU decomposition (practical, $O(n^3)$) |

**Key facts:**

$$
\det(A) = 0 \iff A \text{ is singular (non-invertible)}
$$

$$
\det(AB) = \det(A)\det(B)
$$

The connection to eigenvalues — including $\det(A) = \prod_i \lambda_i$ and the characteristic equation $\det(A - \lambda I) = 0$ — is covered in section 16.
