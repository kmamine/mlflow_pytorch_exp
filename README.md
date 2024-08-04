![https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white](https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white)


# mlflow_pytorch_exp    

# install from PyPI
```bash
pip install mlflow-pytorch-exp==0.0.1
```

# Create a project 
```bash
mlflow-pytorch-exp create <path/to/folder>```
```

# Insall manually 
1. Build  the packege:

```bash
python setup.py sdist bdist_wheel
```

2. Install package :

```bash
pip install dist/mlflow_pytorch_exp-0.0.1-py3-none-any.whl
```

3. Create project 
```bash
mlflow-pytorch-exp create <path/to/folder>```
```

example : 
```bash
mlflow-pytorch-exp create my_project
```



```bash
mlflow_pytorch_exp
├── LICENSE
├── MANIFEST.in
├── mlflow_pytorch_exp
│   ├── __init__.py
│   ├── mlflow_pytorch_exp.py
│   └── templates
│       ├── checkpoints
│       ├── config
│       │   └── config.py
│       ├── data
│       ├── dataloader
│       │   └── dataset.py
│       ├── losses
│       │   └── loss.py
│       ├── metrics
│       │   └── metric.py
│       ├── models
│       │   └── model.py
│       ├── train.py
│       └── utils
│           └── utils.py
├── README.md
└── setup.py
```



