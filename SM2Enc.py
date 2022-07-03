from gmssl import sm2
from base64 import b64encode, b64decode

privateKey = '5444374893e81cdb80debcac293c637f7803e195c799dae6a7c4081e793eea6c'
publicKey = '8410a756ea14225f3b0981b8801ecf2a9ca40de01502e834c1d365840cac6a642db11b12f6d01a1a5a51cd49c00bb248bc5be51ac90542b3b162f7853ebcdfe5'
sm2Crypt = sm2.CryptSM2(public_key=publicKey, private_key=privateKey)

class sm2Encrypt:
    def enc(self, info):
        encode_info = sm2Crypt.encrypt(info.encode(encoding="utf-8"))
        encode_info = b64encode(encode_info).decode()
        return encode_info

    def dec(self, info):
        decode_info = b64decode(info.encode())
        decode_info = sm2Crypt.decrypt(decode_info).decode(encoding="utf-8")
        return decode_info

m = 'sm2EncryptionAndDecryption'
sm2 = sm2Encrypt()
c = sm2.enc(m)
print('加密后：',c)
mm = sm2.dec(c)
print('解密后：',mm)