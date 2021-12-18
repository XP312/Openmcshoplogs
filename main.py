import json
import os
import gzip
output = []
files = os.listdir("logs")
for f in files:

    if f[len(f)-1] == "z" and f[len(f)-2] == "g":
        zeit = str(f[0:10])
        with gzip.open('logs/' + f, 'r') as f:
            content = f.readlines()
            o = 0
            for i in content:

                if b'[CHAT]' in i:
                    if b'Shop Transaktionen' in i:
                        a = 0
                        stop = False
                        while stop == False:
                            content_ = str(content[o + 2 + a])
                            message = content_.split(" ")
                            try:
                                if message[4] == '+':

                                    output.append(
                                        {"Zeit": zeit, "Item": message[9], "Kosten": float(message[len(message) - 2]),
                                         "Anzahl": int(message[7])})

                                else:
                                    break
                            except:
                                break

                            a += 1
                o += 1






print(json.dumps(output))
f = open("data.json","w+")
f.write(json.dumps(output))
f.close()