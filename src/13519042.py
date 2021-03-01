# Haning Nanda Hapsari
# 13519042
# Tugas Kecil Rencana Kuliah

# Prosedur Untuk Fitur Cari Mata Kuliah
def carimatkul(matkul):
    sem = 0
    for j in range(8):
        if(matkul in hasil[j]):
            for i in range (len(hasil)):
                for j in range (len(hasil[i])):
                    if(hasil[i][j]==matkul):
                        sem = i+1
                        print("Mata Kuliah", matkul, "terletak pada semester", sem)
                        break
                if(sem != 0): break
        if(sem != 0): break
    if(sem == 0):
                print ("Mata Kuliah TIDAK Ditemukan")

# Prosedur untuk print hasil penyusunan
def printplan():
    print ("Hasil Penyusunan Rencana Kuliah :")
    for i in range(8):
        print ("Semester", i+1)
        for j in range (len(hasil[i])):
            print (hasil[i][j])

# Prosedur untuk menambahkan mata kuliah
def tambahmatkul(matkulprereq) :
    matkulprereq=matkulprereq.replace(",", "")
    matkulprereq=matkulprereq.replace(".", "")
    addmatkul = matkulprereq.split(" ")
    addmatkulcopy = addmatkul.copy()
    jumlah = len(addmatkul)
    if(jumlah==1):
        cek = False
        for j in range(8):
            if(addmatkul[0] in hasil[j]):
                cek = True
                break
        if(cek):
            print("Mata Kuliah Tersebut Sudah Terdapat Pada Rencana Kuliah")
            carimatkul(addmatkul[0])
        else :
            hasil[0].append(addmatkul[0])
            print("Mata Kuliah",addmatkulcopy[0],"Dapat Diambil Pada Semester 1")
            
    else :
        for b in range (jumlah-1,-1,-1):
            for a in range (8):
                if(addmatkul[b] in hasil[a]):
                    save.append(a)
                    addmatkulcopy.remove(addmatkul[b])
        if(len(addmatkulcopy)==1):
            maks = max(save)
            hasil[maks+1].append(addmatkulcopy[0])
            print("Mata Kuliah",addmatkulcopy[0],"Dapat Diambil Pada Semester", maks+2)
        elif(len(addmatkulcopy)==0):
            print("Mata Kuliah Tersebut Sudah Terdapat Pada Rencana Kuliah")
            carimatkul(addmatkul[0])
        else :
            print("Anda Tidak Memenuhi Prerequisite Mata Kuliah Tersebut")


print()
print("    _____            _________ __            .___       __________.__ ")
print("   /     \\ ___.__.  /   _____//  |_ __ __  __| _/__.__. \\______   \\  | _____    ____   ")
print("  /  \\ /  <   |  |  \\_____  \\\\   __\\  |  \\/ __ <   |  |  |     ___/  | \\__  \\  /    \\ ") 
print(" /    Y    \___  |  /        \\|  | |  |  / /_/ |\\___  |  |    |   |  |__/ __ \\|   |  \ ")
print(" \____|__  / ____| /_______  /|__| |____/\\____ |/ ____|  |____|   |____(____  /___|  / ")
print("         \\/\\/              \\/                 \\/\\/                          \\/     \\/ ") 
print()
print()
# Membuka file 
file = open("./test/test8.txt", "r")
# Membaca file per baris
rfile = (file.readlines())
# Inisialisasi Array
isi = [['*' for x in range(100)] for y in range(100)] 
isi1 = [['*' for x in range(100)] for y in range(100)] 
hasil = [[],[],[],[],[],[],[],[]]
pjg = [0 for i in range (100)]
save =[0]
# Memasukkan text ke dalam array yang sesuai
for i in range (len(rfile)):
    isi[i]=rfile[i].split(" ")
# Menghilangkan tanda ',', '.', dan '\n'
for i in range(len(rfile)):
    for j in range (len(isi[i])):
        isi[i][j]=isi[i][j].replace(",", "")
        isi[i][j]=isi[i][j].replace(".", "")
        isi[i][j]=isi[i][j].replace("\n", "")
# Memasukkan panjang kolom per baris ke dalam array
    pjg[i] = len(isi[i])
# Program Utama
for i in range (8):
    for j in range (len(rfile)):
        if (pjg[j] == 1):
            hasil[i].append(isi[j][0])
    for a in range(len(rfile)):
        for b in range (8):
            for c in range (len(hasil[b])):
                if(hasil[b][c] in isi[a]):
                    isi[a].remove(hasil[b][c])
                    pjg[a]=len(isi[a])
# Mengeluarkan hasil
printplan()

# Fitur tambahan
i = 0
print ("Apakah Anda ingin mencoba fitur lain? Y/N")
masukkan =input("Masukkan : ")
while (i==0):
    if(masukkan=='Y' or masukkan=='y'):
        print("1. Cari Mata Kuliah \n2. Tambah Mata Kuliah \n3. Melihat Rencana Kuliah \n4. Keluar")
        fitur = input("Pilih fitur : ")
        if (fitur=='1'):
            print ("Masukkan mata kuliah yang ingin dicari :", end=" ")
            matkul = input()
            matkulcopy=matkul.replace(".","")
            matkul = matkulcopy.replace(",", "")
            carimatkul(matkul)
        elif(fitur=='2'):
            print("Masukkan Mata kuliah dengan format : <Matkul>, <prereq>, ..., <prereq>.")
            matkulprereq = input("Masukkan sesuai format :")
            tambahmatkul(matkulprereq)
        elif(fitur=='3'):
            printplan()
        else :
            i = 1
    else :
        i=1
file.close()

print("___________          .__                  ____  __.             .__.__     ")
print("\\__    ___/__________|__| _____ _____    |    |/ _|____    _____|__|  |__  ")
print("  |    |_/ __ \\_  __ \\  |/     \\\\__  \\   |      < \\__  \\  /  ___/  |  |  \\ ")
print("  |    |\\  ___/|  | \\/  |  Y Y  \\/ __ \\_ |    |  \\ / __ \\_\\___ \\|  |   Y  \\ ")
print("  |____| \\___  >__|  |__|__|_|  (____  / |____|__ (____  /____  >__|___|  /")
print("             \\/               \\/     \\/          \\/    \\/     \\/        \\/ ")

