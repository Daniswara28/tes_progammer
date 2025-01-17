import requests
from produk.models import Produk, Kategori, Status
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetch data from API and save it to the database'

    def handle(self, *args, **kwargs):
        # URL API
        url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'

        # Username dan Password MD5 untuk autentikasi
        username = 'tesprogrammer170125C15'
        password = '4e6a9250649d8e80f5c35f29bee9b930'

        # Mengirim request ke API dengan autentikasi
        response = requests.post(url, data={
            'username': username,
            'password': password
        })

        # Mengecek apakah request berhasil
        if response.status_code == 200:
            data = response.json()

            # Pastikan data dari API memiliki format yang sesuai
            for item in data.get('produk', []):
                # Ambil data produk, kategori, dan status
                kategori, _ = Kategori.objects.get_or_create(id_kategori=item['kategori_id'], nama_kategori=item['kategori'])
                status, _ = Status.objects.get_or_create(id_status=item['status_id'], nama_status=item['status'])

                # Simpan produk ke database
                Produk.objects.update_or_create(
                    id_produk=item['id_produk'],
                    defaults={
                        'nama_produk': item['nama_produk'],
                        'harga': item['harga'],
                        'kategori_id': kategori,
                        'status_id': status,
                    }
                )

            self.stdout.write(self.style.SUCCESS('Successfully imported products from API'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data from API. Status code: {response.status_code}'))
