import csv
import PySimpleGUI

def lasit_ceturtās_kolonnas_datus(csv_fails):
    try:
        with open(csv_fails, 'r') as fails:
            lasītājs = csv.reader(fails)
            for rinda in lasītājs:
                if len(rinda) >= 4:  
                    ceturtā_kolonna = rinda[3]  
                    print(ceturtā_kolonna)
                else:
                    print("Rindā nav pietiekami daudz kolonnu.")
    except FileNotFoundError:
        print("Faila norādītā adrese nav atrasta.")

if __name__ == "__main__":
    csv_faila_ceļš = input("ievadiet CSV faila ceļu: ")
    lasit_ceturtās_kolonnas_datus(csv_faila_ceļš)