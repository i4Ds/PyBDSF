from skbuild import setup  # This line replaces 'from setuptools import setup'
import os

cmake_args = []

if "CMAKE_ARGS" in os.environ:
    args = list(filter(None, os.environ["CMAKE_ARGS"].split(" ")))
    if len(args) > 0:
        cmake_args += [arg for arg in args if len(arg.split("DCMAKE_INSTALL_PREFIX")) == 1]

setup(
    name='bdsf',
    version='1.11.0a1',
    author='David Rafferty',
    author_email='drafferty@hs.uni-hamburg.de',
    url='https://github.com/lofar-astron/PyBDSF',
    description='Blob Detection and Source Finder',
    long_description=open('README.rst', 'rt').read(),
    cmake_args = cmake_args,
    long_description_content_type='text/x-rst',
    platforms='Linux, Mac OS X',
    packages=['bdsf', 'bdsf.nat'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: C++',
        'Programming Language :: Fortran',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Astronomy'
    ],
    extras_require={
        'ishell': ['ipython<8.11', 'matplotlib']
    },
    install_requires=['backports.shutil_get_terminal_size',
                        'astropy', 'numpy', 'scipy'],
    entry_points = {
        'console_scripts': [
            'pybdsf = bdsf.pybdsf:main [ishell]',
            'pybdsm = bdsf.pybdsf:main [ishell]'
        ]
    },
    zip_safe=False,
)
