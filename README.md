# AlgorithmTranslator

Tool for manipulating Rubik's cube algorithms. Supports rotating, inverting and mirroring algs in standard notation.
This is a porting of the javascript code from "http://cube.rider.biz/algtrans.html" to python.

Thanks To Conrad Rider.

[README.MD em Português](README_PT.md)

## Usage

```python
from AlgTrans import AlgTrans

AT = AlgTrans("R U R'")

generated = AT.generate()

for key, value in generated.items():
    print(key + " : " + value)
```

ways to invert algorithm:

```python
from AlgTrans import AlgTrans

AT = AlgTrans("R U R'")

generated = AT.generate()

print(generated['Inverse'])
```

```python
from AlgTrans import AlgTrans

alg = "U R U' R'"

print(AlgTrans().invertAlg(alg))
```

See [main.py](main.py) for more examples.
