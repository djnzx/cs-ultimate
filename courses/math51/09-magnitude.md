# Vector Magnitude

The **magnitude** of a vector is its **length**.

If a vector represents movement, force, velocity, or direction, then its magnitude tells us **how large** or **how strong** that vector is, ignoring its direction.

For example, the vectors $(3,4)$ and $(-3,-4)$ point in opposite directions, but they have the same magnitude: $5$ because their length is the same.

---

## 1. Magnitude in 2D

Suppose we have a vector: $\mathbf{v} = (x,y)$ Its magnitude is written as: $\lvert \mathbf{v} \rvert$ or sometimes: $\lVert \mathbf{v} \rVert$ The formula is: $\lvert \mathbf{v} \rvert = \sqrt{x^2 + y^2}$ This comes from the Pythagorean theorem.

For example, $\mathbf{v} = (3,4)$: $\lvert \mathbf{v} \rvert = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$. So the vector $(3,4)$ has length $5$.

---

## 2. Magnitude in 3D

For a 3D vector: $\mathbf{v} = (x,y,z)$ the magnitude is: $\lvert \mathbf{v} \rvert = \sqrt{x^2 + y^2 + z^2}$ For example: $\mathbf{v} = (2,3,6)$ Then: $\lvert \mathbf{v} \rvert = \sqrt{2^2 + 3^2 + 6^2}$ So: $\lvert \mathbf{v} \rvert = \sqrt{4 + 9 + 36}$ Therefore:

$$
\lvert \mathbf{v} \rvert = \sqrt{49} = 7
$$

---

## 3. Magnitude in n-dimensional space

For an n-dimensional vector: $\mathbf{v} = (x_1, x_2, \dots, x_n)$ the magnitude is: $\lvert \mathbf{v} \rvert=\sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$ or equivalently: $\lvert \mathbf{v} \rvert=\sqrt{\sum_{i=1}^{n} x_i^2}$ So magnitude is the generalization of ordinary length to any number of dimensions.

---

## 4. Geometric meaning

The magnitude tells us the distance from the origin to the point represented by the vector.

For example, the vector: $\mathbf{v} = (3,4)$ can be seen as an arrow from: $(0,0)$ to: $(3,4)$ The magnitude is the length of this arrow: $\lvert \mathbf{v} \rvert = 5$ So magnitude is simply the vector's length.

---

## 5. Unit vector

A vector with magnitude $1$ is called a **unit vector**.

For example: $\mathbf{u} = \left(\frac{3}{5}, \frac{4}{5}\right)$ has magnitude:

$$
\lvert \mathbf{u} \rvert = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2}
$$

So:

$$
\lvert \mathbf{u} \rvert = \sqrt{\frac{9}{25} + \frac{16}{25}}
$$

Therefore:

$$
\lvert \mathbf{u} \rvert = \sqrt{\frac{25}{25}} = 1
$$

Unit vectors are useful because they represent **direction only**, without changing the scale.

---

## 6. Normalizing a vector

To turn a nonzero vector into a unit vector, divide it by its magnitude.

If: $\mathbf{v} = (x_1, x_2, \dots, x_n)$ then the normalized vector is:

$$
\hat{\mathbf{v}} = \frac{\mathbf{v}}{\lvert \mathbf{v} \rvert}
$$

That means:

$$
\hat{\mathbf{v}} = \left( \frac{x_1}{\lvert \mathbf{v} \rvert}, \frac{x_2}{\lvert \mathbf{v} \rvert}, \dots, \frac{x_n}{\lvert \mathbf{v} \rvert} \right)
$$

For example, if: $\mathbf{v} = (3,4)$ then: $\lvert \mathbf{v} \rvert = 5$ So the normalized vector is:

$$
\hat{\mathbf{v}} = \left( \frac{3}{5}, \frac{4}{5} \right)
$$

This vector points in the same direction as $(3,4)$ but its magnitude is $1$.

---

## 7. Norms

The Euclidean magnitude is one member of a family of **norms** — functions that measure the size of a vector. A norm $\lVert \cdot \rVert$ must satisfy three axioms: non-negativity ($\lVert \mathbf{v} \rVert \geq 0$, equal to 0 only for $\mathbf{0}$), scalar scaling ($\lVert c\mathbf{v} \rVert = \lvert c \rvert\lVert \mathbf{v} \rVert$), and the triangle inequality ($\lVert \mathbf{u}+\mathbf{v} \rVert \leq \lVert \mathbf{u} \rVert + \lVert \mathbf{v} \rVert$).

**$L^2$ norm (Euclidean norm).**

The standard magnitude — what "length" means geometrically:

$$
\lVert \mathbf{v} \rVert_2 = \sqrt{\sum_{i=1}^n v_i^2}
$$

**$L^1$ norm (Manhattan norm).**

Sum of absolute values:

$$
\lVert \mathbf{v} \rVert_1 = \sum_{i=1}^n \lvert v_i \rvert
$$

Geometrically: total distance traveled if you move only along axes.

$L^1$ penalizes each non-zero component equally, regardless of its magnitude, which encourages **sparsity** — many components exactly zero. This is the basis of **Lasso (L1 regularization)**.

**$L^\infty$ norm (max norm).**

The largest absolute entry:

$$
\lVert \mathbf{v} \rVert_\infty = \max_i \lvert v_i \rvert
$$

Used when the worst-case coordinate is what matters (e.g., robustness guarantees).

**Comparing $L^1$, $L^2$, $L^\infty$:**

For $\mathbf{v} = (3, -4)^T$:

$$
\lVert \mathbf{v} \rVert_1 = 7, \qquad
\lVert \mathbf{v} \rVert_2 = 5, \qquad
\lVert \mathbf{v} \rVert_\infty = 4
$$

Always:

$$
\lVert \mathbf{v} \rVert_\infty \leq
\lVert \mathbf{v} \rVert_2 \leq
\lVert \mathbf{v} \rVert_1 \leq
\sqrt{n}\lVert \mathbf{v} \rVert_2
$$

---

## 8. Matrix Norms

For matrices $A \in \mathbb{R}^{m \times n}$, norms measure the "size" of a matrix.

**Frobenius norm.**

The square root of the sum of all squared entries — analogous to the Euclidean norm, but for matrices:

$$
\lVert A \rVert_F =
\sqrt{\sum_{i=1}^{m} \sum_{j=1}^{n} A_{ij}^2}
= \sqrt{\mathrm{tr}(A^T A)}
$$

The connection

$$
\lVert A \rVert_F^2 = \mathrm{tr}(A^T A)
$$

is important in optimization: the gradient of $\lVert A \rVert_F^2$ with respect to $A$ is simply $2A$.

**Spectral norm (operator norm).**

The largest factor by which $A$ stretches any input vector:

$$
\lVert A \rVert_2 = \sigma_{\max}(A)
$$

Here, $\sigma_{\max}$ is the largest singular value of $A$ (covered in the SVD section). This is the matrix analogue of the $L^2$ vector norm.

**Nuclear norm.**

Sum of all singular values: $\lVert A \rVert_* = \sum_i \sigma_i$ The nuclear norm is the matrix analogue of the $L^1$ vector norm. Minimizing it encourages **low-rank** solutions — used in matrix completion and recommender systems.

**Where matrix norms appear in ML:**

| Norm | Typical use |
|---|---|
| Frobenius $\lVert W \rVert_F^2$ | Weight decay (L2 regularization) — shrinks all weights uniformly |
| Spectral $\lVert W \rVert_2$ | Spectral normalization in GANs — controls Lipschitz constant |
| Nuclear $\lVert A \rVert_*$ | Matrix completion — encourages low-rank structure |

---

## 9. Summary

The **magnitude** ($L^2$ norm) of a vector is:

$$
\lVert \mathbf{v} \rVert_2 = \sqrt{\sum_{i=1}^n v_i^2}
$$

Key norms:

| Norm | Formula | Encourages |
|---|---|---|
| $L^1$ | $\sum \lvert v_i \rvert$ | Sparsity (Lasso) |
| $L^2$ (Euclidean) | $\sqrt{\sum v_i^2}$ | Small overall magnitude (Ridge) |
| $L^\infty$ | $\max \lvert v_i \rvert$ | Worst-case control |
| Frobenius | $\sqrt{\mathrm{tr}(A^T A)}$ | Small all-entry magnitude |
| Spectral | $\sigma_{\max}(A)$ | Bounded stretching |
| Nuclear | $\sum \sigma_i(A)$ | Low-rank structure |
