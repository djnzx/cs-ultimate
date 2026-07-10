import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu1 = 15
mu2 = 8
variance = 50
sigma = np.sqrt(variance)

bar_x = 14
output_file = "normal_distributions.png"

# Normal PDF without scipy
def normal_pdf(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x - mu) / sigma) ** 2
    )

# X range wide enough for both distributions
x = np.linspace(mu2 - 4 * sigma, mu1 + 4 * sigma, 1000)

y1 = normal_pdf(x, mu1, sigma)
y2 = normal_pdf(x, mu2, sigma)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(x, y1, label=r"$N_1(\mu=15,\ \sigma^2=50)$")
plt.plot(x, y2, label=r"$N_2(\mu=8,\ \sigma^2=50)$")

# Vertical bar at x = 14
plt.axvline(bar_x, linestyle="--", linewidth=2, label="bar at x = 14")

plt.text(
    bar_x,
    max(y1.max(), y2.max()) * 0.95,
    "x = 14",
    rotation=90,
    va="top",
    ha="right",
    )

plt.title("Two Normal Distributions with Bar at x = 14")
plt.xlabel("x")
plt.ylabel("density")
plt.grid(True, alpha=0.3)
plt.legend()

# Save PNG
plt.savefig(output_file, dpi=300, bbox_inches="tight")

# Optional: show after saving
plt.show()