from pathlib import Path

from setuptools import setup

from progrow.version import get_version

readme_path = Path(__file__).parent.joinpath("README.md")

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.9",
    # "Typing :: Typed",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@hey.com",
    classifiers=classifiers,
    description="Describes the progress of work across rows",
    include_package_data=True,
    install_requires=[
        "colorama>=0.4",
    ],
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="progrow",
    packages=[
        "progrow",
    ],
    # "py.typed" in each package's directory must be included for the package to
    # be considered typed.
    package_data={
        "progrow": ["py.typed"],
    },
    python_requires=">=3.6",
    url="https://github.com/cariad/progrow",
    version=version,
)
