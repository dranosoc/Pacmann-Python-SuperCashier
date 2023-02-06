from tabulate import tabulate

class Transaction:
    
    def __init__(self):
        self.order_dict = {'Nama Item':[],'Jumlah Item':[],'Harga Per Item':[],'Total Harga':[]}
        print("Selamat datang di toko kami, berikut merupakan method yang dapat digunakan:\n",\
        "add_item: untuk menambahkan item ke dalam daftar belanja\n",\
        "update_item_name: untuk memodifikasi nama item\n",\
        "update_item_qty: untuk memodifikasi jumlah item\n",\
        "update_item_price: untuk memodifikasi harga per item\n",\
        "delete_item: untuk menghapus item\n",\
        "reset_transaction: untuk menghapus semua item\n",\
        "check_order: untuk melihat daftar belanjaan yang diinput\n",\
        "total_price: untuk menghitung harga yang perlu anda bayarkan")
        self.check_order_done = False
        self.order_is_empty = True
        
    def peringatan(self):
        print("Mohon lakukan input dengan benar!!!")
        
    def add_item(self):
        """
        method ini berfungsi untuk menambahkan item baru
        terdapat pencegahan agar user tidak memasukkan nama item baru yang sama dengan nama item yang sudah ada di dalam
        daftar belanja
        """
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
    
    def direct_add_item(self, nama_item, jumlah_item, harga_per_item):
        """
        method ini dibuat hanya untuk memudahkan penambahan data agar lebih cepat
        """
        if nama_item == "" or nama_item == 0:
            nama_item = None
        if jumlah_item == "" or jumlah_item == 0:
            jumlah_item = None
        if harga_per_item == "" or harga_per_item == 0:
            harga_per_item = None
        self.order_dict['Nama Item'].append(nama_item)
        self.order_dict['Jumlah Item'].append(jumlah_item)
        self.order_dict['Harga Per Item'].append(harga_per_item)
        if jumlah_item == None or harga_per_item == None:
            total_harga = None
        else:
            total_harga = jumlah_item * harga_per_item
        self.order_dict['Total Harga'].append(total_harga)
        
    
    def update_item_name(self):
        """
        berfungsi untuk mengubah nama item, pada fungsi ini atribut jumlah dan harga tidak berubah
        di fungsi ini juga dapat memeriksa jika nama item baru yang diinputkan sudah ada ataupun nama item yang diganti
        ternyata tidak ada
        """
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
        """
        berfungsi untuk mengubah jumlah item, sekaligus mengkalkulasikan total harga
        """
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
        """
        berfungsi untuk mengganti nilai harga satuan yang lama dengan yang baru, identifikasi menggunakan nama item
        pada fungsi ini juga sekaligus mengkalkulasikan total harga per nama item
        """
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
        
    def delete_item(self):
        """
        berfungsi untuk menghapus item tertentu secara satuan, untuk memilih item mana yang ingin dihapus digunakan
        identifikasi nama item
        """
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
        """
        berfungsi untuk menghapus semua item belanjaan dan mendefinisikan kondisi daftar belanjaan kosong menjadi True
        """
        self.order_dict = {'Nama Item':[],'Jumlah Item':[],'Harga Per Item':[],'Total Harga':[]}
        print('Semua item berhasil di-delete!')
        self.order_is_empty = True
        
    def check_order(self):
        """
        method ini dapat memeriksa apakah ada kesalahan berupa None di dalam order_dict (customer salah melakukan input)
        dapat memeriksa apabila item belanjaan kosong, dan juga menampilkan item belanjaan yang telah ditambahkan atau
        hasil modifikasi dalam bentuk tabulate
        """
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
        
    def total_price(self):
        """
        method ini berfungsi untuk menghitung diskon dan total harga dan menampilkannya apabila beberapa kondisi telah
        terpenuhi.
        """
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
