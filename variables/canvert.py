def myfunc():
  global x
  x = 300
  #nonlocal x
  print(x)

myfunc()

print(x)
