Rangkuman Materi Pengenalan Data Engineer Part 1

# Definisi Data Engineer
Data engineer merupakan sebuah proses mengambil data mentah lalu diolah menjadi data yang siap digunakan oleh analis.

# Tahap Data Engineer
1. Data Ingestion (pengumpulan data)
2. Data Transformation
3. Data Serving

# Data Pipeline
Data pipeline merupakan sekumpulan pemrosesan untuk mempersiapkan data sampai data tsb siap digunakan. Tahap :
-  Data Ingestion (mengumpulkan data dari berbagai sumber, ex : aplikasi, db, cloud storage)
- Data Tranformation (stream and batch processing, distributed processing, data preparation)
- Insights & Decision-making (data warehousing, query & analytics engine, cloud storage)

# Jenis Data Pipeline
* berdasarkan urutan transformasi
a. ETL (Extract-Transform-Load), tahap :
	- ekstrak data dari berbagai sumber lalu dikumpulkan di tempat sementara (staging area)
	- transform (cleaning,penyesuaian format, dll)
	- Load (memasukkan data ke dalam data warehouse / data lake)

b. ELT (Extract-Load-Transform), tahap :
	- ekstrak data dari berbagai sumber
	- data tersebut langsung dimasukkan ke dalam data warehouse / data lake
	-  transform (cleaning,penyesuaian format, dll)

* Berdasarkan sumber data
a. Batch Pipeline, melakukan pemrosesan data pada data yang telah dikumpulkan selama rentang waktu tertentu, proses dilakukan secara periodic, hasilnya dapat diletakkan pada database.

b. Stream Pipeline, melakukan pemrosesan data pada data secara realtime, proses juga dilakukan sejara berlanjut.