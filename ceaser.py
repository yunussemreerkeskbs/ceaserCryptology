# -*- coding: utf-8 -*-
def readFile(): # dosyayı okuyup dizi haline getirdik
    text = ""
    with open("metin.txt","r",encoding = "utf-8") as file:
        for i in file:
            text = text +i
        return text
character = int(input("kaç karaktere kadar şifrelemek istersiniz? : "))
crypto = int(input("ötelemek istediğiniz miktar: ")) # => örneğin a yı c ye kadar öteleme miktarı(3)
def ceaser(character, crypto): # istediğimiz karaktere kadar şifreleme ve öteleme 
    text = ""
    import string
    alphabet =string.ascii_lowercase
    alphabet =list(alphabet)
    with open("metin.txt","r",encoding = "utf-8") as file: # dosyayı açtım
        for i in file: # dosya içinde dönüş yaptım
            text = text +i # yeni bir text oluşturarak oraya ekledim
        # metin = len(chr(text))
        for i in text: # oluşturduğum text için döndürdüm 
            i.lower()
            ceaserFile = "" # şifreleme için yeni bir dizi oluşturdum
            if i not in alphabet: # alfabe dışındaki verileri(sayı noktalama) eklettim
                ceaserFile = ceaserFile+i
            else:
                ceaserFile = ceaserFile + alphabet[(alphabet.index(i)+int(crypto)) % len(alphabet)]
                # alfabedeki harfleri öteleyerek oluşturduğum yeni harfleri ekledim
            character = character - 1 # karakter sayısını azaltarak sıfıra kadar dönmesini istedim
        return ceaserFile 
        print(ceaserFile)
original = readFile()
sezar = ceaser(character, crypto)
print("orjinal hali: " , original)
print("sezar şifreleme ile: " + sezar)


























