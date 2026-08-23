"""
PythonLab 1.0 - CLI working
"""

import json

def crea_persona(nome, eta, residenza, professione):
    return {
        "nome": nome,
        "eta": eta,
        "residenza": residenza,
        "professione": professione
    }

def aggiungi_persona(elenco_persone, id_persona, persona):
    elenco_persone[id_persona] = persona

#def cerca_persona():

def check_risposta(risposta, msg_si=None, msg_no=None):
    risposta = risposta.strip().upper()
       
    if risposta == "S":
        if msg_si:
            return True, msg_si, True
        else: 
            return True, "Nuovo inserimento", True
    elif risposta == "N":
        if msg_no:
            return False, msg_no, True
        else:
            return False, "Alla prossima! Vado via.", True
    else:
        return False, "Hai sbagliato risposta! Ritenta!!!", False

def salva_elenco_persone(elenco_persone, nome_file):
    with open(nome_file, 'w') as file:
        json.dump(elenco_persone, file, indent=4)

def carica_elenco_persone(nome_file):
    try:
        with open(nome_file, 'r') as file:
            elenco_persone = json.load(file)
            elenco_persone = converti_id_persona_a_intero(elenco_persone)
    except FileNotFoundError:
        elenco_persone = {}
    return elenco_persone

def converti_id_persona_a_intero(elenco_persone):
    elenco_convertito = {}
    for id_persona, persona in elenco_persone.items():
        elenco_convertito[int(id_persona)] = persona
    return elenco_convertito

def valida_dato(stringa):
    if stringa != "":
        return stringa, "", True
    else:
        return "", "Il campo non può essere vuoto.", False  

def valida_intero(stringa):
    try:
        numero = int(stringa)
        return numero, "", True
    except ValueError:
        return "", "Inserisci un numero valido.", False      

def chiedi_dato(messaggio):
    while True:
        dato = input(messaggio)
        dato, messaggio_errore, valida = valida_dato(dato)
        if valida:
            return dato
        else:
            print(messaggio_errore)

def chiedi_intero(messaggio, minimo=None, massimo=None):

    while True:

        dato = input(messaggio)

        dato, messaggio_errore, valida = valida_dato(dato)
        if not valida:
            print(messaggio_errore)
            continue
        
        numero, messaggio_errore, valida = valida_intero(dato)
        if valida:

            if minimo is not None and numero < minimo:
                print("Troppo piccolo")
                continue

            if massimo is not None and numero > massimo:
                print("Troppo grande")
                continue

            return numero
        else:
            print(messaggio_errore)          

def trova_persona(elenco_persone, nome):

    for id_persona, persona in elenco_persone.items():
        if persona["nome"].lower() == nome.lower():
            return id_persona, persona
    return None, None

def normalizza_eta(elenco_persone):
    elenco_convertito = {}

    for id_persona, persona in elenco_persone.items():

        persona_convertita = persona.copy()
        eta = persona_convertita["eta"]

        if isinstance(eta, str):
            persona_convertita["eta"] = int(eta)

        elenco_convertito[id_persona] = persona_convertita
    return elenco_convertito

def menu():
    print("+----------------------------------+")
    print("|            PYTHONLAB             |")
    print("+----------------------------------+")
    print("| 1. Inserimento                   |")
    print("| 2. Visualizzazione               |")
    print("| 3. Modifica                      |")
    print("| 4. Esci                          |")
    print("+----------------------------------+")

    scelta = input("Scegli: ")
    try:
        scelta = int(scelta)
        return scelta
    except ValueError:
        print("Non sai nemmeno contare?!")
 
def modifica_persona(elenco_persone):
    nome_cercato = input("Chi vuoi modificare? ")
    id_persona, persona_trovata = trova_persona(elenco_persone, nome_cercato)

    if persona_trovata:
        print(f"\nInformazioni sulla persona trovata:")
        for chiave, valore in persona_trovata.items():
            print(f"{chiave}: {valore}")
    else:
        print("Persona non trovata.")
        return

    while True:
        print("\nQuale campo vuoi modificare? ")
        print("1. Nome ")
        print("2. Età ")
        print("3. Residenza ")
        print("4. Professione ")
        print("5. Annulla")
    
        modifica = chiedi_intero("\nScelta: ", 1, 5)

        if modifica == 5:
            print("Modifica annullata.")
            return

        campi = {
            1: "nome",
            2: "eta",
            3: "residenza",
            4: "professione"
        }
        campo = campi[modifica]

        messaggio = f"Il contenuto attuale del campo {campo} è {persona_trovata[campo]}"
        print(messaggio)
        risposta = input("\nVuoi modificarlo? s/n ")
        scelta, messaggio, valida = check_risposta(
            risposta,
            "Modifica confermata",
            "Modifica annullata"
            )

        if not valida:
            print(messaggio)
            continue

        if not scelta:
            print(messaggio)
            break

        if campo == "eta":
            nuovo_valore = chiedi_intero("Inserisci la nuova età: ", minimo=0, massimo=120)
        else:
            nuovo_valore = chiedi_dato(f"Inserisci il nuovo valore per {campo}: ")

        print(f"Nuovo valore: {nuovo_valore}")
        risposta = input("\nConfermi la modifica? s/n ")
        scelta, messaggio, valida = check_risposta(
            risposta,
            "Modifica confermata",
            "Modifica annullata"
            )
        if not valida:
            print(messaggio)
            continue

        if not scelta:
            print(messaggio)
            return

        persona_trovata[campo] = nuovo_valore
        salva_elenco_persone(elenco_persone, "elenco_persone.json")

        print(f"\nScheda aggiornata (ID {id_persona}):")
        for chiave, valore in elenco_persone[id_persona].items():
            print(f"{chiave}: {valore}")
        input("\nPremi INVIO per continuare...")

    
def main():
    #elenco_persone = {}
    elenco_persone = carica_elenco_persone("elenco_persone.json")

    if elenco_persone:
        id_persona = max(elenco_persone.keys())
    else:
        id_persona = 0

    while True:
        opzione = menu()

        if opzione == 1:

            nome = chiedi_dato("Inserisci il nome: ")
            eta = chiedi_intero("Inserisci l'età: ")
            residenza = chiedi_dato("Inserisci la residenza: ")
            professione = chiedi_dato("Inserisci la professione: ")
        
            id_persona += 1
            persona = crea_persona(nome, eta, residenza, professione)
            aggiungi_persona(elenco_persone, id_persona, persona)
        
            salva_elenco_persone(elenco_persone, "elenco_persone.json")
      
            # for id_persona, persona in elenco_persone.items():
            #     print(f"\nInformazioni sulla persona con ID {id_persona}:")
            #     for chiave, valore in persona.items():
            #         print(f"{chiave}: {valore}")
            # input("\nPremi INVIO per continuare...")
            print(f"\nPersona inserita (ID {id_persona}):")
            for chiave, valore in persona.items():
                print(f"{chiave}: {valore}")

            input("\nPremi INVIO per continuare...")
                    
        elif opzione == 2:
            while True:

                trova = input("Vuoi cercare una persona per nome? (s/n): ")

                scelta, messaggio, valida = check_risposta(trova)

                if not valida:
                    print(messaggio)
                    continue

                if not scelta:
                    print(messaggio)
                    break

                nome_cercato = input("Inserisci il nome della persona da cercare: ")
                id_persona, persona_trovata = trova_persona(elenco_persone, nome_cercato)

                if persona_trovata:
                    print(f"\nInformazioni sulla persona trovata:")
                    for chiave, valore in persona_trovata.items():
                        print(f"{chiave}: {valore}")
                else:
                    print("Persona non trovata.")
                break
            input("\nPremi INVIO per continuare...")

        elif opzione == 3:
            modifica_persona(elenco_persone)

        elif opzione == 4:
            break
        
    # ...




    # while True:
    #     domanda = "Vuoi inserire una nuova persona? (s/n): "
    #     risposta = input(domanda)

    #     scelta, messaggio, valida = check_risposta(risposta)

    #     # se la risposta non è valida, stampo il messaggio di errore e continuo il ciclo
    #     if not valida:
    #         print(messaggio)
    #         continue

    #     # se la risposta è valida e l'utente ha scelto di non inserire una nuova persona, esco dal ciclo
    #     elif not scelta:

    #         while True:

    #             trova = input("Vuoi cercare una persona per nome? (s/n): ")

    #             scelta, messaggio, valida = check_risposta(trova)

    #             if not valida:
    #                 print(messaggio)
    #                 continue

    #             if not scelta:
    #                 print(messaggio)
    #                 break

    #             nome_cercato = input("Inserisci il nome della persona da cercare: ")
    #             persona_trovata = trova_persona(elenco_persone, nome_cercato)

    #             if persona_trovata:
    #                 print(f"\nInformazioni sulla persona trovata:")
    #                 for chiave, valore in persona_trovata.items():
    #                     print(f"{chiave}: {valore}")
    #             else:
    #                 print("Persona non trovata.")

    #             break

    #         if not scelta:
    #             break

    #         continue
        
    #     nome = chiedi_dato("Inserisci il nome: ")
    #     eta = chiedi_intero("Inserisci l'età: ")
    #     residenza = chiedi_dato("Inserisci la residenza: ")
    #     professione = chiedi_dato("Inserisci la professione: ")

    #     id_persona += 1
    #     persona = crea_persona(nome, eta, residenza, professione)
    #     aggiungi_persona(elenco_persone, id_persona, persona)

    # salva_elenco_persone(elenco_persone, "elenco_persone.json")
      
    # for id_persona, persona in elenco_persone.items():
    #     print(f"\nInformazioni sulla persona con ID {id_persona}:")
    #     for chiave, valore in persona.items():
    #         print(f"{chiave}: {valore}")

if __name__ == "__main__":
    main()