#!/usr/bin/python3.8
# -*-coding:utf8 -*

class ANSI:
    R = '\033[1m\033[91m' # Bold red color
    B = '\033[94m' # Blue
    C = '\033[96m' # Cyan 
    G = '\033[92m' # Green
    END = '\033[0m'

import random

class PreferencesBinomes:
    #transform the file into a dictionnary of matches and returns it
    def __init__(self, dico):
        self.preferences = dico

def fileLength(nomfic):
    try:
        fhand = open(nomfic, "r")
    except:
        print("File can't opened: File doesn't exist");
        quit()

    count = 0
    for line in fhand:
        count = count +1
    fhand.close();
    return count;

class ExtensionError(Exception):
    def __init__(self, f, ext):
            self.ext = ext
            self.message = f"File {f} extension not expected. Expected format {ext}."
            super().__init__(self.message)

class TabulationError(Exception):
    def __init__(self, f):
        self.f = f
        self.message = f"File {f} not properly formed. Tabulation must separate values"
        super().__init__(self.message)


def lirePrefs(nomfic):
    #matrix = list()
    dico = {}
    counter = 0
    
    try:
        fhandler = open(nomfic, "r")
        ext = nomfic.split('.')[-1]
        if ext != "txt":
            raise ExtensionError(nomfic, "txt")
        lines = fhandler.readlines()
        for line in lines:
            prenoms = [p.strip('\n') for p in line.split('\t') if p != '']
            counter = counter + len(prenoms)
            dico[prenoms[0]] = prenoms[1:]
            #matrix.append(prenoms)

        if counter <= len(lines):
            raise TabulationError(nomfic)
        print("Nous avons dans dico: ", dico)

    except FileNotFoundError as e:
        print(f"{ANSI.R}File not found{ANSI.END}")
        print(e)
    except ExtensionError as e:
        print(f"{ANSI.R}File {nomfic} doesn't have required extension. Extension required txt. {ANSI.END}")
        print(e)
    except TabulationError as e:
        print(f"{ANSI.R}File {nomfic} doesn't have required format. Names must be separated with a tabulation {ANSI.END}")
        print(e)

def scoreSimple():


def generePrefs(nameFile, prefFile, generationMethod):
    try:
        nameFileHandler = open(nameFile, "r")
    except:
        print("====File can't be opened: File doesn't exist")
        quit()
    
    #File where we write preference
    try:
        prefFile = open(prefFile, "a")
    except:
        print("File can't be opened: File doesn't exist")
        quit()
    
    
    for elt in nameFileHandler:
        file_generated = generationMethod(nameFile, elt)
        print("the returned array is: ",file_generated)
        elt = elt.rstrip()
        prefFile.write(elt)
        for name_generated in file_generated:
            prefFile.write("\t"+name_generated)
        prefFile.write("\n")
        
    #file_generated.close()
    nameFileHandler.close()
    prefFile.close()

def nameInArray(nomfic):
    try:
        fhand = open(nomfic, "r")
    except:
        print("File can't be opened: File doesn't exist")
        quit()
    arr = list()
    for line in fhand:
        line = line.rstrip()
        arr.append(line)

    fhand.close()
    return arr

def method(listePrenom, prenom):
    prenom = prenom.rstrip()
    print("prenom is :", prenom, " and the type is: ", type(prenom))
    try:
        fhand = open(listePrenom, "r")
    except:
        print("File can't be opened: File might not exist or error while written")
        quit()
    file_len = fileLength(listePrenom)
    if(file_len <= 1):
        print("Preference list can't be generated if file is empty or contains a single element")
        quit()
    arr = nameInArray(listePrenom)
    #print("The array before removing is: ",arr)
    arr.remove(prenom)
    #print("The array after removing is: ", arr)
    i = 0
    arr_len = len(arr)
    preference_generated = []
    while(i < arr_len):
        r = random.randrange(0, arr_len)
        preference_generated.append(arr[r])
        arr.remove(arr[r])
        arr_len = len(arr)

    return preference_generated


if __name__== '__main__':
    generePrefs("listepreferences.csv", "fichierSortie.txt", method)
    lirePrefs("fichierSortie.txt")
