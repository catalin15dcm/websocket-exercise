# websocket-exercise
# Python WebSocket Chat App

Folosind libraria [`websockets`](https://pypi.org/project/websockets/), din Python, creaza un sistem de chat basic, cu suport pentru mai multi clienti conectati simultan. Serverul de websockets va trebui sa accepte conexiuni de la oricati clienti. La nivel de client, acesta se va conecta la server si se va prezenta, folosind un nume preluat din linia de comanda - de ex ./client.py --name client1; apoi clientul va afisa un prompt in consola ("> ") care simbolizeaza ca poti sa scrii ceva si sa-l trimiti catre server cand apesi Enter. Serverul primeste mesajul si il trimite tuturor clientilor conectati (face broadcast), in afara de clientul de la care a primit mesajul. Fiecare client va afisa mesajele primite de la server tot in consola, incepand linia cu caracterul "< " urmat de numele clientului care a trimis mesajul intre paranteze (de ex "< (client1) mesaj").

---


## Cerințe

- Biblioteci Python:
  - `websockets`
  - `colorama` (pentru afișare color în client)

Instalare rapidă a tuturor dependențelor:

```
pip install -r requirements.txt
```

## Utilizare
### 1. Pornește serverul:

Deschide un terminal și rulează:

```
python server.py
```
Serverul va porni pe ws://localhost:12346 și va aștepta conexiuni de la clienți.

### 2. Pornește unul sau mai mulți clienți
Deschide câte un terminal pentru fiecare client pe care vrei să-l conectezi. Fiecare client trebuie să aibă un nume unic:

```
python client.py --name client1
python client.py --name client2
```
Clientul va afișa un prompt:


```
>
``` 
Scrie un mesaj și apasă Enter pentru a-l trimite către ceilalți utilizatori conectați.

### 3. Formatul mesajelor
Clientul care primește un mesaj îl va vedea afișat astfel:

```
< (client1) Salut tuturor!
``` 
Mesajul nu este afișat și clientului care l-a trimis, doar celorlalți.

## Exemplu
Terminal client1:
```
> Salut!
```
Terminal client2:
```
< (client1) Salut!
```
Terminal client3:
```
< (client1) Salut!
```` 
