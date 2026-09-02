Nama : Sultan Noor Dafiq

NPM : 2506600713

Kelas : PBP E

### Tugas 1

[DOKUMENTASI KERANGKA & ALUR PERANCANGAN WEB PORTOFOLIO]
(11.27 9/2/2026) 
Sebelum melanjutkan proses desain tambahan, saya berinisasi untuk menginstal python package yang bernama "django-browser-reload" guna mempermudah pemantauan terhadap perubahan struktur ataupun tampilan pada website saya setiap kali ada proses rekayasa pada kode html ataupun css projek saya. 

Pada awalnya hanya bekerja secara efektif pada index.html yang selang 1 detik perubahan pada kode akan langsung berimbas pada tampilan websitenya langsung, sementara style.css masih kurang responsif terhadap kemampuan package ini. Namun saya mencoba mengakali dengan bantuan Gemini untuk segera memperbaiki hambatan ini dengan trik Cache-Busting Sementara di HTML

Berikut ini baris kode baru yang saya timpa pada atribut referensi index.html saya sebelumnya:
<link rel="stylesheet" href="{% static 'css/style.css' %}?v=1.1">

Dan Boom!!!
Kedua program desainer visualisasi website portofolio saya sudah dapat bekerja dengan baik dan responsif terhadap perubahan instan pada website portofolio saya secara langsung.

CATATAN:
Kadangkala laptop saya dapat mati sendiri tanpa ada aba-aba indikasi persentase baterai yang akurat sehingga saya ingin memberikan instruksi agar website saya ini bisa berfungsi dan ada tampilannya lagi dengan beberapa perintah berikut.

- Buka terminal pada VSCode/Powershell dengan shortcut: Ctrl + ~
- Aktifkan kembali Virtual Environment dengan perintah: .\env\Scripts\activate
- Jalankan server Django dengan perintah: python manage.py runserver
- Terminal akan memproses perancangan keterangan sinkronisasi website saya dengan server Django kembali
- Selesai


[PERTANYAAN REFLEKTIF]

1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

[RESPON PRIBADI]

1. (Segera dijawab setelah proses desain tambahan pada website portofolio atau tugas individu 1 saya telah selesai)

2. (Segera dijawab setelah proses desain tambahan pada website portofolio atau tugas individu 1 saya telah selesai)

3. (Segera dijawab setelah proses desain tambahan pada website portofolio atau tugas individu 1 saya telah selesai)