SUMMARY 

- Data transformation merupakan proses konversi data dari suatu format/struktur ke dalam bentuk lainnya
- Pentingnya data transformation :
    1. Memungkinkan data dari berbagai sumber untuk digabungkan
    2. Memastikan kualitas dan konsistensi data
    3. Memfasilitasi analisis dan data business intelligence

- Jenis data transformation :
    1. Normalisasi : mengubah data ke dalam rentang standar. Method : min-max scaling, z-score normalization
    2. Encoding : mengubah data kategorikal ke dalam format numerik. method : one-hot encoding, label encoding.
    3. Aggregation : merangkum data untuk di analisis. method : sum, average, count, max, min

- Tantangan dalam data transformtion :
    1. Mengatasi data yang hilang, nilai yang hilang bisa terjadi karena kesalahan entry data, data sengaja tidak dikumpulkan / data corrupt. Metode : deletion (menghapus baris dengan nilai yang hilang), implutation (mengisi nilai yang hilang dengan data point lain, bisa dilakukan dengan melaukan rata2 dari 2 data point), forward/backward fill (mengisi nilai yang hilang dengan nilai sebelumnya). 

    2. Menangani outliers
        Outliers merupakan nilai yang sangat berbeda dari kebanyakan nilai dalam dataset, dapat mempengaruhi hasil analisis. Metode : Z-Score , IQR (Interquartile Range)

    3. Memastikan integrasi data selama proses penyimpanan /transfer. Metode : regular backups, validation checks, checksums.