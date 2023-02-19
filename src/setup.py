from typing import Tuple, List
from src.modules.path import list_dirs, list_rtfs, join


def dirs(path_to_data: str) -> List[str]:
    return list_dirs(path_to_data)


def files(path_to_data: str) -> List[str]:
    return list_rtfs(path_to_data)


def resolve(path_to_data: str) -> List[Tuple[str, str, Tuple[str | None]]]:

    resolve_items = []
    resolve_dirs = dirs(path_to_data)
    for dir in resolve_dirs:
        print(join(path_to_data, dir))
        resolve_items.append(
            (dir, f"{path_to_data}/{dir}", tuple(list_rtfs(f"{path_to_data}/{dir}"))))

    return resolve_items
