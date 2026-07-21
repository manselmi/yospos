import importlib.metadata as impm

import pytest
from packaging.version import InvalidVersion, Version

import manselmi.yospos as module

DIST_PKG_NAME = "yospos"


def test_version():
    dist_pkg_version = impm.version(DIST_PKG_NAME)
    try:
        Version(dist_pkg_version)
    except InvalidVersion:
        pytest.fail(
            f"The version {dist_pkg_version!r} of distribution package {DIST_PKG_NAME!r} does not "
            "conform to PEP 440: https://www.python.org/dev/peps/pep-0440/"
        )
    module_name = module.__name__
    version_attr = "__version__"
    if not hasattr(module, version_attr):
        pytest.fail(f"The module {module_name!r} does not have a {version_attr!r} attribute.")
    module_version = module.__version__
    if module_version != dist_pkg_version:
        pytest.fail(
            f"The version {module_version!r} from {module_name + '.' + version_attr!r} does not "
            f"equal the version {dist_pkg_version!r} of distribution package {DIST_PKG_NAME!r}."
        )
