#!/usr/bin/env python
from setuptools import (
    setup,
    find_packages
)

from pathlib import Path

version = {}
version_path = Path('ai_agent/version.py').resolve()
with open(version_path) as f:
    exec(f.read(), version)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ai-agent-sdk',
    version=version['__version__'],
    author='APRO',
    author_email='apro@apro.com',
    description='ai agent sdk for apro',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/APRO-com/ai-agent-sdk-python',
    packages=find_packages(),
    install_requires=[
        'web3 > 7.0.0',
        'python_dotenv >= 1.0.1',
        'pytest >= 8.0.0'
    ],
    python_requires='>=3.7, <4',
)
