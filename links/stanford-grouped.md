# Stanford CS Courses — URL Pattern Reference

## Standard Patterns

| Pattern                                                               | Description                                             |
|-----------------------------------------------------------------------|---------------------------------------------------------|
| `https://web.stanford.edu/class/{course}/`                            | Main course portal — by far the most common             |
| `https://web.stanford.edu/class/archive/cs/{course}/{course}.{term}/` | Archived snapshot of a past offering                    |
| `https://see.stanford.edu/Course/{COURSE}`                            | Stanford Engineering Everywhere (course code uppercase) |
| `https://{course}.stanford.edu/`                                      | Course code as subdomain                                |
| `https://stanford-{course}.github.io/`                                | GitHub Pages with `stanford-` prefix                    |
| `https://{course}-stanford.github.io/`                                | GitHub Pages with `-stanford` suffix                    |
| `https://theory.stanford.edu/~{person}/{course}/`                     | Theory group, personal user path                        |
| `https://hci.stanford.edu/courses/{course}/`                          | HCI group                                               |
| `https://graphics.stanford.edu/courses/{course}/`                     | Graphics group (often with `-YY-season` suffix)         |
| `https://cs.stanford.edu/group/manips/teaching/{course}/`             | Robotics / Manipulation group                           |
| `https://snap.stanford.edu/class/{course}/`                           | SNAP group                                              |
| `https://crypto.stanford.edu/{course}/`                               | Crypto group                                            |
| `https://crypto.stanford.edu/~{person}/{course}/`                     | Crypto group, personal user path                        |

---

## Courses That Don't Fit the Patterns

| Course        | URL                                                                 | Why it's an outlier                                                      |
|---------------|---------------------------------------------------------------------|--------------------------------------------------------------------------|
| CS41          | `https://stanfordpython.com/`                                       | Fully external domain — no stanford.edu at all                           |
| CS131         | `https://vision.stanford.edu/teaching/cs131_fall2021/`              | One-off `vision` subdomain with `teaching/` path and `_term` suffix      |
| CS140         | `https://web.stanford.edu/~ouster/cgi-bin/cs140-spring20/index.php` | Personal `~user` cgi-bin path on web.stanford.edu                        |
| CS151         | `https://logicprogramming.stanford.edu/`                            | Topic-named subdomain, no course code in URL                             |
| CS157         | `https://intrologic.stanford.edu/`                                  | Topic-named subdomain, no course code in URL                             |
| CS181         | `https://stanfordcs181.github.io/`                                  | GitHub Pages — no separator between "stanford" and course code           |
| CS184         | `https://i.stanford.edu/~ullman/cs184/`                             | Personal `~user` path under `i.stanford.edu`                             |
| CS193U        | `https://www.tomlooman.com/stanford-cs193u/`                        | Third-party external domain                                              |
| CS243         | `https://suif.stanford.edu/~courses/cs243/`                         | `suif` subdomain with `~courses` pseudo-user path                        |
| CS244b        | `https://www.scs.stanford.edu/20sp-cs244b/`                         | SCS subdomain, term-prefixed path format `{YYss}-{course}`               |
| CS320 / CS235 | `https://canvas.stanford.edu/courses/184853`                        | Canvas LMS opaque numeric ID — no course code in URL                     |
| CS372         | `https://infolab.stanford.edu/~ullman/cs372/`                       | Personal `~user` path under `infolab.stanford.edu`                       |
| CS348E        | `https://ckllab.stanford.edu/cs348e/`                               | Single-use `ckllab` subdomain (CK Locomotion Lab)                        |
| CS476A        | `https://ccrma.stanford.edu/courses/256a/`                          | CCRMA subdomain — URL uses a **different** course code (`256a` ≠ `476a`) |
| CS528         | `https://mlsys.stanford.edu/`                                       | Topic-named subdomain (`mlsys`), no course code in URL                   |
