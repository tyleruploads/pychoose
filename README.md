# pychoose

[![GitHub license](https://img.shields.io/badge/license-MIT-blue)](https://github.com/tyleruploads/pychoose/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/tyleruploads/devtkit)](https://github.com/tyleruploads/pychoose/issues)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

[pychoose](https://github.com/tyleruploads/pychoose) is an open-source Python GUI application built with CustomTkinter that removes the friction from everyday decision making.
The way pychoose does this is by letting the user type in their choices, click a button clearly labeled "Choose" on the bottom of the screen, and receive a cryptographically secure decision via the color of the labels above the text.


## Running & Installation
You can run or install pychoose instantly with [uv](https://docs.astral.sh/uv/getting-started/installation/), or install with [pipx](https://pipx.pypa.io/stable/).

### Installing with uv
```bash
uv tool install git+https://github.com/tyleruploads/pychoose.git
```

## Installing with pipx
```bash
pipx install git+https://github.com/tyleruploads/pychoose.git
```

### Running with uv
```bash
uvx --from git+https://github.com/tyleruploads/pychoose.git pychoose
```

If you are unable to use [uv](https://docs.astral.sh/uv/getting-started/installation/), you can still manually run the file.

### Manually running
To manually run the file, you must clone the repository and run the file located at src/pychoose/main.py.
You must have the customtkinter library accessible by your Python interpreter.

```bash
git clone https://github.com/tyleruploads/pychoose.git
cd pychoose
python3 src/pychoose/main.py
```

## Contributing

Contributions are what make open-source projects important. All contributions are highly appreciated.

* **Found a bug or issue**: Open an Issue and show the output of the script, the steps to reproduce it, and as much information as possible
* **Have an idea**: Open an Issue and explain your idea as much as possible, why you think it would be a good addition to the project, and any other important information.

## Security

For information on reporting security vulnerabilities in pychoose, see [SECURITY.md](SECURITY.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more information.
