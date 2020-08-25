import string
import random
import unidecode
import numpy as np
#Méthode por formater
def format_message(message):
    message=message.upper()
    message=unidecode.unidecode(message)
    caract_valide=[i for i in message if i in(string.ascii_uppercase)] 
    caract_valide_str="".join(caract_valide)
    return caract_valide_str
#La fonction inverse modulo
def inverse(n):
    inverseValue=1
    for i in range(26):
        if (n*i)%26 == 1:
            inverseValue=i
    return inverseValue  
#pgcd de 2 nombre
def gcd(a,b):
    if b > a:
        a, b=b, a
    r=a%b    
    while(r!=0):
        a,b=b,r
        r=a%b  
    return b 
#définir un alphaber
dico={}
for count,j in enumerate(string.ascii_uppercase):
    dico[count]=j
def num_to_letter(num_chaine):
    liste=[]
    for i in (num_chaine):
        liste.append(dico[i])
    liste="".join(liste)
    return liste
#Renverse de l'aplphabet
reverse_dico={}
for count,j in enumerate(string.ascii_uppercase):
    reverse_dico[j]=count
def letter_to_num(chaine):
    liste=[]
    for i in chaine:
        liste.append(reverse_dico[i])
    return liste
#LES SHEMAS CLASSICS DE CHIFFREMENT
#César
def keygen_cesar():
    return(random.randint(0,25))
def cipher_cesar(message,key):
    cipher=[]
    message=format_message(message)
    for i in message:
        cipher.append(dico[(reverse_dico[i]+key)%26])
    cipher="".join(cipher)
    return cipher
#Déchffrement
def decipher_cesar(message,key):
    decipher=[]
    message=format_message(message)
    for i in message:
        decipher.append(dico[(reverse_dico[i]-key+26)%26])
    decipher="".join(decipher)
    return decipher
###Affine
#La clé
def keygen_affine():
    inversible=[i for i in range(26) if inverse(i) != 1 or i==1]
    return(random.choice(inversible),random.randint(0,26))
#Chiffrement
def cipher_affine(message,key):
    k1=key[0]
    k2=key[1]
    message=format_message(message)
    liste=[]
    for alpha in message :
        liste.append(dico[(k1*reverse_dico[alpha]+k2)%26])
    cipher_text ="".join(liste) 
    return cipher_text
#Déchiffrement
def decipher_affine(message,key):
    k1=key[0]
    k2=key[1]
    k1=inverse(k1)
    message=format_message(message)
    liste=[]
    for alpha in message:
        liste.append(dico[ (k1*( (reverse_dico[alpha]-k2)+26))%26 ])
    decipher = ''.join(liste) 
    return decipher
#Substitution
def keygen_subs():
    liste=list(string.ascii_uppercase)
    random.shuffle(liste)
    liste="".join(liste)
    return(liste)

def cipher_substitution(message,key):
    text_to_ciphe = format_message(message)
    cipher_text=[]
    for count,letter in enumerate(dictionary):
        dictionary[letter]=key[count]
    for letters in text_to_ciphe:
        cipher_text.append(dictionary[letters])
    cipher_text_str="".join(cipher_text)
    return cipher_text_str
#déchiffrement
def decipher_substitution(message,key):
    dictionary ={}
    decipher_text=[]    
    for count,letter in enumerate(key):
            dictionary[letter]=dico[count]
    for letters in message:
            decipher_text.append(dictionary[letters])
    decipher_text_str="".join(decipher_text)
    return decipher_text_str
##########VIGENERE##########
dico_vig=dico.copy()
reverse_dico_vige=reverse_dico.copy()
def keygen_vigenere():
    length=random.randint(1,25)
    key=[]
    for i in range(length):
        key.append(dico_vig[random.randint(0,25)])
    keys="".join(key)
    return keys
#Chiffrement
def cipher_vigenere(message,key):
    message = format_message(message)
    cipher_message=[]
    while(len(key)<len(message)):
        key+=key
    for k,m in zip(key,message):
        cipher_message.append(dico[(reverse_dico[k]+reverse_dico[m])%26])
    cipher_message="".join(cipher_message)
    return cipher_message
#Déchiffrement
def decipher_vigenere(message,key):
    message = format_message(message)
    decipher_message=[]
    while(len(key)<len(message)):
        key+=key
    for k,m in zip(key,message):
        decipher_message.append(dico[((reverse_dico[m]-reverse_dico[k])+26)%26])
    decipher_message="".join(decipher_message)
    return decipher_message
#HILL#
inversible=[i for i in range(26) if inverse(i) != 1 or i==1]
def keygen_hill():
    l=[0,0,0,0]
    n=2
    while( n not in inversible or n == 0) :
        for i in range(4):
            l[i]=random.randint(0,25)
        n=(l[0]*l[3]-l[2]*l[1])%26
    n=inverse(n)
    A = np.array([[l[0], l[1]], [l[2], l[3]]])
    inv_A=np.array([[n*l[3] % 26, (-n*l[1])%26], [(-n*l[2])%26, n*l[0]%26]])
    return(A)
#Chiffrement
def cipher_hill(message,key):
    message = format_message(message)
    b=False
    chiffre=[]
    length=len(message)
    if(length%2==0):
        pass
    else:
        message=message+"W"
        b=True
    message= letter_to_num(message)
    for i in range(0,len(message)-1,2):
        chiffre.append((key[0][0]*message[i]+key[0][1]*message[i+1]) % 26)
        chiffre.append((key[1][0]*message[i]+key[1][1]*message[i+1]) % 26)
    chiffre=num_to_letter(chiffre)
    if(b):
        chiffre=chiffre[:len(chiffre)-1]
        pass
    else:
        pass
    return(chiffre)
#PERMUTATION
def cipher_permutation(message,key):
    message=format_message(message)
    cipher=[]
    for i in key:
        cipher.append(message[i])
    cipher="".join(cipher)
    return cipher
#Déchiffrement
def decipher_permutation(message,key):
    message=format_message(message)
    keys_match={}
    for i,j in enumerate(key):
        keys_match[j]=i
    inverse_key=[]
    for i in range(len(keys_match)):
        inverse_key.append(keys_match[i])
    decipher=[]
    print("inverse",inverse_key)
    for i in inverse_key:
        decipher.append(message[i])
    decipher="".join(decipher)
    return decipher
#VERNAM
#key
def keygen_vernam(chaine):
    chaine=format_message(chaine)
    key=[]
    for i in range(len(chaine)):
        key.append(random.choice(string.ascii_uppercase))
    key="".join(key)
    return key
#Chiffrement
def cipher_vernam(message,key):
    message = format_message(message)
    message=letter_to_num(message)
    key=letter_to_num(key)
    cipher=[]
    for m,k in zip(message,key):
        cipher.append((m+k)%26)
    cipher=num_to_letter(cipher)
    return cipher
#Déchiffrement
def decipher_vernam(message,key):
    message = format_message(message)
    message=letter_to_num(message)
    key=letter_to_num(key)
    decipher=[]
    for m,k in zip(message,key):
        decipher.append(((m-k)+26)%26)
    decipher=num_to_letter(decipher)
    return decipher
#Déchiffrement de Hill
def decipher_hill(message,key):
    n=(key[0][0]*key[1][1]-key[0][1]*key[1][0])%26
    n=inverse(n)
    key=np.array([[n*key[1][1] % 26, (-n*key[0][1])%26], [(-n*key[1][0])%26, n*key[0][0]%26]])
    message = format_message(message)
    b=False
    chiffre=[]
    length=len(message)
    if(length%2==0):
        pass
    else:
        message=message+"W"
        b=True
    message = letter_to_num(message)
    for i in range(0,len(message)-1,2):
        chiffre.append((key[0][0]*message[i]+key[0][1]*message[i+1]) % 26)
        chiffre.append((key[1][0]*message[i]+key[1][1]*message[i+1]) % 26)
    chiffre=num_to_letter(chiffre)
    if(b):
        chiffre=chiffre[:len(chiffre)-1]
    else:
        pass
    return(chiffre)