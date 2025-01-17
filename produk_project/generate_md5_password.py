import hashlib

# Buat string password sesuai format yang diinginkan
password = 'bisacoding-17-01-25'  # Ganti dengan tanggal sesuai hari ini

# Menghitung MD5 hash dari password
md5_hash = hashlib.md5(password.encode()).hexdigest()

# Menampilkan hasil MD5
print(md5_hash)
