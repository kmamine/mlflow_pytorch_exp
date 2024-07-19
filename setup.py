from setuptools import setup, find_packages
from .config import PACKAGES 

def get_requirments():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='mlflow-pytorch-exp',
    version='0.0.1',
    description='Create a PyTorch project with MLflow boilerplate.',
    author='Mohamed Amine KERKOURI',
    author_email='mohamed.a.kerkouri@gmail.com',
    license = 'MIT',
    packages=find_packages(),
    install_requires = PACKAGES,
    entry_points={
        'console_scripts': ['mlflow-pytorch-exp=mlflow_pytorch_exp.train:main'],
    },
)
