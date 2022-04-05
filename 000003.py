def sumNumbers(domanda):
   i=0
   risultato_=0
   for i in range(1, int(domanda) +1 ,1):    
        risultato_ += i
   return risultato_

domanda= input('Inserisci un numero: ')
totale_= sumNumbers(domanda)
print(totale_)