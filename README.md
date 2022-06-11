# Directory Hash Calculator
This project is a super simple Python library which can be used in both command line and library ways.

To install it:

```shell
$ pip install dirhashcalc
```

### Commandline Usage
To use it in commandline:

```shell
$ dir_hash path/to/dir
8907645cfe42941cf7dbc656d59ccc4f02ec2a16493c097e04ce2547ad1e5484
```

You can also pass mlutiple arguments:

```shell
$ dir_hash first second
first: 8907645cfe42941cf7dbc656d59ccc4f02ec2a16493c097e04ce2547ad1e5484
second: 9f29e53d60a5a8e92da03e41678374ac584c2c94a24898c0c719736412723c4d
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
