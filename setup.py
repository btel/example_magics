from setuptools import setup, find_packages
setup(
    name="example_magic",
    version="0.1",
    author="Bartosz Telenczuk and IPython Development Team",
    author_email="bartosz@telenczuk.pl",
    description="Example IPython magic extension (used for testing)",
    packages=find_packages(),
    classifiers=[
        "Framework :: IPython",
        "Programming Language :: Python :: 3"
    ]
)
