# Wikipedia downloader
*wikipedia_downloader* is a Python module that makes it easy to download Wikipedia data dumps.
## Installation
To install *wikipedia_downloader*, simply run:
```
pip install wikipedia_downloader
```
## Documentation
### Functions
- wikipedia_downloader.**download_sql_dump**(*language*, *file*, *dump="latest"*, *target_dir="."*)

  Downloads and decompresses a Wikipedia SQL dump.
  
  Arguments:
  - *language*: Wikipedia name (language code).
  - *file*: File name.
  - *dump*: Dump version.
  - *target_dir*: Target directory.
  
  #### Example
  ```Python
  import wikipedia_downloader as wpd
  wpd.download_sql_dump("en", "pagelinks", dump="20190101", target_dir="./dumps")
  ```

- wikipedia_downloader.**get_dataframe**(*language*, *file*, *dump="latest"*, *select=None*, *where=None*)

  Builds a pandas.DataFrame from a Wikipedia SQL dump.
  
  Arguments:
  - *language*: Wikipedia name (language code).
  - *file*: File name.
  - *dump*: Dump version.
  - *select*: Columns to be kept.
  - *where*: Functions used to filter records.
  
  Returns: *pandas.DataFrame*
  
  #### Example
  ```python
  import wikipedia_downloader as wpd
  select = ["page_id", "page_namespace", "page_title"]
  where = {"page_namespace": lambda x: x == 0 or x == 14}
  df = wpd.get_dataframe("en", "page", dump="20190101", select=select, where=where)
  ```
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.