import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mitsubishi-central-controller-adgelbfish",
    version="0.0.2",
    author="Avraham David Gelbfish",
    author_email="adg@adgelb.fish",
    description="Library for Interfacing with a Mitsubishi Central Controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adgelbfish/mitsubishi-central-controller-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
