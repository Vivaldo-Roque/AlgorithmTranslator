
from AlgTrans import AlgTrans

AT = AlgTrans("R U R'")

generated = AT.generate()

for key, value in generated.items():
    print(key + " : " + value)

print()

#print(generated['Inverse'])

#alg = "U R U' R'"

#Inverse
#print(AT.invertAlg(alg))

#Rotate x
#print(AT.transAlg(alg, AT.XTR))

#Rotate y
#print(AT.transAlg(alg, AT.YTR))

#Rotate z
#print(AT.transAlg(alg, AT.ZTR))

#Mirror L/R
#print(AT.transAlg(alg, AT.MTR))

#Mirror F/B
#print(AT.transAlg(alg, AT.STR))

#Mirror U/D
#print(AT.transAlg(alg, AT.ETR))