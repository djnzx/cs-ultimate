# Markov Chains

A **Markov chain** is a system that moves between a set of **states** over time, where the next state depends only on the current state — not on the history of how the system got there.

This is called the **Markov property**:

$$
P(\text{state at time } t+1 \mid \text{all past states}) = P(\text{state at time } t+1 \mid \text{state at time } t)
$$

The past is summarized entirely by the present.

---

## 1. States and Transitions

Suppose the system has $n$ possible states: $s_1, s_2, \dots, s_n$ At each time step the system moves from the current state to some next state.

The probability of moving from state $s_j$ to state $s_i$ is written: $A_{ij} = P(\text{next state} = s_i \mid \text{current state} = s_j)$ These probabilities satisfy:

$$
A_{ij} \geq 0 \qquad \text{and} \qquad \sum_{i=1}^{n} A_{ij} = 1 \quad \text{for each } j
$$

Each column of $A$ sums to 1 because from any state, the chain must go somewhere.

A matrix with this property is called **column-stochastic**.

---

## 2. Transition Matrix

The full collection of transition probabilities forms the **transition matrix**:

$$
A =
\begin{bmatrix}
A_{11} & A_{12} & \cdots & A_{1n} \\
A_{21} & A_{22} & \cdots & A_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
A_{n1} & A_{n2} & \cdots & A_{nn}
\end{bmatrix}
$$

where column $j$ gives the probability distribution over next states when the current state is $s_j$.

**Example:** a weather model with two states, Sunny ($s_1$) and Rainy ($s_2$):

$$
A =
\begin{bmatrix}
0.8 & 0.4 \\
0.2 & 0.6
\end{bmatrix}
$$

Reading column 1: if today is Sunny, tomorrow is Sunny with probability $0.8$ and Rainy with probability $0.2$.

Reading column 2: if today is Rainy, tomorrow is Sunny with probability $0.4$ and Rainy with probability $0.6$.

---

## 3. State Vector

Instead of tracking a single definite state, we track a **probability distribution** over all states.

The **state vector** at time $t$ is:

$$
\mathbf{\pi}^{(t)} =
\begin{bmatrix}
\pi^{(t)}_1 \\
\pi^{(t)}_2 \\
\vdots \\
\pi^{(t)}_n
\end{bmatrix}
$$

where: $\pi^{(t)}_i = P(\text{system is in state } s_i \text{ at time } t)$ Since the entries are probabilities:

$$
\pi^{(t)}_i \geq 0 \qquad \text{and} \qquad \sum_{i=1}^{n} \pi^{(t)}_i = 1
$$

The state vector is a probability distribution over states.

---

## 4. Evolution Over Time

Given the current state vector, the next state vector is obtained by multiplying by the transition matrix: $\mathbf{\pi}^{(t+1)} = A\, \mathbf{\pi}^{(t)}$ This is a linear transformation: the transition matrix maps one probability distribution to the next.

**Example (continuing the weather model):**

Suppose today is definitely Sunny:

$$
\mathbf{\pi}^{(0)} =
\begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

Then tomorrow:

$$
\mathbf{\pi}^{(1)}
= A\,\mathbf{\pi}^{(0)}
$$

$$
\mathbf{\pi}^{(1)} =
\begin{bmatrix}
0.8 \\
0.2
\end{bmatrix}
$$

After two days:

$$
\mathbf{\pi}^{(2)}
= A\,\mathbf{\pi}^{(1)}
$$

$$
\mathbf{\pi}^{(2)} =
\begin{bmatrix}
0.72 \\
0.28
\end{bmatrix}
$$

After $k$ steps from an initial distribution $\mathbf{\pi}^{(0)}$:

$$
\mathbf{\pi}^{(k)} = A^k\, \mathbf{\pi}^{(0)}
$$

---

## 5. Stationary Distribution

A **stationary distribution** is a state vector $\mathbf{\pi}^{\ast}$ that does not change when the transition matrix is applied: $A\, \mathbf{\pi}^{\ast} = \mathbf{\pi}^{\ast}$ Once the chain reaches $\mathbf{\pi}^{\ast}$, it stays there in expectation.

This equation says that $\mathbf{\pi}^{\ast}$ is an **eigenvector of $A$ with eigenvalue 1**.

For the weather example, solving:

$$
A =
\begin{bmatrix}
0.8 & 0.4 \\
0.2 & 0.6
\end{bmatrix}
$$

The stationary equation is:

$$
A\mathbf{\pi}^{\ast} = \mathbf{\pi}^{\ast}
$$

gives:

$$
\mathbf{\pi}^{\ast} =
\begin{bmatrix}
2/3 \\
1/3
\end{bmatrix}
$$

Regardless of the starting state, the chain converges to this distribution: in the long run, $2/3$ of days are Sunny and $1/3$ are Rainy.

---

## 6. Convergence

For many Markov chains, repeated application of $A$ causes the state vector to converge to the stationary distribution from any starting point: $\lim_{k \to \infty} A^k\, \mathbf{\pi}^{(0)} = \mathbf{\pi}^{\ast}$ This happens when the chain is **ergodic**: every state is reachable from every other state, and the chain is not stuck in cycles.

The convergence is governed by the second-largest eigenvalue of $A$.

Let the eigenvalues be: $\lambda_1 = 1 \geq \lvert \lambda_2 \rvert \geq \lvert \lambda_3 \rvert \geq \cdots \geq \lvert \lambda_n \rvert$ Every column-stochastic matrix has $\lambda_1 = 1$.

The speed of convergence depends on: $\lvert \lambda_2 \rvert$ When $\lvert \lambda_2 \rvert$ is close to 1, convergence is slow.

When $\lvert \lambda_2 \rvert$ is far from 1 (close to 0), convergence is fast.

The gap: $1 - \lvert \lambda_2 \rvert$ is called the **spectral gap** and directly controls how quickly the chain mixes.

---

## 7. Use case: PageRank

**PageRank** (the algorithm behind Google's original search engine) is a direct application of Markov chains.

Model: a web surfer follows links at random.

States: web pages.

Transitions: from a page, choose a link uniformly at random.

The transition matrix $A$ encodes which pages link to which.

The **stationary distribution** $\mathbf{\pi}^{\ast}$ of this chain gives the PageRank score of each page: $A\, \mathbf{\pi}^{\ast} = \mathbf{\pi}^{\ast}$ Pages that are linked to from many important pages have high probability in $\mathbf{\pi}^{\ast}$ and are ranked higher.

PageRank is computed by iterating: $\mathbf{\pi}^{(t+1)} = A\, \mathbf{\pi}^{(t)}$ until convergence, which is equivalent to finding the principal eigenvector of $A$.

---

## 8. Use case: language models

The simplest probabilistic language model is a **Markov model over words**.

States: words (or characters, or tokens) in a vocabulary.

Transitions: $A_{ij}$ = probability that word $s_i$ follows word $s_j$ in text.

This is a **bigram model**: the probability of the next word depends only on the current word.

Given a starting word, we can generate text by sampling from the chain repeatedly.

Modern language models (transformers) are more powerful because they condition on a long context, not just one previous token — but the Markov model is the foundational idea that motivates the probabilistic treatment of sequences.

---

## 9. Use case: Hidden Markov Models (HMMs)

In a **Hidden Markov Model**, the true state of the system is not directly observable.

There are two processes:

1. A Markov chain over **hidden states** $z_1, z_2, z_3, \dots$:

$$
P(z_{t+1} \mid z_t)
$$

2. An **emission process** that produces observations $x_1, x_2, x_3, \dots$ based on the hidden state:

$$
P(x_t \mid z_t)
$$

We observe $x_1, x_2, \dots$ but not $z_1, z_2, \dots$.

The goal is to infer the hidden states from the observations.

**Applications:**
- Speech recognition (hidden states = phonemes, observations = audio features)
- Part-of-speech tagging (hidden states = grammatical tags, observations = words)
- Genomics (hidden states = biological regions, observations = DNA bases)

HMMs were the dominant approach in speech recognition before deep learning replaced them.

---

## 10. Use case: Markov Decision Processes and Reinforcement Learning

A **Markov Decision Process (MDP)** extends a Markov chain by adding an **agent** that takes **actions**.

Components:
- States $s \in S$
- Actions $a \in A$
- Transition probabilities: $P(s' \mid s, a)$ — next state depends on current state and action
- Rewards: $R(s, a)$
- Discount factor: $\gamma \in [0, 1)$

The agent's goal is to find a **policy** $\pi(a \mid s)$ that maximizes expected cumulative reward.

**Reinforcement learning** algorithms like Q-learning and policy gradient solve MDPs.

The Markov property is what makes this tractable: since the future depends only on the current state, the value of a state: $V^\pi(s) = \mathbb{E}\left[\sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \;\Big|\; s_0 = s, \pi\right]$ satisfies the **Bellman equation**:

$$
V^\pi(s) = \sum_a \pi(a \mid s) \left[ R(s, a) + \gamma \sum_{s'} P(s' \mid s, a)\, V^\pi(s') \right]
$$

This recursive equation over states is only possible because of the Markov property.

---

## 11. Use case: MCMC — sampling from complex distributions

**Markov Chain Monte Carlo (MCMC)** is a technique for drawing samples from a probability distribution $p(x)$ that is hard to sample from directly.

The idea: construct a Markov chain whose **stationary distribution is exactly $p(x)$**, then run the chain long enough to converge.

Once converged, the chain's samples are approximately distributed as $p(x)$.

**Metropolis-Hastings** is the classical algorithm:
1. From current state $x$, propose a candidate $x'$.
2. Accept $x'$ with probability $\min\left(1,\, \dfrac{p(x')}{p(x)}\right)$.
3. Otherwise stay at $x$.

The resulting chain has $p$ as its stationary distribution.

MCMC is widely used in Bayesian inference, where the posterior distribution over model parameters: $p(\theta \mid \text{data}) \propto p(\text{data} \mid \theta)\, p(\theta)$ is often intractable to compute analytically but can be sampled using MCMC.

---

## 12. Summary

A **Markov chain** is a system that transitions between states with probabilities that depend only on the current state.

The transition matrix $A$ (column-stochastic) governs evolution: $\mathbf{\pi}^{(t+1)} = A\, \mathbf{\pi}^{(t)}$ The **stationary distribution** $\mathbf{\pi}^{\ast}$ satisfies: $A\, \mathbf{\pi}^{\ast} = \mathbf{\pi}^{\ast}$ This is an eigenvector equation: $\mathbf{\pi}^{\ast}$ is the eigenvector of $A$ corresponding to eigenvalue $1$.

Convergence speed is controlled by the **spectral gap** $1 - \lvert \lambda_2 \rvert$.

Key ML applications:

| Application | Role of Markov chain |
|---|---|
| PageRank | Stationary distribution = page importance |
| Language models | Transition probabilities over tokens |
| HMMs | Hidden state sequence with observed emissions |
| Reinforcement learning | MDP: Markov transitions + rewards + policy |
| MCMC | Designed chain whose stationary distribution is the target |

The stationary distribution and convergence analysis of Markov chains are best understood through the lens of **eigenvectors**, covered in the previous section.
