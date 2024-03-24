SUMMARY - DOCKER

### Container VS Virtual Machine
| Container | Virtual Machine |
| --------- | --------------- |
| Sebuah unit yang membungkus kode beserta dependensi (library) sehingga aplikasi dapat dijalankan dengan cepat dan andal (reliable) di berbagai environtment | Representasi virtual dari sebuah komputer dan dapat menjalankan berbagai program |
| Abtraksi di layer aplikasi | Abstraksi di hardware fisik |
|Menggunakan kapasitas yang lebih kecil (biasanya dalam puluhan MB) | Setiap VM satu sistem operasi secara penuh sehingga menggunakan kapasitas yang lebih banyak |
| Booting lebih cepat karena biasanya hanya berisi satu aplikasi saja | Booting lebih lambat |
| Digunakan untuk membungkus sebuah aplikasi. Satu container untuk satu aplikasi |Digunakan untuk menjalankan komputer dalam bentuk virtual |