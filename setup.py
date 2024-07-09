from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        'pagerank',
        ['pagerank.cpp', 'bindings.cpp'],
    ),
]

setup(
    name='pagerank',
    ext_modules=ext_modules,
    license='GPLv3',
    author_email='jero98772@protonmail.com',
    author='jero98772',
    cmdclass={'build_ext': build_ext},
    packages=find_packages(),
    install_requires=['requests','pybind11','setuptools','fastapi'],
    include_package_data=True,

)