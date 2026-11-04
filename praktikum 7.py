# Program menentukan apakah suatu bilangan merupakan bilangan prima atau bukan menggunakan fungsi def
def cek(a):
	if a < 2:
		return False
	b = 2
	while b * b <= a:
		if a % b == 0:
			return False
		b += 1
	return True
def hasil(a, prima):
	if prima:
		print(f"{a} adalah bilangan prima")
	else:
		print(f"{a} bukanlah bilangan prima")
c = int(input("Masukkan angka: "))
hasil(c, cek(c))

#Program input output fungsi
print("Ordinal Number")
print("ketik 0 untuk menghentikan program")
def angka(a):
	if a % 10 == 1:
		b = "st"
	elif a % 10 == 2:
		b = "nd"
	elif a % 10 == 3:
		b = "rd"
	else:
		b = "th"
	return (a, b)
while True:
	a = int(input("Masukkan angka: "))
	if a == 0:
		print(angka(a))
		print("terima kasih telah menggunakan program saya")
		break
	print(angka(a))
