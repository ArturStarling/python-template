# I like batata

Config .git

```bat
git config --global user.email "arturstarling@hotmail.com"
git config --global user.name "Artur Starling"
```


# Setup

Venv

```bat
python -m venv venv
.\venv\Scripts\activate
```

Dependencies

```bat
python -m pip install --upgrade pip
pip install --upgrade cython
pip install wheel
pip install -r dev-requirements.txt
```


# Freezing

## With Windows

```bat
pip freeze > win32-requirements.txt
```
## With Windows (dev environment)


```bat
pip freeze > dev-win32-requirements.txt
```

## With Ubuntu

```bat
pip freeze > ubuntu-requirements.txt
```
## With Ubuntu (dev environment)


```bat
pip freeze > dev-ubuntu-requirements.txt
```