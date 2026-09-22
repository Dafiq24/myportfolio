# My Portfolio - Sultan Noor Dafiq

Nama : Sultan Noor Dafiq

NPM : 2506600713

Kelas : PBP E

## Daftar Isi

- [Tugas Individu 1](#tugas-individu-1)
  - [Dokumentasi Tugas 1](#dokumentasi-tugas-1)
  - [Catatan Tugas 1](#catatan-tugas-1)
  - [Transparansi Penggunaan AI Tugas 1](#transparansi-penggunaan-ai-tugas-1)
  - [Pertanyaan Reflektif Tugas 1](#pertanyaan-reflektif-tugas-1)
  - [Tugas 1](#tugas-1)
- [Tugas Individu 2](#tugas-individu-2)
  - [Dokumentasi Tugas 2](#dokumentasi-tugas-2)
  - [Catatan Tugas 2](#catatan-tugas-2)
  - [Transparansi Penggunaan AI Tugas 2](#transparansi-penggunaan-ai-tugas-2)
  - [Pertanyaan Reflektif Tugas 2](#pertanyaan-reflektif-tugas-2)
  - [Tugas 2](#tugas-2)
- [Tugas Individu 3](#tugas-individu-3)
  - [Dokumentasi Tugas 3](#dokumentasi-tugas-3)
  - [Catatan Tugas 3](#catatan-tugas-3)
  - [Transparansi Penggunaan AI Tugas 3](#transparansi-penggunaan-ai-tugas-3)
  - [Pertanyaan Reflektif Tugas 3](#pertanyaan-reflektif-tugas-3)
  - [Tugas 3](#tugas-3)
- [Tugas Individu 4](#tugas-individu-4)
  - [Dokumentasi Tugas 4](#dokumentasi-tugas-4)
  - [Catatan Tugas 4](#catatan-tugas-4)
  - [Transparansi Penggunaan AI Tugas 4](#transparansi-penggunaan-ai-tugas-4)
  - [Pertanyaan Reflektif Tugas 4](#pertanyaan-reflektif-tugas-4)

## Tugas Individu 1

### Dokumentasi Tugas 1

#### (11.27 9/2/2026)
Sebelum melanjutkan proses desain tambahan, saya berinisasi untuk menginstal python package yang bernama "django-browser-reload" guna mempermudah pemantauan terhadap perubahan struktur ataupun tampilan pada website saya setiap kali ada proses rekayasa pada kode html ataupun css projek saya. 

Pada awalnya hanya bekerja secara efektif pada index.html yang selang 1 detik perubahan pada kode akan langsung berimbas pada tampilan websitenya langsung, sementara style.css masih kurang responsif terhadap kemampuan package ini. Namun saya mencoba mengakali dengan bantuan Gemini untuk segera memperbaiki hambatan ini dengan trik Cache-Busting Sementara di HTML

Berikut ini baris kode baru yang saya timpa pada atribut referensi index.html saya sebelumnya:
<link rel="stylesheet" href="{% static 'css/style.css' %}?v=1.1">

Dan Boom!!!
Kedua program desainer visualisasi website portofolio saya sudah dapat bekerja dengan baik dan responsif terhadap perubahan instan pada website portofolio saya secara langsung.

#### (13.05 - 15.18 9/6/2026)
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

#### (17.00 - 20.32 9/6/2026)
Setelah bagian Profile dan Skills dirasa sudah cukup aman, saya melanjutkan pengembangan ke section **Experience** yang diletakkan tepat setelah Profile. Isi pengalamannya saya ambil dari CV pribadi agar informasi yang dicantumkan tetap relevan dan tidak dilebih-lebihkan. Pengalaman tersebut kemudian disusun dari yang terbaru dalam bentuk timeline, lengkap dengan periode, posisi, organisasi, deskripsi kontribusi, dan beberapa tag kemampuan yang berkaitan.

Saya menggunakan elemen `<article>` untuk setiap pengalaman dan membuat garis vertikal beserta titik penanda supaya urutan waktunya lebih gampang dipahami. Ketika card disorot, hanya border dan bayangannya yang berubah, sedangkan titik timeline tetap diam agar tampilannya tidak terasa goyang. Jarak antara Profile, judul Experience, dan timeline juga saya rapatkan lagi supaya tidak meninggalkan space kosong yang terlalu luas.

Di sebelah timeline, saya menambahkan bagian **Moments Behind the Work** sebagai tempat dokumentasi kegiatan ataupun bukti keikutsertaan baik dalam organisasi maupun kepanitiaan. Bagian ini menggunakan `<aside>` karena fungsinya sebagai informasi visual pendukung dari pengalaman utama. Saya menyediakan total lima bingkai foto dengan placeholder sementara karena file dokumentasinya akan saya tambahkan sendiri di akhir penyelesaian tugas ini. Pada tampilan mobile, galeri tersebut otomatis berpindah ke bawah timeline agar ukuran teks dan fotonya tetap nyaman dilihat.

Setiap bingkai juga sudah diberikan fitur lightbox dengan HTML dan CSS saja. Jadi ketika sebuah foto ditekan, dokumentasinya dapat muncul lebih besar di tengah layar dengan background gelap, lalu ditutup kembali melalui tombol `×` atau area di luarnya. Fitur ini dibuat menggunakan selector `:target`, sehingga masih sesuai dengan batasan Tugas 1 yang belum menggunakan JavaScript. Sampai tahap ini, section Experience, timeline, galeri lima foto, dan interaksi lightbox sudah berhasil dijalankan tanpa error melalui pemeriksaan Django.

#### (11.00 - 12.45 9/7/2026)
Setelah section Experience selesai, saya melanjutkan pengembangan ke section **Achievements & Certifications** yang ditempatkan sebelum Skills & Tools. Saya menyeleksi sertifikat dari koleksi pribadi dan tidak menampilkan semuanya agar isi portofolio tetap relevan dan tidak terasa penuh. Enam sertifikat yang dipilih adalah Finalist ShARE Global Case Summit 2026, Gemini Certified Student, Super Member of Data Science GDGoC UI, Java Collections Framework dari Udemy, GDP Labs: AI Engineer Session, dan HTML Certificate of Completion dari Mimo. Sertifikat ShARE Global Case Summit saya jadikan pencapaian utama karena menunjukkan hasil sebagai finalis, sedangkan sertifikat lainnya menjadi bukti kegiatan belajar pada bidang teknologi, data, AI, dan web development.

Pada `index.html`, setiap sertifikat disusun sebagai card yang memuat gambar, kategori, judul, penerbit, dan tahun. Card tersebut ditempatkan dalam carousel horizontal yang bergerak otomatis dari kiri ke kanan menggunakan animasi CSS. Isi carousel dibuat dalam dua kelompok yang sama agar pergerakannya dapat berulang dengan mulus. Ketika card disorot, ukurannya sedikit membesar tanpa keluar dari jalur pergerakan. Sertifikat juga dapat ditekan untuk membuka preview yang lebih besar di tengah layar melalui lightbox berbasis selector `:target`, sehingga fitur ini tetap dapat berjalan tanpa JavaScript.

File sertifikat PDF yang terpilih diubah menjadi gambar preview dan diletakkan pada folder `static/img/certificates`, sedangkan file sumber aslinya tetap tidak diubah. Ukuran gambar, bingkai, padding, jarak antarkartu, dan bayangan kemudian saya rapatkan kembali supaya carousel terlihat lebih compact. Pada tampilan mobile, animasi otomatis dihentikan dan carousel dapat digeser secara horizontal menggunakan jari agar pengunjung tetap dapat mengontrol sertifikat yang ingin dilihat.

Warna section ini memadukan palet biru sebelumnya dengan tambahan dusty pink, blush, soft blue, slate blue, dan deep navy. Deep navy digunakan sebagai background utama, sedangkan pink dan soft blue digunakan secara terbatas pada border, bayangan, serta efek hover. Hasilnya, section Certifications memiliki tampilan yang sedikit berbeda dari Experience dan Skills, tetapi masih terasa menyatu dengan identitas visual keseluruhan website.

#### (17.35 - 19.48 9/7/2026)
Pada tahap terakhir, saya menambahkan section **Contact** sebagai penutup dari single-page portfolio. Seluruh teks yang tampil pada website diselaraskan menggunakan bahasa Inggris agar penyampaiannya lebih konsisten. Tautan Email, LinkedIn, dan GitHub yang sebelumnya berada di Profile dipindahkan ke Contact, sehingga bagian Profile dapat dibuat lebih ringkas dan fokus pada identitas, foto, bio, NPM, serta program studi. Penulisan program studi juga disesuaikan menjadi "Bachelor's Program in Information Systems" tanpa mengubah informasi akademik aslinya.

Section Contact menggunakan headline "Let's turn ideas into something useful", kalimat ajakan untuk berdiskusi, serta card status ketersediaan untuk kolaborasi dan kesempatan belajar. Empat tindakan utama yang ditampilkan adalah Email, LinkedIn, GitHub, dan View My CV. File CV disimpan pada `static/docs/CV_Sultan_Noor_Dafiq.pdf` dan dibuka melalui tab baru agar pengunjung dapat membacanya tanpa langsung mengunduh. Seluruh tautan eksternal dilengkapi `target="_blank"` dan `rel="noopener noreferrer"`, sedangkan alamat email tetap menggunakan `mailto:`.

Saya kemudian menambahkan WhatsApp, Instagram, X, dan Medium sebagai kontak tambahan. Keempatnya dibuat dalam card yang lebih pendek agar tidak mengganggu hierarki tombol utama. WhatsApp diarahkan melalui tautan `wa.me`, sedangkan platform lainnya menuju profil masing-masing. Setiap card menggunakan ikon SVG inline yang ditulis langsung pada HTML, sehingga ikon tetap tajam pada berbagai ukuran layar tanpa membutuhkan library atau file gambar tambahan. Efek hover dibagi menggunakan aksen biru muda dan dusty pink agar tetap konsisten dengan palet website.

Layout Contact menggunakan CSS Grid dengan empat kolom pada desktop, dua kolom pada tablet, dan satu kolom pada mobile. Navigation bar juga dibuat dapat digeser secara horizontal pada layar sempit karena jumlah section sudah bertambah menjadi Profile, Experience, Certifications, Skills, dan Contact. Beberapa kali penyesuaian dilakukan pada ukuran card, padding, jarak antarderetan, serta ruang menuju footer sampai seluruh bagian terlihat compact tetapi tetap memiliki ruang napas yang cukup.

Pada galeri Experience, foto kegiatan Student Welfare BEM Fasilkom UI dengan nama file `SBFAdkesma.jpeg` mulai dimasukkan sebagai dokumentasi pertama. Posisi BEM Fasilkom UI ditukar dengan BETIS Fasilkom UI agar foto yang sudah tersedia menempati frame utama. Foto ditampilkan menggunakan `object-fit: cover` di dalam bingkai dan `object-fit: contain` ketika dibuka melalui lightbox. Empat bingkai lainnya tetap mempertahankan nama kegiatannya, tetapi area fotonya menampilkan tulisan "Coming soon" sampai seluruh dokumentasi siap ditambahkan. Dengan tahap ini, struktur utama website telah tersusun lengkap dari Profile, Experience, Achievements & Certifications, Skills & Tools, hingga Contact.


### Catatan Tugas 1

#### Mengaktifkan Environment dan Server Django Kembali

Kadangkala laptop saya dapat mati sendiri tanpa ada aba-aba indikasi persentase baterai yang akurat sehingga saya ingin memberikan instruksi agar website saya ini bisa berfungsi dan ada tampilannya lagi dengan beberapa perintah berikut.

- Buka terminal pada VSCode/Powershell dengan shortcut: Ctrl + ~
- Aktifkan kembali Virtual Environment dengan perintah: .\env\Scripts\activate
- Jalankan server Django dengan perintah: python manage.py runserver
- Terminal akan memproses perancangan keterangan sinkronisasi website saya dengan server Django kembali
- Selesai

#### Mengakses Website melalui Mobile

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


### Transparansi Penggunaan AI Tugas 1

Dalam pengerjaan tugas ini, saya menggunakan Gemini dan Codex sebagai alat bantu diskusi serta pendamping teknis pada beberapa tahap pengembangan. Gemini membantu saya menemukan pendekatan cache-busting ketika perubahan CSS belum langsung terbaca, sedangkan Codex membantu mengembangkan alternatif struktur HTML, CSS responsif, dan pemeriksaan teknis. Saya tidak memberikan satu instruksi besar untuk menghasilkan website secara langsung. Prosesnya saya pecah menjadi banyak persoalan kecil, kemudian saya menyampaikan tujuan, referensi visual, tangkapan layar hasil implementasi, dan koreksi yang spesifik untuk setiap persoalan tersebut.

Setiap saran tetap saya analisis berdasarkan kebutuhan portofolio dan hasil tampilannya. Saya menentukan sendiri urutan section, menyeleksi pengalaman dan sertifikat dari data pribadi, menyusun prioritas informasi, memilih serta memadukan palet warna, dan mengevaluasi perubahan layout pada desktop maupun mobile. Ketika hasil implementasi membuat foto terlalu besar, ruang antarelemen tidak seimbang, atau caption galeri ikut berubah, saya mengidentifikasi bagian yang bermasalah lalu mengonstruksi ulang kebutuhannya melalui koreksi yang lebih terarah. Saya juga membandingkan hasil antarukuran layar, menguji navigasi dan tautan, serta menjalankan `python manage.py check` sebelum perubahan disimpan ke Git. Oleh karena itu, bantuan AI menjadi bagian dari proses eksplorasi dan pemecahan masalah, sementara arah desain, penalaran, evaluasi, dan keputusan akhirnya tetap dibangun melalui keterlibatan aktif saya selama proses pengerjaan.


### Pertanyaan Reflektif Tugas 1

1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

### Tugas 1

1. Ya, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, dan `<footer>`. Elemen `<section>` membagi halaman menjadi Profile, Experience, Achievements & Certifications, Skills & Tools, dan Contact, sedangkan `<article>` digunakan untuk konten yang dapat berdiri sendiri seperti card pengalaman dan kategori skills. Saya juga menggunakan `<aside>` untuk galeri dokumentasi karena bagian tersebut berfungsi sebagai pendukung dari informasi utama pada Experience. Penggunaan elemen semantik membantu saya melihat website bukan hanya sebagai kumpulan `<div>`, tetapi sebagai susunan informasi yang memiliki fungsi masing-masing. Struktur kode menjadi lebih mudah dibaca, dikembangkan, dan dirawat ketika section baru ditambahkan. Walaupun website ini masih bersifat statis, struktur tersebut menjadi fondasi yang lebih baik untuk aksesibilitas dan pengembangan website dinamis pada tahap berikutnya.

2. Tantangan terbesar dalam membuat tampilan responsive adalah menyadari bahwa layout desktop tidak dapat hanya diperkecil untuk digunakan pada mobile. Susunan dua kolom pada Profile, timeline dan galeri yang berdampingan pada Experience, card Skills, carousel Certifications, serta navigation bar membutuhkan perlakuan yang berbeda ketika ruang layar semakin terbatas. Pada beberapa percobaan awal, ukuran judul terlalu besar, jarak antarelemen terasa longgar, dan beberapa card menjadi terlalu sempit untuk dibaca dengan nyaman. Saya mengevaluasi setiap elemen berdasarkan keterbacaan, fungsi, dan urutan kepentingannya. Foto Profile dipindahkan ke bawah identitas pada mobile, galeri ditempatkan setelah timeline, card Skills disusun menjadi satu kolom, dan carousel Certifications diubah menjadi horizontal scrolling yang dapat digeser menggunakan jari. Ukuran font, padding, gap, serta lebar card juga disesuaikan melalui media query. Dari proses ini saya memahami bahwa responsive design bukan sekadar mengecilkan ukuran, melainkan menyusun ulang pengalaman pengguna agar informasi utama tetap mudah dipahami pada setiap perangkat.

3. Batasan yang paling saya rasakan dari static web adalah seluruh konten masih ditulis langsung di dalam template HTML. Setiap kali ingin menambahkan pengalaman, sertifikat, skills, atau dokumentasi kegiatan, saya perlu membuka dan mengubah kode secara manual. Cara ini masih cukup untuk portofolio sederhana, tetapi akan menjadi kurang praktis ketika isi website terus berkembang. Bagian Contact juga belum dapat menerima data dari pengunjung karena saat ini hanya menggunakan tautan email dan media profesional. Pada iterasi berikutnya, saya ingin mengembangkan Django Admin dan contact form. Django model, database, dan Django Admin akan digunakan untuk mengelola isi Experience, Certifications, Skills, serta dokumentasi tanpa perlu menyusun ulang desain HTML setiap kali ada data baru. Setelah itu, contact form akan memungkinkan pengunjung mengirimkan nama, email, dan pesan secara langsung dengan validasi dari Django, kemudian pesannya dapat disimpan atau diteruskan ke email saya. Bagi saya, kedua fitur tersebut merupakan langkah penting untuk mengubah portofolio ini dari halaman informasi statis menjadi website yang lebih mudah dikelola oleh pemilik sekaligus lebih interaktif bagi pengunjung.


## Tugas Individu 2

### Dokumentasi Tugas 2

#### (13.00 - 14.26 9/8/2026)
Setelah menyelesaikan Tutorial 02, saya mulai menerapkan kembali alur Model-View-Template pada bagian Certifications. Saya memilih bagian ini karena enam sertifikat pilihan beserta tampilan carousel-nya sudah tersedia dari Tugas Individu 1, tetapi seluruh datanya masih ditulis langsung di dalam `index.html`. Pada tahap awal ini, fokus saya belum berada pada perubahan tampilan, melainkan pada pembentukan struktur data yang nantinya menjadi sumber informasi bagi halaman Certifications yang terpisah.

Saya menambahkan model `Certification` pada aplikasi `main` dengan UUID sebagai primary key. Informasi setiap sertifikat dipisahkan ke dalam field `title`, `issuer`, `category`, `issued_year`, `image_path`, `credential_url`, `description`, dan `is_featured`. Field `category` menggunakan pilihan Achievement, Certification, Course, dan Workshop agar kategorinya konsisten, sedangkan `image_path` digunakan untuk menghubungkan data dengan gambar yang sudah tersimpan di dalam static files tanpa memindahkan aset tersebut. Saya juga menambahkan pengurutan melalui `Meta.ordering` supaya sertifikat unggulan muncul lebih dahulu, kemudian diikuti tahun terbaru dan judul secara alfabetis.

Sebelum membuat migration, saya menjalankan `python manage.py check` dan melakukan preview menggunakan `python manage.py makemigrations --dry-run --verbosity 3`. Setelah struktur model dipastikan sesuai, saya membuat migration `0002_certification.py`, menerapkannya dengan `python manage.py migrate`, lalu memeriksa hasilnya melalui `python manage.py showmigrations main` dan `python manage.py makemigrations --check`. Seluruh pemeriksaan berhasil tanpa masalah dan kedua migration pada aplikasi `main` sudah berstatus diterapkan.

Sebagai validasi awal, saya memasukkan enam data sertifikat pribadi melalui Django shell menggunakan `update_or_create`. Pendekatan ini dipilih agar proses pengisian dapat dijalankan kembali tanpa membuat data duplikat. Queryset kemudian diperiksa berdasarkan judul, kategori, tahun, dan status unggulan; hasilnya menunjukkan enam objek tersimpan dan Finalist ShARE Global Case Summit berada pada urutan pertama karena memiliki nilai `is_featured=True`. Data tersebut masih berada pada database lokal, sedangkan model dan berkas migration disimpan pada Git melalui commit terpisah sebagai fondasi Chapter 1.

#### (19.53 - 21.34 9/10/2026)
Sebelum melanjutkan implementasi halaman dinamis, saya menyesuaikan versi framework dengan ketentuan terbaru Tugas Individu 2. Dependensi Django pada `requirements.txt` dikunci ke versi `5.0` dan `django-browser-reload` dicantumkan secara eksplisit karena digunakan oleh konfigurasi proyek. Setelah memasang ulang dependensi di dalam virtual environment, saya memastikan versi aktif melalui `python -m django --version`, memeriksa kompatibilitas paket menggunakan `python -m pip check`, serta menjalankan kembali system check, migration check, dan seluruh test. Hasil pemeriksaan menunjukkan bahwa proyek tetap berjalan dengan baik pada Django 5.0 sebelum perubahan fitur berikutnya dilakukan.

Pada Chapter 2, saya menghubungkan model `Certification` dengan lapisan view, URL, dan template. View `show_certifications` mengambil queryset melalui `Certification.objects.all()` dan mengirimkannya sebagai `certification_list`. View tersebut didaftarkan pada URL bernama `main:show_certifications` dengan alamat `/certifications/`, sehingga halaman dapat diakses secara terpisah dari halaman Profile. Tautan Certifications pada navigation bar juga diubah menggunakan template tag `{% url %}` agar tidak bergantung pada alamat yang ditulis secara manual.

Saya membuat `certifications.html` dengan tetap mempertahankan bahasa visual dari Tugas Individu 1. Seluruh certificate card dirender menggunakan `{% for certification in certification_list %}`. Judul, penerbit, kategori, tahun, status featured, dan lokasi gambar berasal dari objek model, sedangkan `get_category_display` digunakan untuk menampilkan label kategori yang mudah dibaca. Queryset dirender kembali sebagai salinan noninteraktif agar animasi carousel desktop tetap bergerak secara mulus. Setiap objek juga menghasilkan target lightbox unik berdasarkan UUID-nya, sehingga preview gambar tetap dapat dibuka tanpa JavaScript. Kondisi `{% empty %}` diwujudkan melalui pesan yang informatif ketika belum ada sertifikat yang tersimpan.

Pemisahan halaman sempat membuat desain Experience dari Tugas Individu 1 terlalu sederhana dan database lokal baru berisi dua objek. Saya memperbaikinya tanpa mengembalikan data ke bentuk hardcoded. Model `Experience` diperluas dengan field `organization`, `period`, `display_order`, dan `skills`, serta properti `skill_list` untuk mengubah daftar skill tersimpan menjadi tag yang dapat diiterasi pada template. Migration `0003_expand_and_restore_experiences.py` menambahkan struktur tersebut sekaligus memulihkan empat pengalaman lama secara terurut. Dengan demikian, timeline, organisasi, deskripsi, dan skill tags tetap berasal dari database, sedangkan galeri dokumentasi, placeholder, hover interaction, dan CSS-only lightbox kembali menggunakan desain presentasional sebelumnya.

Sebagai penyelarasan akhir, heading Experience dan Certifications disesuaikan dengan hierarki visual pada section Skills, mencakup ukuran judul responsif, lebar konten, jarak antarjudul dan deskripsi, serta spacing menuju konten utama. Implementasi kemudian diverifikasi menggunakan `python manage.py check`, `python manage.py makemigrations --check`, `python manage.py test`, dan `git diff --check`. Seluruh enam test berhasil dijalankan, tidak terdapat perubahan model yang belum memiliki migration, dan pemeriksaan Django tidak menemukan masalah.

#### (20.42 - 22.51 9/11/2026)
Pada Part 3, saya memusatkan pengerjaan pada pengujian otomatis dan audit sumber data halaman Certifications. Test suite sebelumnya hanya mencakup halaman Profile dan Experience, sehingga belum ada bukti otomatis bahwa implementasi bagian baru benar-benar mengikuti alur Model-View-Template. Saya menambahkan kelas `CertificationTest` yang membangun objek uji secara terisolasi pada test database agar pengujian tidak bergantung pada enam data yang tersimpan di database lokal.

Pengujian yang ditambahkan mencakup representasi string model dan label kategori, keberhasilan named route `main:show_certifications`, penggunaan template `certifications.html`, serta kemunculan judul, penerbit, tahun, dan UUID lightbox dari objek model pada respons HTML. Saya juga menguji empty state dengan menghapus seluruh objek Certification selama test, kemudian memastikan halaman tetap memberikan status HTTP 200 dan menampilkan pesan yang sesuai. Perilaku `Meta.ordering` diverifikasi dengan membuat sertifikat featured dan memastikan objek tersebut ditempatkan pada urutan pertama. Selain itu, halaman Profile diperiksa untuk memastikan navbar menghasilkan alamat Certifications melalui named URL.

Audit template menemukan bahwa markup sertifikat statis dari Tugas Individu 1 masih tersimpan di dalam blok `{% comment %}` pada `index.html`. Meskipun blok tersebut tidak ditampilkan oleh browser, saya menghapusnya secara menyeluruh agar data sertifikat hanya memiliki satu sumber kebenaran, yaitu model `Certification`. Langkah ini juga mengurangi duplikasi sebanyak 160 baris dan membuat batas tanggung jawab antartemplate lebih jelas: `index.html` menangani halaman Profile, sedangkan `certifications.html` menangani daftar sertifikat dinamis.

Setelah perubahan selesai, saya menjalankan `python manage.py check`, `python manage.py test`, `python manage.py makemigrations --check`, dan `git diff --check`. Jumlah test meningkat dari enam menjadi sebelas dan seluruhnya berhasil dijalankan. Django tidak menemukan masalah konfigurasi maupun perubahan model tanpa migration, sedangkan pemeriksaan diff tidak menemukan whitespace error. Dengan pengujian tersebut, route, template, data model, empty state, ordering, dan navigasi halaman Certifications kini memiliki perlindungan regresi yang dapat dijalankan kembali setelah pengembangan berikutnya.

#### (15.49 - 18.15 9/12/2026)
Pada Chapter 4, saya menambahkan halaman detail sertifikat sebagai pengembangan opsional di luar halaman daftar yang diwajibkan. Setiap objek kini memiliki alamat detail sendiri dengan pola `/certifications/<uuid>/`. Named route `main:show_certification_detail` meneruskan UUID ke view `show_certification_detail`, kemudian `get_object_or_404` mencari objek yang sesuai pada model `Certification`. Pendekatan ini membuat URL tetap unik dan memastikan permintaan terhadap sertifikat yang tidak tersedia menghasilkan respons 404 secara aman, bukan error server.

Template `certification_detail.html` menampilkan gambar, judul, penerbit, kategori, tahun, deskripsi, status featured, dan credential URL dari satu objek model. Tautan menuju detail ditempatkan di dalam lightbox setiap sertifikat agar interaksi carousel yang sudah ada tidak berubah. Halaman detail dirancang dengan layout dua kolom pada desktop dan satu kolom pada layar yang lebih sempit, serta menyediakan navigasi kembali ke daftar Certifications. Tautan credential hanya ditampilkan ketika field `credential_url` memiliki nilai, sehingga template tetap rapi untuk data yang belum mempunyai tautan eksternal.

Saya juga mengaktifkan pengelolaan konten melalui Django Admin dengan mendaftarkan model `Experience` dan `Certification`. Konfigurasi `ModelAdmin` menyediakan kolom ringkas untuk informasi penting, pencarian berdasarkan judul, organisasi, penerbit, deskripsi, atau skills, filter kategori, tahun, dan status featured, serta urutan data yang konsisten dengan halaman publik. Fitur ini membuat konten portofolio dapat diperbarui melalui antarmuka terstruktur tanpa mengubah template HTML atau menjalankan query database secara manual.

Empat test tambahan dibuat untuk memverifikasi halaman detail, keterhubungan halaman daftar dengan detail, respons 404 untuk UUID yang tidak dikenal, dan registrasi kedua model pada admin site. Setelah implementasi, `python manage.py test` menjalankan total 15 test dan seluruhnya berhasil. `python manage.py makemigrations --check` juga menyatakan tidak ada perubahan model yang belum tercatat. Penambahan detail page, graceful error handling, admin configuration, responsive presentation, dan regression tests menjadi upaya untuk mengembangkan proyek melampaui checklist minimum sambil tetap mempertahankan pemisahan tanggung jawab Model-View-Template.

#### (Finalisasi 9/13/2026)

Pada audit akhir, saya menyadari bahwa enam data Certification semula dimasukkan melalui Django shell dan hanya tersimpan pada `db.sqlite3` lokal. Karena database lokal tidak dikirim ke Git, fresh clone dan deployment dapat memiliki tabel Certification tanpa data yang ditampilkan. Saya menutup celah tersebut melalui data migration `0004_seed_certifications.py`. Migration menggunakan `update_or_create` agar enam sertifikat tersedia secara konsisten tanpa membuat duplikat ketika judul yang sama sudah ada. Fungsi reverse migration juga disediakan agar data seed dapat dibatalkan secara terkontrol.

Test Certifications kemudian dibuat independen dari seed dengan membersihkan objek pada `setUp` sebelum membangun data uji sendiri. Setelah migration diterapkan, database lokal tetap berisi tepat enam sertifikat dan seluruh 15 test lulus. Pendekatan ini memisahkan data awal aplikasi dari data pengujian sekaligus memastikan bahwa halaman dinamis tidak bergantung pada keadaan SQLite milik satu komputer.

#### Audit Akhir Checklist Tugas 2

| Ketentuan | Implementasi dan bukti |
| --- | --- |
| Model baru pada aplikasi `main` | Model `Certification` menggunakan UUID serta delapan field informasi sertifikat. |
| Migration dibuat dan diterapkan | `0002_certification.py` membuat model dan `0004_seed_certifications.py` menyediakan enam data awal yang portabel. |
| View mengambil data model | `show_certifications` mengambil queryset dan mengirimkan `certification_list` melalui context. |
| Template baru, loop, dan empty state | `certifications.html` menggunakan Django Template Language untuk card, duplikasi carousel, lightbox, dan kondisi tanpa data. |
| Tidak ada data baru yang hardcoded di HTML | Markup sertifikat statis lama sudah dihapus; konten sertifikat berasal dari model dan data migration. |
| Named route dan navbar | `main:show_certifications` tersedia pada `/certifications/` dan dipanggil menggunakan `{% url %}`. |
| Navbar dan footer konsisten | Halaman Profile, Experience, Certifications, dan detail menggunakan susunan navigasi serta footer yang sama. |
| Unit test | Sebanyak 15 test mencakup URL, template, data, empty state, ordering, detail, 404, navigasi, dan registrasi admin. |
| Proyek berjalan tanpa error | Django system check, migration check, dan seluruh test berhasil dijalankan menggunakan Django 5.0. |
| Fitur tambahan | Detail sertifikat berbasis UUID, graceful 404, responsive detail page, CSS-only lightbox, dan custom Django Admin. |


### Catatan Tugas 2

#### Menjalankan Proyek dari Fresh Clone

```powershell
git clone https://github.com/Dafiq24/myportfolio.git
cd myportfolio
python -m venv env
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py check
python manage.py test
python manage.py runserver
```

Setelah server berjalan, halaman utama dapat dibuka melalui `http://127.0.0.1:8000/`, daftar sertifikat melalui `http://127.0.0.1:8000/certifications/`, dan Experience melalui `http://127.0.0.1:8000/experience/`. Perintah `migrate` juga memasang struktur database serta data awal Experience dan Certification yang disediakan melalui migration.

#### Mengakses Django Admin

Django Admin digunakan sebagai antarmuka pengelolaan data `Experience` dan `Certification` pada database. Sebelum mengaksesnya untuk pertama kali, virtual environment perlu diaktifkan dan akun superuser lokal perlu dibuat:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\Activate.ps1
python manage.py createsuperuser
```

Username, email, dan password diisi langsung melalui terminal. Karakter password tidak ditampilkan saat diketik, tetapi tetap diterima oleh terminal. Setelah muncul pesan `Superuser created successfully`, server dapat dijalankan:

```powershell
python manage.py runserver
```

Halaman admin kemudian dibuka melalui `http://127.0.0.1:8000/admin/`. Setelah login, data Experience dan Certification dapat ditambah, dicari, difilter, diurutkan, diperbarui, atau dihapus melalui panel masing-masing. Perubahan yang dilakukan melalui admin langsung memengaruhi database yang sedang digunakan oleh aplikasi.

Akun superuser lokal tersimpan di `db.sqlite3` dan tidak dikirim ke Git karena database tersebut diabaikan oleh `.gitignore`. Username maupun password tidak boleh ditulis di README atau dimasukkan ke repository. Database deployment PWS terpisah dari database lokal, sehingga akun superuser lokal dan perubahan data lokal tidak otomatis tersedia pada PWS.


### Transparansi Penggunaan AI Tugas 2

Dalam Tugas Individu 2, saya menggunakan Codex sebagai pendamping diskusi teknis, pemeriksaan kode, dan dokumentasi. Penggunaannya dilakukan secara bertahap, bukan melalui satu prompt untuk menghasilkan seluruh tugas. Saya terlebih dahulu menentukan Certifications sebagai bagian portofolio yang akan dimigrasikan, memilih enam sertifikat pribadi, menetapkan bahwa desain carousel dan lightbox dari Tugas 1 harus dipertahankan, serta menjalankan sendiri perintah migration, test, Git, deployment, dan pemeriksaan tampilan pada browser.

Strategi prompting yang saya gunakan bersifat iteratif dan berbasis bukti. Saya mengirimkan tujuan untuk satu tahap kecil, lalu menyertakan output terminal atau tangkapan layar aktual. Ketika hasil awal menyederhanakan Experience dan hanya menampilkan dua data, saya mengoreksi kebutuhan tersebut dengan meminta desain TI1 dipulihkan tanpa mengembalikan konten menjadi hardcoded. Saya juga mempertanyakan roadmap ketika tahap finalisasi disebut terlalu cepat karena fitur tambahan untuk target nilai 4 belum dikerjakan. Koreksi tersebut mendorong keputusan untuk menambahkan detail page dan Django Admin sebelum refleksi akhir.

Codex membantu menyusun alternatif model, view, named route, template loop, migration, responsive CSS, unit test, konfigurasi admin, dan langkah diagnosis Git. Bantuan tersebut juga digunakan untuk menjelaskan error seperti migration yang belum diterapkan, PowerShell execution policy, serta push yang ditolak karena riwayat remote bercabang. Saya tetap mengevaluasi setiap saran melalui tampilan desktop dan mobile, `python manage.py check`, `python manage.py test`, `python manage.py makemigrations --check`, pemeriksaan diff, dan riwayat commit. Pada audit akhir, ketergantungan data terhadap SQLite lokal ditemukan dan diperbaiki menggunakan data migration agar hasil deployment dapat direproduksi.

Ringkasan log prompting berikut menunjukkan pembagian masalah dan keputusan yang dihasilkan:

| Tahap | Ringkasan prompt atau koreksi | Keputusan yang diterapkan |
| --- | --- | --- |
| Pemodelan | Memigrasikan Certifications tanpa menghilangkan desain TI1 | Membuat model `Certification`, migration, dan enam data sertifikat terstruktur. |
| Integrasi MVT | Memindahkan data ke halaman terpisah tetapi mempertahankan carousel | Membuat view, context, named route, template loop, empty state, dan UUID lightbox. |
| Koreksi Experience | Memulihkan seluruh timeline dan ukuran lama, bukan menyederhanakan desain | Memperluas metadata Experience dan mengembalikan empat data melalui migration. |
| Pengujian | Memeriksa seluruh checklist dan menghapus sisa hardcode | Menambah test model, URL, template, data, ordering, empty state, serta menghapus markup legacy. |
| Fitur tambahan | Menutup fase yang tertinggal untuk target nilai 4 | Menambahkan detail page, graceful 404, custom Django Admin, dan test terkait. |
| Git dan deployment | Menangani push GitHub yang ditolak tanpa kehilangan commit lokal | Melakukan fetch, membuat backup branch, rebase di atas remote, menguji ulang, lalu push normal. |

Dengan alur tersebut, AI berfungsi sebagai alat bantu analisis dan implementasi, sedangkan pemilihan konten, arah visual, prioritas fitur, koreksi hasil, validasi, dan keputusan akhir tetap melibatkan penalaran serta tanggung jawab aktif saya.


### Pertanyaan Reflektif Tugas 2

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

### Tugas 2

1. Ketika pengguna membuka `/certifications/`, browser mengirimkan HTTP request ke proyek Django. `portofolio/urls.py` menjadi gerbang routing tingkat proyek dan meneruskan pola URL utama ke `main/urls.py` melalui `include`. Pada URL aplikasi, pola `certifications/` cocok dengan named route `main:show_certifications`, sehingga Django menjalankan view `show_certifications`. View tersebut memanggil `Certification.objects.all()`. Melalui ORM, model `Certification` menerjemahkan operasi itu menjadi query terhadap tabel database dan mengembalikan queryset yang sudah mengikuti `Meta.ordering`. View memasukkan queryset tersebut ke dalam context dengan nama `certification_list`, lalu meneruskannya ketika merender `certifications.html`. Template menggunakan `{% for %}` untuk membentuk card dan lightbox dari setiap objek, serta menampilkan empty state apabila queryset kosong. Hasil akhirnya dikembalikan sebagai HTTP response berisi HTML yang dirender browser. Alur serupa terjadi pada detail page, tetapi `main/urls.py` terlebih dahulu menangkap UUID dan view menggunakan `get_object_or_404` untuk mengambil tepat satu objek atau memberikan respons 404.

2. Menyimpan data pada model memisahkan isi portofolio dari cara penyajiannya. Ketika enam sertifikat masih ditulis langsung di HTML, perubahan judul, penerbit, urutan, atau penambahan sertifikat mengharuskan saya mengubah beberapa bagian markup carousel dan lightbox secara manual. Duplikasi itu meningkatkan risiko informasi tidak konsisten. Setelah menggunakan model, setiap sertifikat menjadi satu objek dengan tipe field, pilihan kategori, UUID, dan aturan ordering yang jelas. View yang berbeda, template daftar, detail page, test, dan Django Admin dapat menggunakan sumber data yang sama. Dampaknya, pemeliharaan lebih mudah, perubahan desain tidak mengubah data, dan penambahan konten tidak memerlukan pembuatan struktur HTML baru. Data migration juga membuat enam data awal dapat direproduksi pada fresh clone dan PWS, bukan hanya tersimpan pada SQLite lokal. Bagi saya, manfaat terbesarnya adalah terbentuknya satu sumber kebenaran yang dapat dikembangkan menuju fitur pencarian, filtering, atau API pada iterasi berikutnya.

3. `makemigrations` membaca perubahan definisi model dan menghasilkan berkas migration yang mendeskripsikan perubahan schema, tetapi belum mengubah database. Sebaliknya, `migrate` menjalankan migration yang belum diterapkan agar schema atau operasi data pada database menjadi sesuai dengan riwayat migration. Contohnya, ketika saya menambahkan model `Certification` dengan field `title`, `issuer`, `category`, `issued_year`, `image_path`, dan field pendukung lainnya, saya menjalankan `python manage.py makemigrations` untuk menghasilkan `0002_certification.py`, kemudian `python manage.py migrate` untuk benar-benar membuat tabelnya. Pada pengembangan Experience, penambahan field `organization`, `period`, `display_order`, dan `skills` juga membutuhkan kedua tahap tersebut. Sementara itu, `0004_seed_certifications.py` merupakan data migration dengan `RunPython`; karena tidak mengubah definisi model, migration tersebut dibuat secara terkontrol dan cukup dijalankan melalui `migrate` untuk menambahkan enam data awal. Saya menggunakan `makemigrations --check` pada akhir pengerjaan untuk memastikan tidak ada perubahan model yang belum memiliki migration.


## Tugas Individu 3

### Dokumentasi Tugas 3

#### (16.59 - 19.38 9/14/2026)
Setelah Tutorial 03 selesai dan dikumpulkan, saya memulai Tugas Individu 3 dengan memilih bagian **Experience** sebagai objek penerapan form dan data delivery. Pilihan tersebut dibuat karena Tutorial 03 sudah menggunakan `Certification`, sedangkan tugas ini meminta penerapan mekanisme yang sama pada bagian portofolio lain. Timeline Experience sebelumnya sudah menggunakan model Django dan memiliki desain yang matang, sehingga pengembangan difokuskan pada kemampuan pengelolaan data tanpa mengembalikan kontennya menjadi hardcoded atau mengubah presentasi lama.

Saya menambahkan `ExperienceForm` di `main/forms.py` menggunakan `forms.ModelForm`. Form tersebut memuat seluruh field Experience yang dapat diisi pengguna, yaitu `title`, `organization`, `period`, `display_order`, `description`, `category`, `thumbnail`, dan `skills`. Field `id` tidak disertakan karena UUID dibuat otomatis oleh model, sedangkan `started_at` dan `ended_at` dikecualikan karena berhubungan dengan timestamp. Label, placeholder, jenis widget, serta help text disesuaikan agar fungsi setiap input mudah dipahami. Field `display_order` menjelaskan posisi data pada timeline, `thumbnail` menerima URL dokumentasi opsional, dan `skills` menggunakan daftar yang dipisahkan koma agar dapat dirender kembali sebagai tag.

Alur create diimplementasikan melalui view `create_experience` dan named route `main:create_experience` pada alamat `/experience/add/`. View menggunakan satu instance form untuk menangani request GET maupun POST. Ketika request POST valid, `form.save()` menyimpan objek ke database, Django messages menambahkan umpan balik keberhasilan, lalu pengguna diarahkan kembali ke halaman Experience. Apabila data tidak valid, halaman form yang sama dirender kembali bersama pesan error per field. Template `experience_form.html` memperluas `base.html`, menggunakan `{% csrf_token %}`, dan memanfaatkan styling form bersama yang sebelumnya dibuat agar tampilan tetap konsisten serta responsif.

Tombol **Add experience** ditambahkan pada heading halaman Experience tanpa mengubah struktur timeline dan galeri dokumentasi. Pengujian manual dilakukan menggunakan objek `Temporary Experience Validation` dengan `display_order` bernilai 99. Setelah form dikirim, objek berhasil tersimpan, tampil pada bagian bawah timeline sesuai aturan pengurutan model, dan daftar skills berhasil dipecah menjadi tag Form, Validation, dan Django. Pemeriksaan `python manage.py check`, `python manage.py test`, `python manage.py makemigrations --check`, dan `git diff --check` tetap berhasil; sebanyak 27 test yang sudah ada lulus dan tidak ditemukan perubahan model yang membutuhkan migration baru.

Sebagai peningkatan UI/UX, komponen Django messages pada `base.html` kemudian dibuat dapat ditutup. Setiap success, warning, atau error notification memiliki tombol silang dengan label aksesibilitas `Dismiss notification`. JavaScript hanya menghapus elemen message terkait dari DOM ketika tombol ditekan, sehingga pengguna dapat mengembalikan layout halaman tanpa melakukan refresh. Tombol tersebut memiliki state hover dan keyboard focus yang jelas, sedangkan perubahan stylesheet dilengkapi cache-busting agar langsung termuat pada browser. Fitur ini dipisahkan dari alur create melalui commit tersendiri agar riwayat Git tetap modular.

#### (13.02 - 14.35 9/15/2026)
Pada sesi pengembangan kali ini, saya melanjutkan alur pengelolaan Experience dengan menambahkan fitur update berbasis UUID. Named route `main:update_experience` menggunakan pola `/experience/<uuid:experience_id>/edit/`, kemudian view `update_experience` mengambil objek yang dituju melalui `get_object_or_404`. Pendekatan tersebut memastikan setiap card mengarah ke data yang tepat dan UUID yang tidak tersedia menghasilkan respons 404, bukan menyebabkan error server.

View update menggunakan `ExperienceForm(request.POST or None, instance=experience)`. Argumen `instance` membuat form terhubung dengan objek yang sudah ada: pada request GET, nilai title, organization, period, display order, description, category, thumbnail, dan skills ditampilkan sebagai data awal; pada request POST yang valid, `form.save()` memperbarui baris database yang sama dan tidak membuat objek duplikat. Setelah penyimpanan berhasil, pengguna diarahkan kembali ke timeline dan menerima flash message `Experience updated successfully.` yang dapat ditutup melalui tombol silang.

Template `experience_form.html` digunakan bersama oleh operasi create dan update agar struktur input, validasi, CSRF token, dan styling tidak diduplikasi. Keberadaan context `experience` menentukan judul halaman, deskripsi, form action, dan label tombol. Mode create menampilkan **Add a new chapter** dan **Add experience**, sedangkan mode update menampilkan **Refine this chapter** dan **Save changes**. Setiap card timeline memperoleh tombol **Edit experience** yang menggunakan named URL dengan UUID objek terkait. Styling tombol dibuat responsif serta tetap mengikuti warna, border, dan interaction state desain Experience sebelumnya.

Pengujian manual dilakukan pada objek sementara yang dibuat melalui Chapter 1. Seluruh field lama berhasil terisi pada halaman edit, perubahan tersimpan pada objek yang sama, dan hasil terbaru tampil kembali di timeline tanpa menambah card baru. Validasi teknis melalui `python manage.py check`, `python manage.py test`, `python manage.py makemigrations --check`, dan `git diff --check` berhasil dijalankan. Sebanyak 27 test tetap lulus dan tidak terdapat perubahan model yang membutuhkan migration baru.

#### (19.22 - 20.35 9/15/2026)
Pada bagian kali ini, saya melengkapi operasi pengelolaan dasar Experience dengan fitur delete berbasis UUID. Named route `main:delete_experience` menggunakan pola `/experience/<uuid:experience_id>/delete/`, sedangkan view `delete_experience` mengambil objek melalui `get_object_or_404`. View tersebut dihiasi decorator `@require_POST`, sehingga membuka endpoint menggunakan GET tidak akan menghapus data. Judul objek disimpan sebelum operasi delete agar flash message tetap dapat menyebutkan Experience yang berhasil dihapus, kemudian pengguna diarahkan kembali ke timeline.

Antarmuka penghapusan ditempatkan langsung pada setiap card timeline. Tombol **Delete experience** tidak segera mengirim request, tetapi membuka confirmation modal yang memiliki ID unik berdasarkan UUID objek. Modal menampilkan judul Experience yang akan dihapus, peringatan bahwa tindakan tidak dapat dibatalkan, tombol **Yes, delete it**, serta beberapa jalur pembatalan melalui **Keep experience**, tombol silang, dan backdrop. Form konfirmasi menggunakan method POST dan `{% csrf_token %}` agar request perubahan data memperoleh perlindungan CSRF dari Django.

Styling destructive action menggunakan warna merah yang berbeda dari tombol Edit agar konsekuensi kedua tindakan dapat dikenali sebelum ditekan. Modal memakai komponen lightbox bersama dan tetap responsif pada layar sempit. Setiap card juga memperoleh anchor ID agar pengguna dapat kembali ke posisi Experience yang sama setelah membatalkan modal. Stylesheet dinaikkan ke versi cache-busting berikutnya supaya perubahan tombol dan modal langsung dimuat browser.

Pengujian manual dilakukan menggunakan objek sementara dari chapter sebelumnya. Jalur pembatalan berhasil mempertahankan data, sedangkan konfirmasi POST menghapus tepat satu objek sementara dan mengembalikan pengguna ke timeline dengan success notification yang dapat ditutup. Empat Experience asli tetap tersedia. `python manage.py makemigrations --check` menyatakan tidak ada perubahan model dan `git diff --check` tidak menemukan whitespace error. Pengujian otomatis khusus untuk method restriction, CSRF, successful deletion, dan unknown UUID akan ditambahkan bersama regression test Experience pada chapter pengujian.

Dokumentasi berikutnya akan dilengkapi secara bertahap setelah fitur JSON data delivery, deserialization, antarmuka pencarian atau filtering, serta regression test Experience selesai diimplementasikan dan diverifikasi.

#### (20.45 - 22.03 9/16/2026)
Pada sesi ini, saya menambahkan JSON data delivery untuk Experience melalui view `get_experiences_json` dan named route `main:get_experiences_json` pada `/api/experiences/`. View mengambil queryset `Experience.objects.all()` yang mengikuti `Meta.ordering`, kemudian menjalankan `serializers.serialize("json", experiences)`. Hasil serialization dikembalikan melalui `HttpResponse` dengan content type `application/json`. Struktur JSON memuat identitas model, UUID pada `pk`, dan nilai field pada `fields`, sehingga data dapat dibaca di luar template HTML tanpa kehilangan identitas setiap Experience.

Endpoint tersebut menerima parameter GET `q` dan `category`. Parameter `q` dibersihkan dengan `strip()` dan digunakan dalam query `Q(title__icontains=query) | Q(organization__icontains=query)`, sehingga pencarian dapat menemukan judul peran maupun organisasi tanpa membedakan huruf besar dan kecil. Parameter `category` menambahkan filter kategori yang dapat dikombinasikan dengan pencarian teks. Tanpa filter, endpoint mengembalikan seluruh Experience dalam urutan timeline; apabila tidak ada kecocokan, hasilnya berupa array JSON kosong.

View `show_experience` kemudian diubah agar tidak langsung meneruskan queryset ke template. View memanggil fungsi JSON yang sama secara internal, mendekode response sebagai UTF-8, lalu menggunakan `serializers.deserialize("json", ...)`. Setiap hasil deserialization diambil melalui atribut `.object` dan dimasukkan ke context `experience_list`. Alur ini bukan request HTTP tambahan dari browser, melainkan pemanggilan fungsi pada server. Objek hasil deserialization digunakan untuk rendering tanpa disimpan kembali ke database, sehingga UUID, urutan, dan property `skill_list` tetap dapat digunakan oleh timeline, tombol Edit, serta modal Delete.

Antarmuka Experience memperoleh form GET untuk pencarian judul atau organisasi dan dropdown kategori yang berasal dari `Experience.EXPERIENCE_CHOICES`. Nilai filter dipertahankan setelah form dikirim, sedangkan tombol **Clear filters** mengembalikan halaman tanpa parameter pencarian. Ketika filter aktif, halaman menampilkan jumlah hasil dengan bentuk singular atau plural yang sesuai. Empty state pencarian dibedakan dari kondisi database kosong agar pengguna memahami apakah belum ada data atau filter perlu diubah. Kontrol pencarian menggunakan label yang jelas, keyboard focus yang terlihat, dan layout yang dapat membungkus pada layar sempit. Desain timeline, skills tags, galeri dokumentasi, dan operasi pengelolaan data sebelumnya tetap dipertahankan; stylesheet diperbarui menjadi versi cache `1.9`.

Pengujian manual dilakukan pada endpoint JSON dan halaman timeline. `/api/experiences/` menampilkan empat Experience asli, sedangkan `/api/experiences/?q=BEM&category=internship` mengembalikan tepat satu objek BEM Fasilkom UI. Kombinasi yang sama pada halaman Experience menampilkan satu card dan pesan `1 experience found for “BEM”.`. Kategori tanpa kecocokan menghasilkan empty state, dan pencarian tanpa filter mengembalikan timeline lengkap. Saya juga memastikan bahwa perubahan pilihan dropdown baru diterapkan setelah tombol **Search** ditekan karena form menggunakan submit GET, bukan filtering otomatis.

Validasi teknis menunjukkan 27 test yang sudah ada tetap lulus pada Django 5.0, system check tidak menemukan masalah, `makemigrations --check` tidak mendeteksi perubahan model, dan `git diff --check` tidak menemukan whitespace error. Pemeriksaan request internal tambahan berhasil memverifikasi JSON, ordering, kombinasi filter, rendering hasil deserialization, dan contextual empty state tanpa mengubah data asli. Karena interpreter dasar virtualenv tidak ditemukan pada lingkungan eksekusi pendamping, pemeriksaan tersebut dijalankan menggunakan runtime Python bawaan dengan dependensi Django proyek; konfigurasi virtualenv pengguna tidak diubah. Pengujian otomatis khusus seluruh workflow Experience akan dilengkapi pada chapter regression test.

#### (22.05 - 23.02 9/16/2026)
Pada sesi ini, saya menambahkan class `ExperienceWorkflowTest` di `main/tests.py` untuk menguji seluruh alur pengelolaan Experience yang dikembangkan pada sesi sebelumnya. Sebanyak 21 test baru melengkapi 27 test yang sudah ada, sehingga total regression suite menjadi 48 test. Setiap test menggunakan database test Django yang terpisah dari database portofolio. Data Experience bawaan migration dibersihkan hanya pada setup database test, kemudian fixture khusus dibuat agar jumlah objek, filtering, dan ordering dapat diperiksa secara deterministik tanpa bergantung pada empat Experience asli.

Pengujian `ExperienceForm` memastikan seluruh field portofolio yang dapat diisi tersedia, field opsional menerima nilai kosong, dan input kategori tidak dikenal, urutan negatif, serta URL thumbnail tidak valid ditolak. Alur create diperiksa melalui halaman form yang memperluas `base.html` dan memuat CSRF token, penyimpanan seluruh field pada submission valid, redirect ke timeline, serta success notification yang memiliki kontrol dismiss. Submission invalid harus menampilkan error dan mempertahankan input tanpa menambah objek baru.

Pengujian update memastikan setiap field terisi dari instance yang tepat. Submission valid mengubah objek dengan UUID dan `started_at` yang sama, memperbarui skills tags, serta tidak menambah jumlah record. Submission invalid tidak boleh mengubah data tersimpan. UUID update yang tidak ditemukan diuji pada request GET maupun POST dan harus menghasilkan respons 404. Pemeriksaan tersebut melengkapi pengujian manual sebelumnya dengan assertion terhadap keadaan database, bukan hanya tampilan card.

Untuk operasi delete, test memastikan request GET, PUT, PATCH, DELETE, dan HEAD ditolak dengan status 405 serta tidak menghapus objek. `Client(enforce_csrf_checks=True)` digunakan untuk memastikan create, update, dan delete tanpa token memperoleh status 403. Test penghapusan dengan token CSRF valid mengambil cookie dari halaman timeline, mengirim form POST, lalu memastikan hanya objek yang dituju terhapus sementara objek lain tetap tersedia. Redirect dan success feedback juga diperiksa, sedangkan UUID delete yang tidak dikenal harus menghasilkan status 404. Test markup memastikan tombol create dan edit, action form delete, ID modal berbasis UUID, jalur pembatalan, dan CSRF token mengarah pada target yang benar.

Pengujian JSON mencakup content type `application/json`, identitas model, UUID, nilai seluruh field portofolio, serta urutan berdasarkan `display_order`. Pencarian judul maupun organisasi diuji dengan huruf besar-kecil campuran dan whitespace di tepi input. Filter teks dan kategori harus bekerja bersama, sedangkan query tanpa kecocokan, kategori tidak dikenal, dan database kosong harus menghasilkan array JSON kosong. Pada halaman timeline, test memeriksa bahwa context berisi list objek hasil deserialization dengan UUID dan property `skill_list` yang sesuai, hanya data yang cocok ditampilkan, nilai filter tetap terisi, dan jumlah hasil serta tombol **Clear filters** muncul. Empty state hasil pencarian dibedakan dari empty state database kosong.

Seluruh 48 test berhasil dijalankan tanpa failure pada Django 5.0 melalui runtime pendamping dengan dependensi proyek. Django system check yang berjalan bersama test tidak menemukan masalah, dan `git diff --check` tidak menemukan whitespace error. Warning direktori `staticfiles` tetap muncul karena hasil collectstatic belum tersedia pada lingkungan test, tetapi tidak menyebabkan test gagal. Assertion terhadap HTML memverifikasi keberadaan kontrol dan pesan, bukan membuktikan seluruh perilaku browser seperti keyboard focus, pembatalan modal, atau penutupan notifikasi; pemeriksaan visual dan interaksi manual tetap diperlukan. Cakupan CSRF dan method restriction juga tidak dianggap sebagai pengganti authentication maupun authorization pengguna.

#### (07.22 - 08.25 9/17/2026)
Pada sesi finalisasi, saya melengkapi catatan penggunaan, jawaban pertanyaan reflektif, transparansi penggunaan AI, serta checklist validasi dan pengumpulan Tugas Individu 3. Implementasi menggunakan Experience sebagai bagian portofolio berbeda dari Certification pada Tutorial 03. Halaman-halaman portofolio dan form menggunakan root template `base.html`, sementara Experience memiliki ModelForm, create, update, delete, JSON delivery, dan rendering setelah deserialization. Peningkatan UI/UX meliputi kombinasi pencarian peran atau organisasi dengan kategori, jumlah hasil, contextual empty state, confirmation modal, serta notifikasi yang dapat ditutup.

Finalisasi juga mencatat batasan yang tidak boleh disamakan dengan keberhasilan fitur. CSRF token dan pembatasan method melindungi alur request, tetapi tidak membatasi siapa yang boleh mengubah data. CRUD pada tahap pembelajaran ini belum memiliki authentication dan authorization khusus. Selain itu, 48 test yang lulus bukan jaminan bahwa seluruh interaksi browser dan deployment PWS telah diperiksa. Pemeriksaan endpoint PWS melalui alat web pendamping dibatasi oleh pemeriksaan keamanan URL, sehingga audit deployment terakhir harus dilakukan secara manual sebelum submit. Dokumen tidak mengklaim pemeriksaan deployment tersebut sudah selesai.


### Catatan Tugas 3

#### Menjalankan proyek

Dari direktori proyek, aktifkan virtual environment pada terminal PowerShell yang sama, instal dependensi, dan terapkan migration:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Pada fresh clone, buat virtual environment terlebih dahulu menggunakan `python -m venv env`. Execution policy pada scope Process hanya berlaku untuk terminal saat ini. Konfigurasi environment lokal mengikuti petunjuk setup proyek pada bagian sebelumnya; jangan commit file `.env`, kredensial, atau database lokal. Migration memulihkan data awal pada database baru, sedangkan perubahan melalui form disimpan pada database environment yang sedang digunakan.

#### Route dan alur penggunaan

| Alamat | Fungsi |
| --- | --- |
| `/experience/` | Timeline dari hasil deserialization JSON, dengan search/filter |
| `/experience/add/` | Form create Experience |
| `/experience/<uuid>/edit/` | Form update objek yang sama |
| `/experience/<uuid>/delete/` | Endpoint delete khusus POST; gunakan confirmation modal |
| `/api/experiences/` | JSON seluruh Experience dalam urutan model |
| `/api/experiences/?q=BEM&category=internship` | Contoh kombinasi pencarian dan kategori |

Klik **Add experience** untuk menambahkan data atau **Edit experience** pada card untuk memperbaruinya. Nilai `display_order` yang lebih kecil muncul lebih awal. `thumbnail` adalah URL opsional yang disimpan dan disertakan dalam JSON; galeri dokumentasi yang sudah ada tetap dipertahankan dan tidak otomatis diganti oleh field tersebut. Skills dipisahkan dengan koma dan ditampilkan sebagai tag. Input invalid menampilkan error tanpa menyimpan perubahan. UUID yang tidak tersedia menghasilkan 404.

**Delete experience** membuka modal konfirmasi; **Keep experience**, tombol silang, atau backdrop membatalkan tindakan. Hanya **Yes, delete it** yang mengirim POST dengan CSRF token. Request GET langsung ke endpoint delete menghasilkan 405, bukan menghapus data. Penghapusan bersifat permanen dan tidak memiliki undo. Search menggunakan GET: ketik peran atau organisasi, pilih kategori, lalu tekan **Search**. **Clear filters** mengembalikan daftar lengkap. Notifikasi Django dapat ditutup tanpa refresh.

#### Validasi dan batasan keamanan

```powershell
python manage.py check
python manage.py test
python manage.py makemigrations --check
python -m pip check
git diff --check
```

Regression suite terakhir berisi 48 test yang lulus, termasuk 21 test workflow Experience. Test memakai database terpisah. Warning direktori `staticfiles` pada test tidak membuat suite gagal; untuk deployment, pastikan konfigurasi static file dan proses collectstatic berjalan sesuai environment. Kelulusan tes tidak menggantikan pemeriksaan visual pada desktop dan mobile.

CRUD saat ini belum dibatasi berdasarkan identitas atau peran pengguna. UUID bukan mekanisme authorization, dan CSRF bukan authentication. Sebelum digunakan sebagai pengelola portofolio publik sungguhan, perlu pembatasan akses create/update/delete, pengujian permission, serta backup data. Jangan menganggap confirmation modal sebagai kontrol keamanan server.


### Transparansi Penggunaan AI Tugas 3

Saya menggunakan Codex sebagai alat bantu membaca ketentuan, merencanakan chapter, mengimplementasikan perubahan, menyusun regression test, dan menyiapkan dokumentasi. AI membantu pembuatan `ExperienceForm`, view dan named route CRUD, JSON serialization/deserialization, search/filter, confirmation modal, dismissible messages, serta class `ExperienceWorkflowTest`. Saya tetap menentukan bagian portofolio yang dipilih, mempertahankan desain lama, mencoba alur melalui browser, membaca hasil validasi, dan menjalankan commit serta push sendiri.

Strategi prompting dilakukan bertahap: memilih Experience sebagai bagian lain dari Tutorial 03, menyelesaikan create/update/delete secara terpisah, menambahkan JSON dan filtering, kemudian menguji regresi sebelum finalisasi. Saya meminta perubahan modular, desain tetap konsisten, dan dokumentasi menggunakan format judul serta rentang waktu tugas sebelumnya. Log ringkas berikut merupakan rangkuman percakapan, bukan transkrip lengkap:

| Tahap | Arahan dan tindak lanjut |
| --- | --- |
| Create | Terapkan form pada Experience; uji objek sementara di timeline |
| Feedback | Tambahkan tombol silang agar notifikasi dapat ditutup |
| Update/delete | Pertahankan UUID saat edit; gunakan konfirmasi dan POST saat delete |
| JSON/search | Sajikan JSON dan deserialisasikan sebelum rendering; uji BEM + Internship |
| Regression | Uji input valid/invalid, CSRF, 404/405, ordering, dan hasil filter |
| Dokumentasi | Isi placeholder pada heading waktu pengguna, lalu commit terpisah |

Keterbatasan AI terlihat pada penempatan dokumentasi delete: AI sempat menambahkan heading Chapter 3 tersendiri tetapi membiarkan placeholder di bawah rentang waktu yang saya buat. Saya menunjukkan kesalahan tersebut melalui screenshot. Dokumentasi kemudian dipindahkan ke heading waktu yang benar dan commit lokal diamend sebelum push. Hal ini menunjukkan bahwa hasil yang tampak lengkap belum tentu sesuai struktur yang diminta; diff dan placeholder harus diperiksa sebelum commit.

Pada validasi, interpreter dasar virtualenv tidak ditemukan oleh lingkungan pendamping. AI memakai runtime Python bawaan dengan dependensi Django proyek tanpa mengubah konfigurasi virtualenv saya. Saya kemudian menjalankan suite pada terminal lokal dan memperoleh 48 test lulus. Perbedaan lingkungan harus dinyatakan, bukan disembunyikan sebagai hasil eksekusi yang identik. AI juga tidak dapat memverifikasi PWS melalui alat web internal, sehingga keberhasilan test lokal dan push tidak dipakai sebagai klaim bahwa deployment sudah lolos audit terakhir.

Secara teknis, assertion HTML tidak membuktikan seluruh interaksi browser, dan banyaknya test bukan ukuran tunggal kualitas. Modal berbasis fragment/CSS belum membuktikan focus trapping atau perilaku Escape seperti dialog JavaScript penuh. Alur serialization/deserialization internal sengaja mengikuti materi tugas, tetapi menambah pemrosesan dibanding rendering queryset langsung; untuk pengembangan berikutnya, pemisahan logika query bersama dan strategi delivery dapat dievaluasi berdasarkan kebutuhan. Fitur thumbnail juga belum menjadi galeri dinamis. Batasan akses CRUD tetap perlu ditangani ketika authentication dipelajari. Saya meninjau keluaran AI sebagai usulan yang perlu diperiksa, bukan menerima semua klaim keamanan, aksesibilitas, maupun kesiapan produksi secara otomatis.


### Pertanyaan Reflektif Tugas 3

1. Jelaskan mengapa kita menggunakan `ModelForm` pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form tersebut!

2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

### Tugas 3

1. Saya menggunakan `ModelForm` karena struktur input dan validasinya terhubung langsung dengan model. Pada Experience, pilihan kategori, batas panjang teks, tipe URL, dan field urutan tidak perlu didefinisikan ulang sebagai aturan terpisah pada HTML dan view. Saya tetap menyesuaikan label, widget, serta help text agar form mudah digunakan. Pada create, `form.save()` membuat objek; pada update, `instance=experience` mengisi nilai awal dan menyimpan perubahan ke objek yang sama, sehingga tidak terjadi duplikasi. ModelForm bukan berarti seluruh HTML hilang: template masih diperlukan untuk layout, error, dan tombol. `{% csrf_token %}` wajib pada form POST karena browser dapat membawa cookie secara otomatis ketika mengirim request, termasuk request yang dipicu dari situs lain. Token yang diperiksa middleware membantu mencegah request lintas situs yang tidak sah. Saya memverifikasinya dengan client yang mengaktifkan CSRF checks: POST tanpa token ditolak dengan 403. Namun, CSRF token tidak menentukan siapa pemilik data dan tidak menggantikan authentication atau authorization.

2. JSON lebih praktis untuk pertukaran data aplikasi web karena struktur object, array, string, angka, boolean, dan null dekat dengan representasi data yang digunakan JavaScript. Payload umumnya lebih ringkas daripada XML yang memakai pasangan tag, dan browser dapat memprosesnya melalui `JSON.parse` atau response JSON tanpa parsing elemen XML. Pada proyek saya, kumpulan Experience dapat direpresentasikan sebagai array dengan identitas objek dan field yang jelas, sehingga hasil search/filter mudah diperiksa atau digunakan oleh konsumen API. Ini bukan berarti JSON selalu lebih baik: XML relevan untuk dokumen dengan struktur campuran, namespace, atau integrasi yang memang mensyaratkan XML. JSON juga tetap membutuhkan validasi, penanganan tipe khusus, serta pemilihan field yang aman. Pilihan JSON pada tugas ini sesuai kebutuhan pertukaran data portofolio, bukan anggapan bahwa semua sistem harus meninggalkan XML.

3. Ketika browser membuka `/api/experiences/`, routing proyek meneruskan request ke `main/urls.py`, lalu named route `main:get_experiences_json` menjalankan view `get_experiences_json`. View membaca parameter `q` dan `category`, mengambil queryset Experience melalui ORM, dan menerapkan filter bila diperlukan. Queryset tetap mengikuti ordering model. `serializers.serialize("json", experiences)` mengubah instance Django menjadi teks JSON berisi nama model, UUID pada `pk`, dan nilai field pada `fields`. Teks tersebut dikembalikan melalui `HttpResponse` dengan content type `application/json`. Serialization diperlukan karena queryset dan instance model merupakan objek Python yang tidak dapat langsung dikirim sebagai format pertukaran data; UUID dan timestamp juga perlu direpresentasikan dalam bentuk yang dapat dibaca konsumen JSON. Pada `/experience/`, `show_experience` memanggil fungsi delivery yang sama secara internal, mendekode response, lalu menjalankan `serializers.deserialize`. Atribut `.object` diambil untuk membentuk list context yang dirender template, tanpa menyimpan ulang objek tersebut. Dengan demikian, data yang tampil telah melewati JSON dan deserialization, tetapi browser tidak melakukan request API kedua untuk membentuk timeline. Serialization bukan enkripsi dan bukan kontrol permission, sehingga field yang dikirim dan akses endpoint tetap harus dievaluasi saat aplikasi berkembang.


## Tugas Individu 4

### Dokumentasi Tugas 4

#### (13.01 - 14.48 9/22/2026)
Tugas Individu 4 melanjutkan penerapan authentication, session, cookie, authorization, dan fitur star yang telah dibuat pada Tutorial 04. Tutorial tersebut menggunakan `Certification` sebagai objek penerapan, sedangkan tugas ini menggunakan `Experience` agar pengembangan melanjutkan bagian portofolio dari Tugas 3. Fondasi autentikasi tetap memanfaatkan user, session, dan form bawaan Django. Pengerjaan tugas dibagi menjadi chapter kecil agar perubahan model, interaksi pengguna, pembatasan peran, pengujian, dokumentasi, dan deployment dapat diperiksa secara terpisah.

Chapter pertama menambahkan field `starred_by` pada model `Experience` menggunakan `ManyToManyField` menuju `settings.AUTH_USER_MODEL`. Field memakai `related_name="starred_experiences"` sehingga relasi dapat diakses dari sisi user, sedangkan `blank=True` memungkinkan Experience tetap tersedia tanpa star. Django menyimpan hubungan tersebut pada tabel perantara, bukan menambahkan satu kolom user pada setiap Experience. Constraint relasi Many-to-Many mencegah pasangan user dan Experience yang sama dihitung berulang kali. Perubahan schema direkam pada migration `0006_experience_starred_by.py`; migration menambahkan relasi tanpa menghapus atau menulis ulang data Experience yang sudah tersedia.

Named route `main:toggle_experience_star` ditambahkan pada pola `/experience/<uuid:experience_id>/star/`. View menggunakan `get_object_or_404` agar UUID yang tidak tersedia menghasilkan respons 404, `@login_required` agar pengunjung tanpa sesi diarahkan ke login, dan `@require_POST` agar operasi tidak dapat dijalankan melalui GET. Jika relasi user sudah ada, view menghapusnya; jika belum ada, view menambahkannya. Form pada template mengirim POST bersama `{% csrf_token %}`, sehingga operasi memperoleh perlindungan CSRF dan tidak dilakukan melalui tautan GET.

Setiap card timeline menampilkan komponen star reusable. Pengguna yang sudah login memperoleh tombol **Star** atau **Unstar**, atribut `aria-pressed` yang mencerminkan statusnya, serta jumlah total star. Pengunjung tanpa login tetap dapat melihat jumlah tersebut tetapi memperoleh tautan **Log in to star**, bukan form perubahan data. Styling memakai pola visual tombol Certification dengan ukuran yang disesuaikan untuk card Experience dan state keyboard focus yang terlihat. Versi cache stylesheet dinaikkan agar perubahan termuat pada browser.

Endpoint `/api/experiences/` tetap berfungsi untuk delivery dan deserialization data, tetapi serialization sekarang memakai whitelist field Experience. Relasi `starred_by` tidak dimasukkan ke response JSON, sehingga username, primary key user, email, password, session, dan identitas pemberi star tidak diekspos oleh endpoint portofolio. Timeline masih dapat memperoleh status dan jumlah star dari relasi database berdasarkan UUID setiap objek setelah proses deserialization.

Delapan regression test baru memeriksa redirect anonymous tanpa perubahan data, penolakan GET dengan status 405, penolakan POST tanpa CSRF dengan status 403, toggle dua arah, independensi dan keunikan star antar-user, status serta jumlah pada UI, JSON tanpa identitas pengguna, dan UUID asing dengan respons 404. Sebanyak 29 test khusus workflow Experience dan seluruh 78 test proyek berhasil dijalankan. `python manage.py check`, `python manage.py makemigrations --check`, dan `git diff --check` juga berhasil. Pengujian browser memastikan alur login, Star, Unstar, perubahan jumlah, serta JSON berjalan sesuai harapan. Implementasi kemudian dicatat pada commit `4e77102` dan hash yang sama berhasil diverifikasi pada branch `master` lokal, GitHub, dan PWS.

Pada akhir chapter ini, pembatasan star sudah tersedia tetapi matriks authorization CRUD Experience belum diterapkan. Create, update, dan delete akan dibatasi pada chapter berikutnya menggunakan empat peran: pengunjung, pengguna biasa, Editor, dan superuser. Pemisahan ini disengaja agar keberhasilan fitur star tidak dianggap sebagai bukti bahwa seluruh operasi pengelolaan data sudah aman.


### Catatan Tugas 4

Setelah menarik commit terbaru pada environment baru, terapkan migration sebelum menjalankan aplikasi:

```powershell
python manage.py migrate
python manage.py check
python manage.py test
python manage.py runserver
```

Fitur star Experience tersedia melalui form POST pada timeline `/experience/`, sedangkan endpoint perubahan datanya berada di `/experience/<uuid>/star/`. Endpoint tersebut bukan halaman yang dibuka langsung menggunakan GET. Pengunjung tanpa login dapat membaca timeline dan jumlah star, tetapi harus login sebelum memberi atau membatalkan star. Endpoint `/api/experiences/` bersifat read-only dan tidak mengirim identitas user yang membentuk relasi star.


### Transparansi Penggunaan AI Tugas 4

Codex digunakan secara bertahap untuk membaca ketentuan, memetakan implementasi Tutorial 04 ke Experience, menjelaskan konsep relasi Many-to-Many, membantu perubahan kode, dan menyusun pengujian. Saya tetap menjalankan migration, pemeriksaan Django, seluruh test, Git, deployment, serta pengujian interaksi browser secara langsung. Strategi prompting dan log prompt lengkap akan disusun pada tahap finalisasi berdasarkan catatan setiap chapter agar dapat membedakan arahan awal, hasil AI, koreksi manual, dan bukti verifikasi tanpa mengulang percakapan mentah yang tidak relevan.


### Pertanyaan Reflektif Tugas 4

Pertanyaan reflektif resmi belum dicantumkan pada dokumen awal Tugas Individu 4 dan akan ditambahkan setelah tersedia di SCELE. Jawaban tidak dibuat berdasarkan pertanyaan asumsi agar tetap sesuai instruksi dosen.