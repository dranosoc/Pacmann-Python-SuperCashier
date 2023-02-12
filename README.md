# Super Cashier

## Latar Belakang Problem

>Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang selr-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.

>Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.
___

## Requirements

* Customer dapat membuat sebuah instance id transaksi dengan memanggil class Transaction()
* Customer dapat menambahkan nama item, jumlah item dan harga per item yang dibeli sekaligus menghitung total harga item menggunakan fitur `add_item`
* Apabila terdapat kesalahan input, customer dapat mengubah nama item, jumlah item, ataupun harga per item menggunakan fitur `update_item_name`,`update_item_qty`, dan `update_item_price`
* Apabila customer ingin membatalkan pesanan, customer dapat menghapus salah satu atau keseluruhan daftar pesanan dengan fitur `delete_item` dan `reset_transaction`
* Fitur `check_order` dapat digunakan customer untuk menampilkan daftar seluruh pesanan yang telah dimasukkan
* Setelah customer sudah yakin dengan pesanannya, dapat menggunakan fitur `total_price` untuk menghitung total harga yang perlu dibayarkan dengan ketentuan diskon:
    * untuk total harga di atas Rp 200.000,- mendapat diskon 5%
    * untuk total harga di atas Rp 300.000,- mendapat diskon 8%
    * untuk total harga di atas Rp 500.000,- mendapat diskon 10%



## Alur Program
Flow Chart User Journey:

![User Journey](Flowchart_Method/user_journey.drawio.svg)
___

Flow chart untuk method `add_item`

![Method Add Item](Flowchart_Method/add_item.drawio.svg)

___

Flow chart untuk method `update_item_name`

![Method Update Nama Item](Flowchart_Method/update_item_name.drawio.svg)

___

Flow chart untuk method `update_item_qty`

![Method Update Jumlah Item ](Flowchart_Method/update_item_qty.drawio.svg)

___

Flow chart untuk method `update_item_price`

![Method Update Harga Item](Flowchart_Method/update_item_price.drawio.svg)

___

Flow chart untuk method `delete_transaction`

![Method Hapus Transaksi](Flowchart_Method/delete_item.drawio.svg)

___

Flow chart untuk method `reset_transaction`

![Method Reset Transaksi](Flowchart_Method/reset_transaction.drawio.svg)

___

Flow chart untuk method `check_order`

![Method Check Order](Flowchart_Method/check_order.drawio.svg)

___

Flow chart untuk method `total_price`

![Method Harga Total](Flowchart_Method/total_price.drawio.svg)

___

<br>
<br>


## Penjelasan Code

Pada program ini terdapat beberapa fitur yang dapat dipanggil menggunakan method class

* Fitur `add_item()` membutuhkan input berupa `nama_item`,`jumlah_item`, dan `harga_per_item`. Ketika memanggil method ini user akan diminta untuk memasukkan data masing-masing item, yaitu nama item, jumlah item dan harga item. Di setiap permintaan input, user dapat mengetik perintah '\<stop>' untuk menghentikan proses input. Apabila melakukan kesalahan input, seperti memasukkan empty string ("") ataupun angka nol, maka program akan mengubahnya menjadi nilai `None`. Apabila semua parameter input sudah dimasukkan, maka program akan memasukkan semua parameter input tersebut ke dalam dictionary of list bernama `order_dict` yang telah diinisialisasi di dalam class `Transaction()`. Fitur ini juga mengkalkulasikan nilai total harga masing-masing item sekaligus memasukkannya di dalam `order_dict`

```python
def add_item(self):
        while True:
            try:
                nama_item = str(input("Masukkan Nama Item:\n"))
                if nama_item in self.order_dict["Nama Item"]:
                    print("Nama Item sudah ada di dalam daftar belanja, masukkan nama item yang lain atau ketik '<stop>'\
untuk menghentikan perintah")
                    continue
                elif nama_item == "<stop>":
                    break
                else:
                    if nama_item == "" or nama_item == 0:
                        nama_item = None
                    while True:
                        try:
                            jumlah_item = int(input("Masukkan Jumlah Item:\n"))
                            if jumlah_item == "<stop>":
                                break
                            elif jumlah_item <= 0:
                                print("Masukkan jumlah item dengan benar")
                                continue
                            harga_per_item = int(input("Masukkan Harga Item (satuan):\n"))
                            if harga_per_item == "<stop>":
                                break
                            elif harga_per_item <= 0:
                                print("Masukkan harga dengan benar")
                                continue
                            else:
                                self.order_dict['Nama Item'].append(nama_item)
                                self.order_dict['Jumlah Item'].append(jumlah_item)
                                self.order_dict['Harga Per Item'].append(harga_per_item)
                                self.order_dict['Total Harga'].append(jumlah_item * harga_per_item)
                                print(f"{nama_item} berhasil ditambahkan ke daftar belanja!")
                                break
                        except:
                            self.peringatan()
                    break
            except:
                self.peringatan()

```
* Fitur `update_item_name()`,`update_item_qty()`, dan `update_item price()` berfungsi untuk mengubah atribut data yang ada di dalam `order_dict` dengan cara mengakses memilih `nama_item` yang ingin diubah atribut nya. Input pada fungsi ini adalah nama item lama (`nama_item`) yang ingin diganti atributnya, dan atribut baru (`update_nama_item`, `update_jumlah_item`, `update_item_price`) yang akan menggantikan atribut lama. Terdapat pula fitur yang dapat mencegah pengguna untuk memasukkan `nama_item` yang sudah ada di dalam daftar belanjaan `order_dict`

```python
def update_item_name(self):
        while True:
            try:
                nama_item = str(input("Masukkan Nama Item yang ingin diganti:\n"))
                if nama_item == '<stop>':
                    break
                elif nama_item not in self.order_dict["Nama Item"]:
                    print(f"Nama Item tidak ada di dalam daftar belanja")
                    continue

                else:
                    while True:
                        try:
                            update_nama_item = str(input("Masukkan Nama Item yang baru:\n"))
                            if update_nama_item == "<stop>":
                                break
                            elif update_nama_item in self.order_dict["Nama Item"]:
                                print(f"Nama Item sudah ada di dalam daftar belanja")
                                continue
                            else:
                                baris = self.order_dict['Nama Item'].index(nama_item)
                                self.order_dict['Nama Item'][baris] = update_nama_item
                                print(f'Nama item \"{nama_item}\" telah diganti menjadi \"{update_nama_item}\"')
                                break
                        except:
                            self.peringatan()
                    break
            except:
                self.peringatan()
        
    def update_item_qty(self):
        while True:
            try:
                nama_item = str(input("Masukkan Nama Item yang ingin diganti jumlahnya:\n"))
                if nama_item == '<stop>':
                    break
                elif nama_item not in self.order_dict["Nama Item"]:
                    print("Nama Item tidak ada di dalam daftar belanja")
                    continue

                else:
                    while True:
                        try:
                            update_jumlah_item = int(input("Masukkan Jumlah Item yang baru:\n"))
                            if update_jumlah_item == "<stop>":
                                break
                            elif update_jumlah_item <= 0:
                                print("Mohon masukkan jumlah item baru dengan benar")
                                continue
                            else:
                                baris = self.order_dict['Nama Item'].index(nama_item)
                                jumlah_item_lama = self.order_dict['Jumlah Item'][baris] 
                                self.order_dict['Jumlah Item'][baris] = update_jumlah_item
                                self.order_dict['Total Harga'][baris] = update_jumlah_item * \
                                self.order_dict['Harga Per Item'][baris]
                                print(f'Jumlah item {nama_item} telah diganti dari {jumlah_item_lama} pcs ', \
                                f'menjadi {update_jumlah_item} pcs')
                                break
                        except:
                            self.peringatan()
                    break
            except:
                self.peringatan()
        
    def update_item_price(self):
        while True:
            try:
                nama_item = str(input("Masukkan Nama Item yang mau diganti harga nya:\n"))
                if nama_item == '<stop>':
                    break
                elif nama_item not in self.order_dict["Nama Item"]:
                    print("Nama Item tidak ada di dalam daftar belanja")
                    continue
                else:
                    while True:
                        try:
                            update_harga_item = int(input("Masukkan harga item yang baru:\n"))
                            if update_harga_item == "<stop>":
                                break
                            elif update_harga_item <= 0:
                                print("Mohon masukkan angka dengan benar")
                                continue
                            else:
                                baris = self.order_dict['Nama Item'].index(nama_item)
                                harga_item_lama = self.order_dict['Harga Per Item'][baris]
                                self.order_dict['Harga Per Item'][baris] = update_harga_item
                                self.order_dict['Total Harga'][baris] = update_harga_item * \
                                self.order_dict['Jumlah Item'][baris]
                                print(f'Harga item {nama_item} telah diganti dari Rp{harga_item_lama:,} ', \
                                f'menjadi Rp{update_harga_item:,}')
                                break
                        except:
                            self.peringatan()
                    break
            except:
                self.peringatan()
```

* Fitur hapus transaksi terdiri dari method `delete_item()` dan `reset_transaction()`. Untuk `delete_item()` berfungsi untuk menghapus item satu persatu, sedangkan method `reset_transaction()` dapat menghapus semua item transaksi sekaligus. Pada method `delete_item()` dapat mencegah pengguna memasukkan `nama_item` yang tidak ada di dalam daftar belanjaan `order_dict`. Selain itu, apabila pengguna menghapus satu persatu item hingga habis, program akan mendefinisikan parameter `order_is_empty` sebagai `True`

```Python
def delete_item(self):
        while True:
            try:
                nama_item = str(input("Masukkan Nama Item yang ingin dihapus:\n"))
                if nama_item == '<stop>':
                    break
                elif nama_item not in self.order_dict["Nama Item"]:
                    print("Nama Item tidak ada di dalam daftar belanja")
                    continue

                else:
                    baris = self.order_dict['Nama Item'].index(nama_item)
                    self.order_dict['Nama Item'].pop(baris)
                    self.order_dict['Jumlah Item'].pop(baris)
                    self.order_dict['Harga Per Item'].pop(baris)
                    self.order_dict['Total Harga'].pop(baris)
                    print(f'{nama_item} berhasil di-delete!')
                    if self.order_dict == {'Nama Item':[],'Jumlah Item':[],'Harga Per Item':[],'Total Harga':[]}:
                        self.order_is_empty = True
                    else:
                        pass
                    break
            except:
                self.peringatan()
    
    def reset_transaction(self):
        self.order_dict = {'Nama Item':[],'Jumlah Item':[],'Harga Per Item':[],'Total Harga':[]}
        print('Semua item berhasil di-delete!')
        self.order_is_empty = True
```

* Pada fitur `check_order` terdapat 3 kondisi yang diperiksa. Pertama apabila di dalam order terdapat nilai `None`, program akan menunjukkan pada baris berapa saja yang terdapat nilai `None` tersebut. Kedua, apabila ternyata dalam `order_dict` terdapat empty list maka program akan mem-print bahwa daftar belanjaan kosong. Dan yang ketiga, apabila semua pesanan sudah sesuai, maka akan menampilkan tabel daftar pesanan.

```Python
def check_order(self):
        if (None in self.order_dict["Nama Item"]) or (None in self.order_dict["Jumlah Item"]) \
        or (None in self.order_dict["Harga Per Item"]) or (None in self.order_dict["Total Harga"]):
            a = 1
            baris_kosong = []
            for i in self.order_dict["Nama Item"]:
                if (i == None) or (self.order_dict["Jumlah Item"][self.order_dict["Nama Item"].index(i)] == None) \
                or (self.order_dict["Harga Per Item"][self.order_dict["Nama Item"].index(i)] == None):
                    baris_kosong.append(a)
                else:
                    pass
                a += 1
            print(f'Terdapat kesalahan input data, ada data yang kosong pada baris: {baris_kosong}')
            print(f'Gunakan method reset_transaction() untuk menghapus semua isi daftar belanja')
            print(tabulate(self.order_dict, headers="keys", tablefmt = "fancy_grid"))
            self.check_order_done = True
            self.order_is_empty = False
            self.order_is_valid = False
        elif self.order_dict == {'Nama Item':[],'Jumlah Item':[],'Harga Per Item':[],'Total Harga':[]}:
            print(f'daftar belanjaan kosong!!!')
            self.check_order_done = True
            self.order_is_empty = True
            self.order_is_valid = False
        else:
            print("Pemesanan sudah benar, silahkan panggil method total_price() untuk menghitung total belanjaan anda \n\
\natau gunakan method update_item_name(), update_item_qty(), update_item_price(), delete_item(), \n\
maupun reset_transaction() untuk memodifikasi pesanan anda")
            print(tabulate(self.order_dict, headers="keys", tablefmt = "fancy_grid"))
            self.check_order_done = True
            self.order_is_empty = False
            self.order_is_valid = True

```

* Pada Fitur `total_price()` terdapat beberapa kondisi yang dapat mencegah program untuk menghitung harga total, yaitu ketika pengguna belum mengecek daftar belanjaan menggunakan `check_order()`, terdapat nilai `None`, ataupun daftar belanjaan kosong. Apabila kondisi tersebut tidak terjadi, maka program akan menghitung total harga, dan menyesuaikannya dengan diskon yang didapat.

```Python
def total_price(self):
        if (self.check_order_done is True) and (self.order_is_empty is False) and (self.order_is_valid is True):
            total = sum(self.order_dict['Total Harga'])
            print(f'Item yang dibeli adalah {self.order_dict["Nama Item"]}')

            if total <= 200_000:
                diskon = 0

            elif 200_001 < total <= 300_000:
                diskon = 0.05
                print(f'Anda mendapatkan diskon 5% !')

            elif 300_001 < total <= 500_000:
                diskon = 0.08
                print(f'Anda mendapatkan diskon 8% !')

            elif total > 500_000:
                diskon = 0.1
                print(f'Anda mendapatkan diskon 10% !')

            print(f'Total belanja yang harus dibayarkan adalah Rp. {total - (total * diskon):,.2f}')
        
        elif self.check_order_done is False:
            print("Mohon gunakan method check_order() terlebih dahulu untuk memeriksa pesanan anda!")
        elif self.order_is_empty is True:
            print("Item belanjaan kosong!")
        elif self.order_is_valid is False:
            print("Order tidak valid")
        else:
            print("Terdapat kesalahan, mohon ulangi program dari awal")

```


## Hasil Test Case

Untuk memulai test case, customer perlu untuk mengimport modular code `script.py` ke dalam notebook.

```python
from script.py import *
```

kemudian customer mendefinisikan instance object untuk identifikasi transaksi, sebagai contoh kita buat sebagai `trnsct_123`

```python
trnsct_123 = Transaction()
```

##### Test Case 1:
>customer menambahkan dua item baru menggunakan method `add_item`. Item yang ditambahkan adalah:
>* Nama Item: Ayam Goreng, Jumlah: 2, Harga: 20_000
>* Nama Item: Pasta Gigi, Jumlah: 3, Harga: 15_000

Untuk penyelesaian test case 1, kita dapat memanggil method `add_item()`.
Program akan menampilkan permintaan input, dan customer dapat memasukkan item belanjaan sesuai yang diinginkan.

**output**:

![hasil test case 1](image/test_case_1.jpg)

setelah memasukkan item belanjaan, customer dapat memeriksa daftar belanjaannya dengan memanggil method `check_order()`
![test case 1 check order](image/test_case_1(1).jpg)

<br>
<br>
<br>

##### Test Case 2
>Ternyata customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka user menggunakan method `delete_item()` untuk menghapus item. Item yang dihapuskan adalah **Pasta Gigi**.

untuk test case ke-2, customer memanggil method `delete_item()` dan memasukkan nama item yang ingin dihapus

**output:**

![hasil test case 2](image/test_case_2.jpg)

kemudian customer dapat memeriksa belanjaannya lagi menggunakan method `check_order()`

![test case 2 check order](image/test_case_2(1).jpg)
<br>
<br>
<br>

##### Test Case 3
>Ternyata setelah dipikir-pikir customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.

kita dapat tes fitur ini dengan memasukkan beberapa data menggunakan method `add_item()` secara satu persatu data berikut:
* Nama Item: Ayam Goreng, Qty: 2, Harga: 20_000
* Nama Item: Pasta Gigi, Qty: 3, Harga: 15_000
* Nama Item: Mainan Mobil, Qty: 1, Harga: 200_000
* Nama Item: Mi Instan, Qty: 5, Harga: 3_000

kemudian kita gunakan method `check_order()` untuk menampilkan daftar belanjaan

![test case 3](image/test_case_3.jpg)

lalu kita bisa gunakan method `reset_transaction()` untuk menghapus semua item belanjaan

**output:**

![test case 3(1)](image/test_case_3(1).jpg)

untuk membuktikan daftar belanjaan sudah kosong, kita dapat panggil method `check_order()` kembali

![test case 3(2)](image/test_case_3(2).jpg)

dengan ini, method `reset_transaction()` berfungsi!!!

<br>
<br>
<br>

##### Test Case 4
>Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method `total_price()`. Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

setelah memasukkan item menggunakan method `add_item()`, customer dapat menampilkan daftar belanjaan menggunakan `check_order()` dan menampilkan harga total beserta diskon (jika ada) menggunakan method `total_price()`

**output:**

![test case 4](image/test_case_4.jpg)

<br>

Dalam program yang dibuat, apabila customer belum melakukan `check_order()` tetapi sudah memanggil `total_price()`, maka akan me-print "Mohon gunakan method check_order() terlebih dahulu untuk memeriksa pesanan anda!". Hal ini bertujuan untuk memeriksa apakah hasil inputan sudah valid atau belum dan mencegah terjadi perhitungan harga total yang tidak valid.

**output:**

![test case 4](image/test_case_4(1).jpg)

<br>
<br>

## Conclusion/Future Work
Telah dibuat sebuah program super cashier yang memiliki beberapa fitur seperti yang telah sesuai dengan requirement dan berdasarkan hasil test case, program yang dibuat telah berhasil berjalan dengan baik.

Pada program ini masih terdapat beberapa fitur yang dapat dikembangkan untuk kenyamanan customer, contohnya:
1. Katalog yang dapat menyandingkan antara id nama item dengan harga satuannya, sehingga customer tidak dapat memasukkan nama item selain yang ada di dalam katalog. Lebih daripada itu, customer juga tidak perlu memasukkan harga per item secara manual. 
2. Fitur yang memungkinkan untuk memasukkan item yang memiliki nama yang sama, namun harga yang berbeda
3. Fitur yang memungkinkan untuk menambahkan qty dan menghitung total harga secara otomatis jika nama item dan harga item yang dimasukkan sama dan sudah ada di dalam daftar belanja
4. Fitur yang menganggap sama (tidak mempedulikan) huruf besar/kecil pada nama item sehingga otomatis menambahkan qty dan menghitung total harga
5. FItur menambahkan item belanjaan secara bulk (langsung banyak)
