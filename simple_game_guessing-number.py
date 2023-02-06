import random
print("Bắt đầu nhé!!!")
print('Số bí mật từ 1 đến 5')
your_number = int(input('Hãy nhập số bạn đoán: '))
secret_number = random.randint(1,5)
if your_number < secret_number:
    print('Số bạn chọn quá thấp')
elif  your_number > secret_number:
     print('Số bạn chọn quá cao')
else:
    print('Chúc mừng bạn, đúng rồi!!!')

print(f'Số bí mật là :{secret_number} ') 