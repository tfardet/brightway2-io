from setuptools import setup

REQUIREMENTS = [
    "bw2calc>=2.0.dev14",
    "bw2data>=4.0.dev27",
    "bw2parameters>=1.1.0",
    "bw_migrations>=0.2",
    "bw_processing>=0.8.5",
    "lxml",
    "mrio_common_metadata",
    "numpy",
    "openpyxl",
    "platformdirs",
    "requests",
    "scipy",
    "stats_arrays>=0.6.5",
    "tqdm",
    "unidecode",
    "voluptuous",
    "xlrd",
    "xlsxwriter",
]

v_temp = {}
with open("bw2io/version.py") as fp:
    exec(fp.read(), v_temp)
version = ".".join((str(x) for x in v_temp["version"]))


setup(
    name="bw2io",
    version=version,
    packages=[
        "bw2io",
        "bw2io.data",
        "bw2io.export",
        "bw2io.extractors",
        "bw2io.importers",
        "bw2io.strategies",
    ],
    package_data={
        "bw2io": ["data/*.*", "data/examples/*.*", "data/lci/*.*", "data/lcia/*.*"]
    },
    exclude_package_data={
        "": [".DS_Store"],
    },
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license="BSD 3-clause",
    install_requires=REQUIREMENTS,
    url="https://github.com/brightway-lca/brightway2-io",
    long_description=open("README.rst").read(),
    description=("Tools for importing and export life cycle inventory databases"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
