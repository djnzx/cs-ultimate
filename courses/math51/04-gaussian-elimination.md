# Gaussian Elimination

**Gaussian elimination** is the fundamental algorithm for solving systems of linear equations.

A system of equations like:

$$
\begin{cases}
2x + y - z = 8 \\
-3x - y + 2z = -11 \\
-2x + y + 2z = -3
\end{cases}
$$

can be written compactly as a matrix equation: $A\mathbf{x} = \mathbf{b}$ where:

$$
A =
\begin{bmatrix}
2 & 1 & -1 \\
-3 & -1 & 2 \\
-2 & 1 & 2
\end{bmatrix}
$$

$$
\mathbf{x} =
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$

$$
\mathbf{b} =
\begin{bmatrix}
8 \\
-11 \\
-3
\end{bmatrix}
$$

Gaussian elimination solves this by systematically transforming the system into a simpler form.

---

## 1. Augmented Matrix

The first step is to combine $A$ and $\mathbf{b}$ into a single **augmented matrix**:

$$
[A \mid \mathbf{b}] =
\left[
\begin{array}{ccc|c}
2 & 1 & -1 & 8 \\
-3 & -1 & 2 & -11 \\
-2 & 1 & 2 & -3
\end{array}
\right]
$$

Working with the augmented matrix is more compact than writing equations repeatedly.

---

## 2. Row Operations

The core idea: we can transform the system without changing its solution set, using three allowed **row operations**:

| Operation | Notation | Effect |
|---|---|---|
| Swap two rows | $R_i \leftrightarrow R_j$ | Reorders equations |
| Multiply a row by a nonzero scalar | $c R_i \to R_i$ | Scales an equation |
| Add a multiple of one row to another | $R_i + c R_j \to R_i$ | Eliminates a variable |

The third operation is the workhorse: it is used to make entries below (and above) a pivot equal to zero.

---

## 3. Row Echelon Form

The goal of the forward pass is to reach **Row Echelon Form (REF)**:

- All zero rows are at the bottom.
- The first nonzero entry in each row (called the **pivot**) is strictly to the right of the pivot in the row above.
- All entries below each pivot are zero.

The result looks like a staircase of pivots:

$$
\begin{bmatrix}
\mathbf{p} & * & * & * \\
0 & \mathbf{p} & * & * \\
0 & 0 & \mathbf{p} & * \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

where $\mathbf{p}$ denotes a pivot and $*$ denotes any value.

---

## 4. Reduced Row Echelon Form

**Reduced Row Echelon Form (RREF)** goes one step further:

- All the REF conditions hold.
- Each pivot equals exactly $1$.
- All entries **above** each pivot are also zero.

$$
\begin{bmatrix}
1 & 0 & 0 & * \\
0 & 1 & 0 & * \\
0 & 0 & 1 & * \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

When the augmented matrix is in RREF, the solution can be read off directly.

---

## 5. Worked Example: $3 \times 3$ System

Solve:

$$
\left[
\begin{array}{ccc|c}
2 & 1 & -1 & 8 \\
-3 & -1 & 2 & -11 \\
-2 & 1 & 2 & -3
\end{array}
\right]
$$

**Step 1.** Eliminate the first column below the pivot (row 1):

$R_2 \leftarrow R_2 + \tfrac{3}{2} R_1$:

$$
\left[
\begin{array}{ccc|c}
2 & 1 & -1 & 8 \\
0 & \tfrac{1}{2} & \tfrac{1}{2} & 1 \\
-2 & 1 & 2 & -3
\end{array}
\right]
$$

$R_3 \leftarrow R_3 + R_1$:

$$
\left[
\begin{array}{ccc|c}
2 & 1 & -1 & 8 \\
0 & \tfrac{1}{2} & \tfrac{1}{2} & 1 \\
0 & 2 & 1 & 5
\end{array}
\right]
$$

**Step 2.** Eliminate the second column below the pivot (row 2):

$R_3 \leftarrow R_3 - 4 R_2$:

$$
\left[
\begin{array}{ccc|c}
2 & 1 & -1 & 8 \\
0 & \tfrac{1}{2} & \tfrac{1}{2} & 1 \\
0 & 0 & -1 & 1
\end{array}
\right]
$$

This is **REF**. Now back-substitute.

**Step 3.** From row 3: $-z = 1 \Rightarrow z = -1$.

From row 2: $\tfrac{1}{2}y + \tfrac{1}{2}(-1) = 1 \Rightarrow y = 3$.

From row 1: $2x + 3 - (-1) = 8 \Rightarrow x = 2$.

**Solution:** $x = 2,\; y = 3,\; z = -1$.

---

## 6. Back Substitution

Back substitution reads the solution from the bottom row upward.

Once in REF:

- The last nonzero row gives one variable directly.
- Substitute into the row above to find the next variable.
- Continue upward until all variables are found.

This is the standard method when the system has a unique solution.

If instead you continue to RREF (forward and backward elimination), the solution can be read off without any substitution.

---

## 7. The Three Possible Outcomes

Not every system has a unique solution.

**Case 1: Unique solution**

The number of pivots equals the number of unknowns.

$$
\text{Example: }
\left[
\begin{array}{cc|c}
1 & 0 & 3 \\
0 & 1 & 5
\end{array}
\right]
\implies x = 3,\; y = 5
$$

**Case 2: No solution (inconsistent)**

A row of the form $[0\; 0\; \cdots\; 0 \mid c]$ with $c \neq 0$ appears.

This says $0 = c$, which is impossible.

$$
\text{Example: }
\left[
\begin{array}{cc|c}
1 & 2 & 3 \\
0 & 0 & 5
\end{array}
\right]
\implies \text{no solution}
$$

**Case 3: Infinitely many solutions**

The number of pivots is less than the number of unknowns and there is no contradiction row.

The variables without pivots are called **free variables** — they can take any value; the pivot variables are then determined in terms of them.

$$
\text{Example: }
\left[
\begin{array}{ccc|c}
1 & 0 & 2 & 4 \\
0 & 1 & -1 & 3
\end{array}
\right]
\implies
x = 4 - 2t,\; y = 3 + t,\; z = t \quad (t \in \mathbb{R})
$$

---

## 8. Rank

The **rank** of a matrix $A$ is the number of pivots in its row echelon form: $\mathrm{rank}(A) = \text{number of nonzero rows in REF}$ It counts the number of truly independent pieces of information in the matrix.

For an $m \times n$ matrix: $\mathrm{rank}(A) \leq \min(m, n)$ When $\mathrm{rank}(A) = n$ (full column rank), the system $A\mathbf{x} = \mathbf{b}$ has at most one solution.

When $\mathrm{rank}(A) = m$ (full row rank), the system has at least one solution for every $\mathbf{b}$.

When $\mathrm{rank}(A) = n = m$ (full rank square matrix), the matrix is invertible.

---

## 9. Finding the Inverse via Gaussian Elimination

Gaussian elimination can also compute the inverse of a square matrix $A$.

Form the augmented matrix $[A \mid I]$ and row-reduce until the left side becomes $I$: $[A \mid I] \xrightarrow{\text{row operations}} [I \mid A^{-1}]$ If $A$ is invertible, the right side will be $A^{-1}$.

**Example:** find the inverse of $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$:

$$
\left[
\begin{array}{cc|cc}
1 & 2 & 1 & 0 \\
3 & 4 & 0 & 1
\end{array}
\right]
$$

$R_2 \leftarrow R_2 - 3R_1$:

$$
\left[
\begin{array}{cc|cc}
1 & 2 & 1 & 0 \\
0 & -2 & -3 & 1
\end{array}
\right]
$$

$R_2 \leftarrow -\tfrac{1}{2}R_2$:

$$
\left[
\begin{array}{cc|cc}
1 & 2 & 1 & 0 \\
0 & 1 & \tfrac{3}{2} & -\tfrac{1}{2}
\end{array}
\right]
$$

$R_1 \leftarrow R_1 - 2R_2$:

$$
\left[
\begin{array}{cc|cc}
1 & 0 & -2 & 1 \\
0 & 1 & \tfrac{3}{2} & -\tfrac{1}{2}
\end{array}
\right]
$$

Therefore:

$$
A^{-1} =
\begin{bmatrix}
-2 & 1 \\
\tfrac{3}{2} & -\tfrac{1}{2}
\end{bmatrix}
$$

If at any point the left side develops a zero row where a pivot is needed, the matrix is singular and has no inverse.

---

## 10. Connection to LU Decomposition

Gaussian elimination (without row swaps) produces the **LU decomposition**: $A = LU$ where:
- $L$ is a lower triangular matrix recording the row operations used.
- $U$ is the upper triangular matrix (the REF of $A$).

The determinant follows immediately: $\det(A) = \det(L) \cdot \det(U) = 1 \cdot \prod_i U_{ii} = \prod_i U_{ii}$ since $L$ has 1s on its diagonal, and the determinant of a triangular matrix is the product of its diagonal entries.

LU decomposition is the practical $O(n^3)$ algorithm used to compute determinants, solve linear systems, and find inverses in numerical software.

---

## 11. Use case: Linear Regression

The most common use of Gaussian elimination in ML is solving the **normal equations** for linear regression.

Given data matrix $X \in \mathbb{R}^{m \times n}$ and target vector $\mathbf{y} \in \mathbb{R}^m$, the least-squares solution minimizes: $\lVert \mathbf{y} - X\mathbf{\theta} \rVert^2$ Setting the gradient to zero gives the normal equations: $X^T X\, \mathbf{\theta} = X^T \mathbf{y}$ This is a square linear system in $\mathbf{\theta}$, solved directly by Gaussian elimination (or LU decomposition): $\mathbf{\theta} = (X^T X)^{-1} X^T \mathbf{y}$ For small datasets, this exact solution is fast and numerically stable.

---

## 12. Summary

**Gaussian elimination** transforms the augmented matrix $[A \mid \mathbf{b}]$ using row operations into Row Echelon Form (REF) or Reduced Row Echelon Form (RREF).

Three row operations (none change the solution):
- Swap rows
- Scale a row by a nonzero constant
- Add a multiple of one row to another

Outcomes:

| Pivots | Result |
|---|---|
| $= n$ (unknowns) | Unique solution |
| $< n$, no contradiction row | Infinitely many solutions |
| Contradiction row $[0\cdots 0 \mid c \neq 0]$ | No solution |

The number of pivots is the **rank** of $A$.

Other uses:
- Compute $A^{-1}$ by reducing $[A \mid I] \to [I \mid A^{-1}]$
- Compute $\det(A)$ as a byproduct of LU decomposition
- Solve the normal equations in linear regression
