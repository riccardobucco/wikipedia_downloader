"""Downloads Wikipedia data dumps.

Functions:
    download_sql_dump: Downloads and decompress a Wikipedia SQL dump.
    get_dataframe: Builds a pandas.DataFrame from a Wikipedia SQL dump.
"""

# Standard library imports
from ast import literal_eval
from gzip import GzipFile
from shutil import copyfileobj
from urllib.request import urlopen
import os
import re

# Related third party imports
import pandas as pd

BASE_URL = "https://dumps.wikimedia.org/"

# Return the filename of a .sql file
def _get_name(language, dump, file):
    return "{}wiki-{}-{}.sql".format(language, dump, file)

# Return the url where a .sql.gz file is located
def _get_url(language, dump, file):
    wikipedia_base_url = "{}{}wiki/{}/".format(BASE_URL, language, dump)
    filename = _get_name(language, dump, file)
    return "{}{}.gz".format(wikipedia_base_url, filename)

def download_sql_dump(language, file, dump="latest", target_dir="."):
    """Downloads and decompresses a Wikipedia SQL dump.

    Args:
        language: Wikipedia name (language code).
        file: File name.
        dump: Dump version.
        target_dir: Target directory.
    """

    with urlopen(_get_url(language, dump, file)) as res, \
         GzipFile(fileobj=res) as uncompressed_res, \
         open(os.path.join(target_dir, _get_name(language, dump, file)), 'wb') as out_file:
        copyfileobj(uncompressed_res, out_file)

def get_dataframe(language, file, dump="latest", select=None, where=None):
    """Builds a pandas.DataFrame from a Wikipedia SQL dump.

    Args:
        language: Wikipedia name (language code).
        file: File name.
        dump: Dump version.
        select: Columns to be kept.
        where: Functions used to filter records.

    Returns:
        pandas.DataFrame
    """

    with urlopen(_get_url(language, dump, file)) as res:
        with GzipFile(fileobj=res) as uncompressed_res:
            # Get names of file's columns
            line = next(uncompressed_res).decode("utf-8")
            while not line.startswith("CREATE TABLE"):
                line = next(uncompressed_res).decode("utf-8")
            col_names = []
            while not line.endswith(";\n"):
                line = next(uncompressed_res).decode("utf-8")
                if line.startswith("  `"):
                    col_names.append(re.findall("  `.*`", line)[0].lstrip().strip("`"))
            # Get a mask representing the columns that should be kept
            if select is None:
                select = col_names
            cols_to_keep = [name in select for name in col_names]
            # Get a map col_name -> col_index
            name_to_index = {name: index for index, name in enumerate(col_names)}
            # Parse the file and build the pandas.DataFrame
            linestart = "INSERT INTO `{}` VALUES ".format(file)
            tmp_dfs = []
            for line in uncompressed_res:
                line = line.decode("utf-8")
                if line.startswith("INSERT"):
                    values = [(col for keep, col in zip(cols_to_keep, row) if keep is True)
                              for row in literal_eval(line.lstrip(linestart)
                                                      .rstrip(";\n")
                                                      .replace(",NULL", ",None"))
                              if all(where[name](row[name_to_index[name]]) for name in where)]
                    columns = [name for keep, name in zip(cols_to_keep, col_names) if keep is True]
                    tmp_dfs.append(pd.DataFrame.from_records(values, columns=columns))
    return pd.concat(tmp_dfs)
