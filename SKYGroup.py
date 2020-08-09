import mysql.connector
import basic
db=basic.koneksi()

#menambahkan data baru ke dalam tabel skygroup
def add(data):
    cursor=db.cursor()
    sql="""INSERT INTO skygroup(name,lane,address)VALUES(%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data berhasil ditambahkan!'.format(cursor.rowcount))

#menampilkan seluruh data dari tabel skygroup
def show():
    cursor=db.cursor()
    sql="""SELECT * FROM skygroup"""
    cursor.execute(sql)
    result=cursor.fetchall()
    print("---------------------------------------------------------------------")
    print("|ID|NAME\t\t|LANE\t\t|ADDRESS\t\t|")
    print("---------------------------------------------------------------------")
    for data in result:
        print('|',data[0],'|',data[1],"\t\t|",data[2],"\t\t|",data[3],"\t\t|")
        print('---------------------------------------------------------------------')

#mengubah data per record berdasarkan id pada tabel skygroup
def edit(data):
    cursor=db.cursor()
    sql="""UPDATE skygroup SET name=%s,lane=%s,address=%s WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data berhasil diubah!'.format(cursor.rowcount))

#menghapus data dari tabel skygroup
def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM skygroup WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{} Data berhasil dihapus!'.format(cursor.rowcount))

#mencari data dari tabel skygroup
def search(id_skygroup):
    cursor=db.cursor()
    sql="""SELECT * FROM skygroup WHERE id=%s"""
    cursor.execute(sql,id_skygroup)
    results = cursor.fetchall()

    print('---------------------------------------------------------------------')
    print("|ID|NAME\t\t|LANE\t\t|ADDRESS\t\t|")
    print('---------------------------------------------------------------------')
    for data in results:
        print("|",data[0],"|",data[1],"\t\t|",data[2],"\t\t|",data[3],"\t\t|")
        print('---------------------------------------------------------------------')
