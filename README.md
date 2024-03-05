# Server per query remote con osquery
Esempio di server che consente di ricevere query remote per osquery(d) e restituisce le risposte delle query.

## Installazione ed esecuzione del server
Nota: osquery va installato solamente sul server che si metterà in ascolto di query, sul PC che effettuerà le query non è necessario installarlo.
- Installare osquery
- Creare e attivare un ambiente virtuale python \
`python -m venv venv` \
`source venv/bin/activate`
- Installare le dipendenze \
`pip install -r requirements.txt`
- Far partire il server \
`python run.py`

## Esecuzione di query remote
Prendiamo come esempio che il server abbia IP 192.168.0.100 e abbiamo un altro computer con IP 192.168.0.200. Nel server dobbiamo far partire l'applicazione che si mette in ascolto di richieste come da sezione precedente. dall'altro computer, invece, possiamo effettuare le query in due modi:
- Contattando il server con una richiesta GET
  - `curl -X GET -H "Content-type: application/json" "http://192.168.0.100:5000/exec?query=select version from os_version"`
- Contattando il server con una richiesta POST
  - `curl -X POST -H "Content-type: application/json" -d 'select version from os_version' "http://192.168.0.100:5000/exec`

Se tutto è stato configurato correttamente, il PC che effettua la richiesta otterrà la risposta alla query in formato JSON.