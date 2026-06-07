#Please write a program to compress and decompress the string "hello world!helloworld!hello world!hello world!".

import zlib

string= "hello world!helloworld!hello world!hello world!"

data=string.encode()

compressed_data=zlib.compress(data)

print("Compressed data")

print( f"\n{compressed_data} ")

decommpresed=zlib.decompress(compressed_data)

data2=decommpresed.decode()

print("Decompressed data")

print(f"\n{data2}")