# animal = "CHAT"

# match animal:
#     case "chien":
#         print("Wouf !")
#     case "chat" | "CHAT" :
#         print("Miaou !")
#     case "oiseau":  
#         print("Cui cui !")
#     case "vache":
#         print("Meuh !")
#     case "mouton":
#         print("Bêêê !")
#     case _:
#         print("Je ne connais pas cet animal !")

# for x in range(90, 100):
#     print(f"{x} bouteilles de bière sur le mur")

# capacite_maximale = 10
# capacite_actuelle = 3
# while capacite_actuelle < capacite_maximale:
#     print(capacite_actuelle)
#     capacite_actuelle += 1

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# def message():
#     print("Hello World")

# message()

# def afficher_nom_prenom(nom, prenom):
#     print("nom :", nom)
#     print("prenom :", prenom)

# afficher_nom_prenom("Doe", "John")

# def addition(a, b):
#     resultat = a + b
#     return resultat

# somme = addition(5, 10)
# print(somme)

# numerateur = input("Entrez le numérateur : ")
# denominateur = input("Entrez le dénominateur : ")

# try:
#     resultat = int(numerateur) / int(denominateur)
#     print(resultat)
# except ZeroDivisionError:
#     print("La division par zéro est impossible !")
# except ValueError:
#     print("Vous devez entrer un nombre !")




# def division(numerator, denominateur):

# numerator = input("Entrez le numérateur : ")
# denominateur = input("Entrez le dénominateur : ")
# try:
#     result = numerator / denominateur
#     return result
# except ZeroDivisionError:
#     print("Erreur : division par zéro")

# """
# Mini-calculatrice

# """


# def print_welcome_message():
#     print("Bienvenue sur la mini-calculatrice !")
    
# def input_two_number():
#     num1 = float(input("Entrez le premier nombre : "))
#     num2 = float(input("Entrez le deuxième nombre : "))
#     return num1, num2

# def print_menu_and_get_choice():
#     print("=== MENU ===")
#     print("1. Addition")
#     print("2. Soustraction")
#     print("3. Multiplication")
#     print("4. Division")

#     user_choice = input("Entrez votre choix (1-4) : ")

#     while user_choice not in ["1", "2", "3", "4"]:

#         user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")

#     return user_choice

# def sum(a, b):
#     return a + b

# def substraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b

# def division(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("Erreur : division par zéro")

# def run_calculation(user_choice):
#     num1, num2 = input_two_number()
#     match user_choice:
#         case '1':
#             result = sum(num1, num2)
#         case '2':
#             result = substraction(num1, num2)
#         case '3':
#             result = multiplication(num1, num2)
#         case '4':
#             result = division(num1, num2)
#         case _:
#             print("Choix invalide.")
#     return result

# if __name__ == '__main__':
#     print_welcome_message()
#     user_choice = print_menu_and_get_choice()
#     result = run_calculation(user_choice)
#     print(result)


# import requests

# if __name__ == '__main__':
#     resultat = requests.get("https://www.google.fr")
#     print(resultat.content)

# import requests

# url = "https://www.gov.uk/search/news-and-communications"
# page = requests.get(url)

# # Voir le code html source
# print(page.content)

# import requests

# from bs4 import BeautifulSoup

# url = "https://www.gov.uk/search/news-and-communications"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')

# fichier = open("hello.txt", "w")
# fichier.write("Hello World !")
# fichier.close()

# with open("file.txt") as fichier:
#     for ligne in fichier:
#         # faire quelque chose avec une ligne
#         print(ligne)

# import csv

# with open('couleurs_preferees.csv') as fichier_csv:
#     reader = csv.DictReader(fichier_csv, delimiter=',')
#     for ligne in reader:
#         print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])
#         print(ligne)


# user = [1,2,3,4,5,6,7,8,9,10]
# print(user[7:0:-2])

import requests
r = requests.get("http://www.facebook.com")
print(r.status_code)
