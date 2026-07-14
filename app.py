## حالا میخوایم یک فانکشن بسازیم برای این که از ان استفاده کنیم برای این عدد باینتری بخونم 
## و ازش استفاده کنم به صورت دوتایی یعنی دو تاس رو برگردونه
import pickle
import random
def get_taas(x):
    with open("data_tasse.tass", "rb") as data_file:
        data = pickle.load(data_file)
        '''
        با استفاده از 
        sample  
        میتوانیم رو لیست مون حرکت کنیم و اون رو بخوانیم 

        '''
        indices = random.sample(range(len(data)), x)    
        for tass in indices:
            yield data[tass]


## حالا بدنه اصلی بازی رو میسازیم
dast = 1 
while True:
    tedad_tass = int(input("tedad tass ra vared konid: "))
    for taas in get_taas(tedad_tass):
        if dast > tedad_tass:
            break
        else:
            print(taas)
            dast += 1
    
    print("dast shoma tamoom shod")
    
    dobre = input("aya mikhahid dobare bazi konid? (Y/N): ")
    
    if dobre.upper() == "N":
        print("khosh be hal shoma")
        break
    else:
        dast = 1
        continue
