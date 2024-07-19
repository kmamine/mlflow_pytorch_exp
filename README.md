# mlflow_pytorch_exp    


1. Build  the packege:

```bash
python setup.py sdist
```

2. Install package :

```bash
pip install dist/mlflow-pytorch-exp-0.1.0.tar.gz
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


# TODO 

[] Still can't create a project 

