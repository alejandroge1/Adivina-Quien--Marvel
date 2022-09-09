import cv2
import mysql.connector

def insetar_personaje(Nombre,Valor,Héroe,Poderes,Armas,Humano,Vivo):
    cur= cnn.cursor()
    sql= '''INSERT INTO personajes(Nombre,Valor,Héroe,Poderes,Armas,Humano,Vivo) 
    VALUES("{}","{}","{}","{}","{}","{}","{}")'''.format(Nombre,Valor,Héroe,Poderes,Armas,Humano,Vivo)
    cur.execute(sql)
    cnn.commit()
    cur.close()
    
while True:

    cnn = mysql.connector.connect(host='localhost',
                          user='root',
                          passwd='Sacomode',
                          database= 'marvel')
        
    img = cv2.imread("tablaverdad.jpg")
    respuesta=""
    Variables= "01"
    
    print ("\n\nAdivina Quién: Edición MARVEL")
    
    print ("Selecciona un personaje para contestar las siguientes preguntas:")
    input("Presiona Enter para ver los personajes y despues cero para continuar el programa--->\n")
    
    cv2.imshow('Listado de Personajes',img)
    cv2.waitKey(0)
    
    
    while True:
            print("\nResponde todas las preguntas colocando un 1 para verdadero y 0 para falso:")
            print("1.¿Tu personaje es un héroe?")
            Input = input("Introduce tu respuesta:")
            
            if len(Input) == 1 and all(i in Variables for i in Input):
                r_heroe = Input
                respuesta= Input+respuesta
                break
            else:
                print("\nError, sigue las instrucciones")
                input("***Enter para continuar***\n\n")
                
    while True:
            print("\n2.¿Tu personaje tiene poderes?")
            Input = input("Introduce tu respuesta:")
            if len(Input) == 1 and all(i in Variables for i in Input):
                r_poderes = Input
                respuesta= Input+respuesta
                break
            else:
                print("\nError, sigue las instrucciones")
                input("***Enter para continuar***\n\n")
                
    while True:
            print("\n3.¿Tu personaje posee armas o equipamiento?")
            Input = input("Introduce tu respuesta:")
            if len(Input) == 1 and all(i in Variables for i in Input):
                r_armas = Input
                respuesta= Input+respuesta
                break
            else:
                print("\nError, sigue las instrucciones")
                input("***Enter para continuar***\n\n")
                
    while True:
            print("\n4.¿Tu personaje es humano?")
            Input = input("Introduce tu respuesta:")
            if len(Input) == 1 and all(i in Variables for i in Input):
                r_humano = Input
                respuesta= Input+respuesta
                break
            else:
                print("\nError, sigue las instrucciones")
                input("***Enter para continuar***\n\n")
                
    while True:
            print("\n5.¿Tu personaje está vivo en el universo cinematográfico de Marvel (MCU)?")
            Input = input("Introduce tu respuesta:")
            if len(Input) == 1 and all(i in Variables for i in Input):
                r_vivo= Input
                respuesta= Input+respuesta
                break
            else:
                print("\nError, sigue las instrucciones")
                input("***Enter para continuar***\n\n")
                
    
    respuesta= respuesta[::-1]
    
    cur= cnn.cursor()
    sql= '''SELECT Nombre FROM personajes WHERE Valor = "{}"'''.format (respuesta)
    cur.execute(sql)
    guess= cur.fetchall()
    cur.close
    
    longitud= len(guess)
    
    if longitud == 0 :
        print("\n***Este personaje no existe en la base de datos pero se agregara para el siguiente juego***")
        r_nombre= input("\nEscribe su nombre--->")
        insetar_personaje(r_nombre,respuesta,r_heroe,r_poderes,r_armas,r_humano,r_vivo)
    else:
        print("\n\nTu personaje es: ")
        print(guess)
   
    print ("\n¿Quieres seguir jugando?\nPresiona 1 para si o cualquiera para no.")
    Desicion= input()
   
    if Desicion != "1":
        break

cv2.destroyAllWindows()
cnn.close()
