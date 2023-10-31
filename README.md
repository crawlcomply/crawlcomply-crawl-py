crawlcomply-crawl-py
====================
![Python version range](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11-blue.svg)
![Python implementation](https://img.shields.io/badge/implementation-cpython-blue.svg)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort)

Backend server and CLI for crawlComply's crawler and associated business logic.

## Features

| Feature                                                | Implemented |
|--------------------------------------------------------|-------------|
| Distributed                                            | ❌           |
| Cross-platform                                         | ✅           |
| Multiple Python versions supported                     | ✅           |
| Scripts for deploying to different cloud vendors       | ❌           |
| Website scraping (basic)                               | ❌           |
| JavaScript rendering                                   | ❌           |
| Screenshot capturing                                   | ❌           |
| Tooling to find specific text                          | ❌           |
| ML to find specific image (fuzzily)                    | ❌           |
| Tabulation of presence/absence of features per website | ❌           |
| Website archive format use (e.g., WARC)                | ❌           |
| Database integration                                   | ❌           |
| REST API server                                        | WiP         |
| [OpenAPI](https://openapis.org) spec                   | ❌           |
| Command Line Interface (CLI)                           | ❌           |
| Web frontend (basic)                                   | ❌           |
| Web frontend (auth)                                    | ❌           |
| Web frontend (business analytics dashboard)            | ❌           |

## Install package

### Master

    python -m pip install -r https://raw.githubusercontent.com/crawlcomply/crawlcomply-crawl-py/master/requirements.txt
    python -m pip install https://api.github.com/repos/crawlcomply/crawlcomply-crawl-py/zipball#egg=cdd

## Usage

    $ python -m crawlcomply_crawl -h
    usage: python -m crawlcomply_crawl [-h] [--version] {exec,serve} ...
    
    Backend server and CLI for crawlcomply's crawler and associated business
    logic.
    
    positional arguments:
      {exec,serve}
        exec        For testing on the command line
        serve       Serve REST API
    
    options:
      -h, --help    show this help message and exit
      --version     show program's version number and exit

#### Serve
Serve REST API

    $ python -m crawlcomply_crawl serve -h
    usage: python -m crawlcomply_crawl serve [-h] [--hostname HOST] [--port PORT]
    
    options:
      -h, --help       show this help message and exit
      --hostname HOST  Hostname or address to listen on
      --port PORT      Port to listen on

### Exec
For testing on the command line

---

## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <https://apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
