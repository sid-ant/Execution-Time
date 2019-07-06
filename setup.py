import pathlib
import setuptools
import code_time

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setuptools.setup(
    name=code_time.__name__,
    version=code_time.__version__,
    description="Execution time taken by each function",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/siddhant-curious/Python-Method-Execution-Time",
    author=code_time.__author__,
    author_email="siddhant1042@gmail.com",
    keyword='performance execution time package',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)