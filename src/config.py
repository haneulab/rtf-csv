from src.modules.path import join, static_paths


def paths() -> dict[str, str]:
    return {
        "data": join(static_paths['src'], static_paths['data']),
        "build": join(static_paths['build'])
    }
