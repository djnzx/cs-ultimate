# Linear Transformations

A **linear transformation** is a function that maps vectors to vectors and respects the structure of vector addition and scalar multiplication.

More precisely, a function: $f : \mathbb{R}^n \to \mathbb{R}^m$ is a linear transformation if for all vectors $\mathbf{u}$, $\mathbf{v}$ and all scalars $c$: $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$ and: $f(c\,\mathbf{v}) = c\,f(\mathbf{v})$ These two conditions can be combined into one: $f(\alpha\,\mathbf{u} + \beta\,\mathbf{v}) = \alpha\,f(\mathbf{u}) + \beta\,f(\mathbf{v})$ The key consequence is: $f(\mathbf{0}) = \mathbf{0}$ A linear transformation always maps the zero vector to the zero vector.

---

## 1. Connection to Matrices

Every linear transformation $f : \mathbb{R}^n \to \mathbb{R}^m$ can be represented as a matrix.

There exists a unique matrix $A \in \mathbb{R}^{m \times n}$ such that: $f(\mathbf{v}) = A\mathbf{v}$ for every vector $\mathbf{v} \in \mathbb{R}^n$.

This means:

> matrix-vector multiplication **is** a linear transformation.

Conversely, every linear transformation can be described by a matrix.

So linear transformations and matrices are two ways of describing the same thing.

---

## 2. How to Build the Matrix from the Transformation

To find the matrix $A$ of a linear transformation $f$, apply $f$ to each standard basis vector: $A = \left[ f(\mathbf{e}_1) \mid f(\mathbf{e}_2) \mid \cdots \mid f(\mathbf{e}_n) \right]$ The columns of $A$ are the images of the basis vectors.

For example, if $f : \mathbb{R}^2 \to \mathbb{R}^2$ and:

$$
f(\mathbf{e}_1) =
\begin{bmatrix}
2 \\
1
\end{bmatrix}
$$

and:

$$
f(\mathbf{e}_2) =
\begin{bmatrix}
3 \\
4
\end{bmatrix}
$$

then the matrix is:

$$
A =
\begin{bmatrix}
2 & 3 \\
1 & 4
\end{bmatrix}
$$

This works because any vector can be written in terms of basis vectors, and linearity takes care of the rest.

---

## 3. What a Linear Transformation Does to Space

A linear transformation can deform space in several ways.

**Scaling:** stretch or shrink in one or more directions.

$$
A =
\begin{bmatrix}
2 & 0 \\
0 & 3
\end{bmatrix}
$$

This stretches the x-direction by factor 2 and the y-direction by factor 3.

**Rotation by angle $\theta$ in 2D:**

$$
R_\theta =
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
$$

This rotates every vector by angle $\theta$ around the origin.

**Reflection across the x-axis:**

$$
A =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

**Shearing:** tilt one axis while keeping the other fixed.

$$
A =
\begin{bmatrix}
1 & c \\
0 & 1
\end{bmatrix}
$$

In every case, the transformation is described completely by where it sends the basis vectors.

---

## 4. What Linear Transformations Preserve

A linear transformation always preserves:

- The zero vector (it maps to zero)
- Straight lines through the origin (they stay straight lines through the origin)
- Parallel lines (they remain parallel)
- The ratio at which a line segment is divided

A linear transformation cannot:
- Translate (shift) the origin
- Curve straight lines
- Map one point on a line to a point off the line

This is why the two conditions — $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$ and $f(c\mathbf{v}) = c f(\mathbf{v})$ — capture exactly the idea of a "straight, origin-preserving" map.

---

## 5. Composition of Transformations

Applying one linear transformation after another is called **composition**.

If $f$ has matrix $A$ and $g$ has matrix $B$, then applying $g$ first and then $f$ gives: $f(g(\mathbf{v})) = A(B\mathbf{v}) = (AB)\mathbf{v}$ So the composition of two linear transformations corresponds to **matrix multiplication**.

This is why matrix multiplication is defined the way it is: it represents the composition of transformations.

For example, rotating by $30°$ and then scaling by $2$ is a single linear transformation whose matrix is:

$$
S =
\begin{bmatrix}
2 & 0 \\
0 & 2
\end{bmatrix}
$$

and:

$$
R =
\begin{bmatrix}
\cos 30^\circ & -\sin 30^\circ \\
\sin 30^\circ & \cos 30^\circ
\end{bmatrix}
$$

The combined transformation has matrix $SR$.

---

## 6. The Identity Transformation

The identity transformation maps every vector to itself: $f(\mathbf{v}) = \mathbf{v}$ Its matrix is the identity matrix $I$.

---

## 7. Inverse Transformation

If a linear transformation $f$ with matrix $A$ is invertible, then there is an inverse transformation $f^{-1}$ with matrix $A^{-1}$.

The inverse undoes what $f$ does: $f^{-1}(f(\mathbf{v})) = \mathbf{v}$ In matrix terms: $A^{-1}(A\mathbf{v}) = \mathbf{v}$ which follows from:

$$
A^{-1}A = I
$$

---

## 8. Why This Matters

Linear transformations are the central objects of linear algebra.

Most operations in machine learning involve applying a matrix to a vector: computing activations in a neural network, projecting data, rotating coordinate systems, or solving systems of equations.

All of these are linear transformations.

Understanding that **a matrix is a transformation** — not just a table of numbers — is the key insight that makes the rest of linear algebra intuitive.

The next natural question is:

> Are there special vectors that a transformation acts on in a particularly simple way?

The answer leads to eigenvectors. But first, we need to understand magnitude, dot products, and projections — the geometric tools that let us measure and decompose vectors.

---

## 9. Summary

A **linear transformation** $f : \mathbb{R}^n \to \mathbb{R}^m$ satisfies: $f(\alpha\,\mathbf{u} + \beta\,\mathbf{v}) = \alpha\,f(\mathbf{u}) + \beta\,f(\mathbf{v})$ Every linear transformation is represented by a matrix $A$: $f(\mathbf{v}) = A\mathbf{v}$ The columns of $A$ are the images of the standard basis vectors.

Composition of transformations corresponds to matrix multiplication: $f \circ g \leftrightarrow AB$ Key examples:
- Scaling: diagonal matrix
- Rotation in 2D: rotation matrix with $\cos\theta$, $\sin\theta$
- Identity: $I$ matrix
- Inverse: $A^{-1}$, if it exists
