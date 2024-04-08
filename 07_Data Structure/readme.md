# SUMMARY - DATA STRUCTURE

Dokumentasi resmi python : docs.python.org/3/tutorial/datastructures.html#

### List 
kumpulan dari banyak nilai (item/elemen) yang dapat berupa berbagai tipe data. nilai yang ada pada list dapat dilakukan manipulasi data. Function untuk manipulasi list :
- len(list), mendaatkan berapa banyak data yag dimiliki oleh list
- list.append(value), menambahkan element di akhir list
- list.insert(index, value), menambahkan element di index spesifik
- list.remove(value), menghapus element berdasarkan value
- list.pop(index), menghapus element di index spesifik. Jika tidak menyertakan index maka akan menghapus element terakhir pada list.
- More on list : list.extend(iterable), list.clear(), ect
- del statement , untuk menghapus data pada list di indeks tertentu. Ex : delmy_list[0]

### Tuple 
mirip seperti list. Cara deklarasinya menggunakan tanda kurag biasa. Bersifat immutable , yang artinya datanya tidak dapat di manipulasi. 

### set
seperti list dan tuple, namun tidak akses nilainya melalui index. deklarasi nya menggunakan tanda "{}"

### dictionary 
struktur data yang digunakan untuk menyimpan data berorientasikan key dan value. 
