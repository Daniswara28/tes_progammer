import requests
from django.core.management.base import BaseCommand
from produk.models import Produk, Kategori, Status

class Command(BaseCommand):
    help = 'Ambil data produk dari API dan simpan ke database'

    def handle(self, *args, **kwargs):
        api_url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
        username = 'tesprogrammer170125C15'
        password = '4e6a9250649d8e80f5c35f29bee9b930'
        
        response = requests.post(api_url, auth=(username, password))

        print(response.status_code)  # Cetak status code
        print(response.text)         # Cetak isi response

        if response.status_code == 200:
            data = response.json()

            for item in data['data']:
                kategori, _ = Kategori.objects.get_or_create(id_kategori=item['kategori_id'], nama_kategori=item['kategori'])
                status, _ = Status.objects.get_or_create(id_status=item['status_id'], nama_status=item['status'])

                Produk.objects.create(
                    id_produk=item['id_produk'],
                    nama_produk=item['nama_produk'],
                    harga=item['harga'],
                    kategori_id=kategori.id_kategori,
                    status_id=status.id_status
                )
            
            self.stdout.write(self.style.SUCCESS('Data produk berhasil disimpan ke database!'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data from API. Status code: {response.status_code}'))
