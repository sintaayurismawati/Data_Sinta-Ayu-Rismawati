## Prioritas 1
1. Jawaban :
- Data terstruktur memiliki model, format dan skema data yang ditentukan.  
#### Contoh : 
data dalam basis data relasional, spreadsheet, atau format XML yang memiliki kolom dan baris yang jelas dan dapat diidentifikasi. Data terstuktur disimpan di RDBMS dan mudah dicari melalui SQL.

- Data tidak terstruktur 
#### Contoh :
 teks bebas, media sosial, email, audio, video, dokumen PDF, gambar, data sensor, log file, dan streaming data.  Disimpan dalam sistem penyimpanan file 


2. Jawaban :
Relational database merupakan kumpulan data yang memiliki relasi satu sama lain. Contohnya seperti sistem pada e-commerce yang memiliki entitas seperti user, store, seller, product, order. Dimana tiap2 entitas memiliki relasi dengan entitas lainnya.

3. Jawaban : 
Konsep normalisasi basis data yaitu proses desain database dengan mengorganisasi data ke dalam tabel yang memiliki struktur yang baik tujuannya agar meminimalkan redundansi data, dan menghindari anomali pengubahan.

## Prioritas 2
1. Jawaban : 
Untuk sistem basis data e-commerce dengan data yang beragam, saya akan menggunakan kombinasi basis data relasional dan NoSQL. Basis data relasional akan digunakan untuk kebutuhan proses transaksi seperti pesanan, pembayaran, informasi pembeli, informasi produk, dll. Sedangkan NoSQQL akan digunakan untuk data yang tidak terstruktur seperti log interaksi pengguna di website. Integrasi data terstruktur dan tidak terstruktur dapat dilakukan melalui proses ETL yang mengambil data dari sumber yang berbeda dan mengubahnya ke format yang dapat dimengerti oleh sistem, lalu memuatnya ke dalam basis data relasional atau NoSQL sesuai kebutuhan.

## Eksplorasi 
1. Jawaban : 
Saya akan menggunakan penyimpanan skala besar seperti Amazon S3 atau Azure Data Lake Storage. Data akan diproses menggunakan teknologi seperti Apache Spark, dan data streaming akan ditangani oleh Apache Kafka. Integrasi dengan sistem data lainnya dapat dilakukan melalui alat ETL seperti Apache NiFi atau Apache Airflow, serta menyediakan antarmuka atau API untuk akses data lake. Keamanan dan manajemen akses akan diatasi dengan menerapkan kontrol akses yang ketat dan enkripsi data.

