# data = b'\x00\x00\x00@\x01\x00\x00@\x02\x00\x00\xc0'
# hexstring = data.hex()

# while len(hexstring) > 0:
#     display = hexstring[:8]
#     hexstring = hexstring[8:]
#     print(display[::-1])


# with open("3bins", "wb") as outfile:
#     outfile.write(data)

# New


def to32bitlist(hexstring, reverse=False):
    print(hexstring)

    if reverse:
        blist = bytearray.fromhex(ohexstring)[::-1]
        hexstring = blist.hex()

    fourbyteList = []
    while len(hexstring) > 0:
        fourbyteList.append(hexstring[:8])
        hexstring = hexstring[8:]
    print(fourbyteList)
    return fourbyteList

data = b'\x00\x00\x00@\x01\x00\x00@\x02\x00\x00\xc0'
ohexstring = data.hex()
to32bitlist(ohexstring)

# print(f"Original bytes2hex: {ohexstring}")
bb  = bytearray.fromhex(ohexstring)[::-1]
nhexstring = bb.hex()
to32bitlist(nhexstring)
# print(f"Readable bytes2hex: {nhexstring}")


# print(nhexstring)
# while len(nhexstring) > 0:
#     display = nhexstring[:8]
#     nhexstring = nhexstring[8:]
#     print(display)


# with open("3bins", "wb") as outfile:
#     outfile.write(data)
