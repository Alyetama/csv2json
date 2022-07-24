# CSV2JSON

🚀 A CLI tool to export CSV files to JSON format.

[![Supported Python versions](https://img.shields.io/badge/Python-%3E=3.7-blue.svg)](https://www.python.org/downloads/) [![PEP8](https://img.shields.io/badge/Code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/) 


## Requirements
- 🐍 [python>=3.7](https://www.python.org/downloads/)


## ⬇️ Installation

```sh
pip install tojson
```


## ⌨️ Usage

```
➜ csv2json --help  # You can also use the alias `tojson` or `csvtojson`

usage: csv2json [-h] [-o {dict,list,series,split,records,index}] [-i INDENT]
                [-c]
                path [path ...]

positional arguments:
  path                  Path to a single file/directory or multiple
                        files/directories

options:
  -h, --help            show this help message and exit
  -o {dict,list,series,split,records,index}, --orient {dict,list,series,split,records,index}
                        The type of the values of the dictionary
  -i INDENT, --indent INDENT
                        JSON output indentation
  -c, --compress        Compress the output
```


## 📕 Examples

```sh
csv2json foo.csv
```

```sh
# Orient as list 
csv2json foo.csv -o list
```

```sh
# Compressed output and use zero indentation (minified)
csv2json foo.csv -c -i 0
```
