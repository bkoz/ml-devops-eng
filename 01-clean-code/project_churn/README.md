# Predict Customer Churn

- Project **Predict Customer Churn** of ML DevOps Engineer Nanodegree Udacity

## Project Description
Your project description here.

## Files and data description
Overview of the files and data present in the root directory. 

## Development Environment

- Apple Silicon M1 MacBookAir
- MacOS Monterey 12.3.1

Errors were reported installing `shap`and `llvmlite` under a python 3.9 virtual env.
I had sucesss creating the following stack using [miniforge](https://github.com/conda-forge/miniforge) with a python 3.8 base.

```
conda env create -f environment.yaml
```

Manual steps for creating the Conda environment.

```
conda create --name=ml-devops-eng python=3.8
conda activate ml-devops-eng
conda install shap
conda install scikit-learn
conda install joblib pandas numpy
conda install matplotlib seaborn
conda install pylint autopep8
conda install jupyterlab
```

## Running Files
How do you run your files? What should happen when you run your files?



