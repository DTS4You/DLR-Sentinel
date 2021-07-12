import VSP
VSP.open()
s = ""
while s != "quit":
  n = VSP.rx()
  if n >= 0:
    VSP.tx(n)
    s = (s + chr(n))[-4:]
VSP.close()