""" Subtitle Convertor module"""

from re import compile
from typing import TextIO


def convert_vtt_files_to_srt(*paths: str):
    for path in paths:
        if (result := convert_vtt_to_srt(path)) is not None:
            print(result)


def convert_vtt_to_srt(vtt_file_path) -> FileNotFoundError | None:
    try:
        with open(vtt_file_path, 'rt') as vtt_file:

            _skip_webvtt_in_first_line(vtt_file)

            new_srt_file = _create_new_srt_file_in_vtt_file_dir(vtt_file_path)
            for line in _replace_periods_with_comma_in_timestamps(vtt_file):
                new_srt_file.write(line)
            new_srt_file.close()

    except FileNotFoundError as not_found_error:
        return not_found_error

    return None


def _skip_webvtt_in_first_line(vtt_file: TextIO) -> None:
    """
     move the offset of file after the first line that contains 'WEBVTT'
    """

    webvtt_pattern = compile(r'\s*WEBVTT\s*\n')

    while webvtt_pattern.match(vtt_file.readline()) is None:
        pass
    vtt_file.readline()  # skip blank line after 'WEBVTT'


def _replace_periods_with_comma_in_timestamps(vtt_file: TextIO) -> str:
    vtt_timestamp_pattern = compile(r'(\d{2}:\d{2}:\d{2})\.(\d{3})')
    for line in vtt_file:
        yield vtt_timestamp_pattern.sub(r'\1,\2', line)


def _create_new_srt_file_in_vtt_file_dir(vtt_file_path: str) -> TextIO:
    new_file_path = vtt_file_path.replace('.vtt', '.srt')

    return open(new_file_path, 'wt', encoding='utf-8')

