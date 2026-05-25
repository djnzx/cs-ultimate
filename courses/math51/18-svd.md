# SVD: What It Is and Why It Matters

**SVD** means **Singular Value Decomposition**.

It is very close to eigenvectors, but it is more general and often more practical in Machine Learning.

For any matrix: $A$ SVD says we can decompose it as: $A = U \Sigma V^T$ where: $U$ contains **left singular vectors**, $V$ contains **right singular vectors**, $\Sigma$ contains **singular values**.

---

## 1. Intuition

SVD says:

> any matrix transformation can be understood as three simpler transformations.

The matrix: $A$ can be seen as: $A = U \Sigma V^T$ which means:

$$
\text{rotate/change basis} \rightarrow \text{stretch/shrink} \rightarrow \text{rotate/change basis}
$$

More precisely: $V^T$ changes the input coordinate system, $\Sigma$ scales the axes, $U$ changes the output coordinate system.

So SVD finds the **natural input directions** and **natural output directions** of a matrix.

---

## 2. Relation to Eigenvectors

Eigenvectors require: $A v = \lambda v$ This works most naturally when: $A$ is a square matrix: $A \in \mathbb{R}^{n \times n}$ SVD works for **any rectangular matrix**: $A \in \mathbb{R}^{m \times n}$ That is very important in Machine Learning, because data matrices are usually rectangular.

For example:

$$
A =
\begin{bmatrix}
\text{sample}_1 \\
\text{sample}_2 \\
\vdots \\
\text{sample}_m
\end{bmatrix}
$$

where: $m = \text{number of samples}$ and: $n = \text{number of features}$ Usually: $m \ne n$ So SVD is often more useful than ordinary eigen-decomposition.

---

## 3. Geometric Meaning

SVD says that a matrix transforms space by taking special orthogonal input directions: $v_1, v_2, \ldots, v_n$ and mapping them into special orthogonal output directions: $u_1, u_2, \ldots, u_m$ with scaling factors: $\sigma_1, \sigma_2, \ldots$ The core relation is: $A v_i = \sigma_i u_i$ This is similar to eigenvectors, but not exactly the same.

For eigenvectors: $A v_i = \lambda_i v_i$ The direction stays the same.

For SVD: $A v_i = \sigma_i u_i$ The input direction: $v_i$ is transformed into an output direction: $u_i$ with scale: $\sigma_i$ So SVD is about finding the cleanest directions of transformation **from input space to output space**.

---

## 4. Singular Values

The diagonal matrix $\Sigma$ contains singular values $\sigma_1 \ge \sigma_2 \ge \cdots \ge 0$. A large singular value means this direction is important. A small singular value means this direction is weak, noisy, or less important. A zero singular value means this direction is lost by the transformation.

---

## 5. Why SVD Is Useful

SVD allows us to rewrite a matrix as a sum of simpler rank-one matrices:

$$
A = \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T + \cdots + \sigma_r u_r v_r^T
$$

or, more compactly:

$$
A = \sum_{i=1}^{r} \sigma_i u_i v_i^T
$$

Each term is one structural pattern.

The first term: $\sigma_1 u_1 v_1^T$ captures the strongest pattern.

The second term captures the next strongest pattern, and so on.

So SVD decomposes a matrix into ordered layers of importance.

---

## 6. Low-Rank Approximation

One of the most important uses of SVD is approximation.

Instead of keeping all terms:

$$
A = \sum_{i=1}^{r} \sigma_i u_i v_i^T
$$

we keep only the first: $k$ terms:

$$
A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^T
$$

where: $k \ll r$ This gives a compressed version of the matrix.

It keeps the most important structure and removes weaker details.

That is why SVD is used for:

- compression
- denoising
- dimensionality reduction
- recommender systems
- latent semantic analysis
- PCA
- embeddings
- numerical stability

---

## 7. SVD and PCA

PCA can be computed using SVD.

Suppose we have a centered data matrix: $X$ where rows are samples and columns are features.

PCA can be found from the covariance matrix: $C = \frac{1}{m - 1} X^T X$ Then we can compute eigenvectors of: $C$ But instead, we can compute SVD directly: $X = U \Sigma V^T$ The columns of: $V$ are the principal directions.

The singular values: $\sigma_i$ are related to the explained variance:

$$
\lambda_i = \frac{\sigma_i^2}{m - 1}
$$

So PCA is deeply connected to SVD.

In practice, PCA is often implemented through SVD because it is numerically stable and works well for rectangular data matrices.

---

## 8. SVD in Machine Learning

In Machine Learning, data is often represented as a matrix $X \in \mathbb{R}^{m \times n}$ where $m$ is the number of examples and $n$ is the number of features. SVD helps discover hidden structure in this matrix.

For example, $X = U \Sigma V^T$ can be interpreted informally as data = objects × importance × features. More concretely: $U$ describes samples in a latent coordinate system, $\Sigma$ says how important each latent dimension is, and $V$ describes feature directions.

---

## 9. Example: Recommender Systems

Suppose we have a user-item rating matrix $R$, where rows are users, columns are movies, and $R_{ij}$ is the rating of user $i$ for movie $j$. SVD factorizes:

$$
R \approx U_k \Sigma_k V_k^T
$$

approximating ratings using $k$ hidden factors. These hidden dimensions may roughly correspond to things like action vs drama, serious vs entertaining, or old vs modern movies. The model does not need these labels explicitly — it discovers useful latent dimensions from the matrix structure.

---

## 10. Summary

Eigenvectors ask: $A v = \lambda v$ Meaning:

> which directions stay the same under this square transformation?

SVD asks: $A v_i = \sigma_i u_i$ Meaning:

> which input directions are transformed into clean output directions, and how strongly?

The full decomposition is: $A = U \Sigma V^T$ SVD is useful because it reveals the strongest hidden structure of a matrix.

In Machine Learning, SVD is important because most data is naturally a matrix, and SVD helps with:

- compression
- dimensionality reduction
- noise reduction
- latent factor discovery
- PCA
- recommendation systems

So if eigenvectors are about **natural directions of a square transformation**, SVD is about **natural structure of any matrix**.

---

## 11. Moore-Penrose Pseudo-Inverse

The **pseudo-inverse** $A^+$ generalizes the matrix inverse to non-square and rank-deficient matrices.

For an invertible square matrix, $A^+ = A^{-1}$. For all other matrices, it provides the "best available" inverse.

**Definition via SVD.**

Given the SVD $A = U \Sigma V^T$, the pseudo-inverse is: $A^+ = V \Sigma^+ U^T$ where $\Sigma^+$ is formed by replacing each non-zero singular value $\sigma_i$ by $1/\sigma_i$ and transposing:

$$
\Sigma =
\begin{bmatrix}
\sigma_1 & & \\
& \ddots & \\
& & \sigma_r \\
& &
\end{bmatrix}
$$

Then:

$$
\Sigma^+ =
\begin{bmatrix}
1/\sigma_1 & & & \\
& \ddots & & \\
& & 1/\sigma_r &
\end{bmatrix}
$$

Zero singular values stay zero — we do not invert them.

**What it solves.**

For the system $A\mathbf{x} = \mathbf{b}$:

- If the system is **overdetermined** ($m > n$, more equations than unknowns): $A^+\mathbf{b}$ gives the **least-squares solution** — the $\mathbf{x}$ that minimizes $\lVert A\mathbf{x} - \mathbf{b} \rVert_2$.
- If the system is **underdetermined** ($m < n$, more unknowns than equations): $A^+\mathbf{b}$ gives the **minimum-norm solution** — the least-squares solution with the smallest $\lVert \mathbf{x} \rVert_2$ among all solutions.
- If $A$ is square and invertible: $A^+\mathbf{b} = A^{-1}\mathbf{b}$.

In all cases: $\mathbf{x}^+ = A^+ \mathbf{b}$ is the unique solution that minimizes $\lVert A\mathbf{x} - \mathbf{b} \rVert_2$ and, among all minimizers, has the smallest $\lVert \mathbf{x} \rVert_2$.

**Key properties:**

The pseudo-inverse satisfies the four **Moore-Penrose conditions**:

$$
A A^+ A = A, \qquad A^+ A A^+ = A^+
$$

$$
(A A^+)^T = A A^+, \qquad (A^+ A)^T = A^+ A
$$

The matrices $AA^+$ and $A^+A$ are orthogonal projection matrices — $AA^+$ projects onto the column space of $A$, and $A^+A$ projects onto the row space of $A$.

**Worked example.**

$$
A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}
$$

SVD: $U$ = identity-like $3 \times 3$, $\Sigma = \begin{bmatrix}1 & 0 \\ 0 & 1 \\ 0 & 0\end{bmatrix}$, $V = I_{2 \times 2}$.

$$
A^+ = V \Sigma^+ U^T
$$

Since $V$ and $U$ are identity matrices in this example:

$$
A^+ =
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}
$$

Indeed $A^+A = I_2$ (left inverse) and $AA^+ \neq I_3$ (not a right inverse — $A$ is not surjective).

**Use cases in ML:**

| Scenario | Role of $A^+$ |
|---|---|
| Linear regression ($m \gg n$) | $\mathbf{\theta} = X^+ \mathbf{y}$ is the least-squares solution |
| Underdetermined regression ($m < n$) | Minimum-norm solution, implicit L2 regularization |
| Rank-deficient systems | Handles singular $X^TX$ without adding $\lambda I$ |
| Backpropagation in linear networks | Pseudo-inverse characterizes the set of global minima |
