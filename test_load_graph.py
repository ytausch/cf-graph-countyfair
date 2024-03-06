import logging
from conda_forge_tick.utils import setup_logging
from conda_forge_tick.make_graph import make_graph
from conda_forge_tick.utils import load_graph


def test_load_graph():
    setup_logging(level="DEBUG")
    names = []
    gx = load_graph()
    gx = make_graph(names, gx)
    assert True
