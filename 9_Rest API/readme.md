SUMMARY - Rest API

## Definisi API
API (Application Programming Interface) merupakan sebuah metode komunikasi antara satu aplikasi dengan satu atau banyak aplikasi lainnya.

## REST API
- REST (Representational State Transfer), yaitu sebuah guideline dan rekomendasi untuk membentuk API dengan pemodelan real world object.
- Berbasiskan protokol HTTP

## HTTP Meyhod
- POST , untuk create data
- GET , untuk menampilkan data
- PUT , untuk update data (body yang dikirim saat melakukan post harus lengkap)
- PATCH , untuk update data (body yang dikirim bisa hanya menyertakan atribute tertentu saja yang ingin di update)
- DELETE , untuk menghapus data

## HTTP Response Code
- 200 OK
- 201 Created
- 400 Bad Request
- 404 Not Found
- 401 Unauthorized
- 405 Method Not Allowed
- 500 Internal Server Error

## REST API Component
- Method | URL (Base URL + Path)
- Header , berisikan meta data dari requuest atau response API. Biasanya berisikan data berupa Authentication, Device info and version, Data type, etc.
- Body

## Definisi JSON
JSON (JavaScript Object Notation) merupakan sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna.