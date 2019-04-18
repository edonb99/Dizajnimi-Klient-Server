from socket import *
import random
import datetime
import sys
import threading
import math


print("=============================================================================================")
print('*******  FIEK-TCP Serveri  **********')
print("=============================================================================================")

# IP adresa
serverName = '127.0.0.1'

# Porti 12000 ndahet per soketin e serverit:
serverPort = 12000

# krijimi i soketetit te serverit sipas TCP-protokollit
serverSocket = socket(AF_INET, SOCK_STREAM)

# lidhja e portit të serverit dhe ip adreses me socketin e krijuar
serverSocket.bind((serverName,serverPort))

print('Serveri startoi ne localhost me IP adrese: '+str(gethostbyname(gethostname()))+" ne portin: "+str(serverPort)) 


# pasiqe krijimit te soketit, presim per nje klient te lidhet me server:
serverSocket.listen(5)

print('Serveri eshte i gatshem te pranoj kerkesa.')


# METODAT 
#
#
#
def IPADRESA(address):
    return str(address[0])


def NUMRIIPORTIT(address):
    return str(address[1])


def BASHKETINGELLORE(teksti):
    numriBashketingelloreve = 0
    bashketingelloret = " b c ç d dh f g gj h j k l ll m n nj p q r rr s sh t th v x xh z zh  B C Ç D Dh F G Gj H J K L Ll M N Nj P Q R Rr S Sh T Th V X Xh Z Zh"
    for i in range(1, len(teksti)):
        if teksti[i] in bashketingelloret:
            numriBashketingelloreve +=1
    return str(numriBashketingelloreve)


def PRINTIMI(teksti):
    teksti = str(teksti).strip()
    return teksti

def HOST():
    try:
        hosti = socket.gethostname()
        pergjigja = "Emri i hostit eshte: " + hosti
        return (str(pergjigja))
    except:
        pergjigja = "Emri i hostit nuk mund te percaktohet!"
        return str(pergjigja)


def TIME():
    return str(datetime.datetime.now())

def LOJA():
    listaNumrave = []
    for i in range(7):
        listaNumrave.append(random.randint(1,49))
    listaNumrave.sort()
    return str(listaNumrave)

def FIBONACCI(vlera):
    numri = 1
    numripr = 0
    numriDhene = 0
    numriDhene = int(vlera)
    for i in range(numriDhene-1):
        numri = numri + numripr
        numripr = numri - numripr
    return str(numri)


def KONVERTIMI(opcioni,vlera):
    vleraKonvertuar = 0
    vlera = float(vlera)

    if  opcioni=="KILOWATTTOHORSEPOWER":
        return str(vlera/0.745699872)
    elif opcioni=="HORSEPOWERTOKILOWATT":
        return str(vlera*0.745699872)
    elif opcioni=="DEGREESTORADIANS":
        return str(vlera*3.14/180)
    elif opcioni=="RADIANSTODEGREES":
        return str(vlera*180/3.14)
    elif opcioni=="GALLONSTOLITERS":
        return str(vlera/0.26417)
    elif opcioni=="LITERSTOGALLONS":
        return str(vlera*0.26417)
    else:
        return "ERROR, keni berim gabim gjate shenimit"


def GJUJZARET():
    min = 1
    max = 6
    kubi1 = str(random.randint(min, max))
    kubi2 = str(random.randint(min, max))
    pergjigja = str("Vlerat e zareve jane:   " + kubi1 + " dhe " + kubi2)
    return pergjigja


def PRIME(numri):
    x=True;
    for x in range(2,numri):
        if numri%x ==0:
            x=False;
            return x;
    return x;
    



# te gjitha te dhenat qe dergohen te klienti kjo metode i printon edhe te serveri
def ShtypTeDhenat(teDhenat):
    print("\n----------------------------------------------------------------------------------------------")
    print("Te dhenat e derguara te klienti ======== >>  ", teDhenat)
    return





# funksioni ku shfaqet klienti i ri ne server, ky funksion thirret tek threading
def klienti_i_ri(connectionSocket,addr):
    
    kerkesa = (bytes)("empty".encode())
    try:
        while str(kerkesa.decode()).upper()!="EXIT" and str(kerkesa.decode())!="":
            # pranimi i kerkeses nga klienti
            kerkesa = connectionSocket.recv(128)

            # dekodimi i kerkeses
            kerkesaStr = str(kerkesa.decode()).strip()

            # behet ndarja e kerkeses sipas hapesirave dhe ruhet ne njw Array
            kerkesaArray = kerkesaStr.split(' ')

            # kerkesa e derguar nga klienti kthehet se pari ne upperCase:
            kerkesaArray[0] = kerkesaArray[0].upper()

            # metoda IPADRESA
            if kerkesaArray[0]=="IPADRESA":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("IP adresa juaj eshte: "+IPADRESA(addr)).encode())
                    ShtypTeDhenat(("IP adresa e klientit: "+IPADRESA(addr)))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")

            # metoda NUMRIIPORTIT
            elif kerkesaArray[0]=="NUMRIIPORTIT":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Numri i portit tuaj eshte: "+NUMRIIPORTIT(addr)).encode())
                    ShtypTeDhenat(("Numri i portit te klientit eshte: "+NUMRIIPORTIT(addr)))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")

               # metoda BASHKETINGELLORE
            elif kerkesaArray[0]=="BASHKETINGELLORE":
                if len(kerkesaArray) == 2:
                    rezultati = "Numri i bashketingelloreve ne fjalen e dhene eshte: " + BASHKETINGELLORE(kerkesaArray[1])
                    connectionSocket.send(rezultati.encode())
                    ShtypTeDhenat(rezultati)
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")

            # metoda PRINTIMI
            elif kerkesaArray[0]=="PRINTIMI":
                kerkesaStr2 = (str(kerkesaStr)).replace("PRINTIMI","")
                connectionSocket.send(("Fjalia e printuar: " + PRINTIMI(kerkesaStr2)).encode())
                ShtypTeDhenat(("Fjalia e printuar: " + PRINTIMI(kerkesaStr2)))

            # metoda HOST
            elif kerkesaArray[0]=="HOST":
                if len(kerkesaArray) == 1:
                    if HOST()=="Emri i hostit nuk mund te percaktohet!":
                        connectionSocket.send(("Emri i hostit nuk mund te percaktohet!").encode())
                        ShtypTeDhenat("Emri i hostit nuk mund te percaktohet!")
                    else:
                        connectionSocket.send(("Emri i klientit eshte: "+HOST()).encode())
                        ShtypTeDhenat(("Emri i klientit eshte: "+HOST()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")

            # metoda TIME
            elif kerkesaArray[0]=="TIME":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Koha e tanishme eshte: " + TIME()).encode())
                    ShtypTeDhenat(("Koha e tanishme eshte: " + TIME()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")

            # metoda LOJA
            elif kerkesaArray[0]=="LOJA":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Rezultati nga loja: " + LOJA()).encode())
                    ShtypTeDhenat(("Rezultati nga loja: " + LOJA()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")
            # metoda FIBONACCI
            elif kerkesaArray[0]=="FIBONACCI":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray)==1 or len(kerkesaArray)>2:
                    connectionSocket.send(("Kerkesa juaj eshte invalide, ju lutem provoni perseri!").encode())
                    ShtypTeDhenat("ERROR")
                else:
                    connectionSocket.send(("Numri i "+kerkesaArray[1]+" ne serine fibonacci eshte: "+FIBONACCI(kerkesaArray[1])).encode())
                    ShtypTeDhenat(("Numri i "+kerkesaArray[1]+" ne serine fibonacci eshte: "+FIBONACCI(kerkesaArray[1])))
            # metoda KONVERTIMI
            elif kerkesaArray[0]=="KONVERTIMI":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray)>3 or len(kerkesaArray)<3:
                    connectionSocket.send(("Kerkesa juaj eshte invalide, ju lutem provoni perseri!").encode())
                    ShtypTeDhenat("ERROR")
                else:
                    konverto = str(kerkesaArray[1]).lower().split("to")
                    pergjigja = kerkesaArray[2] + " " + str(konverto[0]) + " jane te barabarte me " + KONVERTIMI(str(kerkesaArray[1]).upper(),kerkesaArray[2]) + " " + str(konverto[1])
                    connectionSocket.send(str(pergjigja).encode())
                    ShtypTeDhenat(pergjigja)
     
            # metoda shtese GjujZaret - kthen vlerat e dy zareve te gjuajtura.
            elif kerkesaArray[0]=="GJUJZARET":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(str(GJUJZARET()).encode())
                    ShtypTeDhenat(str(GJUJZARET()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("ERROR")

            # metoda shtese Prime 
            elif kerkesaArray[0]=='PRIME':
                    numri = int(kerkesaArray[1]);
                    if PRIME(numri):
                        connectionSocket.send(str.encode("Numri " + str(numri) + " eshte numer i thjeshte!"))
                        ShtypTeDhenat(str("Numri " + str(numri) + " eshte numer i thjeshte!"))
                    else:
                        connectionSocket.send(str.encode("Numri " + str(numri) + " nuk eshte numer i thjeshte!"))
                        ShtypTeDhenat(str("Numri " + str(numri) + " nuk eshte numer i thjeshte!"))





  # nqs. nuk shkruhet asnjera nga metodat e percaktuara
            else:
                connectionSocket.send("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode())
                ShtypTeDhenat("ERROR!")

  # kur largohet klienti mbyllet lidhja me te, por serveri ende pret per lidhje me klient te tjere
                connectionSocket.close()
    except Exception as e: 
                    print("\nERROR: ")
                    print(str(e))
                    connectionSocket.close()
           


# pranimi i kerkesave te njepasnjeshme nga klientet
while 1:
    # ky rresht ben qe serveri te "degjoj" per kerkesa nga klienti permes lidhjes TCP
    connectionSocket, addr = serverSocket.accept()
    print('Klienti me IP adrese %s dhe me numrin e portit %s eshte lidhur me server' %(addr))

    # krijimi i nje procesi te ri (threadi te ri), me lidhjen e nje klienti te ri
    threading._start_new_thread(klienti_i_ri,(connectionSocket,addr)) 

