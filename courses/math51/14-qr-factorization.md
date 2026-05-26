# QR Factorization

**QR factorization** decomposes a matrix $A$ into the product: $A = QR$ where:
- $Q$ has **orthonormal columns** — every column has length 1, and any two columns are perpendicular.
- $R$ is **upper triangular**.

For a full-rank $m \times n$ matrix ($m \geq n$):
- $Q \in \mathbb{R}^{m \times n}$ (thin QR) or $Q \in \mathbb{R}^{m \times m}$ (full QR).
- $R \in \mathbb{R}^{n \times n}$ (thin) or $R \in \mathbb{R}^{m \times n}$ (full).

QR exists for **any** $m \times n$ matrix with $m \geq n$ and linearly independent columns.

---

## 1. Thin QR vs Full QR

**Thin QR** (also called "economy QR" or "reduced QR"):

$$
A = Q_{\mathrm{thin}} R_{\mathrm{thin}} \quad Q_{\mathrm{thin}} \in \mathbb{R}^{m \times n},\; R_{\mathrm{thin}} \in \mathbb{R}^{n \times n}
$$

The $n$ columns of $Q_{\mathrm{thin}}$ form an orthonormal basis for the column space of $A$.

This is what Gram-Schmidt produces directly.

**Full QR:**

$$
A = Q_{\mathrm{full}} R_{\mathrm{full}} \quad Q_{\mathrm{full}} \in \mathbb{R}^{m \times m},\; R_{\mathrm{full}} \in \mathbb{R}^{m \times n}
$$

$Q_{\mathrm{full}}$ is a full square orthogonal matrix ($Q^T Q = Q Q^T = I$). Its extra $m - n$ columns span the left null space of $A$ (vectors orthogonal to the column space of $A$).

The bottom $m - n$ rows of $R_{\mathrm{full}}$ are all zero.

For solving linear systems and least squares, thin QR suffices. Full QR is needed when the complete orthogonal structure of $A$ is required.

---

## 2. Connection to Gram-Schmidt

The Gram-Schmidt process (covered in the previous section) directly produces the thin QR factorization.

Running Gram-Schmidt on the columns of $A = [\mathbf{v}_1 \mid \mathbf{v}_2 \mid \cdots \mid \mathbf{v}_n]$ gives orthonormal vectors $\mathbf{u}_1, \dots, \mathbf{u}_n$.

The upper triangular matrix $R$ records the dot products and norms computed:

$$
R_{ij} =
\begin{cases}
\mathbf{v}_j \cdot \mathbf{u}_i & i < j \\
\lVert \mathbf{e}_j \rVert & i = j \\
0 & i > j
\end{cases}
$$

**Example.** For $A =
\begin{bmatrix}
1 & 1 \\
1 & 0 \\
0 & 1
\end{bmatrix}$:

Column 1: $\mathbf{v}_1 = (1,1,0)^T$, $\lVert \mathbf{v}_1 \rVert = \sqrt{2}$, so $\mathbf{u}_1 = (1/\sqrt{2},\, 1/\sqrt{2},\, 0)^T$.

Column 2: projection of $\mathbf{v}_2 = (1,0,1)^T$ onto $\mathbf{u}_1$:

$$
\mathbf{v}_2 \cdot \mathbf{u}_1 = \frac{1}{\sqrt{2}}
$$

$$
\mathbf{e}_2 = (1,0,1)^T - \frac{1}{\sqrt{2}} \cdot \mathbf{u}_1 = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)^T \qquad \lVert \mathbf{e}_2 \rVert = \sqrt{\frac{3}{2}}
$$

$$
\mathbf{u}_2 = \frac{1}{\sqrt{3/2}}\left(\frac{1}{2}, -\frac{1}{2}, 1\right)^T = \left(\frac{1}{\sqrt{6}}, -\frac{1}{\sqrt{6}}, \frac{2}{\sqrt{6}}\right)^T
$$

Therefore:

$$
Q =
\begin{bmatrix}
1/\sqrt{2} & 1/\sqrt{6} \\
1/\sqrt{2} & -1/\sqrt{6} \\
0 & 2/\sqrt{6}
\end{bmatrix}
$$

$$
R =
\begin{bmatrix}
\sqrt{2} & 1/\sqrt{2} \\
0 & \sqrt{3/2}
\end{bmatrix}
$$

---

## 3. Householder Reflections

Gram-Schmidt is simple to understand but numerically unstable for large matrices — rounding errors accumulate and the columns of $Q$ lose orthogonality.

**Householder reflections** are the standard numerical method. They produce the same QR factorization but maintain near-perfect orthogonality.

A Householder reflector is a matrix of the form: $H = I - 2\mathbf{v}\mathbf{v}^T, \qquad \lVert \mathbf{v} \rVert = 1$ It reflects vectors across the hyperplane orthogonal to $\mathbf{v}$. Since $H^T H = I$ and $H^2 = I$, it is both orthogonal and its own inverse.

**The idea:** choose $\mathbf{v}$ so that $H$ maps a given column to a multiple of a standard basis vector: $H\mathbf{a} = \lVert \mathbf{a} \rVert\,\mathbf{e}_1$ Applying $H$ zeros out all but the first entry of $\mathbf{a}$.

Successive Householder reflectors $H_1, H_2, \dots, H_n$ applied to the columns of $A$ produce:

$$
H_n \cdots H_2 H_1 A = R \implies A = H_1 H_2 \cdots H_n R = QR
$$

since each $H_i$ is orthogonal and $Q = H_1 \cdots H_n$ is therefore orthogonal.

**Numerical stability:** Householder reflectors only involve subtractions and a normalization — no divisions by small numbers — making them far more stable than Gram-Schmidt for large matrices.

---

## 4. Solving $A\mathbf{x} = \mathbf{b}$ with QR

For a square invertible $A = QR$:

$$
A\mathbf{x} = \mathbf{b} \implies QR\mathbf{x} = \mathbf{b} \implies R\mathbf{x} = Q^T\mathbf{b}
$$

Since $Q^T Q = I$, multiplying both sides by $Q^T$ is exact (orthogonal multiplication).

Then $R\mathbf{x} = Q^T \mathbf{b}$ is solved by back substitution in $O(n^2)$.

**Compared to LU:** QR is more numerically stable (Householder uses only reflections, no divisions by potentially small pivots) but about twice as expensive for square systems. In practice, both are used depending on the application.

---

## 5. Least Squares via QR

The most important application of QR in machine learning is **solving least-squares problems**.

Given $A \in \mathbb{R}^{m \times n}$ with $m > n$ (overdetermined — more equations than unknowns), there is generally no exact solution to $A\mathbf{x} = \mathbf{b}$.

Instead, find $\mathbf{x}$ that minimizes: $\lVert \mathbf{b} - A\mathbf{x} \rVert^2$ **Using QR:** substitute $A = QR$: $\lVert \mathbf{b} - QR\mathbf{x} \rVert^2 = \lVert Q^T\mathbf{b} - R\mathbf{x} \rVert^2$ (Since multiplication by orthogonal $Q^T$ preserves norms.)

The minimum is achieved when the top $n$ components satisfy: $R\mathbf{x} = (Q^T\mathbf{b})_{1:n}$ This is solved by back substitution.

**Why QR is preferred over the normal equations $(A^TA)\mathbf{x} = A^T\mathbf{b}$:**

The normal equations square the condition number of $A$. If $A$ is mildly ill-conditioned, $A^TA$ can be severely ill-conditioned, causing large numerical errors.

QR avoids forming $A^TA$ entirely, so its condition number equals that of $A$ — far more stable.

---

## 6. QR Algorithm for Eigenvalues

The **QR algorithm** is the standard method for computing all eigenvalues of a matrix.

It works by repeatedly factorizing: $A_k = Q_k R_k$ and then recombining in reverse order: $A_{k+1} = R_k Q_k$ Each iteration preserves the eigenvalues (since $A_{k+1} = Q_k^T A_k Q_k$ is a similarity transformation) but moves the matrix closer to upper triangular form.

When the matrix converges to upper triangular, the eigenvalues appear on the diagonal.

The QR algorithm converges for all real matrices, making it the practical basis for eigenvalue solvers in LAPACK and NumPy's `np.linalg.eig`.

---

## 7. Complexity

| Method | Cost |
|---|---|
| Gram-Schmidt QR | $O(mn^2)$ — simple but unstable |
| Householder QR | $O(mn^2)$ — same asymptotic, far more stable |
| Solve $A\mathbf{x} = \mathbf{b}$ after QR | $O(n^2)$ back substitution |
| Least-squares with QR | $O(mn^2)$ factorization + $O(n^2)$ solve |

For $m \times n$ matrices with $m \gg n$, QR costs $O(mn^2)$, which is dominated by the tall $m$ dimension.

---

## 8. Summary

QR factorization:

$$
A = QR
$$

| | Thin QR | Full QR |
|---|---|---|
| $Q$ size | $m \times n$, orthonormal columns | $m \times m$, full orthogonal matrix |
| $R$ size | $n \times n$, upper triangular | $m \times n$, upper triangular (bottom rows zero) |

Key computation methods:

| Method | When to use |
|---|---|
| Gram-Schmidt | Understanding and small matrices |
| Householder reflections | Production code — numerically stable |

Main applications:

| Application | Why QR |
|---|---|
| Solving $A\mathbf{x} = \mathbf{b}$ | Stable, no condition number squaring |
| Least-squares regression | Avoids forming $A^TA$ |
| Eigenvalue computation | QR algorithm iteratively diagonalizes |
| Basis for SVD algorithms | SVD computed via Golub-Reinsch (uses QR internally) |
