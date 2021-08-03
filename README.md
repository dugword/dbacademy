# `DB Academy`

## Purpose
This repository is an incubator for internal libraries used to test and develop curriculum. It should be assumed that modules will be promoted to more distinct, resuable components as they mature.

## Getting Started
While intended to be used in both notebook/online/remote and "traditional"/offline/local development, this module is specifically structured for local development and as such requires a Conda environment. Instructions to setup the Conda environment are as folllows:
```
conda create -n dbacademy python=3.8
conda activate dbacademy
pip install -r requirements.txt
```
Once setup, unit tests can by ran by executing
```pytest```

## Usage - Notebook/Online/Remote
To use this module in your notebook add to the first command the following call:<br/>
```%pip install git+https://github.com/databricks-academy/dbacademy```
