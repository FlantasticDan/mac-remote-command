import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mac-remote-command",
    version="0.0.1",
    author="Daniel Flanagan",
    description="Client for embedded systems to facilitate remote configuration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlantasticDan/mac-remote-command",
    project_urls={
        "Bug Tracker": "https://github.com/FlantasticDan/mac-remote-command/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    install_requires=['httpx', 'getmac']
)