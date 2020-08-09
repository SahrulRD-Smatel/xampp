import mysql.connector
import basic
import SKYGroup

print('-----------------------------------------------')
print('Hai! Selamat Datang di Nomination : HOTELGroup Indonesia')
print('')
print('Silahkan pilih mana yang akan Anda Nominasi dulu')
print('')
print('* NOMINATION CEO *')
print('1) SKYGroup')
print('2) Hotel Family')
print('3) Other Estelle Groups')
print('-----------------------------------------------')
print('')

menu = int(input('Pilih NOMINATION OPTION : '))

if (menu==1):
    print('')
    print('------------------------------------')
    print('Welcome to SKYGroup FAMILY FANDOM')
    print('')
    print("SKYGroup Family Member : ")
    print('1) Sahrul Ramadhani')
    print('2) RPL Four')
    print('3) Dimas Sodiin')
    print('4) Mparty Six')
    print('5) Khansa Imani')
    print("")
    print('Please nominate your favorite lane in these options!')
    print("")
    print('OPTIONS :')
    print('1. Tambah CEO')
    print('2. Ubah CEO')
    print('3. Hapus CEO')
    print('4. Tampilkan CEO')
    print('------------------------------------')
    print("")

    menu2 = int(input('[SKYGroup] Pilih OPTION : '))
          
    if(menu2==1):
        name = input('Name : ')
        lane = input('Lane : ')
        address = input('Address : ')
        data=[name,lane,address]
        SKYGroup.add(data)
    elif(menu2==2):
        id_skygroup = input('No. ID : ')
        name = input('Name : ')
        lane = input('Lane : ')
        address = input('Address : ')
        data=[name,lane,address,id_skygroup]
        SKYGroup.edit(data)
    elif(menu2==3):
        id_skygroup = input('No. ID : ')
        data=[id_skygroup]
        SKYGroup.search(data)
        confirm = input('Yakin mau menghapus data CEO ini? [Y/N] : ')
        if(confirm == 'Y'):
            SKYGroup.delete(data)
        else:
            print('Tidak jadi menghapus data CEO!')
    elif(menu2==4):
        SKYGroup.show()
    else:
        print('OPTION IS NOT AVAILABLE!!!')
elif (menu==2):
    print('')
    print('------------------------------------')
    print('Welcome to INTERNATIONAL Hotel Family')
    print('')
    print("Hotel Family Member : ")
    print('1) Zethya Dhani')
    print('2) Kayn Duke')
    print('3) Zodiin BMS')
    print('4) Iris Wyatt')
    print('5) Ancha Forest')
    print("")
    print('Please nominate your favorite lane in these options!')
    print("")
    print('OPTIONS :')
    print('1. Tambah CEO')
    print('2. Ubah CEO')
    print('3. Hapus CEO')
    print('4. Tampilkan CEO')
    print('------------------------------------')
    print("")

    menu2 = int(input('[Hotel Family] Pilih OPTION : '))
          
    if(menu2==1):
        name = input('Name : ')
        lane = input('Lane : ')
        address = input('Address : ')
        data=[name,lane,address]
        Nominasi.add(data)
    elif(menu2==2):
        id_nominasi = input('No. ID : ')
        name = input('Name : ')
        lane = input('Lane : ')
        address = input('Address : ')
        data=[name,lane,address,id_nominasi]
        Nominasi.edit(data)
    elif(menu2==3):
        id_nominasi = input('No. ID : ')
        data=[id_nominasi]
        Nominasi.search(data)
        confirm = input('Yakin mau menghapus data CEO ini? [Y/N] : ')
        if(confirm == 'Y'):
            Nominasi.delete(data)
        else:
            print('Tidak jadi menghapus data CEO!')
    elif(menu2==4):
        Nominasi.show()
    else:
        print('OPTION IS NOT AVAILABLE!!!')
elif (menu==3):
    print('')
    print('---------------------------------------')
    print("WELCOME to The Estelle Groups")
    print('')
    print("The other Estelle Groups : ")
    print('1) AnnyDuke Ngkong')
    print('2) Ed Aria')
    print('3) Elton Count')
    print('4) Meliodas Elizabeth')
    print('5) Louis Sakurai')
    print('6) Agus Slamet')
    print("")
    print('Please nominate your favorite lane in these options!')
    print("")
    print('OPTIONS :')
    print('1. Tambah CEO')
    print('2. Ubah CEO')
    print('3. Hapus CEO')
    print('4. Tampilkan CEO')
    print('------------------------------------')
    print("")

    menu2 = int(input('[Estelle Groups] Pilih OPTION : '))
          
    if(menu2==1):
        name = input('Name : ')
        lane = input('Lane : ')
        address = input('Address : ')
        data=[name,lane,address]
        Family.add(data)
    elif(menu2==2):
        id_family = input('No. ID : ')
        name = input('Name : ')
        lane = input('Lane : ')
        address = input('Address : ')
        data=[name,lane,address,id_family]
        Family.edit(data)
    elif(menu2==3):
        id_family = input('No. ID : ')
        data=[id_family]
        Family.search(data)
        confirm = input('Yakin mau menghapus data CEO ini? [Y/N] : ')
        if(confirm == 'Y'):
            Family.delete(data)
        else:
            print('Tidak jadi menghapus data CEO!')
    elif(menu2==4):
        Family.show()
    else:
        print('OPTION IS NOT AVAILABLE!!!')
else:
    print('')
    print('OPTION IS NOT AVAILABLE!!!')
