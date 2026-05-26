# Vector Projection and Orthogonal Components

Vector projection answers a very natural question:

**How much of one vector goes in the direction of another vector?**

Suppose we have two vectors $\mathbf{a}$ and $\mathbf{b}$.

We want to decompose vector $\mathbf{a}$ into two parts:

$$
\mathbf{a} = \mathbf{a}_{\parallel} + \mathbf{a}_{\perp}
$$

Here $\mathbf{a}_{\parallel}$ is the part of $\mathbf{a}$ that goes in the direction of $\mathbf{b}$:

$$
\mathbf{a}_{\parallel} \parallel \mathbf{b}
$$

The vector $\mathbf{a}_{\perp}$ is the part of $\mathbf{a}$ that is perpendicular to $\mathbf{b}$:

$$
\mathbf{a}_{\perp} \perp \mathbf{b}
$$

---

## 1. Geometric idea

Imagine vector $\mathbf{b}$ as a direction or an axis.

Now vector $\mathbf{a}$ may point partly along that axis and partly away from it.

The projection of $\mathbf{a}$ onto $\mathbf{b}$ is the shadow of $\mathbf{a}$ on the direction of $\mathbf{b}$.

So we split $\mathbf{a}$ into a part along $\mathbf{b}$ and a remaining perpendicular part.

In symbols:

$$
\mathbf{a} = \mathrm{proj}_{\mathbf{b}}(\mathbf{a}) + \mathbf{a}_{\perp}
$$

---

## 2. Unit direction vector

To project onto the direction of $\mathbf{b}$, it is useful to first normalize $\mathbf{b}$.

The unit vector in the direction of $\mathbf{b}$ is:

$$
\hat{\mathbf{b}} = \frac{\mathbf{b}}{\lVert \mathbf{b} \rVert}
$$

where $\lVert \mathbf{b} \rVert$ is the magnitude of $\mathbf{b}$.

So:

$$
\lVert \hat{\mathbf{b}} \rVert = 1
$$

---

## 3. Scalar projection

The scalar projection tells us the signed length of the shadow of $\mathbf{a}$ onto $\mathbf{b}$.

It is:

$$
\mathbf{a} \cdot \hat{\mathbf{b}}
$$

Since:

$$
\hat{\mathbf{b}} = \frac{\mathbf{b}}{\lVert \mathbf{b} \rVert}
$$

we get:

$$
\mathbf{a} \cdot \hat{\mathbf{b}} = \mathbf{a} \cdot \frac{\mathbf{b}}{\lVert \mathbf{b} \rVert}
$$

Therefore:

$$
\mathbf{a} \cdot \hat{\mathbf{b}} = \frac{\mathbf{a} \cdot \mathbf{b}}{\lVert \mathbf{b} \rVert}
$$

This value is a scalar.

It can be positive, negative, or zero.

If it is positive, then $\mathbf{a}$ has a component in the same direction as $\mathbf{b}$.

If it is negative, then $\mathbf{a}$ has a component in the opposite direction.

If it is zero, then $\mathbf{a}$ is perpendicular to $\mathbf{b}$.

---

## 4. Vector projection

The vector projection gives the actual vector along the direction of $\mathbf{b}$.

First we find the signed length:

$$
\mathbf{a} \cdot \hat{\mathbf{b}}
$$

Then we multiply by the unit direction vector:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = (\mathbf{a} \cdot \hat{\mathbf{b}})\hat{\mathbf{b}}
$$

Now substitute:

$$
\hat{\mathbf{b}} = \frac{\mathbf{b}}{\lVert \mathbf{b} \rVert}
$$

So:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) =
(\mathbf{a} \cdot \frac{\mathbf{b}}{\lVert \mathbf{b} \rVert})
\frac{\mathbf{b}}{\lVert \mathbf{b} \rVert}
$$

This becomes:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\lVert \mathbf{b} \rVert^2} \mathbf{b}
$$

Since:

$$
\lVert \mathbf{b} \rVert^2 = \mathbf{b} \cdot \mathbf{b}
$$

we can also write:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} \mathbf{b}
$$

This is the most common formula.

---

## 5. Orthogonal component

The orthogonal component is what remains after removing the projection:

$$
\mathbf{a}_{\perp} = \mathbf{a} - \mathrm{proj}_{\mathbf{b}}(\mathbf{a})
$$

So the full decomposition is:

$$
\mathbf{a} = \mathrm{proj}_{\mathbf{b}}(\mathbf{a}) + \mathbf{a}_{\perp}
$$

where:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) \parallel \mathbf{b}
$$

and:

$$
\mathbf{a}_{\perp} \perp \mathbf{b}
$$

---

## 6. Why the remaining part is perpendicular

Let:

$$
\mathbf{a}_{\parallel} = \mathrm{proj}_{\mathbf{b}}(\mathbf{a})
$$

and:

$$
\mathbf{a}_{\perp} = \mathbf{a} - \mathbf{a}_{\parallel}
$$

We want to show:

$$
\mathbf{a}_{\perp} \cdot \mathbf{b} = 0
$$

Using the projection formula:

$$
\mathbf{a}_{\parallel} = \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} \mathbf{b}
$$

Therefore:

$$
\mathbf{a}_{\perp} = \mathbf{a} - \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} \mathbf{b}
$$

Now take the dot product with $\mathbf{b}$:

$$
\mathbf{a}_{\perp} \cdot \mathbf{b} =
(\mathbf{a} - \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} \mathbf{b})
\cdot \mathbf{b}
$$

Distribute the dot product:

$$
\mathbf{a}_{\perp} \cdot \mathbf{b} = \mathbf{a} \cdot \mathbf{b} - \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} (\mathbf{b} \cdot \mathbf{b})
$$

The denominator cancels:

$$
\mathbf{a}_{\perp} \cdot \mathbf{b} = \mathbf{a} \cdot \mathbf{b} - \mathbf{a} \cdot \mathbf{b}
$$

Therefore:

$$
\mathbf{a}_{\perp} \cdot \mathbf{b} = 0
$$

So $\mathbf{a}_{\perp}$ is perpendicular to $\mathbf{b}$.

---

## 7. Concrete example in 2D

Let:

$$
\mathbf{a} = (3,4)
$$

and:

$$
\mathbf{b} = (1,0)
$$

Vector $\mathbf{b}$ points along the x-axis.

The projection of $\mathbf{a}$ onto $\mathbf{b}$ should be the horizontal part of $\mathbf{a}$ Compute:

$$
\mathbf{a} \cdot \mathbf{b} = (3,4) \cdot (1,0)
$$

So:

$$
\mathbf{a} \cdot \mathbf{b} = 3 \cdot 1 + 4 \cdot 0 = 3
$$

Also:

$$
\mathbf{b} \cdot \mathbf{b} = (1,0) \cdot (1,0) = 1
$$

Therefore:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{3}{1}(1,0) = (3,0)
$$

So the parallel component is:

$$
\mathbf{a}_{\parallel} = (3,0)
$$

The orthogonal component is:

$$
\mathbf{a}_{\perp} = \mathbf{a} - \mathbf{a}_{\parallel}
$$

So:

$$
\mathbf{a}_{\perp} = (3,4) - (3,0) = (0,4)
$$

Hence:

$$
(3,4) = (3,0) + (0,4)
$$

The vector $(3,0)$ is parallel to $(1,0)$, and the vector $(0,4)$ is perpendicular to $(1,0)$.

---

## 8. Concrete example with non-unit vector

Let:

$$
\mathbf{a} = (4,3)
$$

and:

$$
\mathbf{b} = (2,0)
$$

Even though $\mathbf{b}$ has length $2$, it still points in the x-direction.

Compute:

$$
\mathbf{a} \cdot \mathbf{b} = (4,3) \cdot (2,0) = 4 \cdot 2 + 3 \cdot 0 = 8
$$

Compute:

$$
\mathbf{b} \cdot \mathbf{b} = (2,0) \cdot (2,0) = 4
$$

Therefore:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{8}{4}(2,0)
$$

So:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = 2(2,0) = (4,0)
$$

The orthogonal component is:

$$
\mathbf{a}_{\perp} = (4,3) - (4,0) = (0,3)
$$

So:

$$
(4,3) = (4,0) + (0,3)
$$

Notice that projecting onto $(2,0)$ gives the same direction as projecting onto $(1,0)$.

The length of $\mathbf{b}$ does not change the direction of the projection; it is corrected by the denominator:

$$
\mathbf{b} \cdot \mathbf{b}
$$

---

## 9. Example in 3D

Let:

$$
\mathbf{a} = (2,3,4)
$$

and:

$$
\mathbf{b} = (1,0,1)
$$

Compute the dot product:

$$
\mathbf{a} \cdot \mathbf{b} = (2,3,4) \cdot (1,0,1)
$$

So:

$$
\mathbf{a} \cdot \mathbf{b} = 2 \cdot 1 + 3 \cdot 0 + 4 \cdot 1 = 6
$$

Compute:

$$
\mathbf{b} \cdot \mathbf{b} = (1,0,1) \cdot (1,0,1)
$$

So:

$$
\mathbf{b} \cdot \mathbf{b} = 1^2 + 0^2 + 1^2 = 2
$$

Therefore:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{6}{2}(1,0,1)
$$

So:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = 3(1,0,1) = (3,0,3)
$$

The orthogonal component is:

$$
\mathbf{a}_{\perp} = \mathbf{a} - \mathrm{proj}_{\mathbf{b}}(\mathbf{a})
$$

So:

$$
\mathbf{a}_{\perp} = (2,3,4) - (3,0,3)
$$

Therefore:

$$
\mathbf{a}_{\perp} = (-1,3,1)
$$

Check that it is perpendicular to $\mathbf{b}$.

Compute:

$$
\mathbf{a}_{\perp} \cdot \mathbf{b} = (-1,3,1) \cdot (1,0,1)
$$

So:

$$
\mathbf{a}_{\perp} \cdot \mathbf{b} = -1 \cdot 1 + 3 \cdot 0 + 1 \cdot 1 = 0
$$

Therefore:

$$
\mathbf{a}_{\perp} \perp \mathbf{b}
$$

The full decomposition is:

$$
(2,3,4) = (3,0,3) + (-1,3,1)
$$

---

## 10. Summary

Projection decomposes a vector into two parts:

$$
\mathbf{a} = \mathbf{a}_{\parallel} + \mathbf{a}_{\perp}
$$

where $\mathbf{a}_{\parallel}$ is parallel to $\mathbf{b}$ and $\mathbf{a}_{\perp}$ is perpendicular to $\mathbf{b}$.

The parallel component is:

$$
\mathbf{a}_{\parallel} = \mathrm{proj}_{\mathbf{b}}(\mathbf{a}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} \mathbf{b}
$$

The orthogonal component is:

$$
\mathbf{a}_{\perp} = \mathbf{a} - \mathrm{proj}_{\mathbf{b}}(\mathbf{a})
$$

The key facts are:

$$
\mathrm{proj}_{\mathbf{b}}(\mathbf{a}) \parallel \mathbf{b}
$$

and:

$$
\mathbf{a}_{\perp} \perp \mathbf{b}
$$

So projection is the mathematical way to split a vector into the part along a direction and the part perpendicular to that direction.
