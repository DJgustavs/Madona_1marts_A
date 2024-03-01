import json
import csv
import PySimpleGUI

def lasit_failu(ceļš, paplašinājums):
    try:
        if paplašinājums == 'json':
            with open(ceļš, 'r') as fails:
                dati = json.load(fails)
                print("Elementi no JSON faila:")
                print(dati)
        elif paplašinājums == 'txt':
            with open(ceļš, 'r') as fails:
                saturs = fails.read()
                print("Teksta fails:")
                print(saturs)
        elif paplašinājums == 'csv':
            with open(ceļš, 'r') as fails:
                lasītājs = csv.reader(fails)
                print("CSV fails:")
                for rinda in lasītājs:
                    print(rinda)
        else:
            print("Nepareizs faila paplašinājums. Atbalstītie formāti: json, txt, csv")
    except FileNotFoundError:
        print("Faila norādītā adrese nav atrasta.")
    except Exception as e:
        print("Kļūda:", e)

if __name__ == "__main__":
    try:
        faila_nosaukums = input("ievadiet faila nosaukumu: ")
        paplašinājums = input(" ievadiet faila paplašinājumu (json, txt, csv): ")
        lasit_failu(faila_nosaukums, paplašinājums)
    except KeyboardInterrupt: