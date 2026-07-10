# Level 0 – Mathematical Maturity

```text id="7ovpl6"
Sets
 ├── Functions
 ├── Relations
 ├── Logic
 └── Proof techniques
```

Topics:

* Sets
* Functions and mappings
* Composition
* Relations
* Equivalence relations
* Orders
* Proof by induction
* Contradiction
* Invariants

This level is often skipped, but later concepts like embeddings and transformers are full of functions and mappings.

---

# Level 1 – Linear Algebra

This is the most important foundation.

```text id="f2lkp8"
Vectors
 ├── Norms
 ├── Inner products
 ├── Projections
 └── Geometry
        ↓
Matrices
 ├── Linear transformations
 ├── Rank
 ├── Eigenvalues
 └── SVD
```

Topics:

1. Vectors
2. Matrix multiplication
3. Linear transformations
4. Basis and dimension
5. Rank
6. Dot product
7. Norms
8. Angles
9. Orthogonality
10. Projections
11. Eigenvalues
12. Eigenvectors
13. Positive semidefinite matrices
14. Singular Value Decomposition (SVD)

This entire section is used directly in BERT.

---

# Level 2 – Calculus

```text id="5i0moj"
Functions
     ↓
Derivatives
     ↓
Partial derivatives
     ↓
Gradients
     ↓
Chain Rule
```

Topics:

* Derivatives
* Partial derivatives
* Multivariable calculus
* Gradient
* Jacobian
* Hessian
* Chain rule
* Taylor expansion

Backpropagation is essentially repeated chain rule.

---

# Level 3 – Probability

```text id="1x3m7j"
Probability
 ├── Conditional probability
 ├── Bayes theorem
 ├── Random variables
 ├── Expectations
 └── Distributions
```

Topics:

* Random variables
* Joint distributions
* Conditional probability
* Independence
* Expectation
* Variance
* Covariance
* Gaussian distribution
* Entropy
* Cross entropy

BERT ultimately predicts probability distributions over tokens.

---

# Level 4 – Statistics

```text id="7v4q3r"
Sampling
     ↓
Estimation
     ↓
Bias/Variance
     ↓
Likelihood
```

Topics:

* Maximum likelihood
* Estimation
* Bias
* Variance
* Overfitting
* Regularization
* Evaluation metrics

---

# Level 5 – Optimization

```text id="zdf6j0"
Gradient
     ↓
Gradient Descent
     ↓
SGD
     ↓
Adam
```

Topics:

* Convexity
* Loss functions
* Gradient descent
* Stochastic gradient descent
* Momentum
* Adam
* Learning rates

BERT is trained using Adam.

---

# Level 6 – Classical Machine Learning

```text id="ybm6ka"
Features
 ├── Linear Regression
 ├── Logistic Regression
 ├── Trees
 ├── SVM
 └── Clustering
```

Topics:

* Feature engineering
* Train/test split
* Regression
* Classification
* Decision trees
* SVM
* PCA
* Clustering

This teaches what neural networks are replacing.

---

# Level 7 – Information Theory

```text id="p64a6z"
Entropy
     ↓
Cross Entropy
     ↓
KL Divergence
```

Topics:

* Entropy
* Information content
* Cross entropy
* KL divergence
* Mutual information

Cross entropy is literally BERT's training loss.

---

# Level 8 – NLP Foundations

```text id="t8s7bi"
Text
 ├── Tokenization
 ├── Stemming
 ├── Lemmatization
 ├── N-grams
 └── Language Models
```

Topics:

* Corpus
* Vocabulary
* Tokens
* Zipf's law
* Bag of words
* TF-IDF
* N-grams
* Statistical language models

---

# Level 9 – Word Embeddings

```text id="7rll4j"
One-hot vectors
       ↓
Distributed representations
       ↓
Word2Vec
       ↓
GloVe
```

Topics:

* Distributional hypothesis
* Embedding space
* Similarity
* Cosine similarity
* Skip-gram
* CBOW
* Negative sampling

This is where "meaning becomes geometry."

---

# Level 10 – Neural Networks

```text id="n4l7op"
Perceptron
      ↓
MLP
      ↓
Backpropagation
```

Topics:

* Neurons
* Activation functions
* Forward pass
* Backpropagation
* Loss functions
* Batch normalization
* Dropout

---

# Level 11 – Deep Learning

Topics:

* Representation learning
* Universal approximation
* Embedding layers
* GPU computation
* Mini-batches
* Initialization

---

# Level 12 – Sequence Models

```text id="pjlwmx"
RNN
 ├── LSTM
 └── GRU
```

Topics:

* Hidden state
* Sequence processing
* Vanishing gradients
* Long-term dependencies

You need these to appreciate why Transformers were revolutionary.

---

# Level 13 – Attention

This is the bridge to BERT.

Topics:

* Query
* Key
* Value
* Attention weights
* Softmax
* Self-attention

The central equation is:

```text id="tn4kmf"
Attention(Q,K,V)
       =
softmax(QKᵀ/√d)V
```

Understanding this equation is almost understanding Transformers.

---

# Level 14 – Transformer Architecture

```text id="gj42zm"
Embeddings
      ↓
Positional Encoding
      ↓
Multi-Head Attention
      ↓
Feed Forward
      ↓
Residual Connections
      ↓
Layer Normalization
```

Topics:

* Encoder
* Decoder
* Multi-head attention
* Residual connections
* Layer normalization
* Positional embeddings

---

# Level 15 – BERT

Finally:

```text id="91kjcc"
Transformer Encoder
        +
Masked Language Modeling
        +
Next Sentence Prediction
        =
BERT
```

Topics:

* Encoder-only transformer
* Bidirectional context
* WordPiece tokenization
* Masked Language Modeling
* Pretraining
* Fine-tuning
* CLS token
* Sentence embeddings
* Pooling strategies

---

# Level 16 – Post-BERT

```text id="tmohxj"
BERT
 ├── RoBERTa
 ├── ALBERT
 ├── DeBERTa
 ├── SBERT
 ├── E5
 └── Modern LLMs
```

---

# Entire dependency graph

```text id="6sxv8r"
Math Foundations
        ↓
Linear Algebra
        ↓
Calculus
        ↓
Probability & Statistics
        ↓
Optimization
        ↓
Classical ML
        ↓
Information Theory
        ↓
Classical NLP
        ↓
Word Embeddings
        ↓
Neural Networks
        ↓
Deep Learning
        ↓
RNN/LSTM
        ↓
Attention
        ↓
Transformers
        ↓
BERT
        ↓
Modern Embedding Models and LLMs
```

If your specific target is **"I want to understand every equation inside BERT and be able to implement it from scratch"**, then the minimum non-skippable prerequisites are:

1. Linear Algebra
2. Multivariable Calculus
3. Probability
4. Optimization
5. Information Theory
6. Neural Networks
7. Attention
8. Transformers
9. BERT

Everything else enriches intuition, but these nine blocks are the true backbone.
