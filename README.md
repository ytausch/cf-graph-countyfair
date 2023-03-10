# cf-graph

[![tests](https://github.com/regro/cf-graph-countyfair/actions/workflows/tests.yaml/badge.svg)](https://github.com/regro/cf-graph-countyfair/actions/workflows/tests.yaml)

Repo for holding the conda-forge dependency graph and its introspection.

Note that this repos is mostly bot managed and operated.

Please open issues in [cf-scripts](https://github.com/regro/cf-scripts/issues).

## code snippets to test building the graph

```python
import logging

from conda_forge_tick.make_graph import make_graph
from conda_forge_tick.all_feedstocks import get_all_feedstocks
from conda_forge_tick.utils import load_graph, setup_logger

names = get_all_feedstocks(cached=True)[0:10]
gx = load_graph()

setup_logger(logging.getLogger("conda_forge_tick.make_graph"))
make_graph(names, gx)
```
