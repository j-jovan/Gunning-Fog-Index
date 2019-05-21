#https://en.wikipedia.org/wiki/Gunning_fog_index
#Skripta ne moze da se kompajluje iz nepoznatog razloga.
#Potrebno dodati specificne reci iz srpskog jezika u formulu
#Potrebno dodati rezultate testa, poput 'Osnovna skola', 'Srednja skola'
from time import sleep

while(True):
	
	unetTekst = input("Unesi tekst\n")

	listaReci = unetTekst.split() #Lista koja sadrzi broj reci podeljenih

	brojReci = len(listaReci)
	brojRecenica = len(unetTekst.split("."))-1 + len(unetTekst.split("!"))-1 + len(unetTekst.split("?"))-1 + len(unetTekst.split("..."))-1
	brojKompleksnihReci = 1 #Kompleksna rec je rec koja ima 3 ili vise vokala

	if(brojRecenica < 0): #Privremeni fix. 
		print("Sistem ne prepoznaje nijednu recenicu.")
		break

	for unetTekst in listaReci:
		brojVokala = unetTekst.count('a') + unetTekst.count('e') + unetTekst.count('i')+ unetTekst.count('o')+ unetTekst.count('u') #Zbir vokala u svakoj unetoj reci
		if(brojVokala >= 3):
			brojKompleksnihReci += 1

	gunningFogIndex = 0.4*((brojReci/brojRecenica)+100*(brojKompleksnihReci/brojReci)) #Formula za Gunning Fog Index

	print (gunningFogIndex)

	opet = input("Da li želiš da uneses nov tekst?\n").lower()

	if(opet == "y" or "yes" or "da"): #Ako korisnik unese 'y', ponovi petlju
		print("")
	
	if(opet == "n" or "no" or "ne"): #Ako korisnik unese 'n', izadji iz petlje
		print("Doviđenja")
		break

	else: #Ako korisnik ne izabere nista, ponovi petlju
		print("")
	