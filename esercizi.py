"""
Esercizi di laboratorio di informatica
Autore: Anna Grazia

dumps → stringa
dump  → file
loads → da stringa
load  → da file

dumps  → da Python → stringa JSON
loads  → da stringa JSON → Python

dump   → da Python → file JSON
load   → da file JSON → Python

Python → file       dump()
file   → Python     load()

Python → stringa    dumps()
stringa → Python    loads()

P.S. attenzione alla "grandine didattica"

"""


import json

persona = {
    "nome": "Anna",
    "eta": 55,
    "residenza": "FI"
}

testo_json = json.dumps(persona)

print(testo_json)

persona = json.loads(testo_json)
print(persona)
print(type(persona))

id_trovati = []

persone = [
    {"nome": "Anna", "eta": 55},
    {"nome": "Alex", "eta": 54}
]

print(persone)
print(type(persone))

# # # for: percorre gli elementi di una sequenza

# # numeri = [3, 7, 2, 9]

# # for numero in numeri:
# #     print(numero)


# # # range: definisce una sequenza numerica
# # # con valore iniziale, limite e passo

# # for i in range(3, 12, 3):
# #     print(i)


# # # for + if + modulo: filtra una sequenza
# # # mantenendo solo i numeri pari

# # for i in range(1, 11):
# #     if i % 2 == 0:
# #         print(i)

# numeri = [3, 7, 2, 9]
# quadrati = []

# # for numero in numeri:
# #     quadrato = numero * numero
# #     quadrati.append(quadrato)  
# #     print(f"Il quadrato di {numero} è {quadrato}")        

# persona = {
#     "nome": "Anna",
#     "eta": 55,
#     "residenza": "Firenze"
# }    
# print("Informazioni sulla persona:")
# for chiave, valore in persona.items():
#     print(f"{chiave}: {valore}")    

# print("\nNuova età:")
# persona["eta"] = 56 # modifica il valore associato alla chiave "eta"
# print(persona["eta"]) # stampa il valore associato alla chiave "eta"
# print("\n")
# persona["professione"] = "informatica disperata" # aggiunge una nuova coppia chiave-valore al dizionario

# print(persona.keys()) # stampa tutte le chiavi del dizionario
# print(persona.values()) # stampa tutti i valori del dizionario
# print(persona.items()) # stampa tutte le coppie chiave-valore del dizionario

# for chiave in persona.keys():
#     print(chiave) # stampa tutte le chiavi del dizionario

# for valore in persona.values():
#     print(valore) # stampa tutti i valori del dizionario    

#id_persona = 0
#elenco_persone = {}

#while True:
#     risposta = input("Vuoi inserire una nuova persona? (s/n): ")
#     if risposta.lower() == "n":
#         break
#     else:
#         id_persona += 1
        
#         nome = input("Inserisci il nome: ")
#         eta = input("Inserisci l'età: ")
#         residenza = input("Inserisci la residenza: ")
#         professione = input("Inserisci la professione: ")

#         persona = {
#         "nome": nome,
#         "eta": eta,
#         "residenza": residenza,
#         "professione": professione
#         }
#         elenco_persone[id_persona]  = persona

# for id_persona, persona in elenco_persone.items():
#     print(f"\nInformazioni sulla persona con ID {id_persona}:")
#     for chiave, valore in persona.items():
#         print(f"{chiave}: {valore}")

# elenco_persona = {
#     "nome": ["Anna", "Luca", "Marco"],
#     "eta": [55, 30, 25],
#     "residenza": ["Firenze", "Roma", "Milano"],
#     "professione": ["informatica disperata", "ingegnere", "studente"]
# }