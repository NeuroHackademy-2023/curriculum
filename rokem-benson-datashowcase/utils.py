


def ls(path):
    "Lists the contents of the given path."
    # If path is not a directory, raise an error:
    if not path.is_dir():
        raise ValueError(f"Path '{path}' is not a directory")
    else:
        return list(path.iterdir())


def crawl(path, indent=0):
    print((' '*indent) + path.name)
    if path.is_dir():
        for subpath in path.iterdir():
            crawl(subpath, indent=(indent + 3))
    else:
        pass
