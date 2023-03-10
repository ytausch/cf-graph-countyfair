import glob
import tqdm
from conda_forge_tick.utils import dump, loads


all_nodes = glob.glob("./node_attrs/*.json")

for node_path in tqdm.tqdm(all_nodes):
    with open(node_path, "r") as fp:
        attrs = loads(fp.read())

    new_ver = attrs.get("new_version", None)
    curr_ver = attrs.get("version", None)
    attempts = attrs.get("new_version_attempts", None)
    if (
        new_ver is not None
        and curr_ver is not None
        and new_ver != curr_ver
        and attempts is not None
        and attempts.get(new_ver, None) is not None
    ):
        attempts[new_ver] = 0
        with open(node_path, "w") as fp:
            dump(attrs, fp)
