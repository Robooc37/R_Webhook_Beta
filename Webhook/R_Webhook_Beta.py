import requests

WEBHOOK_URL = "Qua' devi mettere l'url del webhook"

data = {
    "embeds": [
        {
            "title": "R_Webhook", # QUESTO E' IL TITOLO.

            "description": "Inserisci la descrizione qua' ", # QUA' POTRAI METTERCI LA TUA DESCRIZIONE.

            "color": int("b200ff", 16),  # COLORE IN FORMATO HEX, SE VUOI CAMBIARE COLORE DEL BORDO MODIFICA "b200ff"

            "image": {
                "url": "QUA' METTI L'URL DELLA TUA IMMAGINE"
            }
        }
    ]
}

response = requests.post(WEBHOOK_URL, json=data)

if response.status_code == 204:
    print("Messaggio inviato con successo!")
else:
    print(f"Errore nell'invio del messaggio: {response.status_code}")




# GRAZIE PER AVER SCARICATO IL FILE

# QUESTA E' LA VERSIONE BETA DEL FILE.
