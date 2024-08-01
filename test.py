import random, time, os


ascii = [119, 105, 108, 108, 32, 121, 111, 117, 32, 98, 101, 32, 109, 121, 32, 108, 111, 118, 101, 114]
sentence = ''.join(chr(i) for i in ascii)

text = f"{sentence} "
width = 60

result = ('\n'.join([
    ''.join([
        text[(x - y) % len(text)]
        if ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.05)**2 * (y * 0.1)**3 <= 0
        else ' '
        for x in range(-width, width)
    ])
    for y in range(int(width * 0.5), -int(width*0.5),-1)
]))




secret_number = random.randint(1, 100)

attempts = 0

print("\n==============TEBAK TEBAKAN==============\n")
print("Tebak angka 1-100\n")

while True:

    
    try:
        user_guess = int(input("Tebak: "))

        attempts += 1
        if user_guess == secret_number:
            print(f"\n\n\n============== Selamat, berhasil menebak sebanyak {attempts} percobaan ==============\n")
            print("Tebak kalimat berikut\n")
            for i in range(6, -1, -1):
                print(f"{i}...")
                time.sleep(1)
            os.system('cls')
            break

        elif user_guess > secret_number:
            print("Tebakan terlalu tinggi")
        else:
            print("Tebakan terlalu rendah")
    except ValueError:
        print("============== Input tidak valid. Silakan coba lagi! ==============\n")


print(result)