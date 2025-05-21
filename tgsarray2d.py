n= int(input("Masukkan Titik Koordinat Maximal 10: "))
print("")
if n<=10 :
    x=[]
    for i in range(n):
        elemen= int(input(f"elemen x[{i+1}]: "))
        x.append(elemen)    
        
    print("")
    y=[]
    for i in range(n):
        elemen= int(input(f"elemen y[{i+1}]: "))
        y.append(elemen)
    print("")

    hasil=[]
    for i in range (n):
        hasil.append((x[i],y[i]))
    
    koordinat=["A","B","C","D","E","F","G","H","I","J"]
    print(f"Kumpulan Titik dengan n={n} Adalah:")
    for i in range (n):
        print(f"{koordinat[i]}= ({x[i]},{y[i]})")
    print("")
    
    for i in range (n):
        for j in range(i+1,n):
            if j>i and x[j] != x[i]:
                if x[j] > x[i]:
                    bagian_x=x[j]-x[i]
                else :
                    bagian_x=x[i]-x[j]
                    
                if y[j] > y[i]:
                    bagian_y=y[j]-y[i]
                else :
                    bagian_y=y[i]-y[j]
                print(f" Jarak antara Koordinat {koordinat[i]} dan {koordinat[j]} Adalah: ({bagian_x},{bagian_y})")
else :
    print("Tidak Valid, Masukan Koordinat Sesuai Perintah")

