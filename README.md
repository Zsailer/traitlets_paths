# traitlets_paths

**Traitlets module for pathlib**

This package defines `traitlets` for all pathlib objects.

## Getting Started 

Install from pip:
```
pip install traitlets_paths
```

**Basic Example**

```python
from traitlets import HasTraits, default
from traitlets_paths import PurePath

class Foo(HasTraits):
    path = PurePath()

    @default('path')
    def _default_path(self):
        return 'path/to/foo'


foo = Foo()
foo.path
```
```
# On Posix systems
PurePosixPath('path/to/foo')

# or on Windows systems
PureWindowsPath('path/to/foo')
```

**How to get a TraitError**

When we try passing a bad type:
```
foo = Foo(path=5)
```
we get a TraitError:
```
TraitError: The 'path' trait of a Foo instance must be a pathlib.PurePath trait, but a value of 5 <class 'int'> was specified.
```

## Developing

Download and install this repo from source, and move into the base directory.
```
git clone https://github.com/Zsailer/traitlets_paths
cd traitlets_paths
```
If you use [pipenv](https://pipenv.readthedocs.io/en/latest/), you can install a developement version:
```
pipenv install --dev
``` 

Otherwise you can install a development version using pip
```
pip install -e .
```

## Licensing

The code in this project is licensed under MIT license.