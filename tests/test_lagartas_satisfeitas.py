import os
import sys

# Ajusta path para encontrar o package em src
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.path.join(ROOT, 'src')
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from lagarta import MundoLagarta
from caterpillar_csp_solver import (
    csp_possivel_solucao,
    csp_encontra_alcancaveis_1maca,
    encontra_alcancaveis_1maca,
    encontra_alcancaveis_todas_macas,
)
from csp_v3 import CSP, backtracking_search, number_ascending_order, forward_checking


def possivel_solucao(lagartas, alcancaveis):
    csp_lagartas1 = csp_possivel_solucao(lagartas, alcancaveis)
    return backtracking_search(csp_lagartas1, inference=forward_checking)


def test_csp_possivel_solucao_scenario_exemplo():
    line1 = "= = = = = = =\n"
    line2 = "= . . . . . =\n"
    line3 = "= . . = = x =\n"
    line4 = "= @ . . . = =\n"
    line5 = "= = . = = . =\n"
    line6 = "= . . @ x . =\n"
    line7 = "= = = = = = =\n"
    grelha = line1 + line2 + line3 + line4 + line5 + line6 + line7

    alcancaveis = {
        (1, 1): [(5, 4)],
        (1, 3): [(5, 4)],
        (1, 4): [(5, 4)],
        (1, 5): [(5, 4)],
        (2, 1): [(5, 4)],
        (2, 2): [(5, 4)],
        (2, 3): [(5, 4)],
        (2, 4): [(5, 4)],
        (2, 5): [(5, 4)],
        (3, 1): [(4, 1), (5, 4)],
        (3, 3): [(5, 4)],
        (3, 5): [(5, 4)],
        (4, 1): [(4, 1)],
        (4, 3): [(5, 4)],
        (4, 5): [(5, 4)],
        (5, 1): [(4, 1)],
        (5, 2): [(4, 1)],
        (5, 4): [(5, 4)],
        (5, 5): [(5, 4)],
    }

    l = MundoLagarta(grelha)
    lagartas = l.initial['heads']
    csp = csp_possivel_solucao(lagartas, alcancaveis)

    assert sorted(csp.variables) == [(1, 3), (3, 1)]
    assert dict(sorted(csp.domains.items())) == {
        (1, 3): [(5, 4)],
        (3, 1): [(4, 1), (5, 4)],
    }
    assert dict(sorted((k, sorted(v)) for k, v in csp.neighbors.items())) == {
        (1, 3): [(3, 1)],
        (3, 1): [(1, 3)],
    }
    assert csp.constraints((1, 3), (5, 4), (3, 1), (5, 4)) is False
    assert csp.constraints((1, 3), (5, 4), (3, 1), (4, 1)) is True


def test_possivel_solucao_exemplo_com_resultado_esperado():
    line1 = "= = = = = = =\n"
    line2 = "= x @ . . . =\n"
    line3 = "= = = = . x =\n"
    line4 = "= @ . . . = =\n"
    line5 = "= = = = = x =\n"
    line6 = "= . . @ x @ =\n"
    line7 = "= = = = = = =\n"
    grelha = line1 + line2 + line3 + line4 + line5 + line6 + line7

    alcancaveis = {
        (1, 1): [],
        (1, 3): [(5, 4)],
        (1, 5): [(1, 5)],
        (2, 1): [],
        (2, 3): [(5, 4)],
        (2, 5): [(1, 5), (5, 4)],
        (3, 1): [(4, 1)],
        (3, 3): [(5, 4)],
        (3, 5): [(5, 4)],
        (4, 1): [(4, 1)],
        (4, 3): [(5, 4)],
        (4, 4): [(5, 4)],
        (4, 5): [(5, 4)],
        (5, 1): [(4, 1), (5, 2)],
        (5, 2): [(5, 2)],
        (5, 4): [(5, 4)],
        (5, 5): [(5, 4)],
    }

    l = MundoLagarta(grelha)
    lagartas = l.initial['heads']

    result = possivel_solucao(lagartas, alcancaveis)
    assert result is not None
    result = dict(sorted(result.items()))
    assert result == {
        (1, 3): (5, 4),
        (2, 5): (1, 5),
        (3, 1): (4, 1),
        (5, 1): (5, 2),
    }


def test_encontra_alcancaveis_1maca_exemplo():
    line1 = "= = = = = = =\n"
    line2 = "= @ . . . = =\n"
    line3 = "= = = = = . =\n"
    line4 = "= . . . x . =\n"
    line5 = "= = = = = = =\n"
    grelha = line1 + line2 + line3 + line4 + line5

    l = MundoLagarta(grelha)
    result = encontra_alcancaveis_1maca(l, (4, 1))
    assert result == {
        (1, 1): 1,
        (1, 3): 0,
        (2, 1): 1,
        (2, 3): 0,
        (3, 1): 1,
        (3, 3): 0,
        (4, 1): 1,
        (4, 3): 0,
        (5, 1): 1,
        (5, 2): 1,
    }


def test_encontra_alcancaveis_todas_macas_exemplo():
    line1 = "= = = = = =\n"
    line2 = "= = x = @ =\n"
    line3 = "= x = = x =\n"
    line4 = "= @ . . @ =\n"
    line5 = "= = = = = =\n"
    grelha = line1 + line2 + line3 + line4 + line5

    l = MundoLagarta(grelha)
    result = encontra_alcancaveis_todas_macas(l)
    assert dict(sorted(result.items())) == {
        (1, 1): [(1, 2)],
        (1, 2): [(1, 2)],
        (2, 1): [],
        (2, 3): [(2, 3)],
        (3, 1): [],
        (4, 1): [(4, 2)],
        (4, 2): [(4, 2)],
        (4, 3): [(4, 2)],
    }
