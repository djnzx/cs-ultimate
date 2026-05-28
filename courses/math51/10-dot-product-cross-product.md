# Dot Product and Cross Product

In vector geometry, two very important operations are: $\text{dot product}$ and $\text{cross product}$ They answer different geometric questions.

The **dot product** tells us how much two vectors point in the same direction.

The **cross product** gives a new vector perpendicular to two given vectors.

---

## 1. Dot Product

Suppose we have two vectors in 3D: $\mathbf{a} = (a_x, a_y, a_z)$ and $\mathbf{b} = (b_x, b_y, b_z)$ Their dot product is:

$$
\mathbf{a} \cdot \mathbf{b} = a_xb_x + a_yb_y + a_zb_z
$$

The result is a **number**, not a vector.

So:

$$
\mathbf{a} \cdot \mathbf{b} \in \mathbb{R}
$$

https://www.youtube.com/watch?v=LyGKycYT2v0

### Geometric meaning

The dot product can also be written as:

$$
\mathbf{a} \cdot \mathbf{b} = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \cos \theta
$$

where $\lvert \mathbf{a} \rvert$ is the magnitude of vector $\mathbf{a}$ and $\lvert \mathbf{b} \rvert$ is the magnitude of vector $\mathbf{b}$ and $\theta$ is the angle between them.

So the dot product measures how much two vectors go in the same direction.

---

## 2. Dot Product and Angle

From

$$
\mathbf{a} \cdot \mathbf{b} = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \cos \theta
$$

we can find the angle:

$$
\cos \theta = \frac{\mathbf{a} \cdot \mathbf{b}} {\lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert}
$$

Therefore:

$$
\theta = \arccos \left( \frac{\mathbf{a} \cdot \mathbf{b}} {\lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert} \right)
$$

This is useful when we want to know the angle between two directions.

---

## 3. Important Dot Product Cases

### Same direction

If two vectors point in the same direction, then: $\theta = 0$ and $\cos 0 = 1$ So:

$$
\mathbf{a} \cdot \mathbf{b} = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert
$$

The dot product is positive and maximal.

### Opposite direction

If two vectors point in opposite directions, then: $\theta = \pi$ and $\cos \pi = -1$ So:

$$
\mathbf{a} \cdot \mathbf{b} = -\lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert
$$

The dot product is negative and minimal.

### Perpendicular vectors

If two vectors are perpendicular, then: $\theta = \frac{\pi}{2}$ and $\cos \frac{\pi}{2} = 0$ So: $\mathbf{a} \cdot \mathbf{b} = 0$ This is very important:

$$
\mathbf{a} \perp \mathbf{b} \quad \Longleftrightarrow \quad \mathbf{a} \cdot \mathbf{b} = 0
$$

for nonzero vectors.

---

## 4. Dot Product Example

Let: $\mathbf{a} = (1,2,3)$ and $\mathbf{b} = (4,5,6)$ Then:

$$
\mathbf{a} \cdot \mathbf{b} = 1 \cdot 4 + 2 \cdot 5 + 3 \cdot 6
$$

So:

$$
\mathbf{a} \cdot \mathbf{b} = 4 + 10 + 18
$$

Therefore:

$$
\mathbf{a} \cdot \mathbf{b} = 32
$$

---

## 5. Cross Product

The cross product is defined for two vectors in 3D: $\mathbf{a} = (a_x, a_y, a_z)$ and $\mathbf{b} = (b_x, b_y, b_z)$ Their cross product is: $\mathbf{a} \times \mathbf{b}$ Unlike the dot product, the result is a **vector**: $\mathbf{a} \times \mathbf{b} \in \mathbb{R}^3$ The cross product is:

$$
\mathbf{a} \times \mathbf{b} = \left( a_yb_z - a_zb_y, \; a_zb_x - a_xb_z, \; a_xb_y - a_yb_x \right)
$$

---

## 6. Geometric Meaning of Cross Product

The vector $\mathbf{a} \times \mathbf{b}$ is perpendicular to both $\mathbf{a}$ and $\mathbf{b}$ That means: $(\mathbf{a} \times \mathbf{b}) \cdot \mathbf{a} = 0$ and $(\mathbf{a} \times \mathbf{b}) \cdot \mathbf{b} = 0$ So the cross product gives a normal vector to the plane spanned by $\mathbf{a}$ and

$$
\mathbf{b}
$$

---

## 7. Magnitude of the Cross Product

The magnitude of the cross product is:

$$
\lvert \mathbf{a} \times \mathbf{b} \rvert = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \sin \theta
$$

where $\theta$ is the angle between the vectors.

This magnitude equals the area of the parallelogram built on vectors $\mathbf{a}$ and $\mathbf{b}$ So:

$$
\lvert \mathbf{a} \times \mathbf{b} \rvert = \text{area of parallelogram}
$$

The area of the triangle formed by the same two vectors is half of that:

$$
\text{area of triangle} = \frac{1}{2} \lvert \mathbf{a} \times \mathbf{b} \rvert
$$

---

## 8. Important Cross Product Cases

### Parallel vectors

If two vectors are parallel, then: $\theta = 0$ or $\theta = \pi$ In both cases: $\sin \theta = 0$ Therefore: $\lvert \mathbf{a} \times \mathbf{b} \rvert = 0$ So: $\mathbf{a} \times \mathbf{b} = \mathbf{0}$ This means:

$$
\mathbf{a} \parallel \mathbf{b} \quad \Longleftrightarrow \quad \mathbf{a} \times \mathbf{b} = \mathbf{0}
$$

for nonzero vectors.

### Perpendicular vectors

If two vectors are perpendicular, then: $\theta = \frac{\pi}{2}$ and $\sin \frac{\pi}{2} = 1$ Therefore:

$$
\lvert \mathbf{a} \times \mathbf{b} \rvert = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert
$$

The magnitude is maximal.

---

## 9. Cross Product Example

Let: $\mathbf{a} = (1,2,3)$ and $\mathbf{b} = (4,5,6)$ Then:

$$
\mathbf{a} \times \mathbf{b} = \left( 2 \cdot 6 - 3 \cdot 5, \; 3 \cdot 4 - 1 \cdot 6, \; 1 \cdot 5 - 2 \cdot 4 \right)
$$

So:

$$
\mathbf{a} \times \mathbf{b} = (12 - 15,\; 12 - 6,\; 5 - 8)
$$

Therefore:

$$
\mathbf{a} \times \mathbf{b} = (-3,6,-3)
$$

This vector is perpendicular to both original vectors.

We can check:

$$
(-3,6,-3) \cdot (1,2,3) = -3 + 12 - 9 = 0
$$

and:

$$
(-3,6,-3) \cdot (4,5,6) = -12 + 30 - 18 = 0
$$

So: $\mathbf{a} \times \mathbf{b}$ is really perpendicular to both $\mathbf{a}$ and

$$
\mathbf{b}
$$

---

## 10. Dot Product vs Cross Product

The dot product: $\mathbf{a} \cdot \mathbf{b}$ returns a scalar: $\mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ It measures directional similarity.

The cross product: $\mathbf{a} \times \mathbf{b}$ returns a vector: $\mathbb{R}^3 \times \mathbb{R}^3 \to \mathbb{R}^3$ It gives a direction perpendicular to both vectors.

So: $\text{dot product} \Rightarrow \text{angle / projection / perpendicularity}$ while:

$$
\text{cross product} \Rightarrow \text{normal vector / area / orientation}
$$

---

## 11. Self dot product and magnitude

A useful special case of the dot product is when a vector is dotted with itself.

For a vector: $\mathbf{v} = (v_1, v_2, \dots, v_n)$ the dot product with itself is:

$$
\mathbf{v} \cdot \mathbf{v} = v_1^2 + v_2^2 + \dots + v_n^2
$$

But from the magnitude formula, we also know:

$$
\lvert \mathbf{v} \rvert^2 = v_1^2 + v_2^2 + \dots + v_n^2
$$

Therefore: $\mathbf{v} \cdot \mathbf{v} = \lvert \mathbf{v} \rvert^2$ or equivalently: $\lvert \mathbf{v} \rvert = \sqrt{\mathbf{v} \cdot \mathbf{v}}$ This identity connects the dot product to magnitude, and it appears frequently in derivations — for example, in the projection formula in the next section.

---

## 12. Summary

The dot product is:

$$
\mathbf{a} \cdot \mathbf{b} = a_xb_x + a_yb_y + a_zb_z
$$

and geometrically:

$$
\mathbf{a} \cdot \mathbf{b} = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \cos \theta
$$

It tells us how much two vectors point in the same direction.

The cross product is:

$$
\mathbf{a} \times \mathbf{b} = \left( a_yb_z - a_zb_y, \; a_zb_x - a_xb_z, \; a_xb_y - a_yb_x \right)
$$

and geometrically:

$$
\lvert \mathbf{a} \times \mathbf{b} \rvert = \lvert \mathbf{a} \rvert \lvert \mathbf{b} \rvert \sin \theta
$$

It gives a vector perpendicular to both original vectors.

The key facts are:

$$
\mathbf{a} \cdot \mathbf{b} = 0 \quad \Longleftrightarrow \quad \mathbf{a} \perp \mathbf{b}
$$

and:

$$
\mathbf{a} \times \mathbf{b} = \mathbf{0} \quad \Longleftrightarrow \quad \mathbf{a} \parallel \mathbf{b}
$$

for nonzero vectors.