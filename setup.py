from pathlib import Path

from setuptools import setup  # pyright: reportMissingTypeStubs=false

from cff import get_version

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Other Environment",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.9",
    "Topic :: Internet :: WWW/HTTP",
    "Typing :: Typed",
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
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Amazon Web Services CloudFront lambda function bootstraps",
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="cff",
    packages=[
        "cff",
    ],
    package_data={
        "cff": ["py.typed"],
    },
    python_requires=">=3.9",
    url="https://github.com/cariad/cff",
    version=version,
)
