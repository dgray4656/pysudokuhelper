import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires=[]

setuptools.setup(
    name="pysudokuhelper",
    version="0.0.3",
    author="David E. Gray",
    author_email="dgray4656@yahoo.com",
    description="Python package to help solve sudoku puzzles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dgray4656-org/pysudokuhelper",
    packages=setuptools.find_packages(),
    install_requires=requires,
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
