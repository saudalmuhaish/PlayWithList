import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PlayWithList",
    version="0.0.5",
    author="Saud Almuhaysh",
    author_email="S.Almuhaysh@gmail.com",
    description="User can enter the list and get many function of it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saudalmuhaish/PlayWithList",
    project_urls={
        "Bug Tracker": "https://github.com/saudalmuhaish/PlayWithList/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)