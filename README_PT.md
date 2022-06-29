# AlgoritmoTradutor

Ferramenta para manipular algoritmos de cubo de Rubik. Suporta rotação, inversão e espelhamento de algs em notação padrão.
Esta é uma portabilidade do código javascript de "http://cube.rider.biz/algtrans.html" para python.

Um agradecimento especial para Conrad Rider.

[README.MD in English](README.md)

## Uso

``` python
from AlgTrans import AlgTrans

AT = AlgTrans("R U R'")

generated = AT.generate()

for key, value in generated.items():
    print(key + " : " + value)
```

maneiras de inverter o algoritmo:

``` python
from AlgTrans import AlgTrans

AT = AlgTrans("R U R'")

generated = AT.generate()

print(generated['Inverse'])
```

``` python
from AlgTrans import AlgTrans

alg = "U R U' R'"

print(AlgTrans().invertAlg(alg))
```

Veja [main.py](main.py) para mais exemplos.
