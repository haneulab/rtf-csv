import os
import glob
from typing import List


def join(*paths: str) -> str:
    path_query = "."

    for path in paths:
        path_query += f"/{path}"

    return path_query


def list_dirs(root: str) -> List[str]:
    return os.listdir(root)


def list_rtfs(root: str) -> List[str]:
    rtfs = []
    print("root ", root)
    for file in os.listdir(root):
        print("files ", file)
        if file.endswith(".rtf"):
            rtfs.append(file)

    print("rtfs : ", rtfs)
    return rtfs


static_paths = {
    "src": "src",
    "data": "data",
    "build": "build"
}
