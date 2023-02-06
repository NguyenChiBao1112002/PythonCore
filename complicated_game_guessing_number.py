import random

print('\nBẮT ĐẦU TRÒ CHƠI ĐOÁN SỐ BÍ MẬT NHÉ!!!')
print('--------------------------------------')
print('Con số bí mật sẽ nằm từ 1 đến 10')
so_luot_chon = 5
print(f'Bạn có tối đa {so_luot_chon} lần đoán!!!')
print('--------------------------------------')
so_bi_mat = random.randint(1,10)
so_ban_chon = int(input('Mời bạn đoán số: '))
so_luot_chon-=1
while True :
    if so_bi_mat == so_ban_chon:
        print('--------------------------------------')
        print('Bạn thắng rồi! Chúc mừng nhe')
        print(f'Số bí mật là : {so_bi_mat}')
        break
    elif so_luot_chon > 0:
        print('--------------------------------------')
        print(f'Bạn đoán sai rồi! Bạn còn {so_luot_chon} lần chọn')
        so_luot_chon -=1
        so_ban_chon = int(input(f'Mời bạn chọn lại:'))
    else: 
        print('--------------------------------------')
        print('Bạn thua rồi :((')
        print(f'Số bí mật là : {so_bi_mat}')
        break
    