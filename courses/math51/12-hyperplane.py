import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

fig = plt.figure(figsize=(12, 9), facecolor='white')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('white')

res = 30
xg = np.linspace(1.0, 7.0, res)
yg = np.linspace(0.0, 4.0, res)
X, Y = np.meshgrid(xg, yg)

Z1 = 6 - X - Y   # Π1: x+y+z=6
Z2 = 2 - X + Y   # Π2: x-y+z=2

ax.plot_surface(X, Y, Z1, alpha=0.30, color='royalblue', linewidth=0, antialiased=True)
ax.plot_surface(X, Y, Z2, alpha=0.30, color='tomato',    linewidth=0, antialiased=True)
ax.plot_wireframe(X, Y, Z1, alpha=0.12, color='royalblue', linewidth=0.6, rstride=3, cstride=3)
ax.plot_wireframe(X, Y, Z2, alpha=0.12, color='tomato',    linewidth=0.6, rstride=3, cstride=3)

# Intersection line: p = (4+t, 2, -t)
t = np.linspace(-2.8, 2.8, 300)
lx, ly, lz = 4+t, np.full_like(t, 2.0), -t
ax.plot(lx, ly, lz, color='black',   linewidth=6,   solid_capstyle='round', alpha=0.25)
ax.plot(lx, ly, lz, color='#F5C518', linewidth=3.5, solid_capstyle='round')

# Point p0 = (4, 2, 0)
ax.scatter([4], [2], [0], color='black', s=70, depthshade=False, zorder=5)
ax.text(4.15, 1.55, 0.25, r'$\mathbf{p}_0=(4,2,0)$', fontsize=11, color='black')

# Direction vector label
ax.text(6.6, 2.15, -2.7, r'$\mathbf{v}=(1,0,-1)$', fontsize=11, color='#9B7800')

# Normal n1 from (2, 1, 3) on Π1  (2+1+3=6 ✓)
nlen = 1.6
ax.quiver(2, 1, 3, 1, 1, 1, color='royalblue', linewidth=2.5,
          arrow_length_ratio=0.22, normalize=True, length=nlen)
ax.text(2.0, 2.2, 5.2, r'$\mathbf{n}_1=(1,1,1)$', fontsize=12, color='royalblue', fontweight='bold')

# Normal n2 from (3, 3, 2) on Π2  (3-3+2=2 ✓)
ax.quiver(3, 3, 2, 1, -1, 1, color='tomato', linewidth=2.5,
          arrow_length_ratio=0.22, normalize=True, length=nlen)
ax.text(4.5, 1.3, 3.7, r'$\mathbf{n}_2=(1,-1,1)$', fontsize=12, color='tomato', fontweight='bold')

ax.set_xlabel('$x$', fontsize=13, labelpad=6)
ax.set_ylabel('$y$', fontsize=13, labelpad=6)
ax.set_zlabel('$z$', fontsize=13, labelpad=6)
ax.set_xlim(1, 7)
ax.set_ylim(0, 4)
ax.set_zlim(-3, 5)
ax.tick_params(labelsize=10)
ax.set_title(r'Intersection of Two Planes in $\mathbb{R}^3$', fontsize=15, pad=14)

h1 = mpatches.Patch(facecolor='royalblue', alpha=0.5, label=r'$\Pi_1$: $x + y + z = 6$')
h2 = mpatches.Patch(facecolor='tomato',    alpha=0.5, label=r'$\Pi_2$: $x - y + z = 2$')
hl = mlines.Line2D([], [], color='#F5C518', linewidth=3.5, label=r'Intersection line $L$')
ax.legend(handles=[h1, h2, hl], loc='upper left', fontsize=12, framealpha=0.92)

ax.view_init(elev=22, azim=50)
plt.tight_layout()
plt.savefig('09-hyperplane.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
