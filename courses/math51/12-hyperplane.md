# Hyperplane

## 1. Definition

In **n-dimensional space**, a hyperplane is the natural generalization of a line in 2D and a plane in 3D.

The equation looks like: $a_1x_1 + a_2x_2 + \dots + a_nx_n = d$ or, in vector form: $\mathbf{a} \cdot \mathbf{x} = d$ where $\mathbf{a} = (a_1, a_2, \dots, a_n)$ is the **normal vector** to the hyperplane, and $\mathbf{x} = (x_1, x_2, \dots, x_n)$ is any point lying on the hyperplane.

Equivalently, we can write:

$$
a_1x_1 + a_2x_2 + \dots + a_nx_n - d = 0
$$

## 2. Examples

In 2D: $ax + by = d$ This is a **line**.

In 3D: $ax + by + cz = d$ This is a **plane**.

In 4D: $a_1x_1 + a_2x_2 + a_3x_3 + a_4x_4 = d$ This is a **3-dimensional hyperplane inside 4-dimensional space**.

## 3. Meaning of the Coefficients

The vector $\mathbf{a}$ does not lie inside the hyperplane. It is perpendicular to it.

The number $d$ controls the shift of the hyperplane from the origin.

If $d = 0$ then the hyperplane passes through the origin: $a_1x_1 + a_2x_2 + \dots + a_nx_n = 0$ If $d \neq 0$ then the hyperplane is shifted away from the origin.

Because **one linear equation removes one degree of freedom**.

In 4-dimensional space, a point has 4 coordinates: $(x_1, x_2, x_3, x_4)$ So before any constraint, all 4 coordinates are free.

Now take one hyperplane equation: $a_1x_1 + a_2x_2 + a_3x_3 + a_4x_4 = d$ This equation imposes **one constraint** on the 4 variables. So only 3 variables can be chosen freely; the fourth is determined by the equation.

For example, suppose: $x_1 + x_2 + x_3 + x_4 = 10$ We can freely choose: $x_1, x_2, x_3$ and then $x_4$ must be: $x_4 = 10 - x_1 - x_2 - x_3$ So the set of all solutions can be described using 3 independent parameters: $(x_1, x_2, x_3)$ That is why it is **3-dimensional**.

The pattern is:

$$
\mathbb{R}^2 \Rightarrow \text{line has dimension } 1
$$

$$
\mathbb{R}^3 \Rightarrow \text{plane has dimension } 2
$$

$$
\mathbb{R}^4 \Rightarrow \text{hyperplane has dimension } 3
$$

In general: $\mathbb{R}^n \Rightarrow \text{hyperplane has dimension } n - 1$ A **hyperplane** in $$n$$-dimensional space is always an $$(n-1)$$-dimensional object.

## 4. Intersection of Two Planes in 3D

In 3D space, a plane usually has equation: $ax + by + cz = d$ or in vector form: $\mathbf{n} \cdot \mathbf{x} = d$ where $\mathbf{n} = (a,b,c)$ is the **normal vector** of the plane, and $\mathbf{x} = (x,y,z)$ is any point on the plane.

Now suppose we have two planes:

$$
\Pi_1: a_1x + b_1y + c_1z = d_1
$$

$$
\Pi_2: a_2x + b_2y + c_2z = d_2
$$

Their normal vectors are:

$$
\mathbf{n}_1 = (a_1,b_1,c_1)
$$

$$
\mathbf{n}_2 = (a_2,b_2,c_2)
$$

### What Is the Intersection?

Usually, two planes in 3D intersect in a **line**.

That line consists of all points that satisfy both equations at the same time:

$$
\begin{cases}
a_1x + b_1y + c_1z = d_1 \\
a_2x + b_2y + c_2z = d_2
\end{cases}
$$

So the intersection is a set of points:

$$
L = \Pi_1 \cap \Pi_2
$$

### Why Is the Intersection a Line?

A point in 3D has three coordinates: $(x,y,z)$ So initially there are 3 degrees of freedom.

Each independent plane equation gives one constraint.

The first plane removes one degree of freedom: $3 - 1 = 2$ That leaves a 2-dimensional object: a plane.

The second independent plane removes one more degree of freedom: $3 - 2 = 1$ That leaves a 1-dimensional object: a line.

So, in general:

$$
\mathbb{R}^3 \quad \xrightarrow{\text{one plane equation}} \quad \text{plane} \quad \xrightarrow{\text{second independent plane equation}} \quad \text{line}
$$

### Direction of the Intersection Line

The line of intersection lies inside both planes.

Therefore its direction vector must be perpendicular to both normal vectors:

$$
\mathbf{v} \perp \mathbf{n}_1
$$

and:

$$
\mathbf{v} \perp \mathbf{n}_2
$$

A vector perpendicular to both normals is given by the cross product:

$$
\mathbf{v} = \mathbf{n}_1 \times \mathbf{n}_2
$$

So:

$$
\mathbf{v} = (a_1,b_1,c_1) \times (a_2,b_2,c_2)
$$

Expanding the cross product:

$$
\mathbf{v} = ( b_1c_2 - c_1b_2, \; c_1a_2 - a_1c_2, \; a_1b_2 - b_1a_2 )
$$

This vector gives the **direction** of the intersection line.

### Finding One Point on the Line

To write the full equation of the line, we need:

1. one point on the line;
2. one direction vector.

The direction vector is:

$$
\mathbf{v} = \mathbf{n}_1 \times \mathbf{n}_2
$$

Now we need one point:

$$
\mathbf{p}_0 = (x_0,y_0,z_0)
$$

that satisfies both plane equations:

$$
\begin{cases}
a_1x_0 + b_1y_0 + c_1z_0 = d_1 \\
a_2x_0 + b_2y_0 + c_2z_0 = d_2
\end{cases}
$$

Because the intersection is usually a line, there are infinitely many such points.

To find one simple point, we often choose one coordinate to be zero.

For example, set:

$$
z_0 = 0
$$

Then solve the 2D system:

$$
\begin{cases}
a_1x_0 + b_1y_0 = d_1 \\
a_2x_0 + b_2y_0 = d_2
\end{cases}
$$

If this system has a solution, then we get:

$$
\mathbf{p}_0 = (x_0,y_0,0)
$$

But we do not have to choose $z_0 = 0$.

We could instead choose $x_0 = 0$ or $y_0 = 0$.

The choice is made only for convenience.

### Equation of the Intersection Line

Once we have a point:

$$
\mathbf{p}_0 = (x_0,y_0,z_0)
$$

and a direction vector:

$$
\mathbf{v} = (v_x,v_y,v_z)
$$

the line can be written in parametric form:

$$
\mathbf{x}(t) = \mathbf{p}_0 + t\mathbf{v}
$$

or explicitly:

$$
(x,y,z) = (x_0,y_0,z_0) + t(v_x,v_y,v_z)
$$

That means:

$$
x = x_0 + tv_x
$$

$$
y = y_0 + tv_y
$$

$$
z = z_0 + tv_z
$$

where

$$
t \in \mathbb{R}
$$

### Worked Example

Consider two planes:

$$
\Pi_1: x + y + z = 6
$$

$$
\Pi_2: x - y + z = 2
$$

Their normal vectors are:

$$
\mathbf{n}_1 = (1,1,1)
$$

$$
\mathbf{n}_2 = (1,-1,1)
$$

The direction of the intersection line is:

$$
\mathbf{v} = \mathbf{n}_1 \times \mathbf{n}_2
$$

So:

$$
\mathbf{v} = (1,1,1) \times (1,-1,1)
$$

Using the formula:

$$
\mathbf{v} = ( 1 \cdot 1 - 1 \cdot (-1), \; 1 \cdot 1 - 1 \cdot 1, \; 1 \cdot (-1) - 1 \cdot 1 )
$$

Therefore:

$$
\mathbf{v} = (2,0,-2)
$$

We can simplify it:

$$
\mathbf{v} = (1,0,-1)
$$

Now find one point on the line.

Set:

$$
z = 0
$$

Then the planes become:

$$
x + y = 6
$$

$$
x - y = 2
$$

Add the equations:

$$
2x = 8
$$

So:

$$
x = 4
$$

Then:

$$
y = 2
$$

So one point is:

$$
\mathbf{p}_0 = (4,2,0)
$$

Therefore, the line of intersection is:

$$
(x,y,z) = (4,2,0) + t(1,0,-1)
$$

or:

$$
x = 4 + t
$$

$$
y = 2
$$

$$
z = -t
$$

where

$$
t \in \mathbb{R}
$$

### Special Cases

Two planes do not always intersect in a line.

### Case 1: Same plane

If the two planes are actually the same plane, then their intersection is the whole plane.

This happens when their equations are proportional:

$$
(a_2,b_2,c_2,d_2) = \lambda(a_1,b_1,c_1,d_1)
$$

for some nonzero number $\lambda$.

### Case 2: Parallel different planes

If the normal vectors are proportional but the full equations are not, the planes are parallel and distinct.

That means: $\mathbf{n}_2 = \lambda \mathbf{n}_1$ but $d_2 \neq \lambda d_1$ Then there is no intersection:

$$
\Pi_1 \cap \Pi_2 = \varnothing
$$

### Case 3: Non-parallel planes

If the normal vectors are not proportional, then the planes intersect in a line.

Equivalently: $\mathbf{n}_1 \times \mathbf{n}_2 \neq \mathbf{0}$ Then: $\Pi_1 \cap \Pi_2 = L$ where $L$ is a line.

---

## 5. Projection onto the Normal Vector

The normal vector $\mathbf{n}$ is perpendicular to the hyperplane.

Given any vector $\mathbf{a}$ its projection onto $\mathbf{n}$ is the component of $\mathbf{a}$ that points perpendicular to the hyperplane:

$$
\text{proj}_{\mathbf{n}}(\mathbf{a}) = \frac{\mathbf{a} \cdot \mathbf{n}}{\mathbf{n} \cdot \mathbf{n}} \mathbf{n}
$$

The remaining part:

$$
\mathbf{a}_{\perp} = \mathbf{a} - \text{proj}_{\mathbf{n}}(\mathbf{a})
$$

lies parallel to the hyperplane.

This gives the decomposition:

$$
\mathbf{a} = \underbrace{\text{proj}_{\mathbf{n}}(\mathbf{a})}_{\text{perpendicular to hyperplane}} + \underbrace{\mathbf{a}_{\perp}}_{\text{parallel to hyperplane}}
$$

This is useful when splitting movement into a component toward the hyperplane and a component along it.

---

## 6. Distance from a Point to a Hyperplane

Given the hyperplane $\mathbf{n} \cdot \mathbf{x} = d$ and a point $\mathbf{p}$ the **signed distance** from the point to the hyperplane is: $\frac{\mathbf{n} \cdot \mathbf{p} - d}{\lvert \mathbf{n} \rvert}$ The **unsigned distance** is: $\frac{\lvert \mathbf{n} \cdot \mathbf{p} - d \rvert}{\lvert \mathbf{n} \rvert}$ **Why this formula works:**

The quantity $\mathbf{n} \cdot \mathbf{p} - d$ measures how far the point $\mathbf{p}$ is from satisfying the hyperplane equation.

Points on the hyperplane satisfy $\mathbf{n} \cdot \mathbf{x} = d$ so for them the numerator is zero.

The denominator $\lvert \mathbf{n} \rvert$ normalizes for the length of $\mathbf{n}$ so the result is the true geometric distance regardless of how long the normal vector is.

If $\lvert \mathbf{n} \rvert = 1$ the formula simplifies to: $\lvert \mathbf{n} \cdot \mathbf{p} - d \rvert$ **Example in 2D:**

The line $x + y = 3$ has normal vector $\mathbf{n} = (1, 1)$ and $d = 3$ The distance from point $\mathbf{p} = (4, 1)$ to this line is:

$$
\frac{\lvert (1,1) \cdot (4,1) - 3 \rvert}{\lvert (1,1) \rvert} = \frac{\lvert 5 - 3 \rvert}{\sqrt{2}} = \frac{2}{\sqrt{2}} = \sqrt{2}
$$
