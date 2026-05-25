# Hessian Matrix

The **Hessian matrix** collects all **second-order partial derivatives** of a scalar function into a single matrix.

For a function

$$
f(x_1, x_2, \dots, x_n)
$$

the Hessian is denoted by

$$
H = \nabla^2 f
$$

and its entries are

$$
H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}
$$

So:

$$
H =
\begin{bmatrix}
\dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1 \partial x_n} \\
\dfrac{\partial^2 f}{\partial x_2 \partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\dfrac{\partial^2 f}{\partial x_n \partial x_1} & \dfrac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
$$

The Hessian is an $n \times n$ square matrix.

The first partial derivatives form the gradient:

$$
\nabla f = \left(\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}\right)
$$

The Hessian is one level deeper: it tells us how the gradient itself changes.

---

## 1. Symmetry

Under mild conditions (which hold for all smooth functions encountered in practice), the order of differentiation does not matter:

$$
\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}
$$

This means: $H_{ij} = H_{ji}$.

So the Hessian is always a **symmetric matrix**: $H = H^T$.

Symmetric matrices have particularly nice properties: all their eigenvalues are real numbers.

---

## 2. Concrete Example

Let:

$$
f(x, y) = x^2 + 3xy + 2y^2
$$

**First derivatives (gradient):**

$$
\frac{\partial f}{\partial x} = 2x + 3y \qquad \frac{\partial f}{\partial y} = 3x + 4y
$$

**Second derivatives:**

$$
\frac{\partial^2 f}{\partial x^2} = 2 \qquad \frac{\partial^2 f}{\partial y^2} = 4 \qquad \frac{\partial^2 f}{\partial x \partial y} = 3
$$

So the Hessian is:

$$
H =
\begin{bmatrix}
2 & 3 \\
3 & 4
\end{bmatrix}
$$

Note that the off-diagonal entries are equal (3 = 3), confirming symmetry.

Also note: the Hessian is **constant** here — it does not depend on $x$ or $y$.

For more complex functions, the Hessian will be a matrix-valued function of the input point.

---

## 3. Geometric Meaning: Curvature

The gradient tells us the slope of $f$ at a point.

The Hessian tells us the **curvature** — how the slope is changing.

In one dimension, the second derivative $f''(x)$ tells us:

- $f''(x) \gt 0$: the function curves upward (bowl shape, local minimum)
- $f''(x) \lt 0$: the function curves downward (hill shape, local maximum)
- $f''(x) = 0$: flat curvature (inflection point)

The Hessian generalizes this to multiple dimensions.

A key tool is the eigenvalues of $H$:

- All eigenvalues **positive**: the function curves upward in every direction → **local minimum**
- All eigenvalues **negative**: the function curves downward in every direction → **local maximum**
- Eigenvalues of **mixed sign**: the function curves up in some directions and down in others → **saddle point**

---

## 4. Positive Definite, Negative Definite, Indefinite

The Hessian at a point is called:

**Positive definite** if for every non-zero vector $\mathbf{v}$:

$$
\mathbf{v}^T H \mathbf{v} \gt 0
$$

Equivalently, all eigenvalues of $H$ are strictly positive.

This means the function is locally bowl-shaped: a **local minimum**.

**Negative definite** if for every non-zero vector $\mathbf{v}$:

$$
\mathbf{v}^T H \mathbf{v} \lt 0
$$

All eigenvalues are strictly negative.

This means the function is locally hill-shaped: a **local maximum**.

**Indefinite** if: $\mathbf{v}^T H \mathbf{v}$ is positive for some directions and negative for others.

Some eigenvalues are positive, some are negative.

This is a **saddle point**: the function looks like a minimum from one direction and a maximum from another.

---

## 5. Second-Order Taylor Approximation

Near a point $\mathbf{x}_0$, any smooth function can be approximated as:

$$
f(\mathbf{x}) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T (\mathbf{x} - \mathbf{x}_0) + \frac{1}{2}(\mathbf{x} - \mathbf{x}_0)^T H(\mathbf{x}_0) (\mathbf{x} - \mathbf{x}_0)
$$

The three terms are:

1. The value at the base point.
2. The linear term: gradient dotted with the displacement. This is the first-order (slope) approximation.
3. The quadratic term: the Hessian applied to the displacement. This captures curvature.

This is the multivariate analogue of:

$$
f(x) \approx f(x_0) + f'(x_0)(x - x_0) + \frac{1}{2}f''(x_0)(x - x_0)^2
$$

The Hessian plays exactly the role that $f''$ plays in 1D.

---

## 6. Use case: classifying critical points

A **critical point** is a point where the gradient is zero:

$$
\nabla f(\mathbf{x}^*) = \mathbf{0}
$$

To determine the nature of the critical point, examine the Hessian at $\mathbf{x}^*$:

| Hessian at the critical point | Type of critical point |
|---|---|
| Positive definite (all eigenvalues are positive) | Local minimum |
| Negative definite (all eigenvalues are negative) | Local maximum |
| Indefinite (mixed eigenvalue signs) | Saddle point |
| Eigenvalue = 0 | Inconclusive |

**Example:**

$$
f(x, y) = x^2 - y^2
$$

Gradient:

$$
\nabla f = (2x, -2y)
$$

Setting it to zero: $x = 0$, $y = 0$.

Hessian:

$$
H =
\begin{bmatrix}
2 & 0 \\
0 & -2
\end{bmatrix}
$$

Eigenvalues: $+2$ and $-2$. The Hessian is indefinite.

So $(0, 0)$ is a **saddle point**: the function increases along the x-axis and decreases along the y-axis.

---

## 7. Use case: Newton's method in optimization

**Gradient descent** uses only the gradient:

$$
\theta \leftarrow \theta - \alpha \nabla L(\theta)
$$

It moves in the direction of steepest descent, but it does not account for curvature.

**Newton's method** uses both the gradient and the Hessian:

$$
\theta \leftarrow \theta - H^{-1} \nabla L(\theta)
$$

By multiplying by $H^{-1}$, we account for the local curvature:

- In directions where the function is steeply curved (large eigenvalue), we take a small step.
- In directions where the function is nearly flat (small eigenvalue), we take a larger step.

This leads to much faster convergence than gradient descent when the Hessian can be computed.

The geometric intuition: gradient descent treats the loss surface as a flat plane and takes a fixed step; Newton's method fits a local quadratic (parabola) and jumps directly to its minimum.

---

## 8. Use case: loss landscape in neural networks

When training a neural network, the loss function: $L(\theta)$ where $\theta$ has millions of parameters, has a very complex landscape.

The Hessian of the loss with respect to $\theta$ is a matrix of size: $\lvert \theta \rvert \times \lvert \theta \rvert$.

For a network with 10 million parameters, this is a $10^7 \times 10^7$ matrix — far too large to store or invert directly.

Nevertheless, the Hessian explains several important phenomena:

**Saddle points.** Modern neural networks have an enormous number of parameters. In high dimensions, most critical points of the loss are saddle points, not true minima. The Hessian at such points has eigenvalues of both signs. This is why gradient descent does not get stuck: the gradient is non-zero along the directions with negative curvature, and the optimizer naturally follows those directions downward.

**Ill-conditioned loss surface.** The ratio of the largest to smallest eigenvalue of the Hessian is called the **condition number**. When it is large, the loss surface is much steeper in some directions than others (like a narrow valley). Gradient descent with a fixed learning rate oscillates in the steep directions while moving slowly in the flat directions.

**Learning rate sensitivity.** The maximum eigenvalue of the Hessian determines the maximum safe learning rate. If the learning rate exceeds

$$
\alpha \gt \frac{2}{\lambda_{\max}(H)}
$$

gradient descent diverges in the direction of the largest curvature. This is why choosing the learning rate carefully matters.

---

## 9. Use case: Hessian-vector products in practice

Computing the full Hessian for large models is infeasible.

However, many algorithms only need the product: $H \mathbf{v}$ for a specific vector $\mathbf{v}$.

This can be computed efficiently using **automatic differentiation** without forming $H$ explicitly.

The trick: differentiate the gradient once more in the direction of $\mathbf{v}$:

$$
H \mathbf{v} = \nabla(\nabla f \cdot \mathbf{v})
$$

This has the same computational cost as one gradient computation — linear in the number of parameters.

Algorithms that use Hessian-vector products include:

- **Conjugate gradient** for second-order optimization
- **Hessian-free optimization** (also called truncated Newton)
- **Influence functions** for understanding which training examples most affect model predictions

---

## 10. Summary

The **Hessian** is the matrix of second-order partial derivatives:

$$
H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}
$$

It is always **symmetric**: $H = H^T$.

The Hessian captures **curvature** — how the gradient changes as we move.

At a critical point $\nabla f = \mathbf{0}$:

$$
H \text{ positive definite} \implies \text{local minimum}
$$

$$
H \text{ negative definite} \implies \text{local maximum}
$$

$$
H \text{ indefinite} \implies \text{saddle point}
$$

In machine learning:

- **Gradient descent** uses the gradient (first derivative) only.
- **Newton's method** divides by the Hessian to account for curvature, converging faster.
- The **eigenvalues of the Hessian** explain the condition number of the loss surface, learning rate sensitivity, and the prevalence of saddle points in large neural networks.
