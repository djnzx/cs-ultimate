# PHASE A — Formal reasoning foundations

Insert after:

* CS106B
* before heavy ML.

---

## A1. CS103

Already essential.

Covers:

* logic,
* proof techniques,
* induction,
* recursion,
* mathematical abstraction.

This is the first true “formal thinking” course.

Links:

* classic/practice: [Stanford CS103 Mathematical Foundations of Computing](https://web.stanford.edu/class/cs103/)
* practice: [CS103 Spring 2026 lectures/archive](https://web.stanford.edu/class/archive/cs/cs103/cs103.1266/lectures/)
* practice: [CS103 archived assignments](https://web.stanford.edu/class/archive/cs/cs103/cs103.1192/)

---

## A2. Mathematics for Computer Science (MIT)

Topics:

* invariants,
* recursive reasoning,
* asymptotics,
* graph reasoning,
* formal proofs.

This improves the ability to:

* read papers,
* reason rigorously,
* understand correctness.

Links:

* classic/practice: [MIT 6.042J Mathematics for Computer Science, OCW assignments](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/pages/assignments/)
* practice: [MIT Open Learning Library 6.042J](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/course/)
* classic text: [Mathematics for Computer Science, Lehman/Leighton/Meyer](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf)

---

# PHASE B — Computability and symbolic systems

Insert BEFORE advanced ML.

---

## B1. CS154

Core topics:

* formal languages,
* automata,
* grammars,
* computability,
* Turing machines,
* decidability.

This is foundational for:

* symbolic reasoning,
* parsing,
* tokenization,
* constrained generation,
* program synthesis.

This course teaches what “computation” formally means.

Links:

* classic/practice: [Stanford CS154 Introduction to Automata and Complexity Theory](https://theory.stanford.edu/~liyang/teaching/computability.html)
* classic: [CS154 lecture videos/slides by Omer Reingold](https://omereingold.wordpress.com/cs154/)
* classic text: [Michael Sipser, Introduction to the Theory of Computation](https://www.cengage.com/c/introduction-to-the-theory-of-computation-3e-sipser/)

---

## B2. Compilers

Examples:

* CS143
* CMU compilers
* Cornell compilers

Topics:

* ASTs,
* semantic analysis,
* type checking,
* transformations,
* optimization.

Massively useful for:

* structured generation,
* DSLs,
* code LLMs,
* symbolic systems.

Links:

* classic/practice: [Stanford CS143 Compilers](https://web.stanford.edu/class/cs143/)
* classic/practice: [CMU 15-411 Compiler Design](https://www.cs.cmu.edu/~rjsimmon/15411-f15/)
* practice: [Crafting Interpreters](https://craftinginterpreters.com/)
* practice: [Nand2Tetris projects](https://www.nand2tetris.org/course)

---

# PHASE C — Semantics and type-level thinking

This is where things become VERY interesting.

Insert after:

* CS154,
* before frontier AI.

---

## C1. Programming Language Theory

Examples:

* CS242
* CMU 15-312

Topics:

* operational semantics,
* denotational semantics,
* lambda calculus,
* type systems,
* polymorphism,
* inference.

This is the heart of:

* compositionality,
* symbolic abstraction,
* semantic modeling.

Links:

* classic/practice: [Stanford CS242 Programming Languages](https://web.stanford.edu/class/cs242/)
* practice: [CS242 Fall 2018 assignments](https://stanford-cs242.github.io/f18/assignments/)
* classic/practice: [CMU 15-312 Principles of Programming Languages](https://www.andrew.cmu.edu/course/15-312/)
* classic/practice: [Software Foundations](https://softwarefoundations.cis.upenn.edu/)

---

## C2. *Types and Programming Languages* — Benjamin Pierce

Probably the single best bridge from:

* engineering
  to
* formal computational semantics.

Topics:

* simply typed lambda calculus,
* System F,
* subtyping,
* recursive types,
* type safety.

This directly develops:

* type-level thinking,
* semantic abstraction,
* compositional reasoning.

Links:

* classic text: [Types and Programming Languages official page](https://www.cis.upenn.edu/~bcpierce/typesbook/)
* practice: [TAPL implementations and resources](https://www.cis.upenn.edu/~bcpierce/tapl/)
* next step: [Practical Foundations for Programming Languages](https://www.cs.cmu.edu/~rwh/pfpl/)

---

# PHASE D — Compositionality and abstraction

This phase strongly overlaps with FP.

---

## D1. Lambda calculus

Can be:

* standalone,
* or part of PL theory.

Critical for:

* compositionality,
* substitution,
* abstraction,
* evaluation models.

Transformers themselves are not symbolic,
but compositionality is central to intelligence.

Links:

* classic/practice: [CS242 Assignment 1: Lambda Theory](https://stanford-cs242.github.io/f18/assignments/assign1/)
* practice: [Programming Language Foundations in Agda](https://plfa.github.io/)
* classic text: [The Lambda Calculus: Its Syntax and Semantics](https://www.collegepublications.co.uk/logic/mlf/?00001)

---

## D2. Category theory (optional but powerful)

Topics:

* morphisms,
* functors,
* monads,
* natural transformations,
* compositional structure.

Very useful for:

* abstraction,
* semantics,
* differentiable programming,
* compositional AI.

Given your FP background,
this will likely feel natural.

Links:

* classic/practice: [Category Theory for Programmers](https://github.com/hmemcpy/milewski-ctfp-pdf)
* practice: [Seven Sketches in Compositionality](https://arxiv.org/abs/1803.05316)
* practical bridge: [Applied Category Theory course material](https://www.appliedcategorytheory.org/school/)

---

# PHASE E — Symbolic reasoning systems

Insert AFTER ML fundamentals.

---

## E1. Logic programming

Topics:

* Prolog,
* Datalog,
* Horn clauses,
* unification,
* resolution.

This becomes increasingly relevant for:

* reasoning agents,
* planning,
* symbolic memory,
* hybrid AI systems.

Links:

* practice: [Stanford CS151 Logic Programming](https://logicprogramming.stanford.edu/)
* classic/practice: [Stanford CS157 Computational Logic](https://intrologic.stanford.edu/)
* practice: [Learn Datalog interactive tutorial](https://learn-some.com/)
* classic text: [The Art of Prolog](https://mitpress.mit.edu/9780262193382/the-art-of-prolog/)

---

## E2. SAT/SMT solving

Topics:

* satisfiability,
* constraint solving,
* theorem proving.

Useful for:

* verification,
* reasoning engines,
* symbolic planning,
* AI correctness.

Links:

* practice/state-of-the-art: [Stanford CS357 Advanced Topics in Formal Methods](https://web.stanford.edu/class/cs357/)
* practice: [Automated Reasoning: satisfiability](https://www.coursera.org/learn/automated-reasoning-sat)
* practice: [Z3 Guide](https://microsoft.github.io/z3guide/)
* classic/state-of-the-art: [Handbook of Satisfiability](https://ebooks.iospress.nl/volume/handbook-of-satisfiability-second-edition)

---

# PHASE F — Semantics of information

Very important for modern AI.

---

## F1. Information theory

Topics:

* entropy,
* KL divergence,
* mutual information,
* coding theory.

Core formula:

H(X)=-\sum_x p(x)\log p(x)

This connects:

* language modeling,
* prediction,
* compression,
* uncertainty,
* representation learning.

Links:

* classic/practice: [MIT 6.441 Information Theory assignments](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/resources/assignments/)
* classic: [Stanford EE376A Information Theory](https://web.stanford.edu/class/ee376a/)
* classic text: [Elements of Information Theory, Cover and Thomas](https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959)
* practice/ML bridge: [UMass CS650 Applied Information Theory](https://people.cs.umass.edu/~arya/courses/650/CS650-2016.html)

---

# PHASE G — Modern reasoning AI

Only after all foundations.

---

## G1. Neuro-symbolic AI

Topics:

* symbolic + neural hybrids,
* differentiable logic,
* graph reasoning,
* structured memory.

Links:

* state-of-the-art: [CMU 10-747 Neuro-Symbolic AI](https://www.cs.cmu.edu/~pradeepr/747)
* state-of-the-art/practice: [Neurosymbolic Programming seminar](https://neurosymbolic.metareflection.club/syllabus.html)
* practice bridge: [Berkeley CS294/194-196 Large Language Model Agents](https://rdi.berkeley.edu/llm-agents/f24)

---

## G2. AI Safety / Mechanistic Interpretability

Topics:

* reasoning transparency,
* representation analysis,
* circuit discovery,
* interpretability.

These fields increasingly require:

* semantics,
* abstraction,
* formal reasoning.

Links:

* state-of-the-art/practice: [ARENA Transformer Interpretability](https://learn.arena.education/chapter1_transformer_interp/02_intro_mech_interp/)
* state-of-the-art/practice: [ARENA circuits in LLMs](https://learn.arena.education/chapter1_transformer_interp/21_ioi/)
* state-of-the-art: [CS221M Interpretability](https://cs221m.github.io/)
* frontier seminar: [Stanford CS25 Transformers United](https://web.stanford.edu/class/cs25/)

---

# Practical assignment spine

If the goal is skill-building rather than browsing, follow this order:

1. CS103 problem sets.
2. MIT 6.042J problem sets.
3. CS154 automata/computability homework.
4. Stanford CS143 or CMU 15-411 compiler project.
5. CS242 programming language assignments.
6. Software Foundations or PLFA proof exercises.
7. Stanford CS357 or Z3 Guide SAT/SMT exercises.
8. MIT 6.441 information theory problem sets.
9. Stanford CS224N, CS336, or ARENA for modern neural/reasoning systems.

Modern ML/LLM practice links:

* practice/state-of-the-art: [Stanford CS224N Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/)
* practice/state-of-the-art: [Stanford CS336 Language Modeling from Scratch](https://cs336.stanford.edu/)
* frontier seminar: [Stanford CS25 Transformers United](https://web.stanford.edu/class/cs25/)

---

# If I compress this into “core additions”

## MUST ADD

* CS154
* compilers
* PL theory
* lambda calculus
* information theory

## HIGH VALUE

* theorem proving
* SAT/SMT
* logic programming
* semantics

## OPTIONAL BUT EXTREMELY POWERFUL

* category theory
* proof assistants
* HoTT
* denotational semantics

---

# Interesting observation

Modern frontier AI is slowly rediscovering topics that PL/logic people studied for decades:

* compositionality,
* symbolic abstraction,
* semantics,
* type safety,
* reasoning systems,
* structured representations.

Which is why FP/PL backgrounds are becoming increasingly valuable in advanced AI research.
