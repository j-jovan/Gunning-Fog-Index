#https://en.wikipedia.org/wiki/Gunning_fog_index

while(a):
	unetTekst = input("Unesi tekst\n")

	listaReci = unetTekst.split() #Lista koja sadrzi broj reci podeljenih

	brojReci = len(listaReci)
	brojRecenica = len(unetTekst.split("."))-1
	brojKompleksnihReci = 1 #Kompleksna rec je rec koja ima 3 ili vise vokala

	for unetTekst in listaReci:
		brojVokala = unetTekst.count('a') + unetTekst.count('e') + unetTekst.count('i')+ unetTekst.count('o')+ unetTekst.count('u') #Zbir vokala u svakoj unetoj reci
		if(brojVokala >= 3):
			brojKompleksnihReci += 1

	gunningFogIndex = 0.4*((brojReci/brojRecenica)+100*(brojKompleksnihReci/brojReci)) #Formula za Gunning Fog Index

	print (gunningFogIndex)

	opet = input("Da li želiš da uneses nov tekst? y/n\n").lower()

	if(opet == "y"):
		print("Idemo opet")

	elif(opet == "n"):
		print("Doviđenja")
		input("Pritisni bilo koje dugme za kraj.")
		a = False
	