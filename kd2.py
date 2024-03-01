import json
import PySimpleGUI

def lasit_json_failu(ceļš):
    try:
        with open(ceļš, 'r') as fails:
            dati = json.load(fails)
            print("Elementi no JSON faila:")
            for elements in dati:
                print(elements)
    except FileNotFoundError:
        print("Faila norādītā adrese nav atrasta.")

if __name__ == "__main__":
    json_faila_ceļš = input("Lūdzu, ievadiet JSON faila ceļu: ")
    lasit_json_failu(json_faila_ceļš)