# MY STUDY PLAN
Sebuah program topological sort yang digunakan untuk menentukan rencana kuliah

## Algoritma Decrease and Conquer pada Progam My Study Plan
1. Program akan membaca file berupa txt yang berisi daftar nama mata kuliah dan prerequisitenya. 
2. File ini akan dimasukkan kedalam array 2 dimensi (matriks).
3. Matriks tersebut akan menghitung panjang setiap baris. 
4. Baris yang memiliki panjang 1 atau simpul yang memiliki derajat masuk 0 akan dimasukkan ke dalam array hasil dan dihapus beserta dengan derajat keluarnya.
5. Mengulangi langkah tersebut hingga semua simpul terpilih dan dimasukkan ke dalam array hasil.

Penggunaan topological sort memenuhi kriteria strategi algoritma decrease and conquer. Topological sort merupakan variasi pertama dari algoritma decrease and conquer yaitu decrease by a constant. Dalam program ini, setiap simpul yang memilki derajat masuk 0 akan dihilangkan, yang mana derajat keluarnya akan dihilangkan pula sehingga simpul yang berhubungan dengan simpul yang dihapus akan berkurang 1 konstanta.

## Requirement
Requirement :
1. Python 
2. Text Editor

## Cara Menjalankan Program
1. Download program (dalam bentuk zip)
2. Extract program
3. Pilih test case yang ingin kalian gunakan dengan mengganti 
' ./test/tes yang ingin digunakan'
4. Run program 

## Author
Haning Nanda Hapsari - 1359042