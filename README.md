# Traitlets module for pathlib

This package defines `traitlets` TraitTypes for pathlib objects.

`traitlet_paths` traits accept Python *strings* or pathlib *path objects*.

Example

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
PurePosixPath('path/to/foo')
```
If you're on Mac or Linux:
```
PureWindowsPath('path/to/foo')
```
if you're on Windows.