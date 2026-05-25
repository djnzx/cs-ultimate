# LU Factorization

**LU factorization** decomposes a square matrix $A$ into the product of two triangular matrices: $A = LU$ where:
- $L$ is **lower triangular** — all entries above the main diagonal are zero, and all diagonal entries equal 1.
- $U$ is **upper triangular** — all entries below the main diagonal are zero.

$$
L =
\begin{bmatrix}
1 & 0 & 0 \\
l_{21} & 1 & 0 \\
l_{31} & l_{32} & 1
\end{bmatrix}
$$

$$
U =
\begin{bmatrix}
u_{11} & u_{12} & u_{13} \\
0 & u_{22} & u_{23} \\
0 & 0 & u_{33}
\end{bmatrix}
$$

LU factorization is Gaussian elimination expressed as a matrix product rather than as a sequence of operations.

---

## 1. Connection to Gaussian Elimination

Gaussian elimination transforms $A$ into an upper triangular matrix $U$ by applying row operations.

Each row operation "add $c$ times row $j$ to row $i$" can be written as multiplication by an **elementary matrix** $E$:

$$
E_{ij}(c) =
\begin{bmatrix}
1 & & & \\
& \ddots & & \\
& c & 1 & \\
& & & 1
\end{bmatrix}
\quad \text{(1 in position }(i,j)\text{ below the diagonal)}
$$

Applying a sequence of such operations gives: $E_k \cdots E_2 E_1 A = U$ Therefore: $A = E_1^{-1} E_2^{-1} \cdots E_k^{-1} U = LU$ The matrix $L = E_1^{-1} \cdots E_k^{-1}$ turns out to be lower triangular, with the multipliers used in elimination as its off-diagonal entries.

**The key insight:** the multiplier used to eliminate entry $(i, j)$ becomes entry $L_{ij}$.

---

## 2. Worked Example

Factorize:

$$
A =
\begin{bmatrix}
2 & 1 & 1 \\
4 & 3 & 3 \\
8 & 7 & 9
\end{bmatrix}
$$

**Elimination step 1.** Eliminate column 1 below the pivot $a_{11} = 2$:

Multipliers: $l_{21} = 4/2 = 2$, $l_{31} = 8/2 = 4$.

$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 4R_1$:

$$
\begin{bmatrix}
2 & 1 & 1 \\
0 & 1 & 1 \\
0 & 3 & 5
\end{bmatrix}
$$

**Elimination step 2.** Eliminate column 2 below the pivot $u_{22} = 1$:

Multiplier: $l_{32} = 3/1 = 3$.

$R_3 \leftarrow R_3 - 3R_2$:

$$
U =
\begin{bmatrix}
2 & 1 & 1 \\
0 & 1 & 1 \\
0 & 0 & 2
\end{bmatrix}
$$

**Assemble $L$** from the multipliers (1s on diagonal, multipliers below):

$$
L =
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
4 & 3 & 1
\end{bmatrix}
$$

**Verify:** $LU = A$:

$$
L =
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
4 & 3 & 1
\end{bmatrix}
$$

$$
U =
\begin{bmatrix}
2 & 1 & 1 \\
0 & 1 & 1 \\
0 & 0 & 2
\end{bmatrix}
$$

Then:

$$
LU =
\begin{bmatrix}
2 & 1 & 1 \\
4 & 3 & 3 \\
8 & 7 & 9
\end{bmatrix}
$$

So $LU = A$.

---

## 3. PLU Decomposition (Partial Pivoting)

Basic LU fails when a pivot is zero (or very small), because we cannot divide by it.

**Partial pivoting** swaps rows to put the largest available entry in the pivot position before each elimination step.

This produces the **PLU decomposition**: $PA = LU$ where $P$ is a **permutation matrix** that records the row swaps.

A permutation matrix has exactly one 1 in each row and column. For example:

$$
P =
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

means "swap rows 1 and 2".

Partial pivoting makes LU numerically stable and is the standard in practice. Software libraries (NumPy, LAPACK) always use PLU.

---

## 4. Solving $A\mathbf{x} = \mathbf{b}$ with LU

Once $A = LU$ is computed, solving $A\mathbf{x} = \mathbf{b}$ splits into two triangular systems: $A\mathbf{x} = LU\mathbf{x} = \mathbf{b}$ Let $\mathbf{y} = U\mathbf{x}$. Then:

**Step 1: Forward substitution** — solve $L\mathbf{y} = \mathbf{b}$:

Since $L$ is lower triangular, solve from the top down:

$$
y_1 = b_1
$$

$$
y_2 = b_2 - l_{21} y_1
$$

$$
y_i = b_i - \sum_{j=1}^{i-1} l_{ij} y_j
$$

**Step 2: Back substitution** — solve $U\mathbf{x} = \mathbf{y}$:

Since $U$ is upper triangular, solve from the bottom up:

$$
x_n = y_n / u_{nn}
$$

$$
x_i = \frac{1}{u_{ii}}\left(y_i - \sum_{j=i+1}^{n} u_{ij} x_j\right)
$$

**Computational advantage:**

Computing $LU$ costs $O(n^3)$ once.

Each subsequent solve costs only $O(n^2)$.

If the same matrix $A$ must be used with many different right-hand sides $\mathbf{b}_1, \mathbf{b}_2, \dots$, LU factorization amortizes the heavy work.

---

## 5. Determinant from LU

Since $\det(AB) = \det(A)\det(B)$: $\det(A) = \det(L)\det(U)$ $L$ has 1s on its diagonal, so $\det(L) = 1$.

$U$ is upper triangular, so $\det(U) = u_{11} \cdot u_{22} \cdots u_{nn}$.

Therefore: $\det(A) = u_{11} \cdot u_{22} \cdots u_{nn}$ This is how determinants are computed in practice — not by cofactor expansion, but as a byproduct of LU with cost $O(n^3)$.

If pivoting is used ($PA = LU$), one adjustment is needed: $\det(A) = (-1)^s \cdot u_{11} \cdot u_{22} \cdots u_{nn}$ where $s$ is the number of row swaps performed.

---

## 6. Matrix Inverse from LU

To compute $A^{-1}$, solve $A\mathbf{x} = \mathbf{e}_j$ for each standard basis vector $\mathbf{e}_j$.

Each solve uses the same $LU$ factorization and costs $O(n^2)$.

Since there are $n$ columns, total cost is $O(n^3)$.

This is more efficient than Gaussian elimination on $[A \mid I]$ only in the constant factor — both are $O(n^3)$.

---

## 7. Summary

LU factorization decomposes:

$$
A = LU \quad (\text{or } PA = LU \text{ with pivoting})
$$

| Matrix | Shape | Entries |
|---|---|---|
| $L$ | Lower triangular | 1s on diagonal, multipliers from elimination below |
| $U$ | Upper triangular | Result of forward elimination |
| $P$ | Permutation | Records row swaps for stability |

Key uses:

| Task | Cost with LU |
|---|---|
| Factorize $A$ once | $O(n^3)$ |
| Solve $A\mathbf{x} = \mathbf{b}$ (after factorization) | $O(n^2)$ |
| Compute $\det(A)$ | $O(1)$ — product of $U$'s diagonal |
| Compute $A^{-1}$ | $O(n^3)$ — $n$ solves |

LU is the workhorse of numerical linear algebra: it underlies every solver in NumPy, MATLAB, and LAPACK.
