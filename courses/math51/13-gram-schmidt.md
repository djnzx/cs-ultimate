# Gram-Schmidt Orthogonalization

The **Gram-Schmidt process** takes a set of linearly independent vectors and produces a set of **orthonormal** vectors that span the same space.

**Orthogonal** means every pair of vectors is perpendicular: $\mathbf{u}_i \cdot \mathbf{u}_j = 0 \quad \text{for } i \neq j$ **Orthonormal** means orthogonal and each vector has length 1:

$$
\mathbf{u}_i \cdot \mathbf{u}_j =
\begin{cases}
1 & i = j \\
0 & i \neq j
\end{cases}
$$

Why this matters: orthonormal bases simplify almost every computation — projections become simple dot products, matrices whose columns are orthonormal have many special properties, and numerical algorithms are more stable in orthonormal coordinates.

---

## 1. The Problem

Suppose we have vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k$ that are linearly independent but not orthogonal.

We want to find $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_k$ such that:

1. They span the same space as the original vectors.
2. They are mutually perpendicular.
3. Each has length 1.

Gram-Schmidt does this by building the orthonormal vectors one at a time, at each step removing all components that point in the already-chosen directions.

---

## 2. The Algorithm

**Step 1.** Normalize the first vector: $\mathbf{u}_1 = \frac{\mathbf{v}_1}{\lVert \mathbf{v}_1 \rVert}$ **Step 2.** Remove from $\mathbf{v}_2$ its component along $\mathbf{u}_1$, then normalize:

$$
\mathbf{e}_2 = \mathbf{v}_2 - (\mathbf{v}_2 \cdot \mathbf{u}_1)\,\mathbf{u}_1
$$

$$
\mathbf{u}_2 = \frac{\mathbf{e}_2}{\lVert \mathbf{e}_2 \rVert}
$$

The term $(\mathbf{v}_2 \cdot \mathbf{u}_1)\,\mathbf{u}_1$ is the projection of $\mathbf{v}_2$ onto $\mathbf{u}_1$, which was covered in the orthogonal components section.

**Step 3.** Remove from $\mathbf{v}_3$ its components along $\mathbf{u}_1$ and $\mathbf{u}_2$, then normalize:

$$
\mathbf{e}_3 = \mathbf{v}_3 - (\mathbf{v}_3 \cdot \mathbf{u}_1)\,\mathbf{u}_1 - (\mathbf{v}_3 \cdot \mathbf{u}_2)\,\mathbf{u}_2
$$

$$
\mathbf{u}_3 = \frac{\mathbf{e}_3}{\lVert \mathbf{e}_3 \rVert}
$$

**General step $k$:**

$$
\mathbf{e}_k = \mathbf{v}_k - \sum_{i=1}^{k-1} (\mathbf{v}_k \cdot \mathbf{u}_i)\,\mathbf{u}_i
$$

$$
\mathbf{u}_k = \frac{\mathbf{e}_k}{\lVert \mathbf{e}_k \rVert}
$$

At each step we subtract all projections onto the previously computed orthonormal vectors, leaving a vector perpendicular to all of them.

---

## 3. Worked Example in 2D

Let:

$$
\mathbf{v}_1 =
\begin{bmatrix}
3 \\
4
\end{bmatrix}
$$

$$
\mathbf{v}_2 =
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

**Step 1.** Normalize $\mathbf{v}_1$:

$$
\lVert \mathbf{v}_1 \rVert = \sqrt{9 + 16} = 5
$$

$$
\mathbf{u}_1 = \frac{1}{5}\mathbf{v}_1
$$

$$
\mathbf{u}_1 =
\begin{bmatrix}
3/5 \\
4/5
\end{bmatrix}
$$

**Step 2.** Project $\mathbf{v}_2$ onto $\mathbf{u}_1$: $\mathbf{v}_2 \cdot \mathbf{u}_1 = 1 \cdot \frac{3}{5} + 0 \cdot \frac{4}{5} = \frac{3}{5}$ Remove the projection:

$$
\mathbf{e}_2
= \mathbf{v}_2 - \frac{3}{5}\mathbf{u}_1
$$

$$
\mathbf{e}_2 =
\begin{bmatrix}
16/25 \\
-12/25
\end{bmatrix}
$$

Normalize:

$$
\lVert \mathbf{e}_2 \rVert = \frac{1}{25}\sqrt{16^2 + 12^2} = \frac{20}{25} = \frac{4}{5}
$$

$$
\mathbf{u}_2 = \frac{25}{20}\mathbf{e}_2
$$

$$
\mathbf{u}_2 =
\begin{bmatrix}
4/5 \\
-3/5
\end{bmatrix}
$$

**Verify orthonormality:**

$$
\mathbf{u}_1 \cdot \mathbf{u}_2 = \frac{3}{5} \cdot \frac{4}{5} + \frac{4}{5} \cdot \left(-\frac{3}{5}\right) = \frac{12}{25} - \frac{12}{25} = 0 \checkmark
$$

$$
\lVert \mathbf{u}_1 \rVert = \sqrt{(3/5)^2 + (4/5)^2} = 1 \checkmark \qquad \lVert \mathbf{u}_2 \rVert = \sqrt{(4/5)^2 + (3/5)^2} = 1 \checkmark
$$

---

## 4. Worked Example in 3D

Let:

$$
\mathbf{v}_1 =
\begin{bmatrix}
1 \\
1 \\
0
\end{bmatrix}
$$

$$
\mathbf{v}_2 =
\begin{bmatrix}
1 \\
0 \\
1
\end{bmatrix}
$$

$$
\mathbf{v}_3 =
\begin{bmatrix}
0 \\
1 \\
1
\end{bmatrix}
$$

**Step 1.**

$$
\lVert \mathbf{v}_1 \rVert = \sqrt{2}
\implies
\mathbf{u}_1 = \frac{1}{\sqrt{2}}\mathbf{v}_1
$$

**Step 2.**

$$
\mathbf{v}_2 \cdot \mathbf{u}_1 = \frac{1}{\sqrt{2}}(1 \cdot 1 + 0 \cdot 1 + 1 \cdot 0) = \frac{1}{\sqrt{2}}
$$

$$
\mathbf{e}_2
= \mathbf{v}_2 - \frac{1}{2}\mathbf{v}_1
$$

$$
\mathbf{e}_2 =
\begin{bmatrix}
1/2 \\
-1/2 \\
1
\end{bmatrix}
$$

$$
\lVert \mathbf{e}_2 \rVert = \sqrt{1/4 + 1/4 + 1} = \sqrt{3/2}
\implies
\mathbf{u}_2 = \frac{1}{\sqrt{3/2}}\mathbf{e}_2
$$

$$
\mathbf{u}_2 =
\frac{1}{\sqrt{6}}
\begin{bmatrix}
1 \\
-1 \\
2
\end{bmatrix}
$$

**Step 3.**

$$
\mathbf{v}_3 \cdot \mathbf{u}_1 = \frac{1}{\sqrt{2}}(0 + 1 + 0) = \frac{1}{\sqrt{2}}
$$

$$
\mathbf{v}_3 \cdot \mathbf{u}_2 = \frac{1}{\sqrt{6}}(0 - 1 + 2) = \frac{1}{\sqrt{6}}
$$

$$
\mathbf{e}_3
= \mathbf{v}_3
- \frac{1}{\sqrt{2}}\mathbf{u}_1
- \frac{1}{\sqrt{6}}\mathbf{u}_2
$$

$$
\mathbf{e}_3 =
\begin{bmatrix}
-2/3 \\
2/3 \\
2/3
\end{bmatrix}
$$

$$
\lVert \mathbf{e}_3 \rVert = \frac{2}{\sqrt{3}}
\implies
\mathbf{u}_3 =
\frac{1}{\sqrt{3}}
\begin{bmatrix}
-1 \\
1 \\
1
\end{bmatrix}
$$

The three vectors $\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$ are mutually orthonormal.

---

## 5. QR Decomposition

Gram-Schmidt directly produces the **QR decomposition** of a matrix.

Given a matrix $A$ with linearly independent columns $\mathbf{v}_1, \dots, \mathbf{v}_n$, running Gram-Schmidt gives: $A = QR$ where:

- $Q = [\mathbf{u}_1 \mid \mathbf{u}_2 \mid \cdots \mid \mathbf{u}_n]$ is a matrix with **orthonormal columns** (an orthogonal matrix when square).
- $R$ is an **upper triangular** matrix whose entries are the dot products and norms computed during Gram-Schmidt.

The entries of $R$ are:

$$
R_{ij} =
\begin{cases}
\mathbf{v}_j \cdot \mathbf{u}_i & i < j \quad \text{(dot products)} \\
\lVert \mathbf{e}_j \rVert & i = j \quad \text{(norms before normalizing)} \\
0 & i > j
\end{cases}
$$

**Uses of QR decomposition:**
- Solving least-squares problems numerically (more stable than computing $(X^TX)^{-1}$).
- Computing eigenvalues iteratively (QR algorithm).
- Numerical implementations of SVD.

---

## 6. Why Orthonormal Bases Are Useful

**Projections become dot products.**

For any vector $\mathbf{x}$, its coordinate in the direction $\mathbf{u}_i$ is simply: $c_i = \mathbf{x} \cdot \mathbf{u}_i$ and: $\mathbf{x} = \sum_i c_i\, \mathbf{u}_i$ No matrix inversion needed — just dot products.

**Matrix products simplify.**

If $Q$ has orthonormal columns: $Q^T Q = I$ So $Q^{-1} = Q^T$ — inversion is just transposition, which is cheap.

**Numerical stability.**

Orthonormal bases keep numbers well-scaled. Algorithms that maintain orthonormality (like the QR algorithm) avoid the numerical blowup that can occur with arbitrary bases.

---

## 7. Connection to Eigenvectors

For **symmetric matrices**, eigenvectors corresponding to distinct eigenvalues are automatically orthogonal to each other.

If we normalize them, we get an orthonormal set without needing Gram-Schmidt.

This is why symmetric matrices (like covariance matrices and the Hessian) have particularly clean decompositions: their eigenvectors form an orthonormal basis, and the matrix can be written as: $A = Q \Lambda Q^T$ where $Q$ is orthogonal (eigenvectors as columns) and $\Lambda$ is diagonal (eigenvalues on diagonal).

---

## 8. Connection to SVD

In Singular Value Decomposition: $A = U \Sigma V^T$ both $U$ and $V$ are orthogonal matrices — their columns are orthonormal.

These columns are the **left singular vectors** and **right singular vectors** of $A$, and they form orthonormal bases for the output and input spaces respectively.

Gram-Schmidt is conceptually the process by which such orthonormal bases are found, though in practice SVD is computed via more numerically stable algorithms.

---

## 9. Summary

**Gram-Schmidt** converts $k$ linearly independent vectors $\mathbf{v}_1, \dots, \mathbf{v}_k$ into $k$ orthonormal vectors $\mathbf{u}_1, \dots, \mathbf{u}_k$ spanning the same space.

At each step $k$:

$$
\mathbf{e}_k = \mathbf{v}_k - \sum_{i=1}^{k-1} (\mathbf{v}_k \cdot \mathbf{u}_i)\,\mathbf{u}_i \qquad \mathbf{u}_k = \frac{\mathbf{e}_k}{\lVert \mathbf{e}_k \rVert}
$$

The result is a matrix of orthonormal columns $Q$, which together with the upper triangular $R$ gives the **QR decomposition**: $A = QR$.

Key applications:

| Use | Why Gram-Schmidt matters |
|---|---|
| QR decomposition | Directly produced by the algorithm |
| Least-squares solving | QR is more numerically stable than normal equations |
| Eigenvalue algorithms | QR algorithm iteratively orthogonalizes |
| SVD | $U$ and $V$ are orthogonal matrices |
| Symmetric matrices | Eigenvectors are already orthogonal — just normalize |
