import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="vercel_kv",
    version="0.1.4",
    description="https://vercel.com/docs/storage/vercel-kv/rest-api",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bestK/python-vercel-kv",
    author="bestk",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["python-dotenv==1.0.0"],
    extras_require={'dev': ['pytest', 'tox']},
    entry_points={},
)
