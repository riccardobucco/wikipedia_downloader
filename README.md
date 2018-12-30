# Wikipedia downloader
*wikipedia_downloader* is a Python module that makes it easy to download Wikipedia data dumps.
## Installation
To install *wikipedia_downloader*, simply run:
```
pip install wikipedia_downloader
```
## Documentation
### Functions
- wikipedia_downloader.**download_sql_dump**(*language*, *file*, *dump=latest*, *target_dir="."*)

  Downloads and decompresses a Wikipedia SQL dump.
  
  Arguments:
  - *language*: Wikipedia name (language code).
  - *file*: File name.
  - *dump*: Dump version.
  - *target_dir*: Target directory.
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.