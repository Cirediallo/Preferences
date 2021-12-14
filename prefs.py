#!/usr/bin/python3.8
# -*-coding:utf8 -*

import random

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

def lirePrefs(nomfic):
    pass

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

def prefAlea(listePrenom, prenom):
    try:
        fhand = open(listePrenom, "r")
    except: 
        print("****File can't be opened: File doesn't exist")
        quit();
    file_len = fileLength(listePrenom)
    if file_len <= 1:
        print("File can't be empty or contains a single element")
        quit()
    arr = nameInArray(listePrenom)
    print("The array is: ", arr)
    created_file = open("created.txt", "w")
    len_liste_prenom = fileLength(listePrenom)
    print("The length is: ",len_liste_prenom)
    """
    
    """
    print("////////////// STARTING: ", arr, len(arr))
    for index, name in enumerate(arr):
        print("+++++++++++++++ we have: ", index, name)
        cpy = arr.copy()
        cpy.remove(cpy[index])
        len_cpy = len(cpy)
        print("THE CPY ARR: ", cpy," \n")
        tmp = []
        created_file.write(name)
        #tmp.append(name)
        #for i in range(0, len_cpy): #here too
        i = 0
        while i < len_cpy: #this loop replace the loop above
            r = random.randrange(0, len_cpy) #replaced line_number with len_cpy
            #while (index == r):
                #r = random.randrange(0, len_cpy) #here too
            print("THE RANDOM NUMBER IS: ",r)
            tmp.append(cpy[r])
            cpy.remove(cpy[r])
            len_cpy = len(cpy)
            print("NEW LENGHT OF CPY: ", len_cpy, " AND THE ARRAY IS: ",cpy)
            #i = i + 1
        print("===============================")
        print(tmp)
        #tmp_set = set(tmp)
        #print(tmp_set)
        for elt in tmp: #tmp_set replaced by tmp
            created_file.write("\t"+elt)
        created_file.write("\n")
    return created_file


if __name__== '__main__':
    generePrefs("listepreferences.csv", "fichierSortie.txt", method)
