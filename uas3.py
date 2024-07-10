class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        """Menambahkan pesanan ke dalam antrian."""
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' ditambahkan ke antrian.")

    def dequeue(self):
        """Menghapus pesanan dari depan antrian."""
        if not self.antrian:
            print("Antrian kosong.")
        else:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan '{pesanan}' selesai dan dihapus dari antrian.")

restoran = AntrianRestoran()
restoran.enqueue("rujak spageti")
restoran.enqueue("mie rambut kuntilanak")
restoran.enqueue("Es coklat harimau")
restoran.dequeue()
restoran.dequeue()
restoran.dequeue()
