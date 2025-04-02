import requests

def scarica_pagina():
    url = input("Inserisci l'URL della pagina da scaricare: ").strip()

    if not url.startswith("http"):
        print("Errore: L'URL deve iniziare con 'http' o 'https'.")
        return

    try:
        # Effettua la richiesta GET alla pagina
        response = requests.get(url)
        response.raise_for_status()  # Controlla se la richiesta ha avuto successo

        # Salva il contenuto HTML in un file
        nome_file = "pagina.html"
        with open(nome_file, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Pagina scaricata con successo e salvata in '{nome_file}'.")

    except requests.exceptions.RequestException as e:
        print(f"Errore durante il download: {e}")

if __name__ == "__main__":
    scarica_pagina()
