#! /usr/bin/python3


from pwn import *
import math

HOST = 'misc.csaw.io'
PORT = 3000

lst = []

# Extract from a0 to a29
for i in range(0, 30):
    p = remote(HOST, PORT)

    for j in range(30):
        if j == i:
            p.sendlineafter(b'Enter your input: \r\n', b'1')
        else:
            p.sendlineafter(b'Enter your input: \r\n', b'0')
    print(f"Sent {i}!")

    p.recvline()
    lst.append(p.recvline())
    print(lst)
    p.close()


# Extract b
p = remote(HOST, PORT)

for j in range(30):
    p.sendlineafter(b'Enter your input: \r\n', b'0')
print(f"Sent 30!")

p.recvline()
lst.append(p.recvline())
print(lst)
p.close()

# Construct Flag
# lst = [b'1.603810890548638e-28\r\n', b'1.8048513878454153e-35\r\n', b'1.1850648642339812e-27\r\n', b'3.305700626760734e-37\r\n', b'1.603810890548638e-28\r\n', b'6.639677199580733e-36\r\n', b'7.984904245686979e-30\r\n', b'6.054601895401186e-39\r\n', b'8.315280276641321e-07\r\n', b'8.75651076269652e-27\r\n', b'6.639677199580733e-36\r\n', b'1.0806392777072785e-30\r\n', b'2.2603242979035746e-06\r\n', b'2.4426007377405277e-36\r\n', b'2.9374821117108028e-30\r\n', b'1.0806392777072785e-30\r\n', b'2.0611536181902037e-09\r\n', b'8.75651076269652e-27\r\n', b'8.315280276641321e-07\r\n', b'8.75651076269652e-27\r\n', b'3.305700626760734e-37\r\n', b'4.1399375473943306e-08\r\n', b'1.522997951276035e-08\r\n', b'8.75651076269652e-27\r\n', b'1.8048513878454153e-35\r\n', b'8.315280276641321e-07\r\n', b'2.9374821117108028e-30\r\n', b'7.281290178321645e-33\r\n', b'4.1399375473943306e-08\r\n', b'8.194012623990515e-40\r\n', b'0.9999999999999993\r\n']

newlst = [float(l.strip()) for l in lst]
adapt_to_logistic = [math.ceil(math.log(l / (1 - l))) for l in newlst]
flag_chars = [chr(-(c - adapt_to_logistic[-1])) for c in adapt_to_logistic]
flag = ''.join(flag_chars)

print(flag)