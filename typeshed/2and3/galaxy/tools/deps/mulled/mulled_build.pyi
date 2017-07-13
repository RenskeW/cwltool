# Stubs for galaxy.tools.deps.mulled.mulled_build (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import installable
from sys import platform as _platform

class BuildExistsException(Exception): ...

class InvolucroContext(installable.InstallableContext):
    installable_description = ...  # type: str
    involucro_bin = ...  # type: str
    shell_exec = ...  # type: Any
    verbose = ...  # type: Any
    def __init__(self, involucro_bin: Optional[Any] = ..., shell_exec: Optional[Any] = ..., verbose: str = ...) -> None: ...
    def build_command(self, involucro_args): ...
    def exec_command(self, involucro_args): ...
    def is_installed(self): ...
    def can_install(self): ...
    @property
    def parent_path(self): ...

def main(argv: Optional[Any] = ...): ...