import setuptools

setuptools.setup(
    name="perlin-cupy",
    version="0.1",
    author="jpvt",
    author_email="joaoteixeira@eng.ci.ufpb.br",
    description="Perlin-NumPy for GPU",
    url="https://github.com/jpvt/perlin-cupy",
    project_urls={
        "Source": "https://github.com/jpvt/perlin-cupy",
        "Tracker": "https://github.com/jpvt/perlin-cupy/issues"
    },
    license="MIT",
    packages=["perlin_cupy"],
    install_requires=['cupy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)