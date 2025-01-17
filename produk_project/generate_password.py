import hashlib
import datetime

# Ambil tanggal hari ini
now = datetime.datetime.now()

# Format tanggal sesuai instruksi (DD-MM-YY)
formatted_date = now.strftime("%d-%m-%y")

# Buat string password sesuai format yang diinginkan
password = f'bisacoding-{formatted_date}'

# Menghitung MD5 hash dari password
md5_hash = hashlib.md5(password.encode()).hexdigest()

# Menampilkan hasil MD5
print(md5_hash)
