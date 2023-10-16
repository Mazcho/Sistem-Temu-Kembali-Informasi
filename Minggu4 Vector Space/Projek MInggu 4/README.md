![image](https://github.com/Mazcho/Sistem-Temu-Kembali-Informasi/assets/77985996/9889b833-04fa-4f31-b23a-552334275127)


Projek Tugas Ahkir STKI : ChatBot Bantuan Kesehatan Mental Remaja dengan Model Sequential

Kesehatan mental adalah kondisi dimana batin kita berada dalam keadaan tentram dan tenang, sehingga memungkinkan kita untuk menikmati kehidupan sehari hari, dan menghargai orang lain disekitar. Kesehatan mental yang baik akan mempengaruhi jalan lika liku hidup kita. Lalu bagaimana jika kesehatan mental kita terganggu, pastinya kita tidak bisa menikmati hidup ini dengan tenang. Mulai dari selalu cemas, _overtingking_, perasaan takut dan lain sebagainya
Gangguan kesehatan mental dapat memiliki berbagai gejala dan ciri-ciri yang bervariasi tergantung pada jenis gangguan, tingkat keparahan, dan individual yang terpengaruh. Beberapa ciri umum gangguan kesehatan mental meliputi:
1. Perubahan suasana hati: Perasaan sedih, gelisah, marah, atau hampa yang berlebihan dan berkepanjangan.
2. Gangguan tidur: Kesulitan tidur (insomnia) atau tidur berlebihan (hipersomnia), terbangun di malam hari, mimpi buruk, atau gangguan dalam pola tidur.
3. Perubahan dalam nafsu makan: Penurunan atau peningkatan berat badan yang tidak wajar, perubahan dalam pola makan, atau gangguan makan seperti anoreksia, bulimia, atau binge-eating disorder.
4. Isolasi sosial: Menarik diri dari teman, keluarga, dan aktivitas sosial, merasa cemas atau tidak nyaman dalam situasi sosial.
5. Perasaan kecemasan dan ketegangan: Kecemasan yang berlebihan, ketegangan, ketakutan yang tidak wajar, atau serangan panik yang bisa muncul tiba-tiba.
6. Perasaan tidak berdaya: Merasa kehilangan minat atau motivasi untuk melakukan aktivitas sehari-hari, merasa tidak berdaya atau tidak berharga.
7. Gangguan kognitif: Kesulitan berkonsentrasi, memori yang buruk, dan perubahan dalam kemampuan berpikir dan pengambilan keputusan.
8. Perubahan perilaku: Perubahan dalam perilaku seperti peningkatan penggunaan alkohol atau obat-obatan, perilaku impulsif, atau tindakan berbahaya.
9. Gangguan fisik: Keluhan fisik tanpa penyebab medis yang jelas, seperti sakit kepala, sakit perut, atau gangguan tidur yang berhubungan dengan gangguan mental.
10. Perasaan putus asa: Perasaan putus asa, pikiran tentang kematian, atau bahkan upaya bunuh diri.
11. Perubahan dalam persepsi realitas: Pada beberapa jenis gangguan seperti skizofrenia, seseorang mungkin mengalami halusinasi, delusi, atau gangguan persepsi yang lain.

Beberapa contoh hal terburuk yang dapat terjadi ketika gangguan kesehatan mental tidak ditangani atau dikelola dengan baik:

1. Bunuh diri: Tindakan bunuh diri adalah risiko terparah yang dapat muncul ketika seseorang mengalami gangguan kesehatan mental yang parah. Ini termasuk perasaan yang kuat untuk mengakhiri hidup.
2. Self-harm (melukai diri sendiri): Self-harm adalah tindakan merusak fisik diri sendiri, seperti memotong diri, membakar diri, atau melukai diri sendiri dengan tujuan untuk meredakan rasa sakit emosional.

Maka dari itu, penulis ingin membuat sebuah chat bot bantuan kesehatan mental remaja, yang dimana chat bot ini setidaknya bisa membantu remaja merasa lebih tenang, karena pada dasarnya tidak smua orang bisa menceritakaan apa yang dia rasakan. Tidak semua orang dapat mengungkapkan isi di otaknya di depan umum, maupun orang terdekatnya, karena mengalami trust issue.

Untuk workflow pengerjaan chat bot ini ada
1. collecting data
2. data cleansing
3. Preprocesing data ( tokenizer)
4. Modeling ( tensorflow "sequential")
5. Percobaan
6. Evaluasi

Pada chat bot ini, akan digunakan model "Sequential" dari Tensorflow.
model Sequential dengan beberapa lapisan yang umum digunakan dalam tugas pemrosesan bahasa alami (Natural Language Processing, NLP). Berikut adalah ringkasan dari apa yang akan peneliti lakukan:

1. Lapisan Input: Peneliti mendefinisikan lapisan input dengan bentuk yang sesuai. Ini adalah titik awal untuk data masukan model peneliti.
2. Lapisan Embedding: Peneliti menggunakan lapisan Embedding untuk mengubah token-token masukan menjadi vektor numerik yang dapat dipahami oleh model. mask_zero=True memungkinkan model untuk mengabaikan token nol.
3. Lapisan LSTM: Peneliti menggunakan tiga lapisan LSTM berturut-turut. Lapisan LSTM digunakan untuk memahami konteks dari teks masukan. Dengan pengaturan return_sequences=True, lapisan LSTM terakhir mengembalikan urutan output sekuensial, yang dapat berguna dalam tugas NLP tertentu.
4. Lapisan LayerNormalization: Lapisan LayerNormalization digunakan untuk mengstabilkan proses pelatihan dan meningkatkan konvergensi model.
5. Lapisan Dense: Apeneliti memiliki beberapa lapisan Dense untuk memproses representasi yang dihasilkan oleh lapisan LSTM. Ini termasuk lapisan Dense dengan fungsi aktivasi ReLU dan dropout untuk mencegah overfitting.
6. Kompilasi Model: Peneliti mengompilasi model dengan optimisasi 'adam' dan fungsi kerugian 'sparse_categorical_crossentropy'. Anda juga memantau metrik akurasi selama pelatihan.

Alasan menggunakan model Sequential :
1. Pengenalan Pola Teks: Jika Anda ingin memahami atau mengenali pola-pola tertentu dalam teks atau urutan data teks, seperti pengenalan pola dalam kalimat atau paragraf, model Sequential dapat digunakan untuk memodelkan urutan data tersebut dan mengidentifikasi pola yang relevan.

2. Klasifikasi Teks: Jika Anda ingin mengklasifikasikan teks ke dalam kategori tertentu berdasarkan pola yang terdapat dalam kolom "patterns," seperti membedakan pertanyaan dari pernyataan atau mengklasifikasikan masukan ke dalam kategori yang sesuai, model Sequential cocok digunakan.

3. Generasi Teks: Jika Anda ingin menghasilkan teks berkelanjutan sebagai tanggapan terhadap pola yang ada dalam kolom "patterns," seperti merespons pertanyaan dengan jawaban yang sesuai dalam kolom "responses," model Sequential bisa digunakan untuk membuat model generatif.

4. Pengolahan Urutan Data: Jika Anda ingin mengolah atau menganalisis data yang memiliki struktur urutan, seperti mengenali urutan yang memiliki pola tertentu atau melakukan tugas pemrosesan bahasa terkait urutan data teks, model Sequential sangat berguna.

