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
fig = splom(X,feature-names,classvar = C,order = 1,fname="myplot.png")

```
