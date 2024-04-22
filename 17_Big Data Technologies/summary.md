SUMMARY - BIG DATA TECHNOLOGIES

### Definisi Big Data
Big data merupakan sekumpulan data dengan jumlah yang sangat besar yang bisa mencapai hingga exabytes

### Sumber Big Data
- ***Kueri pencarian*** :
 Informasi yang diperoleh dari mesin pencari seperti Google, Bing, atau Yahoo. Ini mencakup kueri yang dimasukkan oleh pengguna untuk mencari informasi tertentu di internet. Data ini mencakup tren pencarian, preferensi pengguna, dan banyak lagi.

- ***Aktivitas user*** :
Data yang dihasilkan dari interaksi pengguna dengan berbagai platform online seperti media sosial, situs web e-commerce, aplikasi seluler, dan lainnya. Ini mencakup aktivitas seperti klik, like, share, komentar, dan lainnya. Data aktivitas pengguna dapat memberikan wawasan berharga tentang perilaku pengguna dan preferensi mereka.

- ***Jumlah video di platform online*** : 
Data tentang jumlah dan jenis video yang diunggah dan ditonton di platform online seperti YouTube, Vimeo, dan platform streaming lainnya. Ini mencakup metadata video, jumlah penayangan, durasi, rating, dan lainnya. Data ini memiliki potensi besar untuk analisis tren, preferensi pengguna, dan pemahaman lebih lanjut tentang konten yang populer.

- ***Transaksi online*** :
Informasi yang dihasilkan dari transaksi yang dilakukan secara online, seperti pembelian di situs web e-commerce, pembayaran tagihan, transfer uang, dan lainnya. Data ini mencakup detail transaksi, informasi pelanggan, jumlah pembayaran, waktu transaksi, dan lainnya. Analisis transaksi online dapat memberikan wawasan tentang perilaku pembelian pelanggan, tren pasar, dan kebutuhan konsumen.

### Karakteristik Big Data (5V)
1. ***Volume***
Volume data big data bisa sangat besar, bahkan mencapai petabyte atau eksabyte, dan terus meningkat seiring waktu.

2. ***Velocity***
Mengacu pada kecepatan dengan mana data dibuat, disimpan, diperbarui, dan dianalisis. Dalam konteks big data, data sering kali dibuat dengan kecepatan yang sangat tinggi, seperti data streaming dari sensor IoT atau aktivitas pengguna di media sosial.

3. ***Variety***
Keragaman jenis data yang dihasilkan dari berbagai sumber dan dalam berbagai format, termasuk teks, gambar, video, suara, struktur terstruktur, dan tidak terstruktur. Karakteristik ini menuntut kemampuan untuk mengelola dan menganalisis data dari berbagai sumber dan format.

4. ***Veracity***
Berkaitan dengan keandalan dan kebenaran data. Karena data big data sering kali berasal dari berbagai sumber yang berbeda, keandalan dan kualitas data dapat bervariasi. Tantangan utama adalah memastikan keakuratan, konsistensi, dan integritas data.

5. ***Value***
Merujuk pada nilai yang dapat diekstraksi dari data. Meskipun memiliki volume, kecepatan, dan keragaman yang tinggi, nilai sebenarnya dari big data terletak pada kemampuan untuk menghasilkan wawasan yang bernilai dan informasi yang dapat digunakan untuk mengambil keputusan yang lebih baik, meningkatkan efisiensi, dan menciptakan nilai bagi organisasi.

### Tools Big Data :
1. ***Apache Hadoop***
Hadoop adalah platform perangkat lunak open-source yang dirancang untuk menyimpan, mengelola, dan menganalisis data besar secara terdistribusi. Hadoop terutama terdiri dari dua komponen utama: Hadoop Distributed File System (HDFS) untuk penyimpanan data terdistribusi dan Apache MapReduce untuk pemrosesan data terdistribusi.
    - Hadoop distributed file system
        HDFS adalah sistem penyimpanan file terdistribusi yang dirancang untuk menyimpan data besar di cluster komputer yang terdiri dari banyak node. Karakteristik utama HDFS adalah replikasi data secara otomatis untuk toleransi terhadap kegagalan dan kemampuan untuk memproses data secara terdistribusi di node-node yang berbeda. HDFS membagi file menjadi blok-blok yang disimpan secara terdistribusi di node-node dalam cluster, memungkinkan proses pemrosesan data paralel. HDFS adalah komponen inti dari ekosistem Hadoop dan menjadi fondasi untuk berbagai aplikasi analisis data.
        
    - Hadoop MapReduce
        MapReduce adalah model pemrograman dan sistem eksekusi yang digunakan untuk memproses data besar di cluster Hadoop. Model ini terdiri dari dua tahap utama: tahap map dan tahap reduce. Pada tahap map, data dipecah menjadi bagian-bagian yang lebih kecil dan diproses secara terdistribusi di node-node dalam cluster. Pada tahap reduce, hasil dari tahap map digabungkan dan dianalisis untuk menghasilkan output akhir. MapReduce dirancang untuk mengatasi masalah skala dalam pemrosesan data dan memberikan kemampuan paralelisasi yang tinggi.

    - Hadoop YARN
        YARN adalah manajer sumber daya yang bertanggung jawab untuk mengelola sumber daya cluster dan menjadwalkan tugas-tugas pemrosesan data di dalamnya. YARN memisahkan manajemen sumber daya dari pemrosesan data, memungkinkan cluster untuk menjalankan berbagai jenis aplikasi dan beban kerja, termasuk MapReduce, streaming data, dan algoritma machine learning. YARN menyediakan mekanisme untuk menetapkan sumber daya yang sesuai untuk setiap tugas dan memastikan penggunaan sumber daya yang efisien dalam cluster Hadoop.

2. ***Apache Spark***
Spark adalah platform analisis data terdistribusi open-source yang dirancang untuk kinerja yang tinggi dan kemudahan penggunaan. Ini menyediakan antarmuka pemrograman yang ekspresif dalam bahasa seperti Scala, Java, Python, dan R, serta mendukung berbagai jenis beban kerja data seperti pemrosesan batch, streaming, dan machine learning.

3. ***Apache Cassandra***
Cassandra adalah sistem manajemen basis data terdistribusi yang dirancang untuk menangani volume data besar dengan ketersediaan dan ketahanan terhadap kegagalan yang tinggi. Cassandra dirancang untuk menyimpan data secara terdistribusi di beberapa node tanpa titik tunggal kegagalan, membuatnya ideal untuk aplikasi yang membutuhkan skalabilitas horizontal dan toleransi terhadap kegagalan.

4. ***Apache Flink***
Flink adalah platform pengolahan data terdistribusi open-source yang dirancang untuk analisis data real-time dan batch. Flink menyediakan model pemrosesan data yang kuat dan ekspresif, serta mendukung berbagai aliran data yang bersifat terbatas maupun tak terbatas, memungkinkan analisis real-time yang akurat dan efisien.

### Teknik Penyimpanan pada Big Data
- ***Cluster :***
Sekumpulan server yang terhubung satu sama lain menjadi satu unit

- ***Distributed File System :***
Sistem penyimpanan file dengan ukuran yang besar secara terdistribusi. Ex : Google File System (GFS), Hadoop Distributed File System (HDFS)

- ***NoSQL :***
Mekanisme penyimpanan data non relasional yang fleksibel dan sebagai alternatif dari penyimpanan data relasional

- ***Replication :***
Mekanisme untuk melaukan duplikasi data dari database utama kepada beberapa instance database lainnya

- ***Sharding :***
Mekanisme untuk menyimpan sebuah data melalui beberapa database secara terpisah