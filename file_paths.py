""" This module is used to extract vtt files from a directory """
from os import listdir, path


def get_vtt_file_paths(directory: str):
    """
    :returns: iterator over all existing vtt files in the given directory.
    """
    cleaned_dir_path = clean_dir_path(directory)
    for file_name in listdir(cleaned_dir_path):
        cleaned_path = clean_file_path(file_name)
        if validate_file_extension(cleaned_path):
            yield path.join(cleaned_dir_path, file_name)


def clean_file_path(file_path: str):
    return file_path.strip('\'')


def clean_dir_path(directory: str):
    return directory.strip('\"')


def validate_file_extension(vtt_file_path: str):
    return vtt_file_path.endswith(".vtt")
