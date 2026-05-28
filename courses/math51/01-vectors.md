# Vectors

A **vector** is an ordered list of numbers.

For example: $\mathbf{v} = (3, 5)$ is a vector with two numbers, and: $\mathbf{w} = (1, 0, -2)$ is a vector with three numbers.

The individual numbers are called **components** or **coordinates** of the vector.

---

## 1. Geometric Interpretation

In 2D, a vector can be drawn as an arrow from the origin to a point.

For example, the vector: $\mathbf{v} = (3, 5)$ is an arrow that goes 3 units to the right and 5 units up.

The arrow starts at: $(0, 0)$ and ends at: $(3, 5)$ Two arrows that are parallel, have the same length, and point in the same direction represent the **same vector**, even if they start at different points.

So a vector describes a **displacement**: how far and in what direction.

---

## 2. Notation

Vectors are usually written as column vectors:

$$
\mathbf{v} =
\begin{bmatrix}
v_1 \\
v_2 \\
\vdots \\
v_n
\end{bmatrix}
$$

or, for compactness, as a tuple: $\mathbf{v} = (v_1, v_2, \dots, v_n)$ Both notations represent the same object.

The **dimension** of the vector is the number of components.

For example: $\mathbf{v} = (3, 5)$ is a 2-dimensional vector.

And: $\mathbf{w} = (1, 0, -2)$ is a 3-dimensional vector.

In general, a vector in $n$-dimensional space belongs to:

$$
\mathbf{v} \in \mathbb{R}^n
$$

---

## 3. Vector Addition

Two vectors of the same dimension can be added together.

If: $\mathbf{a} = (a_1, a_2, \dots, a_n)$ and: $\mathbf{b} = (b_1, b_2, \dots, b_n)$ then:

$$
\mathbf{a} + \mathbf{b} = (a_1 + b_1,\ a_2 + b_2,\ \dots,\ a_n + b_n)
$$

So we add component by component.

For example: $(1, 2) + (3, 4) = (1+3,\ 2+4) = (4, 6)$ Geometrically, adding two vectors means placing the second arrow at the tip of the first arrow, and the sum is the arrow from the start to the end of that chain.

---

## 4. Scalar Multiplication

A vector can be multiplied by a number.

If: $\mathbf{v} = (v_1, v_2, \dots, v_n)$ and $c$ is a number (called a **scalar**), then: $c \mathbf{v} = (c v_1,\ c v_2,\ \dots,\ c v_n)$ We multiply each component by the scalar.

For example: $3 \cdot (2, -1) = (6, -3)$ Geometrically, scalar multiplication stretches or shrinks the vector.

If $c > 1$, the vector gets longer.

If $0 < c < 1$, the vector gets shorter.

If $c < 0$, the vector flips direction.

If $c = 0$, the vector becomes the zero vector.

---

## 5. Zero Vector

The **zero vector** has all components equal to zero: $\mathbf{0} = (0, 0, \dots, 0)$ Adding the zero vector to any vector leaves it unchanged:

$$
\mathbf{v} + \mathbf{0} = \mathbf{v}
$$

---

## 6. Negative Vector

The **negative** of a vector flips its direction: $-\mathbf{v} = (-v_1, -v_2, \dots, -v_n)$ Adding a vector and its negative gives the zero vector:

$$
\mathbf{v} + (-\mathbf{v}) = \mathbf{0}
$$

---

## 7. Vector Subtraction

Subtracting one vector from another is defined as: $\mathbf{a} - \mathbf{b} = \mathbf{a} + (-\mathbf{b})$ So: $\mathbf{a} - \mathbf{b} = (a_1 - b_1,\ a_2 - b_2,\ \dots,\ a_n - b_n)$ Geometrically, $\mathbf{a} - \mathbf{b}$ is the arrow from the tip of $\mathbf{b}$ to the tip of $\mathbf{a}$.

---

## 8. Standard Basis Vectors

In $n$-dimensional space, the **standard basis vectors** are:

$$
\mathbf{e}_1 = (1, 0, 0, \dots, 0)
$$

$$
\mathbf{e}_2 = (0, 1, 0, \dots, 0)
$$

$$
\mathbf{e}_n = (0, 0, 0, \dots, 1)
$$

Each basis vector has exactly one component equal to 1, and the rest are 0.

In 2D: $\mathbf{e}_1 = (1, 0)$ points along the x-axis, and: $\mathbf{e}_2 = (0, 1)$ points along the y-axis.

Any vector can be written as a combination of basis vectors.

For example: $(3, 5) = 3 \cdot (1, 0) + 5 \cdot (0, 1) = 3\,\mathbf{e}_1 + 5\,\mathbf{e}_2$ More generally:

$$
\mathbf{v} = v_1\,\mathbf{e}_1 + v_2\,\mathbf{e}_2 + \dots + v_n\,\mathbf{e}_n
$$

---

## 9. Properties of Vector Operations

Vector addition and scalar multiplication satisfy the following properties.

- **Commutativity:** $\mathbf{a} + \mathbf{b} = \mathbf{b} + \mathbf{a}$
- **Associativity:** $(\mathbf{a} + \mathbf{b}) + \mathbf{c} = \mathbf{a} + (\mathbf{b} + \mathbf{c})$
- **Distributivity over scalar multiplication:** $c(\mathbf{a} + \mathbf{b}) = c\mathbf{a} + c\mathbf{b}$ and: $(c + d)\mathbf{a} = c\mathbf{a} + d\mathbf{a}$ These properties hold for all vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c}$ and all scalars $c$, $d$.

---

## 10. Summary

A **vector** is an ordered list of numbers: $\mathbf{v} = (v_1, v_2, \dots, v_n) \in \mathbb{R}^n$ The two basic operations are:

- **Addition:** $\mathbf{a} + \mathbf{b} = (a_1 + b_1,\ \dots,\ a_n + b_n)$
- **Scalar multiplication:** $c\,\mathbf{v} = (c v_1,\ \dots,\ c v_n)$ Geometrically, a vector represents a direction and a magnitude (length) in space.

The next topic covers **linear independence, span, and basis** — the structural properties of sets of vectors.

https://www.youtube.com/watch?v=eu6i7WJeinw&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab