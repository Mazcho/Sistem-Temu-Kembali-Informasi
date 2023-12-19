# <p align="center">Implementasi Sequential LSTM Model dalam Chatbot Kesehatan Mental Remaja Menggunakan TensorFlow</p>
Nicholaus Verdhy Putranto|| A11.2020.12447

Ringkasan
Pada tahun 2023, kesehatan mental merupakan masalah terbesar bagi kaum remaja . Banyak kaum remaja yang mengalami berbagai masalah akan tetapi tidak ada yang bisa mendengarkan ceritanya, bahkan di keluarganya sendiri. Tidak semua orang mudah untuk menceritakan apa yang terjadi pada dirinya terhadap orang sekitarnya. Maka dari itu , menggunakan Machine Learning (ML) dan Deep Learning untuk membuat chatbot yang dapat merespon chat dari seseorang yang sedang mengalami masalah.
PENDAHULUAN
Latar Belakang
Kesehatan mental adalah kondisi seorang individu terbebas dari segala bentuk gejala-gejala gangguan mental(1). Pada pertumbuhan di masa remaja, banyak terjadi perubahan biologis, psikis, maupun dari segi sosial(2). Kesehatan jiwa terdiri dari beberapa jenis kondisi yang secara umum dikategorikan dalam kondisi sehat, gangguan kecemasan, stres dan depresi (3). Tidak semua orang dapat mengungkapkan isi di otaknya di depan umum, maupun orang terdekatnya, karena mengalami trust issue. Maka dari itu, penulis ingin membuat sebuah chat bot bantuan kesehatan mental remaja, yang dimana chat bot ini setidaknya bisa membantu remaja merasa lebih tenang, karena pada dasarnya tidak smua orang bisa menceritakaan apa yang dia rasakan (4).


Rumusan Masalah
1.	Apakah model Sequence dapat melakukan interaksi dengan baik dari inputan user yang diberikan?
2.	Bagaimana peforma yang dihasilkan dari model Sequence ?

Tinjauan Studi

Pada penelitian yang dilakukan oleh Yogi (5) Sistem Question and Answering (QA) merupakan permasalahan dalam pemrosesan bahasa alami yang dapat digunakan sebagai sistem dialog dan chatbot. Dapat digunakan sebagai layanan pelanggan yang dapat memberikan respon kepada pelanggan dengan cepat. Sistem QA menerima masukan berupa kalimat dan menghasilkan kalimat prediktif yang merupakan respon terhadap masukan tersebut. model tersebut menghasilkan skor BLEU yang cukup tinggi yaitu 41,04. Selain itu, penelitian yang dilakukan oleh (6) aplikasi messenger sebagai penghubung bagi penderita masalah mental terbukti dapat mengatasi masalah gangguan mental pada remaja. Penelitian lainnya yang dilakukan Yulius Denny (7) menyatakan bahwa model LSTM Sequential dapat merespon inputan dari user dengan baik dalam Bahasa Indonesia.
DATASET
Data set yang didapat bersumber dari Kaggle dan dataset bersifat public. Dataset yang diadapat terdapat 3 kolom dan 80 baris. Kolom tersebut diantaranya ada kolom tag, patterns, dan responses. Untuk kolom tag menjelaskan penegelompokan dari hasil pattern dan responses. Kolom tag beriskan greeting, morning, afternoon, night, dan lainnya. Lalu untuk kolom patterns, memuat kalimat dan kata kata yang biasanya diinputkan oleh user, sedangkan responses adalah hasil respon dari kalimat/ kata yang diberikan dari kolom pattern.

# Tentang Kumpulan Data

Untuk mengambil datanya saya ambil dari situs data publik yaitu dari Kaggle. Halaman ini menyajikan data dalam format .json yang berisi obrolan umum dan pengetahuan mengenai kesehatan mental. Ada link untuk Dataset : https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data/data

# Fitur Kumpulan Data

![image](https://github.com/Mazcho/Sistem-Temu-Kembali-Informasi/assets/77985996/aa40b101-9fc9-4440-b3fc-2c2734e11a14)

Fitur Dataset Pada data set ini terdapat 3 fitur. Ini termasuk tag, pola, dan tanggapan. Tag merupakan penanda data teks untuk menandai teks tersebut termasuk dalam suatu kategori (salam, salam pagi, siang, sore, minta tolong, dan sebagainya). Pola adalah pola yang diberikan oleh pengguna untuk kategori tersebut. Saat pengguna mengetik selamat pagi, ia akan memasukkan penanda tag di mesin pembelajaran nantinya. Dan yang terakhir adalah respon, respon disini adalah memberikan respon terhadap masukan dari pengguna mengenai apa yang pengguna berikan dari komputer. Dan sasaran penelitiannya adalah tag, dan variabel prediktornya adalah pola dan respon

# Kondisi Kumpulan Data
Kumpulan data ini berisi 237 data percakapan. Tidak ada nilai yang hilang dari data ini. Namun saya menambahkan beberapa data tambahan di dalamnya agar percakapan antara robot dan pengguna menjadi lebih baik. Dari 237 data menjadi 360 data. Data yang diberikan mengenai pemecahan masalah menambah pengetahuan mengenai topik kesehatan mental.

# Pra-Pemrosesan Data
Pertama, panggil data berformat .json ke dalam kode editor, lalu kita ubah menjadi Dataframe
Gambar 3.0 Load format .json dan konversikan ke Dataframe Kedua, kita akan pisahkan semua nilai yang ada di setiap kolom dan akan kita masukkan ke dalam setiap fitur yang sudah ditentukan.

![image](https://github.com/Mazcho/Sistem-Temu-Kembali-Informasi/assets/77985996/0189391b-6ba8-4212-9a6b-aa4d35ff02ee)

Hal ini untuk memudahkan model melatih data yang kami berikan untuk memberikan respons dari pengguna
Gambar 5.0 Tokenizer di patternsTokenizers digunakan untuk mengonversi teks menjadi rangkaian angka yang dapat dipahami oleh model deep learning. Proses ini melibatkan langkah-langkah seperti tokenisasi (memecah teks menjadi kata atau token), mengubah kata menjadi indeks, dan sebagainya. Setelah tokenizer dilatih, kita dapat menggunakannya untuk mengubah setiap teks baru menjadi urutan angka yang sesuai.


# Metode

Model yang saya rancang adalah Model LSTM Sequential, yang didasarkan pada tiga lapisan LSTM yang berurutan. Setiap lapisan LSTM terdiri dari 32 unit, dirancang untuk menangkap ketergantungan jangka panjang dalam rangkaian data teks. Keberadaan lapisan normalisasi setelah setiap lapisan LSTM memastikan stabilitas dalam pembelajaran, memungkinkan model saya lebih memahami pola kompleks dalam rangkaian data.

Setelah lapisan LSTM, model saya menggabungkan dua lapisan Padat. Lapisan Dense pertama memiliki 128 unit dan menggunakan fungsi aktivasi ReLU, diikuti oleh lapisan normalisasi dan dropout untuk mencegah overfitting. Konfigurasi serupa diterapkan pada lapisan Dense kedua.

Lapisan keluaran akhir adalah lapisan Padat dengan jumlah unit yang sesuai dengan kelas unik dalam data. Fungsi aktivasi softmax digunakan untuk menghasilkan distribusi probabilitas kelas.
Dalam proses kompilasi, model saya menggunakan fungsi kerugian sparse_categorical_crossentropy, pengoptimal Adam, dan metrik akurasi. Selama pelatihan, model saya akan menghentikan pelatihan jika tidak ada peningkatan akurasi setelah 3 periode menggunakan panggilan balik EarlyStopping.

Secara keseluruhan, model saya dirancang untuk memahami dan mengekstrak pola kompleks dalam rangkaian data teks, memberikan kemampuan optimal dalam tugas klasifikasi atau prediksi yang memerlukan pemahaman tentang ketergantungan jangka panjang. Proses pelatihan model menggunakan fungsi kerugian sparse_categorical_crossentropy dan pengoptimal Adam untuk mengoptimalkan parameter model. Dengan adanya callback EarlyStopping, model saya akan berhenti berlatih jika tidak ada peningkatan akurasi setelah beberapa periode tertentu. Model ini dapat diimplementasikan dalam sistem chatbot untuk memberikan respons yang kontekstual dan relevan terhadap masukan pengguna. 

# Evaluasi

Evaluasi yang ditampilkan dari penelitian ini adalah akurasi dari kecocokan antara user input dengna chat bot.

UI/UX

![image](https://github.com/Mazcho/Sistem-Temu-Kembali-Informasi/assets/77985996/157ff643-9207-4b38-932c-d476b576b3ba)

 
Jadwal Penelitian

![image](https://github.com/Mazcho/Sistem-Temu-Kembali-Informasi/assets/77985996/fdfc4320-38b9-4b95-8098-c4c8a0ca521b)


DAFTAR PUSTAKA

1.	Putri AW, Wibhawa B, Gutama AS. KESEHATAN MENTAL MASYARAKAT INDONESIA (PENGETAHUAN, DAN KETERBUKAAN MASYARAKAT TERHADAP GANGGUAN KESEHATAN MENTAL). Pros Penelit Dan Pengabdi Kpd Masy [Internet]. 2015 Oct 1 [cited 2023 Oct 31];2(2). Available from: http://journal.unpad.ac.id/prosiding/article/view/13535
2.	Indarjo S. KESEHATAN JIWA REMAJA. J Kesehat Masy [Internet]. 2009 Jul 17 [cited 2023 Oct 31];5(1). Available from: https://journal.unnes.ac.id/nju/index.php/kemas/article/view/1860
3.	Zulfia I. Kesehatan Mental Remaja Pada Masa Pandemi. 2021; 
4.	Al-Mahdi S. APLIKASI CHATBOT BERBASIS RULE-BASED SEBAGAI MEDIA KONSULTASI MANDIRI UNTUK KESEHATAN MENTAL REMAJA. 2021 Jul 30; 
5.	Chandra YW, Suyanto S. Indonesian Chatbot of University Admission Using a Question Answering System Based on Sequence-to-Sequence Model. Procedia Comput Sci. 2019 Jan 1;157:367–74. 
6.	Hendriana C. Aplikasi Messenger Sebagai Penghubung Bagi Penderita Masalah Mental Berbasis Android [Internet] [other]. Universitas Komputer Indonesia; 2021 [cited 2023 Oct 31]. Available from: https://elibrary.unikom.ac.id
7.	Denny Prabowo Y, Warnars HLHS, Budiharto W, Kistijantoro AI, Heryadi Y, Lukas. Lstm And Simple Rnn Comparison In The Problem Of Sequence To Sequence On Conversation Data Using Bahasa Indonesia. In: 2018 Indonesian Association for Pattern Recognition International Conference (INAPR) [Internet]. 2018 [cited 2023 Oct 31]. p. 51–6. Available from: https://ieeexplore.ieee.org/abstract/document/8627029

