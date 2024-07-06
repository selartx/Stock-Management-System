from tkinter import *
from tkinter import Tk, StringVar, ttk
import random
import sqlite3

con = sqlite3.connect('stock.db')
root = Tk()
root.geometry("1350x750+0+0")
root.title("Parça Kontrol Sistemi")

# Create cursor
c = con.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS stocks(
        product_name text,
        product_brand text,
        product_year integer,
        product_stock integer,
        product_ID integer PRIMARY KEY
)""")
#stok gösterimi saysında parça id öğrenme sayfasına yönlendirsin
# FONKSİYONLAR
def submit():
    submitted=Tk()
    submitted.geometry("1350x750+0+0")
    con = sqlite3.connect('stock.db')
    c = con.cursor()
    # Parça ismi
    lblproductname = Label(submitted,font=('arial', 18, 'bold'), text="Parça Adı:", bd=10, width=40, justify='left')
    lblproductname.grid(row=0, column=0)
    txtproductname1 = Entry(submitted,bd=10, width=40)
    txtproductname1.grid(row=0, column=1)
    # Parça markası
    lblproductbrand = Label(submitted,font=('arial', 18, 'bold'), text="Parça Markası:", bd=10, width=40, justify='left')
    lblproductbrand.grid(row=1, column=0)
    txtproductbrand1 = Entry(submitted,bd=10, width=40)
    txtproductbrand1.grid(row=1, column=1)
    # Parça yılı
    lblproductyear = Label(submitted,font=('arial', 18, 'bold'), text="Parça Yılı:", bd=10, width=40, justify='left')
    lblproductyear.grid(row=3, column=0)
    txtproductyear1 = Entry(submitted,bd=10, width=40)
    txtproductyear1.grid(row=3, column=1)
    #stok miktarı
    lblproductstock=Label(submitted,font=('arial', 18, 'bold'), text="Parça Stoğu:", bd=10, width=40, justify='left')
    lblproductstock.grid(row=4, column=0)
    txtproductstock1=Entry(submitted,bd=10, width=40)
    txtproductstock1.grid(row=4, column=1)
    #sadece yeni girilecek parçalarda stok girilecek şekilde ayarla 
    #parça ID
    lblproductID=Label(submitted,font=('arial', 18, 'bold'), text="Parça ID:", bd=10, width=40, justify='left')
    lblproductID.grid(row=5, column=0)
    txtproductID1=Entry(submitted,bd=10, width=40)
    txtproductID1.grid(row=5, column=1) 
    def submit2():
     c.execute('''INSERT INTO stocks VALUES (:product_name,:product_brand,:product_year,:product_stock,:product_ID)''',
              {
                  'product_name': txtproductname1.get(),
                  'product_brand': txtproductbrand1.get(),
                  'product_year': txtproductyear1.get(),
                  'product_stock':txtproductstock1.get(),
                  'product_ID':txtproductID1.get()
              })
    # Clear the text boxes after inserting data
     txtproductname1.delete(0, END)
     txtproductbrand1.delete(0, END)
     txtproductyear1.delete(0, END)
     txtproductstock1.delete(0, END)
     txtproductID1.delete(0, END)
     con.commit()
     con.close()
     submitted.destroy()

    submitted_btn = Button(submitted, text='Sıfırdan Parça Ekle', command=submit2)
    submitted_btn.grid(row=6, column=1)
    

def query():
    lookup=Tk()
    lookup.geometry("1350x750+0+0")
    con = sqlite3.connect('stock.db')
    c = con.cursor()
    # Parça ID
    lblproductID=Label(lookup,font=('arial', 18, 'bold'), text="Parça ID:", bd=10, width=40, justify='left')
    lblproductID.grid(row=0, column=0)
    txtproductID1=Entry(lookup,bd=10, width=40)
    txtproductID1.grid(row=0, column=1) 
    def query_db():
        con = sqlite3.connect('stock.db')
        c = con.cursor()
        c.execute('''SELECT product_stock FROM stocks WHERE product_ID=?''', (txtproductID1.get(),))
        records = c.fetchall()
        if records:
            result = f"Parça Stoğu: {records[0][0]}"
        else:
            result = "Parça bulunamadı"
        result_label = Label(lookup, text=result, font=('arial', 18, 'bold'), bd=10, width=40, justify='left')
        result_label.grid(row=2, column=0, columnspan=2)
        con.close()
    lookup_btn = Button(lookup, text='Stok Göster', command=query_db)
    lookup_btn.grid(row=1, column=1)
    con.commit()
    con.close()

def search():
    search=Tk()
    search.geometry("1350x750+0+0")
    con = sqlite3.connect('stock.db')
    c = con.cursor()
    # Parça ismi
    lblproductname = Label(search,font=('arial', 18, 'bold'), text="Parça Adı:", bd=10, width=40, justify='left')
    lblproductname.grid(row=0, column=0)
    txtproductname1 = Entry(search,bd=10, width=40)
    txtproductname1.grid(row=0, column=1)
    # Parça markası
    lblproductbrand = Label(search,font=('arial', 18, 'bold'), text="Parça Markası:", bd=10, width=40, justify='left')
    lblproductbrand.grid(row=1, column=0)
    txtproductbrand1 = Entry(search,bd=10, width=40)
    txtproductbrand1.grid(row=1, column=1)
    # Parça yılı
    lblproductyear = Label(search,font=('arial', 18, 'bold'), text="Parça Yılı:", bd=10, width=40, justify='left')
    lblproductyear.grid(row=3, column=0)
    txtproductyear1 = Entry(search,bd=10, width=40)
    txtproductyear1.grid(row=3, column=1)
    def search_db():
           con = sqlite3.connect('stock.db')
           c = con.cursor()
           c.execute('''SELECT product_ID FROM stocks WHERE product_name=? AND product_brand=? AND product_year=?''',
                     (txtproductname1.get(), txtproductbrand1.get(), txtproductyear1.get()))
           records = c.fetchall()
           if records:
               result = f"Parça ID: {records[0][0]}"
           else:
               result = "Parça bulunamadı"
           result_label = Label(search, text=result, font=('arial', 18, 'bold'), bd=10, width=40, justify='left')
           result_label.grid(row=4, column=0, columnspan=2)
           con.close()
    search_btn = Button(search, text='Parça Ara', command=search_db)
    search_btn.grid(row=4, column=1)
    con.commit()
    con.close()

def update():
    editor=Tk()
    editor.geometry("1350x750+0+0")
    con = sqlite3.connect('stock.db')
    c = con.cursor()
    
    # Parça ID
    lblproductID = Label(editor, font=('arial', 18, 'bold'), text="Parça ID:", bd=10, width=40, justify='left')
    lblproductID.grid(row=0, column=0)
    txtproductID = Entry(editor, bd=10, width=40)
    txtproductID.grid(row=0, column=1)
    
    # Parça stoğu
    lblproductstock = Label(editor, font=('arial', 18, 'bold'), text="Yeni Parça Stoğu:", bd=10, width=40, justify='left')
    lblproductstock.grid(row=1, column=0)
    txtproductstock = Entry(editor, bd=10, width=40)
    txtproductstock.grid(row=1, column=1)
    
    def update_db():
        con = sqlite3.connect('stock.db')
        c = con.cursor()
        c.execute('''UPDATE stocks SET product_stock=? WHERE product_ID=?''', (txtproductstock.get(), txtproductID.get()))
        con.commit()
        con.close()
        editor.destroy()
    
    update_btn = Button(editor, text='Stok Güncelle', command=update_db)
    update_btn.grid(row=2, column=1)
    
    con.commit()
    con.close()
# FONKSİYONLAR



# Parça ekleme
submit_btn = Button(root, text='Sıfırdan Parça Ekle', command=submit)
submit_btn.grid(row=40, column=200,padx=100,pady=50)
# Query button 
query_btn = Button(root, text='Stok Gösterimi', command=query)
query_btn.grid(row=30, column=200,padx=100,pady=50)
# Parça arama
search_btn = Button(root, text="Parça ID Öğrenme", command=search)
search_btn.grid(row=50,column=200,padx=100,pady=50)

#parça bilgisi güncelleme
update_btn = Button(root, text="Stok Bilgisi Güncelleme", command=update)
update_btn.grid(row=60, column=200,padx=100,pady=50)

# Commit change
con.commit()
# Close connection
con.close()
root.mainloop()
