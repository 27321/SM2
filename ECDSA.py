import ecdsa
import random
import hashlib

gen=ecdsa.NIST256p.generator
order=gen.order()

privateKey = random.randrange(1,order-1)
publicKey = ecdsa.ecdsa.Public_key(gen,gen * privateKey)
private_key = ecdsa.ecdsa.Private_key(publicKey,privateKey)

message = "ecdsa"
m = int(hashlib.sha1(message.encode("utf8")).hexdigest(),16)
k = random.randrange(1,order-1)
signature = private_key.sign(m,k)
r = signature.r
s = signature.s