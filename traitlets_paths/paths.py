import pathlib
from traitlets import (
    TraitType,
    TraitError
)

class PathTrait(TraitType):
    """Base class for pathlib traits.
    """
    # Name of object from pathlib.
    _pathlib_class_name = ''

    @property
    def info_text(self):
        return f'A pathlib.{self._pathlib_class_name} trait.'

    def validate(self, obj, value):
        # Get named object from pathlib
        pathlib_object = getattr(pathlib, self._pathlib_class_name)

        if isinstance(value, str):
            return pathlib_object(value)

        elif isinstance(value, self._pathlib_class_name):
            return value

        self.error(obj, value)


class PurePath(PathTrait):
    """A trait for pathlib's PurePath object.

    If a path string is given, it is converted 
    to a PurePath object.
    """
    _pathlib_class_name = 'PurePath'


class Path(PathTrait):
    """A trait for pathlib's Path object.

    If a path string is given, it is converted 
    to a Path object.
    """
    _pathlib_class_name = 'Path'


class PurePosixPath(PathTrait):
    """A trait for pathlib's PurePosixPath object.

    If a path string is given, it is converted 
    to a PurePosixPath object.
    """
    _pathlib_class_name = 'PurePosixPath'


class PureWindowsPath(PathTrait):
    """A trait for pathlib's PureWindowsPath object.

    If a path string is given, it is converted 
    to a PureWindowsPath object.
    """
    _pathlib_class_name = 'PureWindowsPath'


class PosixPath(PathTrait):
    """A trait for pathlib's PosixPath object.

    If a path string is given, it is converted 
    to a PosixPath object.
    """
    _pathlib_class_name = 'PosixPath'


class WindowsPath(PathTrait):
    """A trait for pathlib's WindowsPath object.

    If a path string is given, it is converted 
    to a WindowsPath object.
    """
    _pathlib_class_name = 'WindowsPath'
