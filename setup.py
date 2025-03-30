import distutils.core
from Cython.Build import cythonize

distutils.core.setup(
    ext_modules = cythonize("main.pyx"))