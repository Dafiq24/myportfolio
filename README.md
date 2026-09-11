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

1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

### Respon Reflektif Tugas 1

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


### Catatan Tugas 2

### Transparansi Penggunaan AI Tugas 2


### Pertanyaan Reflektif Tugas 2

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

### Respon Reflektif Tugas 2

1. Akan segera saya isi tepat di akhir penyelesaian Tugas Individu 2 ini.

2. Akan segera saya isi tepat di akhir penyelesaian Tugas Individu 2 ini.

3. Akan segera saya isi tepat di akhir penyelesaian Tugas Individu 2 ini.
