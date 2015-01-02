cranberry
=========

Cranberry is an OPTICS clustering library for Python with a simiple and easy to use interface. The module currently works on 2-dimensional data but will soon be modified to accomondate for more dimensions. To use the library, instatiate an `OPTICS` class and run the `fit` function on a list of tuples, as such:

````python
from cranberry.optics import OPTICS

data = [()]

clusterer = OPTICS(epsilon = 0.5, min_samples = 5)
clusterer.fit(data)
```
