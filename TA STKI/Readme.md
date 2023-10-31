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

METODE YANG DIGUNAKAN
Preprocessing
Pertama dilakukan penerjemahan Bahasa dari inggris ke Indonesia.Lalu data dimpor dan dimuat di dalam sebuah variabel. Data tersebut masuk ke tahap preprocessing data, pada preprocessing data dilakukan pemisahan untuk kolom pattern supaya nantinya model dapat Memahami pola apa saja yang dapat memiliki respon yang sama. 
Metode
Metode yang digunakan dalam penelitian ini adalah untuk membangun sebuah model deep learning menggunakan TensorFlow dan Keras untuk tugas klasifikasi teks. Pertama, library TensorFlow dan modul-modul Keras diimpor. Selanjutnya, sebuah objek model Sequential dibentuk, yang digunakan untuk mendefinisikan arsitektur model secara berurutan. Model dimulai dengan layer Input, yang menerima input data dengan bentuk yang sesuai. Kemudian, layer Embedding digunakan untuk mengubah kata-kata menjadi representasi vektor numerik, sebuah langkah penting dalam pemrosesan teks. Tiga layer LSTM berturut-turut dengan masing-masing 32 unit ditambahkan ke model. LSTM (Long Short-Term Memory) digunakan untuk memproses data dalam urutan, seperti teks. Dua dari tiga layer LSTM memiliki parameter `return_sequences=True`, yang berarti outputnya adalah urutan sekuensial. Selama proses pembangunan model, juga digunakan layer Normalisasi untuk meningkatkan stabilitas dan percepatan pelatihan. Layer Dense digunakan untuk menambahkan lapisan-lapisan terhubung penuh dengan aktivasi ReLU, yang akan menghasilkan output akhir berdasarkan pola yang dipelajari oleh model. Setelah model dibuat, dilakukan pengujian 
Evaluasi
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

