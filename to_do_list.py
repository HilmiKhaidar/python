bilangan = (1,3,5,7,9)
BilanganGanjil = bilangan

if 5 in BilanganGanjil:
    print("Angka 5 terdapat dalam variable pada bilanganGanjil")

else:
    print("Angka 5 tidak terdapat dalam variablel bilanganGanjil")


bilangan = list(BilanganGanjil)
BilanganGanjil[BilanganGanjil.index(7)] = 11 
BilanganGanjil = tuple(BilanganGanjil)

print("Isi variable bilanganGanjil setelah penggantian:" , BilanganGanjil)