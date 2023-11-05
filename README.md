# Project-Pacman---Analisa-Fundamental-LQ45
Project untuk melengkapi syarat kelulusan kelas bisnis analitik PACMANN 

Business Analytics Project Pacmann - Analisa Kinerja Saham LQ45 Kuartal II 2023

![alt text](https://github.com/tikumsatu/Project-Pacman---Analisa-Fundamental-LQ45/blob/main/data/Gambar%20saham%20LQ45.jpg)
1. Latar Belakang dan Tujuan Analisa

Sebuah perusahaan pengelola dana pensiun, ingin melakukan investasi di bursa saham Indonesia dengan berinvestasi di saham yang liquid, profitable dan memiliki fundamental yang baik. Manajer investasi Dapen memerintahkan stafnya untuk memilih 5 saham terbaik di index LQ45 untuk masing-masing kriteria metrics. Adapun kriteria yang dicari oleh staf investasi adalah sebagai berikut:
a. 5 saham dengan market cap besar?
b. 5 saham dengan NPM dan EPS terbesar?
c. 5 saham dengan dividen yield terbesar?
d. 5 saham dengan ROA dan ROE terbesar?
e. 5 saham dengan PBV dan PER terkecil?
f. 5 saham dengan DER terendah?

2. User Story Line dan User Flow
Pengguna dashboard ini adalah manajer investasi dapen yang akan menentukan instrumen investasi apa yang akan digunakan untuk mengelola dana pensiun. Melalui dashboard ini manajer investasi dapat melihat analisa fundamental dari saham-saham di index LQ45, dan dapat dijadikan screening awal untuk menentukan saham dengan kinerja terbaik yang akan dibeli untuk investasi.
Dashboard dibuat dengan menyajikan ratio-ratio keuangan yang sering digunakan dalam analisa fundamental meliputi market cap, earning per share, net profit margin, return on asset, return on equity, price to book value, price to earning ratio, debt to equity ratio dan dividend yield.

3. Dataset, Metrics dan Tools
a. Dataset
Dataset menggunakan data laporan keuangan kuartal II tahun 2023 yang diambil dari website IDX (https://www.idx.co.id/id/perusahaan-tercatat/laporan-keuangan-dan-tahunan/) yang sudah di tabulasikan menjadi 1 file data excel/csv berdasarkan data perusahaan tercatat.
Data dalam dataset meliputi:
Kode
Merupakan inisial perusahaan yang digunakan untuk penyebutan perusahaan dengan lebih singkat dan lebih mudah.

Company
Merupakan nama dari perusahaan yang tercatat listing di IDX (Bursa Efek Indonesia).

Sector
Merupakan bidang usaha dari perusahaan tercatat.

Currency
Merupakan mata uang dalam laporan keuangan yang digunakan meliputi IDR dan USD, dalam dataset ini mata uang USD sudah dikonversi ke dalam mata uang IDR sesuai nilai tengah kurs BI pada waktu pelaporan.

Listing
Merupakan tahun dimana perusahaan tercatat di Bursa Efek Indonesia.

Share
Merupakan jumlah seluruh saham yang beredar per Juni 2023.

Price
Merupakan harga penutupan bursa pada akhir Juni 2023.

Asset
Merupakan nilai asset yang dimiliki oleh perusahaan per Juni 2023

Liabilities
Merupakan nilai liabilitas yang dimiliki perusahaan per Juni 2023

Equity
Merupakan nilai ekuitas yang dimiliki perusahaan per Juni 2023.

Revenue
Merupakan total pendapatan perusahaan selama 2 kuartal awal tahun 2023.

Gross Profit
Merupakan laba bruto perusahaan per Juni 2023.

Net Profit
Merupakan laba bersih perusahaan selama 2 kuartal awal tahun 2023

Cash of the Beginning Period
Merupakan jumlah cash on hand di awal tahun 2023

Cash from Operating
Merupakan cash yang berasal dari aktivitas operasional.

Cash from Investing
Merupakan cash yang berasal dari aktivitas investasi, jika perusahaan banyak melakukan investasi maka nilainya akan minus (dihitung sebagai arus cash keluar).

Cash from Financing
Merupakan cash yang berasal dari aktivitas pendanaan, semakin banyak pendanaan/pembayaran hutang maka nilainya akan semakin minus (dihitung sebagai arus cash keluar)

Dividend Per Share
Merupakan besaran nilai rupiah yang dibagikan kepada setiap pemegang 1 lembar saham perusahaan.

b. Metrics
Market Cap
Mengukur besar nilai kapitalisasi pasar sebuah saham, semakin tinggi semakin baik. Untuk memperoleh nilai market cap digunakan rumus:
Market Cap = Share x Price

Net Profit Margin (NPM)
Rasio profitabilitas yang menunjukkan seberapa besar presentase laba bersih yang diperoleh dari setiap penjualan. Semakin besar rasio ini maka semakin baik karena dianggap kemampuan perusahaan dalam mendapatkan laba cukup tinggi. Untuk mendapatkan nilai NPM digunakan rumus:
NPM = Net Profit / Revenue x 100%

Earning Per Share (EPS)
Menunjukkan keuntungan yang bisa dibagikan kepada setiap pemegang 1 lembar saham. Dalam prakteknya ada perusahaan yang membagikan hasil keuntungan mencapai 100% dari EPS kepada pemegang saham, namun ada juga yang tidak membagikan sama sekali tergantung dari hasil RUPS tahunan perusahaan. Untuk mendapatkan nilai EPS digunakan rumus:
EPS = Net Profit/Share

Dividen Yield (DY)
Ratio nilai dividen per lembar saham yang dibagikan kepada pemegang saham dibandingkan dengan harga. Untuk menghitung dividen yield digunakan rumus:
DY = DPS/Price x 100%

On Asset (ROA)
Rasio yang digunakan untuk mengukur kemampuan manajemen perusahaan dalam menghasilkan laba secara menyeluruh. Semakin tinggi ROA sebuah perusahaan berarti kemampuan perusahaan dalam mencetak laba semakin baik. Untuk mendapatkan nilai ROA digunakan rumus:
ROA = Net Profit/Asset x 100%

Return On Equity (ROE)
Rasio untuk mengukur laba bersih sesudah pajak dengan modal sendiri (tanpa hutang). Rasio ini menunjukkan efisiensi penggunaan modal sendiri. Semakin tinggi rasio ini, semakin baik. Untuk mendapatkan nilai ROE digunakan rumus:
ROE = Net Profit/Equity x 100%

Price to Book Value Ratio (PBV)
Mengukur seberapa mahal harga saat ini dibanding dengan harga bukunya (book value) dimana book value adalah nilai ekuitas per lembar saham. Untuk memperoleh nilai PBV digunakan rumus:
PBV = Price/Book Value

Price to Earning Ratio (PER)
Rasio yang digunakan untuk menilai mahal murahnya saham berdasarkan kemampuan perusahaan menghasilkan laba bersih per saham . Price earning ratio yang tinggi pada saham dapat diinterpretasikan sebagai saham yang mahal jika pada periode waktu mendatang perusahaan tidak mampu meraih laba bersih yang lebih tinggi. Untuk mendapatkan nilai PER digunakan rumus:
PER = Price/EPS

Debt to Equity Ratio (DER)
Rasio yang digunakan untuk menilai hutang dengan ekuitas. Rasio ini dicari dengan cara membandingkan antara seluruh hutang, termasuk hutang lancar dengan seluruh ekuitas. Semakin tinggi nilai DER, semakin mengkhawatirkan kondisi keuangan perusahaan. Untuk mendapatkan nilai DER digunakan rumus:
DER = Liabilities/Equity x 100%

c. Tool
Tools data cleaning menggunakan Google Colabs
Tools visualisasi menggunakan Tableu Public
