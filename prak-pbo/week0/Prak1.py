string = ""

x = int(input("Masukkan angka :"))
bar = x
# Looping baris
while bar >= 0:
	# Looping kolom spasi
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1
	# Looping kolom bintang kiri	
	kiri = 1
	while kiri < (x - (bar-1)):
		string = string + " * "
		kiri = kiri + 1		
	# Looping kolom bintang kanan
	kanan = 1
	while kanan < kiri -1:
		string = string + " * "
		kanan = kanan + 1	

	string = string + "\n\n"
	bar = bar - 1
	
print (string)