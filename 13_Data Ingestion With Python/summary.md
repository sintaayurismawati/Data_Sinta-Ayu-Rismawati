SUMMARY - DATA INGESTION WITH PYTHON

Data ingestion adalah proses yang kritis dalam manajemen data yang memungkinkan organisasi untuk mengumpulkan, menyimpan, dan mengelola data dari berbagai sumber untuk analisis lebih lanjut. Ini melibatkan ekstraksi data dari sumber, transformasi data ke format yang sesuai, dan memuat data ke dalam sistem penyimpanan yang dituju.

Manfaat data ingestion termasuk:
- Peningkatan dalam analisis data dan pemahaman bisnis melalui akses yang lebih cepat dan lebih mudah ke data yang relevan.
- Meningkatkan keputusan bisnis dengan dasar data yang lebih kuat.
- Mengurangi kesalahan dan inkonsistensi dalam data dengan proses pembersihan dan validasi yang tepat sebelum data dimasukkan ke dalam sistem.

Key components dari data ingestion:

1. **Data Source**: Ini bisa berupa database, file seperti CSV atau JSON, aliran data real-time seperti Kafka, atau sensor-sensor dalam Internet of Things (IoT). Setiap sumber ini memiliki format data yang berbeda dan perlu diakses dengan metode yang sesuai.

2. **Data Pipeline**: Ini adalah serangkaian langkah yang diperlukan untuk membersihkan, transformasi, dan memuat data ke dalam sistem penyimpanan yang dituju. Tahap pembersihan melibatkan identifikasi dan penanganan nilai-nilai yang hilang atau tidak valid. Tahap transformasi mengubah format data ke format yang dibutuhkan, sementara tahap validasi memastikan bahwa data sesuai dengan kriteria kualitas yang telah ditetapkan.

3. **Data Target**: Ini adalah tempat penyimpanan akhir untuk data yang telah diingest. Ini bisa berupa data lakes untuk penyimpanan data mentah, data warehouse untuk analisis yang lebih terstruktur, atau penyimpanan lainnya sesuai kebutuhan organisasi.

Jenis data ingestion:

1. **Batch Ingestion**: Proses pengumpulan data dalam jumlah besar dalam interval waktu tertentu. Ini cocok untuk pemrosesan data yang tidak memerlukan respons real-time dan memungkinkan pengolahan data dalam volume besar secara efisien.

2. **Real-time Ingestion**: Proses di mana data diambil dan dimasukkan ke dalam sistem segera setelah data tersedia. Ini memungkinkan organisasi untuk merespons perubahan data secara instan dan mengambil keputusan yang lebih cepat berdasarkan informasi yang paling mutakhir.

3. **Hybrid Ingestion**: Pendekatan yang menggabungkan baik batch ingestion maupun real-time ingestion sesuai dengan kebutuhan dan karakteristik data yang diingest. Ini memungkinkan organisasi untuk memanfaatkan keuntungan keduanya, seperti pengolahan data besar dalam volume besar dan respons real-time terhadap perubahan data.