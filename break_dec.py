full =0
flo =0
dec = str(3.143644847484)
for i in range(len(dec)):
    if i == ".":
        j = i.index()
    full = int(dec[:j])
    flo = int(dec[j+1:])
        

print(full)
print(flo)
