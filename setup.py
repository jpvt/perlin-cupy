from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="perlin-cupy",
    version="0.0.2",
    author="jpvt (João Pedro Vasconcelos)",
    author_email="joaoteixeira@eng.ci.ufpb.br",
    description="Perlin-NumPy for GPU",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/jpvt/perlin-cupy",
    project_urls={
        "Source": "https://github.com/jpvt/perlin-cupy",
        "Tracker": "https://github.com/jpvt/perlin-cupy/issues"
    },
    license="MIT",
    packages=find_packages(),
    install_requires=['cupy-cuda113'],
    keywords=['python', 'perlin', 'noise', 'gpu'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "License :: OSI Approved :: MIT License",
    ],
)