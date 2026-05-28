# Five-Year Magister Course — Formal CS, PL, and Modern Reasoning AI

This is a polished five-year curriculum for a strong computer science magister program.
The spine is deliberately not “AI first”. It builds the habits that make advanced AI work possible:

* mathematical maturity,
* disciplined programming,
* systems understanding,
* semantics and type-level reasoning,
* symbolic reasoning,
* machine learning,
* modern language models and interpretability,
* research-level project work.

## Professor's stance

After 20 years of teaching, I would not design this program as a sequence of fashionable technologies.
Students should graduate with durable intellectual machinery: proof, abstraction, implementation, experimentation, and judgment.

The central teaching principle is:

* every theoretical course must have hard exercises,
* every systems course must have a real artifact,
* every AI course must include reproducible experiments,
* every advanced course must require reading primary sources,
* every year must end with a project that exposes whether the knowledge is actually usable.

The curriculum should produce graduates who can:

* read and implement research papers,
* design correct abstractions,
* build compilers, solvers, and ML systems,
* reason about uncertainty and computation,
* connect symbolic and neural approaches,
* evaluate frontier AI claims critically.

---

# Year 1 — Programming, Discrete Thinking, and Mathematical Discipline

Goal: move students from “can code” to “can reason about programs”.

## 1. Programming Methodology and Abstractions

Core:

* Python or Java for first programming methodology.
* C++ or similar for data structures and abstraction.
* recursion, ADTs, memory models at an introductory level.

Classic/practice links:

* [Stanford CS106A Programming Methodology](https://web.stanford.edu/class/cs106a/)
* [Stanford CS106B Programming Abstractions](https://web.stanford.edu/class/cs106b/)
* [Stanford CS106L Standard C++ Programming](https://web.stanford.edu/class/cs106l/)

Assignments:

* implement recursion-heavy search problems,
* build custom containers,
* write a small interpreter for arithmetic expressions,
* complete weekly programming labs with tests.

## 2. Mathematical Foundations of Computing

Core:

* logic,
* proof techniques,
* induction,
* invariants,
* sets and relations,
* recursion,
* graphs,
* counting.

Classic/practice links:

* [Stanford CS103 Mathematical Foundations of Computing](https://web.stanford.edu/class/cs103/)
* [CS103 Spring 2026 lectures/archive](https://web.stanford.edu/class/archive/cs/cs103/cs103.1266/lectures/)
* [MIT 6.042J Mathematics for Computer Science, OCW assignments](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/pages/assignments/)
* [MIT Open Learning Library 6.042J](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/course/)
* [Mathematics for Computer Science, Lehman/Leighton/Meyer](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf)

Assignments:

* weekly proof sets,
* induction proof portfolio,
* invariant-based correctness proofs,
* graph modeling problems.

## 3. Linear Algebra, Multivariable Calculus, and Numerical Thinking

Core:

* vectors and matrices,
* linear transformations,
* eigenvalues and eigenvectors,
* orthogonality,
* SVD,
* gradients,
* Jacobians,
* Hessians,
* numerical stability.

Classic/practice links:

* [MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
* [Stanford Math 51 Linear Algebra and Multivariable Calculus](https://web.stanford.edu/class/math51)
* [Stanford CS205L Continuous Mathematical Methods with an Emphasis on Machine Learning](https://web.stanford.edu/class/cs205l/)
* [CS205L assignments](https://web.stanford.edu/class/cs205l/assignments.html)

Assignments:

* implement matrix operations and decompositions,
* derive gradients for simple models,
* compare analytical and automatic differentiation,
* run numerical stability experiments.

Year 1 checkpoint:

* students must be able to write readable programs and rigorous elementary proofs.

---

# Year 2 — Algorithms, Systems, and Computation

Goal: make students fluent in algorithmic and machine-level thinking before advanced AI.

## 4. Data Structures and Algorithms

Core:

* asymptotic analysis,
* divide and conquer,
* dynamic programming,
* greedy algorithms,
* graph algorithms,
* randomized algorithms,
* lower-bound intuition.

Classic/practice links:

* [Stanford CS161 Design and Analysis of Algorithms](https://web.stanford.edu/class/cs161/)
* [Stanford CS166 Data Structures](https://web.stanford.edu/class/cs166/)
* [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

Assignments:

* implement core data structures,
* prove algorithm correctness,
* analyze complexity,
* solve graph and dynamic-programming projects.

## 5. Computer Systems

Core:

* C,
* memory,
* assembly basics,
* processes,
* concurrency,
* file systems,
* networking basics.

Classic/practice links:

* [Stanford CS107 Computer Organization and Systems](https://web.stanford.edu/class/cs107/)
* [Stanford CS110 Principles of Computer Systems](https://web.stanford.edu/class/cs110/summer-2021/)
* [Stanford CS107E Computer Systems from the Ground Up](https://cs107e.github.io/)

Assignments:

* implement malloc-like memory management,
* write shell/process exercises,
* build concurrent programs,
* debug with sanitizers and profilers.

## 6. Theory of Computation

Core:

* formal languages,
* automata,
* grammars,
* computability,
* Turing machines,
* decidability,
* complexity foundations.

Classic/practice links:

* [Stanford CS154 Introduction to Automata and Complexity Theory](https://theory.stanford.edu/~liyang/teaching/computability.html)
* [CS154 lecture videos/slides by Omer Reingold](https://omereingold.wordpress.com/cs154/)
* [Michael Sipser, Introduction to the Theory of Computation](https://www.cengage.com/c/introduction-to-the-theory-of-computation-3e-sipser/)

Assignments:

* design automata and grammars,
* prove undecidability reductions,
* implement small parsers,
* connect regular/context-free languages to tokenization and syntax.

Year 2 checkpoint:

* students must understand computation both as machine execution and as a mathematical object.

---

# Year 3 — Compilers, Programming Languages, and Formal Semantics

Goal: make abstraction operational. Students should not merely use languages; they should understand how languages mean things.

## 7. Compilers

Core:

* lexical analysis,
* parsing,
* ASTs,
* semantic analysis,
* type checking,
* intermediate representations,
* optimization,
* code generation.

Classic/practice links:

* [Stanford CS143 Compilers](https://web.stanford.edu/class/cs143/)
* [CMU 15-411 Compiler Design](https://www.cs.cmu.edu/~rjsimmon/15411-f15/)
* [Crafting Interpreters](https://craftinginterpreters.com/)
* [Nand2Tetris projects](https://www.nand2tetris.org/course)

Assignments:

* build a lexer and parser,
* implement a type checker,
* compile a small language to bytecode or native code,
* add one optimization pass and measure it.

## 8. Programming Language Theory

Core:

* operational semantics,
* denotational intuition,
* lambda calculus,
* type systems,
* polymorphism,
* inference,
* type safety.

Classic/practice links:

* [Stanford CS242 Programming Languages](https://web.stanford.edu/class/cs242/)
* [CS242 Fall 2018 assignments](https://stanford-cs242.github.io/f18/assignments/)
* [CMU 15-312 Principles of Programming Languages](https://www.andrew.cmu.edu/course/15-312/)
* [Types and Programming Languages official page](https://www.cis.upenn.edu/~bcpierce/typesbook/)
* [TAPL implementations and resources](https://www.cis.upenn.edu/~bcpierce/tapl/)
* [Practical Foundations for Programming Languages](https://www.cs.cmu.edu/~rwh/pfpl/)

Assignments:

* implement interpreters for several calculi,
* prove preservation and progress for a small typed language,
* implement Hindley-Milner type inference,
* compare dynamic, static, and gradual typing.

Selected compositionality module:

* category theory for programmers,
* functors, applicatives, monads,
* algebraic structure in program design,
* denotational semantics as compositional meaning.

Module links:

* [Category Theory for Programmers](https://github.com/hmemcpy/milewski-ctfp-pdf)
* [Seven Sketches in Compositionality](https://arxiv.org/abs/1803.05316)
* [Applied Category Theory course material](https://www.appliedcategorytheory.org/school/)

Module assignment:

* model a small typed DSL using compositional semantics,
* implement its interpreter,
* prove or test that interpretation respects substitution.

## 9. Proof Assistants and Mechanized Metatheory

Core:

* propositions as types,
* Curry-Howard correspondence,
* inductive definitions,
* formal proofs,
* executable specifications,
* proof automation basics.

Classic/practice links:

* [Software Foundations](https://softwarefoundations.cis.upenn.edu/)
* [Programming Language Foundations in Agda](https://plfa.github.io/)
* [Theorem Proving in Lean 4](https://lean-lang.org/theorem_proving_in_lean4/)
* [Natural Number Game](https://adam.math.hhu.de/#/g/leanprover-community/nng4)

Assignments:

* formalize arithmetic and list proofs,
* mechanize a small-step semantics,
* prove type safety for a toy language,
* write a short proof-engineering report.

Year 3 checkpoint:

* students must be able to build a language implementation and explain its semantics formally.

---

# Year 4 — Symbolic Reasoning, Information, and Machine Learning

Goal: connect formal reasoning with probabilistic learning.

## 10. Logic Programming and Computational Logic

Core:

* Prolog,
* Datalog,
* Horn clauses,
* unification,
* resolution,
* knowledge representation,
* rule-based inference.

Classic/practice links:

* [Stanford CS151 Logic Programming](https://logicprogramming.stanford.edu/)
* [Stanford CS157 Computational Logic](https://intrologic.stanford.edu/)
* [Learn Datalog interactive tutorial](https://learn-some.com/)
* [The Art of Prolog](https://mitpress.mit.edu/9780262193382/the-art-of-prolog/)

Assignments:

* implement unification,
* write Prolog/Datalog analyzers,
* model dependency graphs and inference rules,
* build a symbolic query engine.

## 11. SAT, SMT, and Formal Methods

Core:

* SAT,
* DPLL and CDCL,
* SMT theories,
* constraint modeling,
* verification,
* solver-aided programming.

Classic/practice/state-of-the-art links:

* [Stanford CS357 Advanced Topics in Formal Methods](https://web.stanford.edu/class/cs357/)
* [Automated Reasoning: satisfiability](https://www.coursera.org/learn/automated-reasoning-sat)
* [Z3 Guide](https://microsoft.github.io/z3guide/)
* [Handbook of Satisfiability](https://ebooks.iospress.nl/volume/handbook-of-satisfiability-second-edition)

Assignments:

* encode Sudoku, scheduling, and graph coloring as SAT/SMT,
* implement a small DPLL solver,
* use Z3 for program verification,
* compare solver encodings experimentally.

## 12. Probability, Statistics, and Information Theory

Core:

* probability spaces,
* distributions,
* expectation,
* Bayes rule,
* estimation,
* entropy,
* KL divergence,
* mutual information,
* coding theory.

Formula spine:

```text
H(X) = -sum_x p(x) log p(x)
D_KL(P || Q) = sum_x P(x) log(P(x) / Q(x))
```

Classic/practice links:

* [Stanford CS109 Probability for Computer Scientists](https://cs109.stanford.edu/)
* [MIT 6.441 Information Theory assignments](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/resources/assignments/)
* [Stanford EE376A Information Theory](https://web.stanford.edu/class/ee376a/)
* [Elements of Information Theory, Cover and Thomas](https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959)
* [UMass CS650 Applied Information Theory](https://people.cs.umass.edu/~arya/courses/650/CS650-2016.html)

Assignments:

* derive common estimators,
* compute entropy/KL for real datasets,
* implement compression experiments,
* connect cross-entropy loss to coding and likelihood.

## 13. Optimization for Machine Learning

Core:

* gradient descent,
* stochastic optimization,
* convexity,
* duality,
* constrained optimization,
* automatic differentiation,
* numerical conditioning.

Classic/practice links:

* [Stanford EE364A Convex Optimization](https://web.stanford.edu/class/ee364a/)
* [Stanford Engineering Everywhere EE364A](https://see.stanford.edu/Course/EE364A)

Assignments:

* implement gradient descent, momentum, and Adam-like optimizers,
* solve convex programs with CVX-style tools,
* derive KKT conditions for small problems,
* compare optimization behavior across loss landscapes.

## 14. Machine Learning Foundations

Core:

* supervised learning,
* optimization,
* bias/variance,
* generalization,
* probabilistic models,
* kernel methods,
* neural networks,
* evaluation methodology.

Classic/practice links:

* [Stanford CS229 Machine Learning](https://cs229.stanford.edu/)
* [Stanford CS229M Statistical Learning Theory](https://web.stanford.edu/class/cs229m/)
* [Stanford CS231N Convolutional Neural Networks for Visual Recognition](https://cs231n.stanford.edu/)

Assignments:

* implement linear/logistic regression from scratch,
* implement backpropagation,
* train and evaluate neural networks,
* reproduce a small published result.

Year 4 checkpoint:

* students must be able to use both symbolic solvers and statistical models, and know when each paradigm is appropriate.

---

# Year 5 — Frontier AI, Interpretability, and Research

Goal: turn the previous four years into research capacity.

## 15. Deep Learning for Language and LLMs

Core:

* embeddings,
* sequence models,
* attention,
* transformers,
* tokenization,
* pretraining,
* fine-tuning,
* evaluation,
* scaling laws,
* data pipelines.

Practice/state-of-the-art links:

* [Stanford CS224N Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/)
* [Stanford CS336 Language Modeling from Scratch](https://cs336.stanford.edu/)
* [Stanford CS25 Transformers United](https://web.stanford.edu/class/cs25/)

Assignments:

* implement a tokenizer,
* implement a small transformer,
* train a tiny language model,
* evaluate hallucination and calibration,
* reproduce a small scaling-law experiment.

## 16. Neuro-Symbolic AI and Agents

Core:

* symbolic + neural hybrids,
* differentiable logic,
* tool use,
* planning,
* retrieval,
* structured memory,
* program synthesis,
* constrained generation.

State-of-the-art/practice links:

* [CMU 10-747 Neuro-Symbolic AI](https://www.cs.cmu.edu/~pradeepr/747)
* [Neurosymbolic Programming seminar](https://neurosymbolic.metareflection.club/syllabus.html)
* [Berkeley CS294/194-196 Large Language Model Agents](https://rdi.berkeley.edu/llm-agents/f24)

Assignments:

* build a tool-using agent with a restricted action space,
* combine an LLM with a solver,
* use Datalog or SMT for constrained reasoning,
* evaluate failures with adversarial tasks.

## 17. Mechanistic Interpretability and AI Safety

Core:

* activation analysis,
* circuits,
* probing,
* representation geometry,
* sparse autoencoders,
* model editing,
* evaluation and red-teaming,
* safety cases.

State-of-the-art/practice links:

* [ARENA Transformer Interpretability](https://learn.arena.education/chapter1_transformer_interp/02_intro_mech_interp/)
* [ARENA circuits in LLMs](https://learn.arena.education/chapter1_transformer_interp/21_ioi/)
* [CS221M Interpretability](https://cs221m.github.io/)

Assignments:

* use TransformerLens on a small model,
* reproduce induction-head analysis,
* train or analyze a small sparse autoencoder,
* write a safety evaluation report.

## 18. Research Seminar and Magister Thesis

Core:

* paper reading,
* experimental design,
* artifact evaluation,
* ablation studies,
* reproducibility,
* academic writing,
* thesis defense.

Assignments:

* weekly paper presentations,
* one replication study,
* one original research prototype,
* thesis proposal,
* final magister thesis.

Thesis directions:

* typed DSL for agent tools,
* solver-aided constrained generation,
* mechanistic analysis of toy reasoning models,
* Datalog memory for LLM agents,
* proof assistant support for program synthesis,
* homotopy type theory or dependent type theory formalization project,
* compiler techniques for ML systems,
* information-theoretic analysis of representations.

Year 5 checkpoint:

* students must produce a defensible thesis with code, evaluation, and a clear relation to existing research.

---

# Critical Ordering Rules

1. Do not teach deep learning before probability, linear algebra, multivariable calculus, and optimization are usable.
2. Do not teach LLM agents before students understand compilers, semantics, and systems.
3. Do not teach mechanistic interpretability as visualization; teach it as causal reverse engineering.
4. Do not treat proof assistants as optional decoration; they are the cleanest bridge between PL, logic, and trustworthy AI.
5. Do not let projects become demos only; every project needs tests, evaluation, and a written argument.
6. Do not overload Year 5 with fundamentals; it must be a research year.

---

# Practical Assignment Spine

This is the minimum practical path through the full program:

1. CS106B-style recursive programming project.
2. CS103 or MIT 6.042J proof sets.
3. MIT 18.06 or Stanford Math 51 linear algebra/calculus assignments.
4. CS161-style algorithm implementation and proof portfolio.
5. CS107/CS110 systems labs.
6. CS154 automata and computability homework.
7. CS143 or CMU 15-411 compiler project.
8. CS242 interpreter/type-checker assignments.
9. Software Foundations, PLFA, or Lean formalization exercises.
10. Prolog/Datalog symbolic reasoning project.
11. Z3/SAT/SMT verification project.
12. MIT 6.441 information theory problem sets.
13. EE364A or CS205L optimization assignments.
14. CS229 ML implementations.
15. CS224N or CS336 transformer implementation.
16. ARENA interpretability exercises.
17. Year-long magister thesis.

---
