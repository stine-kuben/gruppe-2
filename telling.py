def tell_tegn(tegn, tekst):
  antall = 0
  for karakter in tekst:
    if karakter == tegn:
      antall += 1
  return antall


print(tell_tegn('a', 'banana'))
