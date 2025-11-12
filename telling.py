def tell_tegn(tegn, tekst):
  antall = 0
  for i in tekst:
    if i == tegn:
      antall += 1
  return antall


print(tell_tegn('a', 'banana'))
