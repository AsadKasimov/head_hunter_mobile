def abs_path_from_project(relative_path: str):
    import hh_ru_mobile
    from pathlib import Path

    return (
        Path(hh_ru_mobile.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
