# Partial Derivatives

## 1. Definition

**Partial derivatives are essentially about functions with multiple input variables**.

A usual derivative is for a function of one variable: $f(x)$ For example: $f(x) = x^2$ Then: $\frac{df}{dx}$ means: how does \(f\) change when \(x\) changes?

---

A **partial derivative** appears when the function has several independent variables: $f(x, y)$ or more generally: $f(x_1, x_2, \dots, x_n)$ For example: $f(x, y) = x^2 + 3xy + y^2$ Now the function depends on both \(x\) and \(y\).

The partial derivative with respect to \(x\) is: $\frac{\partial f}{\partial x}$ It means: how does \(f\) change when \(x\) changes, while \(y\) is treated as constant?

So, for: $f(x, y) = x^2 + 3xy + y^2$ we get:

$$
\frac{\partial f}{\partial x} = 2x + 3y
$$

because \(y\) is treated as constant.

The partial derivative with respect to \(y\) is:

$$
\frac{\partial f}{\partial y} = 3x + 2y
$$

because \(x\) is treated as constant.

---

The symbol changes from: $\frac{d}{dx}$ to: $\frac{\partial}{\partial x}$ because we are not differentiating the whole function along one single input direction. We are differentiating with respect to **one variable at a time**.

So: $\frac{\partial f}{\partial x}$ means:

> change in \(f\) caused by changing \(x\), assuming all other variables stay fixed.

For a function: $f(x_1, x_2, \dots, x_n)$ we can have many partial derivatives:

$$
\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n}
$$

Together, they form the **gradient**:

$$
\nabla f = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right)
$$

So, a partial derivative is mainly the derivative concept generalized to **multivariable functions**.

---

## 2. Geometric Meaning

For a function of two variables: $f(x, y)$ the graph is a surface in 3D.

The partial derivative: $\frac{\partial f}{\partial x}$ at a point $(x_0, y_0)$ is the **slope of the surface** in the direction of the x-axis at that point.

Similarly: $\frac{\partial f}{\partial y}$ is the slope in the direction of the y-axis.

By fixing all other variables, we reduce the problem to a single-variable slope at each step.

---

## 3. The Gradient as Direction of Steepest Ascent

The gradient:

$$
\nabla f = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right)
$$

is a vector.

It points in the direction in which: $f$ increases fastest.

That is, if you move from a point in the direction of: $\nabla f$ you climb the steepest slope of: $f$ Moving in the **opposite** direction: $-\nabla f$ decreases: $f$ as fast as possible.

---

## 4. Use Case: Gradient Descent

**Gradient descent** is the fundamental algorithm for training machine learning models.

The idea is: given a loss function: $L(\theta)$ where: $\theta = (\theta_1, \theta_2, \dots, \theta_n)$ are the model parameters, we want to find: $\theta^* = \arg\min_\theta L(\theta)$ We do this by repeatedly stepping in the direction of steepest descent: $\theta \leftarrow \theta - \alpha \nabla_\theta L$ where: $\alpha$ is the **learning rate**, a small positive number that controls how large each step is.

At each step we compute:

$$
\nabla_\theta L = \left( \frac{\partial L}{\partial \theta_1}, \frac{\partial L}{\partial \theta_2}, \dots, \frac{\partial L}{\partial \theta_n} \right)
$$

and move the parameters against it.

**Example:** suppose the loss is: $L(\theta_1, \theta_2) = \theta_1^2 + 2\theta_2^2$ Then:

$$
\frac{\partial L}{\partial \theta_1} = 2\theta_1, \quad \frac{\partial L}{\partial \theta_2} = 4\theta_2
$$

So the update is:

$$
\theta_1 \leftarrow \theta_1 - \alpha \cdot 2\theta_1
$$

$$
\theta_2 \leftarrow \theta_2 - \alpha \cdot 4\theta_2
$$

At each step, both parameters move toward zero, which is the minimum of this loss.

---

## 5. Jacobian Matrix

When a function maps vectors to vectors: $\mathbf{f} : \mathbb{R}^n \to \mathbb{R}^m$ the generalization of the gradient is the **Jacobian matrix**.

Each output component: $f_1, f_2, \dots, f_m$ is a scalar function of: $(x_1, x_2, \dots, x_n)$ The Jacobian is the matrix of all partial derivatives:

$$
J =
\begin{bmatrix}
\dfrac{\partial f_1}{\partial x_1} & \dfrac{\partial f_1}{\partial x_2} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\
\dfrac{\partial f_2}{\partial x_1} & \dfrac{\partial f_2}{\partial x_2} & \cdots & \dfrac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\dfrac{\partial f_m}{\partial x_1} & \dfrac{\partial f_m}{\partial x_2} & \cdots & \dfrac{\partial f_m}{\partial x_n}
\end{bmatrix}
$$

So: $J_{ij} = \frac{\partial f_i}{\partial x_j}$ The Jacobian generalizes the gradient (which is the special case $m = 1$, a single scalar output) to vector-valued functions.

**Why it matters:** the Jacobian appears in backpropagation. A neural network is a composition of functions: $\mathbf{h} = \sigma(W \mathbf{x} + \mathbf{b})$ To propagate the gradient of the loss backward through each layer, we multiply Jacobians in reverse order (chain rule). That is why understanding partial derivatives and the Jacobian is essential for understanding how neural networks are trained.

---

## 6. Chain Rule for Partial Derivatives

If: $z = f(u, v)$ and both: $u = g(x, y), \quad v = h(x, y)$ depend on: $x$ and: $y$ then by the **chain rule**:

$$
\frac{\partial z}{\partial x} = \frac{\partial f}{\partial u} \cdot \frac{\partial u}{\partial x} + \frac{\partial f}{\partial v} \cdot \frac{\partial v}{\partial x}
$$

The change in: $z$ due to a change in: $x$ flows through every intermediate variable.

---

## 7. Matrix Calculus

When functions take vectors or matrices as inputs, derivatives become vectors and matrices. These identities are essential for deriving update rules in machine learning.

Throughout, $\mathbf{x} \in \mathbb{R}^n$ is a column vector, $A \in \mathbb{R}^{m \times n}$ is a constant matrix, and $f$ is a scalar-valued function.

**Gradient of a linear function.**

$$
\nabla_{\mathbf{x}} (A\mathbf{x}) = A^T \qquad \text{(result is } n \times m \text{ Jacobian)}
$$

For the scalar case $f(\mathbf{x}) = \mathbf{a}^T \mathbf{x}$: $\nabla_{\mathbf{x}} (\mathbf{a}^T \mathbf{x}) = \mathbf{a}$ **Gradient of a quadratic form.**

For a symmetric matrix $A$: $\nabla_{\mathbf{x}} (\mathbf{x}^T A \mathbf{x}) = 2A\mathbf{x}$ For a general (not necessarily symmetric) $A$: $\nabla_{\mathbf{x}} (\mathbf{x}^T A \mathbf{x}) = (A + A^T)\mathbf{x}$ which reduces to $2A\mathbf{x}$ when $A = A^T$.

**Squared $L^2$ norm.** $\nabla_{\mathbf{x}} \lVert \mathbf{x} \rVert_2^2 = \nabla_{\mathbf{x}} (\mathbf{x}^T \mathbf{x}) = 2\mathbf{x}$ **Least-squares objective.**

$$
f(\mathbf{x}) = \lVert A\mathbf{x} - \mathbf{b} \rVert_2^2 = (A\mathbf{x} - \mathbf{b})^T(A\mathbf{x} - \mathbf{b})
$$

$$
\nabla_{\mathbf{x}} f = 2A^T(A\mathbf{x} - \mathbf{b})
$$

Setting this to zero gives the **normal equations**: $A^T A\mathbf{x} = A^T \mathbf{b}$.

**Derivative with respect to a matrix.**

For $f(W) = \mathbf{u}^T W \mathbf{v}$ (scalar, $W \in \mathbb{R}^{m \times n}$, $\mathbf{u} \in \mathbb{R}^m$, $\mathbf{v} \in \mathbb{R}^n$): $\frac{\partial f}{\partial W} = \mathbf{u}\mathbf{v}^T$ This is a rank-1 matrix. In neural networks, each weight update is the outer product of the upstream gradient ($\mathbf{u}$) and the downstream activation ($\mathbf{v}$) — this is exactly the backpropagation update rule.

**Derivative of the Frobenius norm.** $\nabla_A \lVert A \rVert_F^2 = \nabla_A \mathrm{tr}(A^T A) = 2A$ **Summary of common identities:**

| Expression | Gradient w.r.t. $\mathbf{x}$ |
|---|---|
| $\mathbf{a}^T \mathbf{x}$ | $\mathbf{a}$ |
| $\mathbf{x}^T \mathbf{x}$ | $2\mathbf{x}$ |
| $\mathbf{x}^T A \mathbf{x}$ (symmetric $A$) | $2A\mathbf{x}$ |
| $\lVert A\mathbf{x} - \mathbf{b} \rVert^2$ | $2A^T(A\mathbf{x} - \mathbf{b})$ |

This is exactly the rule used in **backpropagation**: the gradient of the loss flows backward through each composed function by multiplying the local partial derivatives along the way.
