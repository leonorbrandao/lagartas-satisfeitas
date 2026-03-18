# Satisfied Caterpillars (Academic Project)

## Project Description

Course project (Artificial Intelligence, 2025/26).
Goal: model and solve a caterpillar-grid control problem with apples and obstacles using CSP (Constraint Satisfaction Problem) + informed search.

- Skills applied: state modeling, Python programming, CSP, backtracking, AC-3, forward checking.
- Problem domain: ensure each caterpillar head reaches an achievable apple without allocation conflicts.

## My Contribution

- Implemented core functions in `src/caterpillar_csp_solver.py`:
  - `csp_possivel_solucao` (checks if there is a possible assignment with no target collisions)
  - `csp_encontra_alcancaveis_1maca` / `encontra_alcancaveis_1maca` (reachable apple map for a single apple)
  - `encontra_alcancaveis_todas_macas` (full reachable map for all apples)
- Created unit tests in `tests/test_lagartas_satisfeitas.py` covering base scenarios and example cases.
- Integrated with `src/csp_v3.py` (CSP framework and generic solvers).
- Used `src/lagarta.py` for world representation, actions, and movement dynamics.

## Technologies and Tools

- Language: Python 3.11+
- Libraries: standard library only + `pytest` for tests
- Project modules:
  - `src/csp_v3.py` (CSP framework + algorithms)
  - `src/lagarta.py` (problem and state model)
  - `src/caterpillar_csp_solver.py` (specific CSP solution)
  - `tests/test_lagartas_satisfeitas.py` (unit tests)

## Quick Start

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install pytest
```

2. Run tests:

```powershell
pytest -q
```

3. Example usage in Python console:

```python
from src.lagarta import MundoLagarta
from src.caterpillar_csp_solver import encontra_alcancaveis_todas_macas

grid = """\
= = = = = =
= @ . . @ =
= . = x . =
= = = = = =
"""

m = MundoLagarta(grid)
print(encontra_alcancaveis_todas_macas(m))
```

## Results and Impact

- Practical application of symbolic AI techniques (CSP).
- Example cases solved and validated via unit tests.
- Base for extension to logic games and autonomous agent planning.

## How to cite in resume

- Designed and implemented CSP algorithm for a caterpillar-and-apple goal assignment problem.
- Implemented search and heuristics with backtracking and forward checking.
- Added unit tests and performed state-space complexity analysis.
