from socket import *
import sys

print("=============================================================================================")
print('*******  FIEK-UDP Klienti  **********')
print("=============================================================================================")

# I percaktohet klientit hosti: localhost dhe porti: 12000
serverName = input("Shenoni emrit e serverit: ");

Port = input("Shenoni portin: ");
serverPort = int(Port);


#krijimi i soketit te klientit
# kurse parametri i dyte tregon se tipi i socketit eshte UDP socket
s = socket(AF_INET, SOCK_DGRAM)

# te protokolli TCP ne menyre qe te komunikojne klienti dhe serveri se pari duhet te vendoset nje lidhje nepermjet tyre: 
s.connect((serverName, serverPort))

kerkesa = "sample"

print("Jeni lidhur ne serverin ", serverName," ne portin", serverPort)
print("==========================================================================================================================")

# Metodat
print("""Jeni te lidhur me serverin!

       Cilat nga keto metoda deshironi ti perdorni: 
               
       *IPADRESA                             - Percakton dhe kthen IP adresen e klientit
               
       *NUMRIIPORTIT                         - Percakton dhe kthen portin e klientit(hostit)
               
       *BASHKETINGELLORE {hapesire} teksti   - Merr si parameter nje tekst dhe kthen numrin e bashketingelloreve ne ate tekst
               
       *PRINTIMI {hapesire} teksti           - Kthen fjaline e shtypur ne tekst. Hapsirat ne fillim dhe ne fund te fjalise nuk duhet te kthehen
               
       *HOST                                 - Kerkon emrin e kompjuterit dhe e kthen ate
               
       *TIME                                 - Percakton kohen aktuale ne server
               
       *LOJA                                 - Kthen 7 numra nga rangu [1,49]
               
       *FIBONACCI {hapesire} numer           - Gjen numrin Fibonacci si rezultat i parametrit te dhene hyres
               
       *KONVERTIMI {hapesire}                - Kthen si rezultat konvertimin e opcioneve varesisht opcionit te zgjedhur: 
        opcioni {hapesire} vlera              KILOWATTTOHORSEPOWER, HORSEPOWERTOKILOWATT, DEGREESTORADIANS
                                              RADIANSTODEGREES, GALLONSTOLITERS, LITERSTOGALLONS

       *GJUJZARET                           - Kjo metodë simulon hudhjen e dy zareve, dy numra të plotë random nga 1 deri në 6.

       *PRIME                               - Shikon nëse një numër është një numer i thjesht.
                                             
               


               
               Sheno EXIT per te dalur nga programi!
==========================================================================================================================================================              
               """)

while 1:
    try:
        kerkesa = input('Shkruaj emrin e metodes dhe argumentin perkates: ')
        if kerkesa!="" and kerkesa.upper()!="EXIT":
            # behet enkodimi i kerkeses dhe dergimi tek TCP serveri
            s.sendall(str(kerkesa).encode())
        else:
            break
        # ketu behet pranimi i pergjigjes nga serveri dhe dekodimi i saj
        # madhesia me e madhe qe mund tw mirret eshte 128 byte
        data = s.recv(128)
        print('Te dhenat nga serveri: ')
        print(str(data.decode()).strip())
        print("----------------------------------------------------------------------------------------\n")
    except Exception as e:
        print(str(e))
        break
    
  
# mbyllet lidhja
s.close() 
