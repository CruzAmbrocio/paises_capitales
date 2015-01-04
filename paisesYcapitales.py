biblioteca={}
biblioteca2=[]
def inicio():
	question=raw_input("Do you want to insert another Countries and Capital --Countries--")
	questionlower=question.lower()
	if questionlower == "Countries" or questionlower == "countries" or questionlower == "Countries " or questionlower == "countries ":
		addCountries()
	else:
		print "Ingresa una opcion valida"
		inicio()

def menu():
	print"  "
	print "welcome to Countries and Capitals "
	print"  "
	print "Opciones:  "
	print "Write Countriess if you want to add an item."
	print "Press Capitals if you want to sell an item."
	print "Press All if you want to exit."
	print "Write AllOrdered para ordenado"
	print "Write AllMail para enviar al correo"
	try:
		options=raw_input("Choose an option:  ")
		if options == "Countriess":
			listCoutries()
		elif options== "capitals":
			addCountries()

	except ValueError:
		print "Enter valid option for the Menu:  "
		menu()
def listCoutries():
	for i in biblioteca2:
		print i
	menu()

def addCountries():
	"""Esta funcion permite agregar datos a las listas y diccionarios"""
	try:
		key = raw_input("Add item: ")
		keylow = key.lower()
		biblioteca2.append(keylow)
		global value
		value= raw_input("Add price: ")
		biblioteca[key]=value
		print biblioteca
		print biblioteca2
		again()
	except ValueError:
		print "Ingresa correctamente los datos"
		addCountries()
def again():
	"""Esta funcion pregunta si se quieren agregar oto pais"""
	question=raw_input("Do you want to insert another Countries and Capital y/n ")
	questionlower=question.lower()
	if questionlower == "y" or questionlower == "yes" or questionlower == "y " or questionlower == "yes ":
		addCountries()
	elif questionlower == "n" or questionlower == "no" or questionlower == "n " or questionlower == "no ":
		menu()
	else:
		print "ingresa una opcion valida y/n"
		again()
inicio()