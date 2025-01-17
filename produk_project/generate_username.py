import datetime

# Ambil tanggal sekarang
now = datetime.datetime.now()

# Format tanggal sesuai instruksi
username = f"tesprogrammer{now.strftime('%d%m%y')}C15"

print(username)
