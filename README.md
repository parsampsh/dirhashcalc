# Directory Hash Calculator
This project is a super simple Python library which can be used in both command line and library ways.

To install it:

```shell
$ pip install dirhashcalc
```

### Commandline Usage
To use it in commandline:

```shell
$ dirhashcalc path/to/dir
8907645cfe42941cf7dbc656d59ccc4f02ec2a16493c097e04ce2547ad1e5484
```

You can also pass mlutiple arguments:

```shell
$ dirhashcalc first second
first: 8907645cfe42941cf7dbc656d59ccc4f02ec2a16493c097e04ce2547ad1e5484
second: 9f29e53d60a5a8e92da03e41678374ac584c2c94a24898c0c719736412723c4d
```

Also there are some options that you can use:

```shell
$ dirhashcalc --version # shows version of the tool

# verbose output (prints name of each file when calculating hash of it)
$ dirhashcalc some/dir -v
$ dirhashcalc some/dir --verbose

# super verbose output (prints file names and hash of each one of them)
$ dirhashcalc some/dir -vv
$ dirhashcalc some/dir --super-verbose
```

### Library Usage
You can use this project in your own projects to calculate directory hash.

```python
from dirhashcalc import DirHashCalculator

dir_sha256 = DirHashCalculator('path/to/dir').calc()
```

Class `DirHashCalculator` has more methods. To see them and use it in any other way that you want, see content of `dir_hash.py` in the project and read description of each method in docstring.

### License
This project is licensed under [MIT License](LICENSE).
