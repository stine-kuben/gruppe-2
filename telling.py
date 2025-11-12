def er_tre_like(verdi1, verdi2, verdi3):
  return verdi1 == verdi2 == verdi3



tallListe = [5, 7, 13, 2]
def dobleListe(tallListe):
  tallListe_dobbel = []
  for tall in tallListe:
    ny_tall = tall*2
    tallListe_dobbel.append(ny_tall)
  return tallListe_dobbel 

print(dobleListe(tallListe))
def tell_tegn(tegn, tekst):
  antall = 0
  for karakter in tekst:
    if karakter == tegn:
      antall += 1
  return antall


print(tell_tegn('a', 'banana'))
