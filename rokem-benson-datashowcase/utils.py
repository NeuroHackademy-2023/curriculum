"""Utilities for use with the 2023 NeuroHackademy data showcase.
"""


def ls(path):
    "Lists the contents of the given path."
    # If path is not a directory, raise an error:
    if not path.is_dir():
        raise ValueError(f"Path '{path}' is not a directory")
    else:
        return list(path.iterdir())


def crawl(path, indent=0):
    "Prints a nested tree of the contents of the given path."
    print((' '*indent) + path.name)
    if path.is_dir():
        for subpath in path.iterdir():
            crawl(subpath, indent=(indent + 3))
    else:
        pass


def load_aws_credentials(profile_name):
    "Returns (access_key, secred_key) from ~/.aws/credentials for the given profile."
    import boto3
    ses = boto3.Session(profile_name=profile_name)
    creds = ses.get_credentials()
    return (creds.access_key, creds.secret_key)
