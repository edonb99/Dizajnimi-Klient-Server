from socket import *
import random
import time
import datetime
import sys
import threading



print("=============================================================================================")
print('*******  FIEK-UDP Serveri  **********')
print("=============================================================================================")

# IP adresa
serverName = '127.0.0.1'

# Porti 12000 ndahet per soketin e serverit:
serverPort = 12000

# krijimi i soketetit te serverit sipas UDP-protokollit
serverSocket = socket(AF_INET, SOCK_DGRAM)

# lidhja e portit të serverit dhe ip adreses me socketin e krijuar
serverSocket.bind((serverName,serverPort))

print('Serveri startoi ne localhost me IP adrese: '+str(gethostbyname(gethostname()))+" ne portin: "+str(serverPort)) 

print('Serveri eshte i gatshem te pranoj kerkesa...')

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
        return str(pergjigja)
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



while 1:
    kerkesa = (bytes)("empty".encode())
    try:
        while str(kerkesa.decode()).upper()!="EXIT" and str(kerkesa.decode())!="":
            
            # pranimi i kerkeses nga klienti
            kerkesa, clientAddress = serverSocket.recvfrom(128)
            
            # dekodimi i kerkeses
            kerkesaStr = str(kerkesa.decode()).strip()
            
            # behet ndarja e kerkeses sipas hapesirave dhe ruhet ne njw Array
            kerkesaArray = kerkesaStr.split(' ')

            # kerkesa e derguar nga klienti kthehet se pari ne upperCase:
            kerkesaArray[0] = kerkesaArray[0].upper()
           
            # metoda IPADRESA
            if kerkesaArray[0]=="IPADRESA":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(("IP adresa juaj eshte: "+IPADRESA(clientAddress)).encode(), clientAddress)
                    ShtypTeDhenat(("IP adresa e klientit: "+IPADRESA(clientAddress)))
                else:
                    serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
            # metoda NUMRIIPORTIT
            elif kerkesaArray[0]=="NUMRIIPORTIT":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(("Numri i portit tuaj eshte: "+NUMRIIPORTIT(clientAddress)).encode(), clientAddress)
                    ShtypTeDhenat(("Numri i portit te klientit eshte: "+NUMRIIPORTIT(clientAddress)))
                else:
                    serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
            # metoda BASHKETINGELLORE
            elif kerkesaArray[0]=="BASHKETINGELLORE":
                if len(kerkesaArray) == 2:
                    rezultati = "Numri i bashketingelloreve ne fjaline e dhene eshte: " + BASHKETINGELLORE(kerkesaArray[1])
                    serverSocket.sendto(rezultati.encode(), clientAddress)
                    ShtypTeDhenat(rezultati)
                else:
                    serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
            # metoda PRINTIMI
            elif kerkesaArray[0]=="PRINTIMI":
                kerkesaStr2 = (str(kerkesaStr)).replace("PRINTIMI","")
                serverSocket.sendto(("Fjalia e printuar: " + PRINTIMI(kerkesaStr2)).encode(), clientAddress)
                ShtypTeDhenat(("Fjalia e printuar: " + PRINTIMI(kerkesaStr2)))
            # metoda HOST
            elif kerkesaArray[0]=="HOST":
                if len(kerkesaArray) == 1:
                    if HOST()=="Emri i hostit nuk mund te percaktohet!":
                        serverSocket.sendto(("Emri i hostit nuk mund te percaktohet!").encode(), clientAddress)
                        ShtypTeDhenat("Emri i hostit nuk mund te percaktohet!")
                    else:
                        serverSocket.sendto(("Emri i klientit eshte: "+HOST()).encode(), clientAddress)
                        ShtypTeDhenat(("Emri i klientit eshte: "+HOST()))
                else:
                    serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
            # metoda TIME
            elif kerkesaArray[0]=="TIME":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(("Koha e tanishme eshte: " + TIME()).encode(), clientAddress)
                    ShtypTeDhenat(("Koha e tanishme eshte: " + TIME()))
                else:
                    serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
            # metoda LOJA
            elif kerkesaArray[0]=="LOJA":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(("Rezultati nga loja: " + LOJA()).encode(), clientAddress)
                    ShtypTeDhenat(("Rezultati nga loja: " + LOJA()))
                else:
                    serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
            # metoda FIBONACCI
            elif kerkesaArray[0]=="FIBONACCI":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray)==1 or len(kerkesaArray)>2:
                    serverSocket.sendto(("Kerkesa juaj eshte invalide, ju lutem provoni perseri!").encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
                else:
                    serverSocket.sendto(("Numri i "+kerkesaArray[1]+" ne serine fibonacci eshte: "+FIBONACCI(kerkesaArray[1])).encode(), clientAddress)
                    ShtypTeDhenat(("Numri i "+kerkesaArray[1]+" ne serine fibonacci eshte: "+FIBONACCI(kerkesaArray[1])))
            # metoda KONVERTIMI
            elif kerkesaArray[0]=="KONVERTIMI":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray)>3 or len(kerkesaArray)<3:
                    serverSocket.sendto(("Kerkesa juaj eshte invalide, ju lutem provoni perseri!").encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
                else:
                    konverto = str(kerkesaArray[1]).lower().split("to")
                    pergjigja = kerkesaArray[2] + " " + str(konverto[0]) + " jane te barabarte me " + KONVERTIMI(str(kerkesaArray[1]).upper(),kerkesaArray[2]) + " " + str(konverto[1])
                    serverSocket.sendto(str(pergjigja).encode(), clientAddress)
                    ShtypTeDhenat(pergjigja)
            # metoda shtese GjujZaret - kthen vlerat e dy zareve te gjuajtura.
            elif kerkesaArray[0]=="GJUJZARET":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(str(GJUJZARET()).encode(), clientAddress)
                    ShtypTeDhenat(str(GJUJZARET()))
                else:
                    serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(), clientAddress)
                    ShtypTeDhenat("ERROR")
           # metoda shtese Prime 
            elif kerkesaArray[0]=='PRIME':
                    numri = int(kerkesaArray[1]);
                    if PRIME(numri):
                        serverSocket.sendto(str.encode("Numri " + str(numri) + " eshte numer i thjeshte!"), clientAddress)
                        ShtypTeDhenat(str("Numri " + str(numri) + " eshte numer i thjeshte!"))
                    else:
                        serverSocket.sendto(str.encode("Numri " + str(numri) + " nuk eshte numer i thjeshte!"), clientAddress)
                        ShtypTeDhenat(str("Numri " + str(numri) + " nuk eshte numer i thjeshte!"))


            # nqs. nuk shkruhet asnjera nga metodat e percaktuara
            else:
                serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(), clientAddress)
                ShtypTeDhenat("ERROR!")

       
    except Exception as e:
        print("\nERROR: ")
        print(str(e))