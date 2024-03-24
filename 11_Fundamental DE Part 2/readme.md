SUMMARY - FUNDAMENTAL DE PART 2

## Structured Data
- memiliki model, format, dan skema data yang ditentukan
- disimpan di RDBMS dan mudah dicari melalui SQL
- membutuhkan lebih sedikit penyimpanan 

## Unstructured Data
- data memiliki struktur internal tetapi tidak terstruktur melalui model atau skema data yang telah ditentukan sebelumnya
- tidak cocok dengan database relasional seperti SQL
- memerlukan pemrosesan lanjutan agar dapat dicari

## Semi-Structured Data
- berada di antara terstruktur dan tidak terstruktur
- tidak memiliki skema yang kaku
- tidak sesuai dengan tabel data atau struktur database relasional
- memiliki karakteristik klasifikasi yang terkait dengannya

## Relational Database
- kumpulan data yang memiliki relasi satu sama lain
- dapat dilakukan normalisasi untuk mengeliminasi duplikat data dan meningkatkan integritas database
- Contoh RDMS berbayar : Oracle Database, Microsoft SQL Server, IBM DB2
- Contoh RDBMS Open Source : MySQL, PostgreSQL

## NoSQL Database
- support semi-structured data
- memiliki schema yang fleksibel untuk membangun sebuah aplikasi modern
- tipikal sitem terdistribusi dimana beberapa mesin dapat bekerja bersama dalam 1 kelompok

## Jenis NoSQL by Data Model
### Key/value
Data disimpan sebagai pasangan kunci dan nilai, di mana kunci adalah identifikasi unik untuk setiap data dan nilai adalah data yang sesuai. Basis data key/value store biasanya sangat sederhana dan efisien dalam penyimpanan data tetapi sering kali memiliki keterbatasan dalam kemampuan pencarian dan query yang kompleks.
- Use case : caching, user session management, gaming leaderboards
- tools : redis, memcached

### Document DB
Model ini menyimpan data dalam dokumen, yang biasanya berformat JSON, BSON, atau XML. Setiap dokumen memiliki struktur yang fleksibel dan dapat berbeda dari satu dokumen ke dokumen lainnya. Ini memungkinkan pengembang untuk menyimpan data yang kompleks dan beragam dalam satu dokumen.
- Use cases : user profiles, content management, book database, product catalog
Tools : Amazon DocumentDB, MOngoDB, Cosmos DB, ArangoDB, Couchbase Server, CouchDB

### Wide Column DB
Basis data model ini mengorganisir data dalam kolom daripada baris seperti yang dilakukan dalam basis data relasional. Ini cocok untuk kasus penggunaan di mana skema data sangat bervariasi atau berubah sering. Mereka juga sangat scalable secara horizontal.
- Use cases : sensor logs, user preferences, geographis information, reporting systems, time series data, logging and other writeheavy applications
- Tools : HBase, Google BigTable AWS DynamoDB, Apache Cassandra, MariaDB

### Graph DB
Model ini mendefinisikan entitas sebagai "node" dan hubungan antara entitas sebagai "edge". Mereka sangat cocok untuk data yang memiliki struktur yang sangat terhubung dan kompleks, seperti jejaring sosial, grafik jaringan, atau analisis peringkat.

## OLTP VS OLAP
1. OLTP :
- Digunakan untuk memproses transaksi bisnis sehari-hari secara online. Ini berfokus pada input, penyimpanan, dan pengambilan data transaksi yang cepat dan efisien.
- Transaksi biasanya berupa operasi tambah, hapus, atau ubah (insert, delete, update).
- Data yang diproses cenderung bersifat operasional, real-time, dan transaksional.
- Skema data pada OLTP biasanya disusun agar memungkinkan pengolahan transaksi sehari-hari dengan cepat.

2. OLAP :
- Digunakan untuk menganalisis data bisnis secara mendalam untuk mendapatkan wawasan yang berguna bagi pengambilan keputusan. Ini berfokus pada analisis data historis dan kompleks.
- Data yang diproses cenderung bersifat historis, agregat, dan berorientasi pada analisis.
- Operasi OLAP meliputi pemrosesan dan analisis data kompleks seperti operasi roll-up, drill-down, slicing, dan dicing.
- Skema data pada OLAP biasanya didesain agar mendukung analisis multidimensi dan kompleks.

## Perbedaan Database, Data Lake, Data Warehouse, Data Mart
1. Database:
- Digunakan untuk menyimpan data transaksional operasional.
- Biasanya mengikuti model skema terstruktur.
- Fokus pada operasi tambah, hapus, ubah (insert, delete, update).

2. Data Lake:
- Digunakan untuk menyimpan berbagai jenis data dalam format mentah dan mentah.
- Tidak memiliki skema atau struktur yang ditentukan sebelumnya.
- Dirancang untuk analisis dan eksplorasi data yang fleksibel.

3.Data Warehouse:
- Digunakan untuk menyimpan data yang telah diproses dan dipersiapkan untuk analisis.
- Mengikuti skema bintang atau snowflake untuk menyimpan data dengan struktur yang dimaksudkan untuk analisis.
- Data diintegrasikan dari berbagai sumber dan dibereskan sebelum dimuat ke dalam data warehouse.

4.Data Mart:
- Subset dari data warehouse yang menyimpan data terfokus pada satu subjek bisnis atau departemen tertentu.
- Biasanya digunakan untuk menyajikan data yang disesuaikan dengan kebutuhan analisis atau kebijakan di tingkat yang lebih rendah.
- Memiliki struktur yang dioptimalkan untuk pertanyaan analitis spesifik.