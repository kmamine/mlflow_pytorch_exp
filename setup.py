from setuptools import setup, find_packages

setup(
    name='mlflow-pytorch-exp',
    version='0.0.1',
    description='Create a PyTorch project with MLflow boilerplate.',
    author='Your Name',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['mlflow-pytorch-exp=mlflow_pytorch_exp.train:main'],
    },
)
