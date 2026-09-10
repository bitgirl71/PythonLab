from flask import Flask, request, session, render_template

from pythonlab import (
    carica_elenco_persone,
    trova_corrispondenze,
    valida_dato,
    valida_intero,
    crea_persona,
    aggiungi_persona,
    salva_elenco_persone
    )

app = Flask(__name__)
app.secret_key = "pythonlab"

elenco_persone = carica_elenco_persone("elenco_persone.json")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/visualizzazione")
def visualizzazione():

    campo = request.args.get("campo")
    valore = request.args.get("valore")

    messaggio = ""
    risultato = {}

    if campo == "eta" and valore:
        valore, messaggio_errore, valida = valida_intero(valore)

        if not valida:
            messaggio = messaggio_errore
        else:
            risultato = trova_corrispondenze(
                campo,
                valore,
                elenco_persone
            )

    elif campo and valore:
        risultato = trova_corrispondenze(
            campo,
            valore,
            elenco_persone
        )
    elif campo and valore == "":
        risultato = elenco_persone

    if campo and valore and not risultato and not messaggio:
        messaggio = "Nessuna persona trovata."

    return render_template(
        "visualizzazione.html",
        risultato=risultato,
        messaggio=messaggio
    )

@app.route("/inserimento", methods=["GET", "POST"])
def inserimento():

    persona = None
    messaggi_errore = []
    completato = False

    if request.method == "POST":

        if request.form.get("conferma") == "si":

            persona = session["persona"]
            id_persona = session["id_persona"]

            aggiungi_persona(
                elenco_persone,
                id_persona,
                persona
            )

            salva_elenco_persone(
                elenco_persone,
                "elenco_persone.json"
            )

        else:
            nome, messaggio_nome, valido_nome = valida_dato(
                request.form["nome"]
            )

            eta, messaggio_eta, valido_eta = valida_intero(
                request.form["eta"]
            )

            residenza, messaggio_residenza, valido_residenza = valida_dato(
                request.form["residenza"]
            )

            professione, messaggio_professione, valido_professione = valida_dato(
                request.form["professione"]
            )

            if valido_nome and valido_eta and valido_residenza and valido_professione:

                if elenco_persone:
                    id_persona = max(elenco_persone.keys()) + 1
                else:
                    id_persona = 1

                persona = crea_persona(
                    nome,
                    eta,
                    residenza,
                    professione
                )

                session["persona"] = persona
                session["id_persona"] = id_persona

            else:

                if not valido_nome:
                    messaggi_errore.append(messaggio_nome)

                if not valido_eta:
                    messaggi_errore.append(messaggio_eta)

                if not valido_residenza:
                    messaggi_errore.append(messaggio_residenza)

                if not valido_professione:
                    messaggi_errore.append(messaggio_professione)

                contenuto = ""

                for messaggio in messaggi_errore:
                    contenuto += f"<p>{messaggio}</p>"

    return render_template(
        "inserimento.html",
        persona=persona,
        messaggi_errore=messaggi_errore,
        completato=completato
    )

@app.route("/modifica", methods=["GET", "POST"])
def modifica():

    risultato = {}
    persona = None
    id_persona = None
    campo = None
    nuovo_valore = None
    messaggio = ""
    modificato = False

    if request.method == "POST":

        if request.form.get("conferma") == "si":

            nuovo_valore = request.form.get("nuovo_valore")
            id_persona = request.form.get("id_persona")
            campo = request.form.get("campo")

            persona = elenco_persone.get(int(id_persona))

            persona[campo] = nuovo_valore

            salva_elenco_persone(
                elenco_persone,
                "elenco_persone.json"
            )
            modificato = True

        else:

            nuovo_valore = request.form.get("nuovo_valore")
            id_persona = request.form.get("id_persona")
            campo = request.form.get("campo")

            if campo == "eta":
                nuovo_valore, messaggio_errore, valida = valida_intero(nuovo_valore)
            else:
                nuovo_valore, messaggio_errore, valida = valida_dato(nuovo_valore)

            if not valida:
                messaggio = messaggio_errore
            else:
                persona = elenco_persone.get(int(id_persona))

    else:

        nome = request.args.get("nome")
        id_persona = request.args.get("id_persona")
        campo = request.args.get("campo")

        if nome:
            risultato = trova_corrispondenze(
                "nome",
                nome,
                elenco_persone
            )

        if id_persona:
            persona = elenco_persone.get(int(id_persona))

    return render_template(
        "modifica.html",
        risultato=risultato,
        persona=persona,
        id_persona=id_persona,
        campo=campo,
        nuovo_valore=nuovo_valore,
        messaggio=messaggio,
        modificato=modificato
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)