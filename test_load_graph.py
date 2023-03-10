import logging
from conda_forge_tick.utils import setup_logger
from conda_forge_tick.make_graph import make_graph
from conda_forge_tick.utils import load_graph


def test_load_graph():
    setup_logger(logging.getLogger("conda_forge_tick"), level="DEBUG")
    names = []
    gx = load_graph(reset_bad=True)
    gx = make_graph(names, gx)
    assert True
