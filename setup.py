import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_pkg_nrvanwyck",
    version="0.0.1",
    author="Nathan Van Wyck",
    author_email="nathanvanwyck@gmail.com",
    description="This simple package has a function to check nulls in a pandas DataFrame and a function to plot a labeled confusion matrix.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nrvanwyck/lambdata_nrvanwyck_repo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)