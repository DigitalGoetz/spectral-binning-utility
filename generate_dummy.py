data = b'\x00\x00\x00@\x01\x00\x00@\x02\x00\x00\xc0'
hexstring = data.hex()

while len(hexstring) > 0:
    display = hexstring[:8]
    hexstring = hexstring[8:]
    print(display[::-1])


with open("dummy.sb", "wb") as outfile:
    outfile.write(data)