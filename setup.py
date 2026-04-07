from setuptools import setup, find_packages

with open("README.md", encoding="UTF-8") as file:
    long_description = file.read()

setup(
    name="maxbot-api-client-python",
    version="1.1.0",
    author="Green API",
    description="Python client for MAX Bot API with Sync and Async support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/green-api/maxbot-api-client-python",
    packages=find_packages(exclude=["examples", "docs"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=[
        "httpx>=0.24.0",
        "aiofiles>=23.1.0",
        "pydantic>=2.0.0",
        "tenacity>=9.1.2"
    ],
)