import PySimpleGUI

def ierakstit_vardu_faila(vards):
    try:
        with open("lietotajs.txt", 'w') as fails:
            fails.write(vards)
        print("Vārds veiksmīgi ierakstīts failā 'lietotajs.txt'.")
    except IOError:
        print("Kļūda: Nevarēja ierakstīt failā.")
    except Exception as e:
        print("Kļūda:", e)

if __name__ == "__main__":
    try:
        vards = input("Lūdzu, ievadiet savu vārdu: ")
        ierakstit_vardu_faila(vards)
    except KeyboardInterrupt:
        print("\nProgrammas izpilde pārtraukta ar CTRL+C")