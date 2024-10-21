import binascii
text = 102740453687142852317864098784299626183297464100221

res = binascii.unhexlify(hex(text)[2:])
print(res)
