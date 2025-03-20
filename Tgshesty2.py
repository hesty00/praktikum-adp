#tgs praktikum modul 3 perulangan

print("VARIABEL ACAK POISSON")
print()

lambda_t = float(input("Masukkan nilai lambda t: "))
M = int(input("Masukkan nilai M :"))
e = 2.71828
print()

#menghitung (P(N(t)=n) untuk n=0,1,2,...,M
print(f"Hasil P(N(t)=n) untuk n = 0 hingga {M} :")
for n in range (M + 1):
    faktorial = 1
    for i in range (1 , n + 1) :
        faktorial *= i

    poisson = (e ** (-lambda_t)) * (lambda_t ** n) / faktorial
    print (f"P(N(t)= {n}) = {poisson :.6f}")

    n = n+1
    
print()
print("SELESAI")
