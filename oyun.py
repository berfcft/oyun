savascı = {
    "Güç" : 85 ,
    "Can"  : 1500,
    "Zırh" : 30
}

büyücü = {
    "Güç" : 120 ,
    "Can"  : 1500,
    "Zırh" : 10
}

def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["Güç"]-vurulan["Zırh"]
    vurulan["Can"] -= eksilen

print("Savaşçı :" ,savascı)
print("Büyücü  :" ,büyücü)

while True:
    
    input("Vurmak için enter'a basınız!")
    vur(savascı,büyücü)
    print("Savaşçı büyücüye saldırdı.\U00002694")
    print("Savaşçının Can Değeri  :",savascı["Can"])
    print("Büyücünün Can Değeri   :",büyücü["Can"])
    input("Vurmak için enter'a basınız!")
    vur(büyücü,savascı)
    print("Büyücü savaşçıya saldırdı.\U00002694")
    print("Savaşçının Can Değeri  :",savascı["Can"])
    print("Büyücünün Can Değeri   :",büyücü["Can"])