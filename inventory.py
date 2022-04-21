while True :
    i = input ("Input Data Inventory Baru (ya/tidak) ?")
    if i == 'ya' or i== 'Ya':
        file = open ("db-inventory.txt", "a")
        print ("*"*40)
        x = input ("Masukan Nama Perangkat :")
        y = input ("Masukan Lokasi :")
        file.write("Nama Perangkat : "+x+", Lokasi : "+y+"\n")
        print("-"*40)
    elif i == 'tidak' or i== 'Tidak':
        file2 = open ("db-inventory.txt", "r")
        print ("*"*40)
        for item in file2:
            item = item.strip()
            print(item)
        break