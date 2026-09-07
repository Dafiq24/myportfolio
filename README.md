Nama : Sultan Noor Dafiq

NPM : 2506600713

Kelas : PBP E

## Tugas Individu 1

### DOKUMENTASI KERANGKA & ALUR PERANCANGAN WEB PORTOFOLIO
(11.27 9/2/2026) 
Sebelum melanjutkan proses desain tambahan, saya berinisasi untuk menginstal python package yang bernama "django-browser-reload" guna mempermudah pemantauan terhadap perubahan struktur ataupun tampilan pada website saya setiap kali ada proses rekayasa pada kode html ataupun css projek saya. 

Pada awalnya hanya bekerja secara efektif pada index.html yang selang 1 detik perubahan pada kode akan langsung berimbas pada tampilan websitenya langsung, sementara style.css masih kurang responsif terhadap kemampuan package ini. Namun saya mencoba mengakali dengan bantuan Gemini untuk segera memperbaiki hambatan ini dengan trik Cache-Busting Sementara di HTML

Berikut ini baris kode baru yang saya timpa pada atribut referensi index.html saya sebelumnya:
<link rel="stylesheet" href="{% static 'css/style.css' %}?v=1.1">

Dan Boom!!!
Kedua program desainer visualisasi website portofolio saya sudah dapat bekerja dengan baik dan responsif terhadap perubahan instan pada website portofolio saya secara langsung.

(13.05 - 15.18 9/6/2026)
Setelah halaman Profile dari Tutorial 1 sudah dapat berjalan, saya mulai memikirkan bagaimana caranya mengembangkan halaman tersebut tanpa menghilangkan struktur dan identitas desain awalnya. Saya memilih untuk tetap menggunakan konsep **single-page portfolio**, yaitu seluruh informasi portofolio tetap berada dalam satu halaman yang memanjang ke bawah. Dengan konsep ini, pengunjung tidak perlu berpindah halaman dan nantinya dapat menggunakan navigation bar untuk menuju section tertentu secara langsung.

Sebelum menambahkan section baru, saya mencoba memahami kembali batasan dari static web. Pada tahap Tugas 1 ini, isi website masih disajikan langsung melalui HTML5 dan CSS3 sehingga belum menggunakan database, form dinamis, ataupun pengolahan data melalui backend. Django masih digunakan sebagai fondasi proyek dan untuk menampilkan template, tetapi fokus rekayasa saya pada tahap ini tetap berada pada struktur `index.html` dan tampilan `style.css`. Oleh karena itu, saya memutuskan untuk tidak menyentuh konfigurasi server dan deployment yang sebelumnya sudah berhasil diatur.

Saya kemudian menentukan beberapa section yang mungkin relevan untuk dikembangkan pada portofolio, seperti Skills, Experience, Education, Organizations & Activities, Achievements & Certifications, dan Contact. Akan tetapi, supaya proses pengembangannya tetap progresif dan riwayat pengerjaannya tidak langsung menjadi satu perubahan besar, saya memilih untuk memulai dari section **Skills & Tools** terlebih dahulu.

Dalam menentukan isi Skills, saya tidak ingin mencantumkan persentase kemampuan seperti "Python 90%" atau membuat klaim bahwa saya sudah mahir terhadap seluruh teknologi yang dicantumkan. Saya menggunakan CV pribadi sebagai sumber utama, lalu memilih kemampuan yang memang pernah saya gunakan melalui perkuliahan, workshop, organisasi, dan proyek praktik. Dari proses tersebut, skills saya dikelompokkan menjadi empat bagian berikut:

- **Programming & Web**, yang terdiri dari Python, JavaScript, HTML & CSS, dan SQL.
- **Data & Analysis**, yang terdiri dari Pandas & NumPy, Data Preparation, Exploratory Data Analysis, dan Basic Data Visualization.
- **Design & Productivity**, yang terdiri dari Spreadsheet, Figma, LaTeX, dan Presentation Development.
- **Professional Skills**, yang terdiri dari Analytical Thinking, Project Coordination, Content Development, dan Collaboration.

Pengelompokan tersebut saya pilih agar daftar kemampuan tidak terlihat seperti kumpulan kata yang berdiri sendiri. Setiap jenis kemampuan memiliki konteks dan kedekatan fungsi yang sama sehingga informasi di dalamnya lebih mudah dipindai oleh pembaca. Saya juga menggunakan kalimat pembuka "A growing toolkit" untuk menunjukkan bahwa kemampuan tersebut masih terus saya pelajari dan kembangkan, bukan sebagai klaim bahwa seluruhnya sudah saya kuasai secara sempurna.

Pada `index.html`, saya menambahkan tautan **Skills** di dalam elemen `<nav>` yang mengarah ke `id="skills"`. Saya juga menambahkan elemen `<section>` baru setelah section Profile. Di dalamnya terdapat empat elemen `<article>` yang masing-masing mewakili satu kategori skill. Sementara itu, setiap daftar teknologi dan kemampuan disusun menggunakan `<ul>` dan `<li>`. Struktur ini sengaja dibuat secara semantik agar browser maupun pembaca layar dapat memahami bahwa Skills adalah satu bagian halaman, setiap card adalah konten yang dapat berdiri sendiri, dan setiap kemampuan merupakan bagian dari sebuah daftar.

Untuk interaktivitas sederhana, saya menambahkan `scroll-behavior: smooth` pada CSS. Dengan demikian, saat menu Skills ditekan, halaman akan menggulir menuju section tersebut secara halus. Header juga dibuat sticky supaya navigation bar tetap dapat dijangkau ketika halaman digulir. Pendekatan ini cukup menggunakan HTML dan CSS tanpa menambahkan JavaScript, sehingga masih sesuai dengan materi dan batasan Tugas 1.

Pada `style.css`, section Skills dibuat menggunakan CSS Grid. Dalam tampilan desktop, empat card disusun menjadi dua kolom dan dua baris. Ketika lebar layar mencapai 600px atau kurang, media query mengubah susunannya menjadi satu kolom agar isi card tidak terlalu sempit pada perangkat mobile. Setiap card dilengkapi efek hover ringan sebagai umpan balik visual ketika kursor diarahkan ke dalamnya. Saya juga menambahkan dukungan `prefers-reduced-motion` agar smooth scroll dan transisi dapat dikurangi bagi pengguna yang memilih pengaturan minim animasi pada perangkatnya.

Proses desainnya tidak langsung selesai dalam satu percobaan. Pada tampilan awal, lebar konten masih terlalu sempit karena `.container` menggunakan batas maksimum 960px. Hal tersebut menyebabkan ruang kosong di sisi kanan dan kiri terlihat terlalu luas. Saya kemudian memperluas container secara terkontrol, memadatkan ukuran dan jarak antar-card, serta menyesuaikan ukuran tipografi agar section Profile dan Skills terlihat lebih selaras dalam satu viewport.

Saya juga melakukan beberapa iterasi terhadap section Profile. Ukuran nama diperbesar agar menjadi fokus utama halaman, sementara proporsi kolom kiri diperlebar dan jarak menuju foto diperkecil. Foto dibuat berukuran medium, kemudian posisinya sedikit digeser ke atas dan ke kiri agar komposisinya lebih seimbang. Jarak antara hero kicker, nama, bio, informasi akademik, dan tombol sosial dibuat menggunakan ritme `gap` yang konsisten supaya susunan elemen di kolom kiri tidak terasa terlalu renggang maupun terlalu menumpuk.

Bio yang sebelumnya menggunakan kalimat contoh dari tutorial kemudian disesuaikan dengan ringkasan About Me pada CV saya. Isi bio dibuat lebih singkat agar tetap nyaman dibaca pada halaman web, tetapi masih menyampaikan latar belakang saya sebagai mahasiswa Sistem Informasi Universitas Indonesia serta ketertarikan pada strategic thinking, data-driven analysis, technology, educational programs, student advocacy, dan project coordination. Bagian NPM dan Program juga diberikan card atau highlighter tersendiri agar informasi akademik tersebut dapat dibedakan dari paragraf bio dan tombol media sosial.

Dalam menentukan warna, saya sempat mencoba palet merah yang kuat dari desain awal, kemudian mengevaluasi kembali keterbacaan dan keselarasan antarelemen. Setelah beberapa kali penyesuaian, saya memilih kelompok warna bernuansa biru yang terdiri dari deep navy, navy, medium blue, soft blue, dan light blue. Warna navy digunakan sebagai warna teks utama dan background section Skills, warna biru muda digunakan pada card dan elemen informasi, sedangkan warna ungu digunakan secara terbatas sebagai highlight pada bayangan foto dan efek hover. Pembagian warna ini membuat Profile dan Skills tetap memiliki karakter yang berbeda, tetapi masih terasa sebagai bagian dari website yang sama.

Pada card Skills, posisi nomor kategori dipindahkan ke sudut kanan atas. Perubahan tersebut membuat judul masing-masing kategori dapat berada lebih dekat dengan batas atas card. Jarak antara judul dan daftar skills juga dibuat konsisten agar card terlihat lebih padat, rapi, dan tidak memiliki ruang kosong yang terlalu besar.

Setelah setiap perubahan penting, saya menjalankan pemeriksaan Django menggunakan `python manage.py check` dan memeriksa respons halaman melalui server lokal. Halaman utama dan berkas CSS berhasil memberikan respons tanpa error, sedangkan section Skills tetap dapat ditemukan pada hasil render template. Sampai tahap dokumentasi ini, section Skills sudah berhasil ditampilkan sebagai section baru dengan struktur yang sistematis, responsif, dan gaya visual yang sedikit dibedakan dari Profile. Meskipun demikian, perubahan ini masih berada dalam proses penyempurnaan tampilan dan belum saya commit sampai susunan Profile dan Skills benar-benar sudah sesuai dengan hasil yang saya inginkan.

Dalam proses perancangan dan penulisan ini saya menggunakan bantuan AI, yaitu Gemini untuk membantu menemukan solusi cache-busting pada tahap awal dan Codex untuk membantu menginterpretasikan kebutuhan desain, menyusun struktur semantik section Skills, menyesuaikan CSS responsif, serta melakukan pemeriksaan teknis. Setiap detail teknis tetap saya evaluasi melalui tampilan website secara langsung dan saya mencoba untuk mengubah tampilan lanjutan secara mandiri apabila ukuran, jarak, warna, atau susunan elemen belum sesuai dengan preferensi saya.

(17.00 - 20.32 9/6/2026)
Setelah bagian Profile dan Skills dirasa sudah cukup aman, saya melanjutkan pengembangan ke section **Experience** yang diletakkan tepat setelah Profile. Isi pengalamannya saya ambil dari CV pribadi agar informasi yang dicantumkan tetap relevan dan tidak dilebih-lebihkan. Pengalaman tersebut kemudian disusun dari yang terbaru dalam bentuk timeline, lengkap dengan periode, posisi, organisasi, deskripsi kontribusi, dan beberapa tag kemampuan yang berkaitan.

Saya menggunakan elemen `<article>` untuk setiap pengalaman dan membuat garis vertikal beserta titik penanda supaya urutan waktunya lebih gampang dipahami. Ketika card disorot, hanya border dan bayangannya yang berubah, sedangkan titik timeline tetap diam agar tampilannya tidak terasa goyang. Jarak antara Profile, judul Experience, dan timeline juga saya rapatkan lagi supaya tidak meninggalkan space kosong yang terlalu luas.

Di sebelah timeline, saya menambahkan bagian **Moments Behind the Work** sebagai tempat dokumentasi kegiatan ataupun bukti keikutsertaan baik dalam organisasi maupun kepanitiaan. Bagian ini menggunakan `<aside>` karena fungsinya sebagai informasi visual pendukung dari pengalaman utama. Saya menyediakan total lima bingkai foto dengan placeholder sementara karena file dokumentasinya akan saya tambahkan sendiri di akhir penyelesaian tugas ini. Pada tampilan mobile, galeri tersebut otomatis berpindah ke bawah timeline agar ukuran teks dan fotonya tetap nyaman dilihat.

Setiap bingkai juga sudah diberikan fitur lightbox dengan HTML dan CSS saja. Jadi ketika sebuah foto ditekan, dokumentasinya dapat muncul lebih besar di tengah layar dengan background gelap, lalu ditutup kembali melalui tombol `×` atau area di luarnya. Fitur ini dibuat menggunakan selector `:target`, sehingga masih sesuai dengan batasan Tugas 1 yang belum menggunakan JavaScript. Sampai tahap ini, section Experience, timeline, galeri lima foto, dan interaksi lightbox sudah berhasil dijalankan tanpa error melalui pemeriksaan Django.

(11.00 - 12.45 9/7/2026)
Setelah section Experience selesai, saya melanjutkan pengembangan ke section **Achievements & Certifications** yang ditempatkan sebelum Skills & Tools. Saya menyeleksi sertifikat dari koleksi pribadi dan tidak menampilkan semuanya agar isi portofolio tetap relevan dan tidak terasa penuh. Enam sertifikat yang dipilih adalah Finalist ShARE Global Case Summit 2026, Gemini Certified Student, Super Member of Data Science GDGoC UI, Java Collections Framework dari Udemy, GDP Labs: AI Engineer Session, dan HTML Certificate of Completion dari Mimo. Sertifikat ShARE Global Case Summit saya jadikan pencapaian utama karena menunjukkan hasil sebagai finalis, sedangkan sertifikat lainnya menjadi bukti kegiatan belajar pada bidang teknologi, data, AI, dan web development.

Pada `index.html`, setiap sertifikat disusun sebagai card yang memuat gambar, kategori, judul, penerbit, dan tahun. Card tersebut ditempatkan dalam carousel horizontal yang bergerak otomatis dari kiri ke kanan menggunakan animasi CSS. Isi carousel dibuat dalam dua kelompok yang sama agar pergerakannya dapat berulang dengan mulus. Ketika card disorot, ukurannya sedikit membesar tanpa keluar dari jalur pergerakan. Sertifikat juga dapat ditekan untuk membuka preview yang lebih besar di tengah layar melalui lightbox berbasis selector `:target`, sehingga fitur ini tetap dapat berjalan tanpa JavaScript.

File sertifikat PDF yang terpilih diubah menjadi gambar preview dan diletakkan pada folder `static/img/certificates`, sedangkan file sumber aslinya tetap tidak diubah. Ukuran gambar, bingkai, padding, jarak antarkartu, dan bayangan kemudian saya rapatkan kembali supaya carousel terlihat lebih compact. Pada tampilan mobile, animasi otomatis dihentikan dan carousel dapat digeser secara horizontal menggunakan jari agar pengunjung tetap dapat mengontrol sertifikat yang ingin dilihat.

Warna section ini memadukan palet biru sebelumnya dengan tambahan dusty pink, blush, soft blue, slate blue, dan deep navy. Deep navy digunakan sebagai background utama, sedangkan pink dan soft blue digunakan secara terbatas pada border, bayangan, serta efek hover. Hasilnya, section Certifications memiliki tampilan yang sedikit berbeda dari Experience dan Skills, tetapi masih terasa menyatu dengan identitas visual keseluruhan website.

### CATATAN:

#### Mengaktifkan Environment dan Server Django Kembali

Kadangkala laptop saya dapat mati sendiri tanpa ada aba-aba indikasi persentase baterai yang akurat sehingga saya ingin memberikan instruksi agar website saya ini bisa berfungsi dan ada tampilannya lagi dengan beberapa perintah berikut.

- Buka terminal pada VSCode/Powershell dengan shortcut: Ctrl + ~
- Aktifkan kembali Virtual Environment dengan perintah: .\env\Scripts\activate
- Jalankan server Django dengan perintah: python manage.py runserver
- Terminal akan memproses perancangan keterangan sinkronisasi website saya dengan server Django kembali
- Selesai

##### Mengakses Website melalui Mobile

Untuk mengecek apakah tampilan website saya sudah responsive di perangkat mobile, laptop dan HP harus terhubung ke jaringan Wi-Fi yang sama. Setelah itu, saya dapat melihat IPv4 laptop melalui terminal dengan perintah:

```powershell
ipconfig | findstr /i "IPv4"
```

Alamat IPv4 yang muncul kemudian ditambahkan sementara ke bagian `ALLOWED_HOSTS` pada `portofolio/settings.py`. Sebagai contoh, apabila IP laptop saya adalah `192.168.0.4`, konfigurasinya menjadi:

```python (file: settings.py)
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "192.168.0.4",
    "sultan-noor-myportofolio.pws.cs.ui.ac.id",
]
```

Selanjutnya, server Django dijalankan agar dapat menerima koneksi dari perangkat lain dalam jaringan yang sama:

```powershell
python manage.py runserver 192.168.0.4:8000
```

Terakhir, saya membuka `http://192.168.0.4:8000` melalui browser HP dengan menyesuaikan alamatnya berdasarkan IPv4 laptop yang sedang digunakan. Jika Windows Firewall meminta izin, akses cukup diberikan untuk **Private Network**. IP lokal dapat berubah ketika berganti atau menyambungkan ulang Wi-Fi, jadi saya perlu menjalankan `ipconfig` lagi apabila alamat sebelumnya sudah tidak dapat digunakan.


### PERTANYAAN REFLEKTIF

1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

### RESPON PRIBADI

1. (Segera dijawab setelah proses desain tambahan pada website portofolio atau tugas individu 1 saya telah selesai)

2. (Segera dijawab setelah proses desain tambahan pada website portofolio atau tugas individu 1 saya telah selesai)

3. (Segera dijawab setelah proses desain tambahan pada website portofolio atau tugas individu 1 saya telah selesai)
