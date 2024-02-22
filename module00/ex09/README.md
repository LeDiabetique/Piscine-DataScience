
## Create the package

```sh
pip install --upgrade setuptools wheel
python setup.py sdist bdist_wheel
```
## Install the package

```sh
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```
or
```sh
pip install ./dist/ft_package-0.0.1.tar.gz
```
## Uninstall the package

```sh
pip uninstall ft_package
```