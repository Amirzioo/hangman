from lib2to3.pytree import LeafPattern
import random
from tkinter import W
import os

def mensaje():
    
    print("¡Adivina la palabra!")
    # # print("Ingresa tu nombre")
    # # nombre = input()
    # # print("Hola A" + nombre + ", bienvenido al juego del ahorcado. \n")

def read():
    dict = []
    with open("/home/amir/Documents/Platzi/Python/Intermedio/proyecto_hangman/data.txt","r", encoding = "utf-8") as f:
       dict = f.read()    
    word = random.choice(dict.split()) 
    #print(dict)
    return word
#Hace falta agregar una corrección para los acentos y las mayúsculas.

def guess(word):
    try:
        word_to_guess = word 
        word_guessed = len(word_to_guess) * "_"
  
        while word_to_guess != word_guessed:

          print("Adivina la palabra: \n")
          print("La palabra tiene " + str(len(word)) + " letras.")
          print(" ".join(word_guessed).upper())

          guess = input()
          if guess in word_to_guess:
            word_guessed = list(word_guessed)
            for i,x in enumerate(word_to_guess):
                if x == guess:
                    word_guessed[i] = x
            word_guessed = "".join(word_guessed)
          os.system("clear")       
                
        print("¡Ganaste! Eres el mejor" )
        print("La palabra que adivinaste era: " + word_guessed)
        play_again = input("¿Quieres volver a jugar? \n1. Sí \n2. No \n")

        if play_again == 1:
            run()
        elif play_again == 0:
            print("Hasta la próxima :)")
            
    except ValueError:
            print("Sólo debes ingresar letras")
        
def run():

    #mensaje()
    w = read()
    #print(w)
    guess(w)



if __name__ == "__main__":
    run()