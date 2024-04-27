Simple Python server that shows Taskwarrior tasks using javascript [fullcalendar](http://fullcalendar.io/) library.

## Usage:
```
python server.py

// navigate to http://127.0.0.1:9001/
```

## Problem
es funktioniert nicht auf windows, da in dem Programm die shell aufgerufen wird mit dem Comands "task export". Das ist eine Funktion von Taskwarrior, welche die Aufgaben injson convertiert. die json objekte werden dann an den Fullcalendar weitergegeben. 
Da ich aber mit Windows arbeite kann da nicht funktionieren. 

### Lösung 1
In Linux-VM arbeiten. 
Programm sollte dann Funktionieren.

### Lösung 2
in Python cygwin aufrufen und dan den "task export" command.
hat gekklappt 
(2 h)

## Problem 2.0
Json wird übermittelt, jedoch nicht angezeigt
falschen Json format 
Taskwarrior settings json.array = on
(1h 20 min)

# Schlusswort
ganz Stark analysiert. 
nicht aus der Ruhe bringen lassen

## Task bei Click öffnen
https://stackoverflow.com/questions/22448097/fullcalendar-with-clickable-popup-on-hover

1. qtip Datei in js/ Oerdner ablegen
2. in index.html datei auf besagte _Datei verweisen
3. Fehler qtip ist funktion?

