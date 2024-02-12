#import module
import random
import string
#definesc functia
def generare_parola(lungime=8):
    #referinta funciei
    caractere = string.ascii_letters + string.digits
    #genereaza parola 
    parola = ''.join(random.choice(caractere) for _ in range(lungime))
    return parola

lungime_parola = 10  # Poți schimba lungimea după preferințe
parola_generata = generare_parola(lungime_parola)
print(f" {parola_generata}")



