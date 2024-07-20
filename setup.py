from setuptools import setup, find_packages


PACKAGES = [
    "matplotlib==3.9.1",
    "mlflow==2.14.3",
    "mpmath==1.3.0",
    "networkx==3.2.1",
    "numpy==1.26.3",
    "nvidia-cublas-cu11==11.11.3.6",
    "nvidia-cuda-cupti-cu11==11.8.87",
    "nvidia-cuda-nvrtc-cu11==11.8.89",
    "nvidia-cuda-runtime-cu11==11.8.89",
    "nvidia-cudnn-cu11==8.7.0.84",
    "nvidia-cufft-cu11==10.9.0.58",
    "nvidia-curand-cu11==10.3.0.86",
    "nvidia-cusolver-cu11==11.4.1.48",
    "nvidia-cusparse-cu11==11.7.5.86",
    "nvidia-nccl-cu11==2.20.5",
    "nvidia-nvtx-cu11==11.8.86",
    "opentelemetry-api==1.25.0",
    "opentelemetry-sdk==1.25.0",
    "opentelemetry-semantic-conventions==0.46b0",
    "packaging==24.1",
    "pandas==2.2.2",
    "pillow==10.2.0",
    "protobuf==4.25.3",
    "pyarrow==15.0.2",
    "pynvml==11.5.3",
    "pyparsing==3.1.2",
    "python-dateutil==2.9.0.post0",
    "pytz==2024.1",
    "PyYAML==6.0.1",
    "querystring-parser==1.2.4",
    "requests==2.32.3",
    "threadpoolctl==3.5.0",
    "torch==2.3.1+cu118",
    "torchaudio==2.3.1+cu118",
    "torchvision==0.18.1+cu118",
    "triton==2.3.1",
    "typing_extensions==4.9.0",
    "tzdata==2024.1",
    "urllib3==2.2.2",
    "Werkzeug==3.0.3",
    "wrapt==1.16.0",
    "zipp==3.19.2"
]



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
        'console_scripts': ['mlflow-pytorch-exp=mlflow_pytorch_exp.mlflow_pytorch_exp:main'],
    },
)
