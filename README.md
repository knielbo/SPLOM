# SPLOM
Scatter plot matrix with/without class information. Class information should be
last column with header 'class'.

## Usage
```bash
$ python splom.py dat/iris.dat

```
or
```py
from splom import splom

# with class
fig = splom(X, X_names, classvar = X_class, order = 1, fname="splom_class.png")

# without class
fig = splom(X, X_names, order = 1, fname="splom_noclass.png")

```
