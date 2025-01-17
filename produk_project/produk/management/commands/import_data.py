from django.core.management.base import BaseCommand
import requests
import hashlib
import datetime
from produk.models import Produk, Kategori, Status

# Fungsi untuk menghasilkan password MD5 sesuai dengan instruksi
def generate_password():
    now = datetime.datetime.now()
    password = f"bisacoding-{now.strftime('%d-%m-%y')}"
    return hashlib.md5(password.encode()).hexdigest()

class Command(BaseCommand):
    help = 'Ambil data dari API dan simpan ke database'

    def handle(self, *args, **kwargs):
        # Ambil username dan password
        username = f"tesprogrammer{datetime.datetime.now().strftime('%d%m%y')}C15"
        password = generate_password()

        # Cek apakah username dan password terisi dengan benar
        print(f"Username: {username}")
        print(f"Password: {password}")

        # URL API
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

        # Kirim data menggunakan POST
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(url, json={
            'username': username,
            'password': password
        }, headers=headers)

        # Cek status dan hasil response
        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS("Data fetched successfully"))
            data = response.json()  # Mendapatkan data dalam format JSON

            # Proses dan simpan data ke database
            for item in data.get("produk", []):  # Misalnya produk ada dalam key "produk"
                kategori = Kategori.objects.get(id=item['kategori_id'])
                status = Status.objects.get(id=item['status_id'])

                produk = Produk(
                    nama_produk=item['nama_produk'],
                    harga=item['harga'],
                    kategori=kategori,
                    status=status
                )
                produk.save()

            self.stdout.write(self.style.SUCCESS("Data berhasil disimpan ke database."))
        else:
            self.stderr.write(f"Failed to fetch data from API. Status code: {response.status_code}")
            self.stderr.write(f"Response content: {response.content}")
