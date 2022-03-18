import re

logs_ = {'woodenlog':0, 'EPIClog':0, 'SUPERlog':0, 'MEGAlog':0, 'HYPERlog':0, 'ULTRAlog':0, 'ULTIMATElog':0}

f = open("items.txt")
texto = f.read()
items = re.findall(r":([a-zA-Z]+): [a-zA-Z ]+: (\d+).*?", texto)
if items == []:
    items = re.findall(r"([a-zA-Z ]+): (\d+).*?", texto)
    
for item in items:
    name = item[0].replace(' ', '')
    logs_[name] = int(item[1])

logs_fin = []
logs_next = 0
for name, cant in logs_.items():
    cant_act = cant + logs_next
    if name == 'woodenlog':
        logs_fin.append(cant_act%25)
        logs_next = int(cant_act/25)
    elif name == 'ULTIMATElog':
        logs_fin.append(cant_act)
    else: 
        logs_fin.append(cant_act%10)
        logs_next = int(cant_act/10)
        
    

print('En total tendrías: ') 
for name, cant in zip(logs_.keys(), logs_fin):
    print('  - ' + name + ': ' + str(cant))


import keyboard as kb

print('press Enter to exit')
kb.wait('enter')