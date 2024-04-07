import csv


# EN COURS



def view(path):
    with open(path, mode="r") as file:
        text_csv = csv.DictReader(file)
        for line in text_csv:
            print(line)

"""                if type is "r":
                    print("Ok pour modifier")
                if type is "r+":"""
# with open("packageCsv/essai.csv") as file:
# with open("packageCsv/essai.csv", mode="r") as file: r __lire
# with open("packageCsv/essai.csv", mode="r+") as file: r+ __lire,écrire(sans écraser)
# with open("packageCsv/essai.csv", mode="w") as file: w __écrire(écraser)
# with open("packageCsv/essai.csv", mode="a") as file: a __continuer d'écrire
# text_csv = csv.reader
# text_csv = csv.reader(file, delimiter=",")
# text_csv = csv.DictReader(file)
# text_csv = csv.writer(file, delimiter=',')
"""                    if format is "csv":
                        print("Ok pour csv")
                    if format is "json":
                        print("Ok pour json")"""