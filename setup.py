from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="perlin-cupy",
    version="0.0.1",
    author="jpvt",
    author_email="joaoteixeira@eng.ci.ufpb.br",
    description="Perlin-NumPy for GPU",
    url="https://github.com/jpvt/perlin-cupy",
    project_urls={
        "Source": "https://github.com/jpvt/perlin-cupy",
        "Tracker": "https://github.com/jpvt/perlin-cupy/issues"
    },
    license="MIT",
    packages=find_packages(),
    install_requires=['cupy'],
    classifiers=[
        "Development Status :: 1 - First Version",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
        "License :: OSI Approved :: MIT License",
    ],
)