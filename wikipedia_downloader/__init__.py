"""Downloads Wikipedia data dumps.

Functions:
    download_sql_dump: Downloads and decompress a Wikipedia SQL dump
"""

# Standard library imports
from gzip import GzipFile
from shutil import copyfileobj
from urllib.request import urlopen
import os

BASE_URL = "https://dumps.wikimedia.org/"

def download_sql_dump(language, file, dump="latest", target_dir="."):
    """Downloads and decompresses a Wikipedia SQL dump.

    Args:
        language: Wikipedia name (language code).
        file: File name.
        dump: Dump version.
        target_dir: Target directory.
    """

    # Return the filename of a .sql file
    def _get_name():
        return "{}wiki-{}-{}.sql".format(language, dump, file)

    # Return the url where a .sql.gz file is located
    def _get_url():
        wikipedia_base_url = "{}{}wiki/{}/".format(BASE_URL, language, dump)
        filename = _get_name()
        return "{}{}.gz".format(wikipedia_base_url, filename)

    with urlopen(_get_url()) as res, \
         GzipFile(fileobj=res) as uncompressed_res, \
         open(os.path.join(target_dir, _get_name()), 'wb') as out_file:
        copyfileobj(uncompressed_res, out_file)
