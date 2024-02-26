# Version Control and Branch Management (Git)

### Git
Salah satu version control system populer yang digunakan para developer untuk mengembangkan software secara bersama-sama.

### Alur Git
working directory --(git add)--> staging area --(git commit)--> repository

### Perintah Git
#### 1. GIT INIT
Menginisialisasi repositori Git baru di direktori kerja saat ini.

#### 2. GIT CLONE
Menduplikasi repositori Git yang sudah ada ke dalam direktori lokal Anda. Ex : git clone https://github.com/username/repository.git

#### 3. GIT CONFIG
Mengonfigurasi pengaturan Git seperti nama pengguna, alamat email, dan preferensi lainnya. Ex :
- git config --global user.name "Your Name"
- git config --global user.email "your_email@example.com"

#### 4. GIT STATUS
Menampilkan status perubahan pada repositori, termasuk perubahan yang belum di-commit.

#### 5. GIT ADD
Menambahkan perubahan pada file tertentu ke dalam staged area untuk disiapkan untuk commit. Ex :
- git add filename.txt
- git add .

#### 6. GIT COMMIT
Membuat snapshot dari staged changes dan menyimpannya ke dalam repositori. Ex : git commit -m "Initial commit"

#### 7. GIT DIFF
Menunjukkan perbedaan antara file yang ada dalam working directory dan staged changes.

#### 8. GIT STASH
Menyimpan perubahan yang belum di-commit secara sementara untuk digunakan nanti.

#### 9. GIT LOG
Menampilkan riwayat commit pada repositori, termasuk informasi seperti penulis, timestamp, dan pesan commit.

#### 10. GIT CHECKOUT
Pindah ke branch lain atau mengembalikan file ke versi sebelumnya. Ex : git checkout branch-name

#### 11. GIT RESET
Mengembalikan HEAD ke commit tertentu dalam riwayat, yang juga dapat mempengaruhi staged changes dan working directory.
#### 12. GIT FETCH
Mengambil perubahan dari repositori remote tanpa menggabungkannya ke dalam branch lokal Anda. Ex : git fetch origin

#### 13. GIT PULL
Mengambil perubahan dari repositori remote dan menggabungkannya ke dalam branch lokal Anda. Ex : git pull origin master

#### 14. GIT BRANCH
Menampilkan, membuat, atau menghapus branch di repositori Anda. Ex : git branch new-feature

#### 15. GIT MERGE
Menggabungkan perubahan dari branch lain ke branch saat ini. Ex : git merge feature-branch