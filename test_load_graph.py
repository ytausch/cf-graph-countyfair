from conda_forge_tick.make_graph import make_graph
from conda_forge_tick.utils import load_existing_graph, setup_logging


def test_load_graph():
    setup_logging()
    names = []
    gx = load_existing_graph()
    make_graph(names, gx)
