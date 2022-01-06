from setuptools import setup, find_packages
from pathlib import Path

root = Path(__file__).parent.resolve()

required = (root / 'requirements.txt').read_text(encoding='utf-8')

setup(
    name="kube_sample",
    version="0.1",
    author="Carlos Donado",
    author_email="cf.donado@hotmail.com",
    packages=find_packages(),
    install_requires=required,
    # entry_points={
    #     'console_scripts': ['ast-cli=src.backend.commands:cli']
    # }
)
