from setuptools import setup, find_packages


setup(
    name='mlflow-pytorch-exp',
    version='0.0.1',
    description='Create a PyTorch project with MLflow boilerplate.',
    long_description = open('README.md').read_text()
    author='Mohamed Amine KERKOURI',
    author_email='mohamed.a.kerkouri@gmail.com',
    license = 'MIT',
    packages=find_packages(),
    install_requires = ["mlflow==2.14.3","pynvml==11.5.3" ],
    include_package_data=True,
    package_data={
        'mlflow_pytorch_exp': [
            'templates/checkpoints/*',
            'templates/config/*',
            'templates/data/*',
            'templates/dataloader/*',
            'templates/losses/*',
            'templates/metrics/*',
            'templates/models/*',
            'templates/utils/*'
        ]
    },
    entry_points={
        'console_scripts': ['mlflow-pytorch-exp=mlflow_pytorch_exp.mlflow_pytorch_exp:main'],
    },
)
