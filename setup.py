import setuptools

REQUIRED = ["numpy", "pandas", "scipy"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nofan",
    version="0.2.0",
    author="ik-okoro",
    description="Collection of Data Science functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ik-okoro/nofan",
    packages=setuptools.find_packages(),
    install_requires = REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)