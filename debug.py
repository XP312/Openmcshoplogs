import json
import os
import gzip
output = []
files = os.listdir("logs")
print("Datein in logs ordner: ", files)
for f in files:

    if f[len(f)-1] == "z" and f[len(f)-2] == "g":
        zeit = str(f[0:10])
        print("Datei:"+ f)
        with gzip.open('logs/' + f, 'r') as f:
            content = f.readlines()
            o = 0
            for i in content:

                if b'[CHAT]' in i:
                    
                    if b'Shop Transaktionen' in i:
                        print("[SHOP Trans]")
                        a = 0
                        stop = False
                        while stop == False:
                            
                            content_ = str(content[o + 2 + a])
                            print("content" + content_)
                            message = content_.split(" ")
                            try:
                                if message[4] == '+':

                                    output.append(
                                        {"Zeit": zeit, "Item": message[9], "Kosten": float(message[len(message) - 2]),
                                         "Anzahl": int(message[7])})

                                else:
                                    print("kein +")
                                    break
                            except:
                                print("auslese fehler")
                                break

                            a += 1
                            print("-------")
                o += 1






print(output)
f = open("data.json","w+")
f.write(json.dumps(output))
f.close()