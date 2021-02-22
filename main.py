from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as MessageBox
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user= "root", password = "root", database = "Galerie_de_Arta")


master = Tk()
master.geometry("400x450")
master.title("Galerie de arta")


def openNewWindow_Artisti():
    newWindow = Toplevel(master)
    newWindow.title("Artisti")
    newWindow.geometry("450x450")

    cod_artist = Label(newWindow, text='Cod artist', font=('bold',10))
    cod_artist.place(x=20, y=30);

    nume_artist = Label(newWindow, text='Nume artist', font=('bold', 10))
    nume_artist.place(x=20, y=60);

    tara = Label(newWindow, text='Tara', font=('bold', 10))
    tara.place(x=20, y=90);

    data_nastere = Label(newWindow, text='Data nastere', font=('bold', 10))
    data_nastere.place(x=20, y=120);

    data_deces = Label(newWindow, text='Data deces', font=('bold', 10))
    data_deces.place(x=20, y=150);

    entry_cod_artist = Entry(newWindow)
    entry_cod_artist.place(x=150, y=30)

    entry_nume_artist = Entry(newWindow)
    entry_nume_artist.place(x=150, y=60)

    entry_tara = Entry(newWindow)
    entry_tara.place(x=150, y=90)

    entry_data_nastere = Entry(newWindow)
    entry_data_nastere.place(x=150, y=120)

    entry_data_deces = Entry(newWindow)
    entry_data_deces.place(x=150, y=150)

    def insert():
        cod_artist1 = entry_cod_artist.get();
        nume_artist1 = entry_nume_artist.get();
        tara1 = entry_tara.get();
        data_nastere1 = entry_data_nastere.get();
        data_deces1 = entry_data_deces.get();

        if (cod_artist1=="" or nume_artist1=="" or tara1=="" or data_nastere1==""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            #mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()

            cursor.execute("insert into ARTIST values (' "+ cod_artist1 +" ',' "+ nume_artist1+" ',' " + tara1+ " ',' " +data_nastere1 +"','" +data_deces1+"')")
            cursor.execute("commit");

            entry_cod_artist.delete(0, 'end')
            entry_nume_artist.delete(0, 'end')
            entry_tara.delete(0, 'end')
            entry_data_nastere.delete(0, 'end')
            entry_data_deces.delete(0, 'end')
            show()

            MessageBox.showinfo("Insert Status","Inserted Successfully");
            con.close();

    def delete():

        if (entry_cod_artist.get() == ""):
            MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("delete from ARTIST where cod_artist=' "+entry_cod_artist.get()+" '")
            cursor.execute("commit");

            entry_cod_artist.delete(0, 'end')
            entry_nume_artist.delete(0, 'end')
            entry_tara.delete(0, 'end')
            entry_data_nastere.delete(0, 'end')
            entry_data_deces.delete(0, 'end')
            show()

            MessageBox.showinfo("Delete Status", "Deleted Successfully");
            con.close();

    def update():

        cod_artist1 = entry_cod_artist.get();
        nume_artist1 = entry_nume_artist.get();
        tara1 = entry_tara.get();
        data_nastere1 = entry_data_nastere.get();
        data_deces1 = entry_data_deces.get();

        if (cod_artist1=="" or nume_artist1=="" or tara1=="" or data_nastere1=="" or data_deces1==""):
            MessageBox.showinfo("Update Status", "All fields are required")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            #print(nume_artist1)
            cursor.execute(f"update ARTIST set nume_artist='{nume_artist1}', tara='{tara1}', data_nastere='{data_nastere1}', data_deces='{data_deces1}'where cod_artist='{cod_artist1}'")
            cursor.execute("commit");

            entry_cod_artist.delete(0, 'end')
            entry_nume_artist.delete(0, 'end')
            entry_tara.delete(0, 'end')
            entry_data_nastere.delete(0, 'end')
            entry_data_deces.delete(0, 'end')
            show()

            MessageBox.showinfo("Update Status Status", "Updated Successfully");
            con.close();

    def get ():
        entry_nume_artist.delete(0, 'end')
        entry_tara.delete(0, 'end')
        entry_data_nastere.delete(0, 'end')
        entry_data_deces.delete(0, 'end')
        if (entry_cod_artist.get() == ""):
            MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("select * from ARTIST where cod_artist='"+ entry_cod_artist.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                #entry_cod_artist.delete(0, row[1])
                entry_nume_artist.insert(0, row[1])
                entry_tara.insert(0, row[2])
                entry_data_nastere.insert(0, row[3])
                entry_data_deces.insert(0, row[4])

            #MessageBox.showinfo("Fetch Status", "Fetched Successfully");
            con.close();

    def show ():
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from ARTIST")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0]) + '    '+row[1]
            list.insert(list.size()+1, insertData)

    def replaceNull(x):
        if x is None:
            return 0
        else:
            return x

    def ARTIST_sortare_cod_artist ():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from ARTIST order by cod_artist")
        rows = cursor.fetchall()
        show()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[1]
            list1.insert(list1.size() + 1, insertData)

    def ARTIST_sortare_dupa_nume ():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from ARTIST order by nume_artist")
        rows = cursor.fetchall()
        show()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[1]
            list1.insert(list1.size() + 1, insertData)

    def ARTIST_sortare_dupa_tara ():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from ARTIST order by tara")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[2]
            list1.insert(list1.size() + 1, insertData)

    def ARTIST_sortare_dupa_data_nastere ():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from ARTIST order by data_nastere")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[3])
            list1.insert(list1.size() + 1, insertData)

    def ARTIST_sortare_dupa_data_deces ():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from ARTIST order by data_deces")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[4])
            list1.insert(list1.size() + 1, insertData)

    insert = Button(newWindow,text="Insert", command=insert)
    insert.place(x=20, y=200)

    delete = Button(newWindow, text="Delete", command=delete)
    delete.place(x=100, y=200)

    update = Button(newWindow, text="Update", command=update)
    update.place(x=180, y=200)

    get = Button(newWindow, text="Get", command=get)
    get.place(x=260, y=200)

    sort = Button(newWindow, text="Sortare dupa cod arist", command=ARTIST_sortare_cod_artist)
    sort.place(x=280, y=30)

    sort1 = Button(newWindow, text="Sortare dupa nume", command=ARTIST_sortare_dupa_nume)
    sort1.place(x=280, y=60)

    sort2 = Button(newWindow, text="Sortare dupa tara", command=ARTIST_sortare_dupa_tara)
    sort2.place(x=280, y=90)

    sort3 = Button(newWindow, text="Sortare dupa data nastere", command=ARTIST_sortare_dupa_data_nastere)
    sort3.place(x=280, y=120)

    sort4 = Button(newWindow, text="Sortare dupa data deces", command=ARTIST_sortare_dupa_data_deces)
    sort4.place(x=280, y=150)

    list = Listbox(newWindow)
    list.place(x=50, y=250)
    show()

    list1 = Listbox(newWindow)
    list1.place(x=200, y=250)
    show()

    #Label(newWindow, text="Artisti").pack()


def openNewWindow_Clienti():
    newWindow = Toplevel(master)
    newWindow.title("Clienti")
    newWindow.geometry("450x425")

    cod_client = Label(newWindow, text='Cod client', font=('bold', 10))
    cod_client.place(x=20, y=30);

    nume = Label(newWindow, text='Nume', font=('bold', 10))
    nume.place(x=20, y=60);

    prenume = Label(newWindow, text='Prenume', font=('bold', 10))
    prenume.place(x=20, y=90);

    numar_telefon = Label(newWindow, text='Numar telefon', font=('bold', 10))
    numar_telefon.place(x=20, y=120);

    entry_cod_client= Entry(newWindow)
    entry_cod_client.place(x=150, y=30)

    entry_nume = Entry(newWindow)
    entry_nume.place(x=150, y=60)

    entry_prenume = Entry(newWindow)
    entry_prenume.place(x=150, y=90)

    entry_numar_telefon = Entry(newWindow)
    entry_numar_telefon.place(x=150, y=120)

    def insert():
        cod_client1 = entry_cod_client.get();
        nume1 = entry_nume.get();
        prenume1 = entry_prenume.get();
        numar_telefon1 = entry_numar_telefon.get();

        if (cod_client1=="" or nume1=="" or prenume1=="" or numar_telefon1==""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            #mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("insert into CLIENTI values ('"+ cod_client1 +"','"+ nume1+"','" + prenume1 + "','" +numar_telefon1 +"')")
            cursor.execute("commit");

            entry_cod_client.delete(0, 'end')
            entry_nume.delete(0, 'end')
            entry_prenume.delete(0, 'end')
            entry_numar_telefon.delete(0, 'end')
            show()

            MessageBox.showinfo("Insert Status","Inserted Successfully");
            con.close();

    def delete():

        if (entry_cod_client.get() == ""):
            MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("delete from CLIENTI where cod_client=' "+entry_cod_client.get()+" '")
            cursor.execute("commit");

            entry_cod_client.delete(0, 'end')
            entry_nume.delete(0, 'end')
            entry_prenume.delete(0, 'end')
            entry_numar_telefon.delete(0, 'end')
            show()

            MessageBox.showinfo("Delete Status", "Deleted Successfully");
            con.close();

    def update():
        cod_client1 = entry_cod_client.get();
        nume1 = entry_nume.get();
        prenume1 = entry_prenume.get();
        numar_telefon1 = entry_numar_telefon.get();

        if (cod_client1=="" or nume1=="" or prenume1=="" or numar_telefon1==""):
            MessageBox.showinfo("Update Status", "All fields are required")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            #print(nume_artist1)
            cursor.execute(f"update CLIENTI set nume='{nume1}', prenume='{prenume1}', numar_telefon='{numar_telefon1}'where cod_client='{cod_client1}'")
            cursor.execute("commit");

            entry_cod_client.delete(0, 'end')
            entry_nume.delete(0, 'end')
            entry_prenume.delete(0, 'end')
            entry_numar_telefon.delete(0, 'end')
            show()

            MessageBox.showinfo("Update Status Status", "Updated Successfully");
            con.close();

    def get ():
        entry_nume.delete(0, 'end')
        entry_prenume.delete(0, 'end')
        entry_numar_telefon.delete(0, 'end')

        if (entry_cod_client.get() == ""):
            MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("select * from CLIENTI where cod_client='"+ entry_cod_client.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                entry_nume.insert(0, row[1])
                entry_prenume.insert(0, row[2])
                entry_numar_telefon.insert(0, row[3])

            #MessageBox.showinfo("Fetch Status", "Fetched Successfully");
            con.close();

    def show ():
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CLIENTI")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0]) + '    '+row[1]
            list.insert(list.size()+1, insertData)

    def CLIENTI_sortare_cod_client():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CLIENTI order by cod_client")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[1]
            list1.insert(list1.size() + 1, insertData)

    def CLIENTI_sortare_dupa_nume():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CLIENTI order by nume")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[1]
            list1.insert(list1.size() + 1, insertData)

    def CLIENTI_sortare_dupa_prenume():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CLIENTI order by prenume")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[2]
            list1.insert(list1.size() + 1, insertData)

    def CLIENTI_sortare_dupa_telefon():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CLIENTI order by numar_telefon")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[3]
            list1.insert(list1.size() + 1, insertData)

    insert = Button(newWindow, text="Insert", command=insert)
    insert.place(x=20, y=175)

    delete = Button(newWindow, text="Delete", command=delete)
    delete.place(x=100, y=175)

    update = Button(newWindow, text="Update", command=update)
    update.place(x=180, y=175)

    get = Button(newWindow, text="Get", command=get)
    get.place(x=260, y=175)

    sort = Button(newWindow, text="Sortare dupa cod client", command=CLIENTI_sortare_cod_client)
    sort.place(x=280, y=30)

    sort1 = Button(newWindow, text="Sortare dupa nume", command=CLIENTI_sortare_dupa_nume)
    sort1.place(x=280, y=60)

    sort2 = Button(newWindow, text="Sortare dupa prenume", command=CLIENTI_sortare_dupa_prenume)
    sort2.place(x=280, y=90)

    sort3 = Button(newWindow, text="Sortare dupa telefon", command=CLIENTI_sortare_dupa_telefon)
    sort3.place(x=280, y=120)

    list = Listbox(newWindow)
    list.place(x=50, y=225)
    show()

    list1 = Listbox(newWindow)
    list1.place(x=200, y=225)
    show()

    #Label(newWindow, text="Clienti").pack()

def openNewWindow_Cumparare():
    newWindow = Toplevel(master)
    newWindow.title("Cumparare")
    newWindow.geometry("450x450")

    cod_bon = Label(newWindow, text='Cod bon', font=('bold', 10))
    cod_bon.place(x=20, y=30);

    cod_client = Label(newWindow, text='Cod client', font=('bold', 10))
    cod_client.place(x=20, y=60);

    cod_met_plata = Label(newWindow, text='Cod metoda plata', font=('bold', 10))
    cod_met_plata.place(x=20, y=90);

    pret_cumparare = Label(newWindow, text='Pret cumparare', font=('bold', 10))
    pret_cumparare.place(x=20, y=120);

    data_cumparare = Label(newWindow, text='Data cumparare', font=('bold', 10))
    data_cumparare.place(x=20, y=150);

    entry_cod_bon = Entry(newWindow)
    entry_cod_bon.place(x=150, y=30)

    entry_cod_client = Entry(newWindow)
    entry_cod_client.place(x=150, y=60)

    entry_cod_met_plata = Entry(newWindow)
    entry_cod_met_plata.place(x=150, y=90)

    entry_pret_cumparare = Entry(newWindow)
    entry_pret_cumparare.place(x=150, y=120)

    entry_data_cumparare = Entry(newWindow)
    entry_data_cumparare.place(x=150, y=150)

    def insert():
        cod_bon1 = entry_cod_bon.get();
        cod_client1 = entry_cod_client.get();
        cod_met_plata1 = entry_cod_met_plata.get();
        pret_cumparare1 = entry_pret_cumparare.get();
        data_cumparare1 = entry_data_cumparare.get();

        if (cod_bon1=="" or cod_client1=="" or cod_met_plata1=="" or pret_cumparare1=="" or data_cumparare1==""):
            MessageBox.showinfo("Insert Status", "All fields are required")
        else:
            #mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("insert into CUMPARARE values (' "+cod_bon1+" ',' "+cod_client1+" ',' "+cod_met_plata1+" ',' "+pret_cumparare1+" ',' "+data_cumparare1+" ')")
            cursor.execute("commit");

            entry_cod_bon.delete(0, 'end')
            entry_cod_client.delete(0, 'end')
            entry_cod_met_plata.delete(0, 'end')
            entry_pret_cumparare.delete(0, 'end')
            entry_data_cumparare.delete(0, 'end')
            show()

            MessageBox.showinfo("Insert Status","Inserted Successfully");
            con.close();

    def delete():

        if (entry_cod_bon.get() == ""):
            MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("delete from CUMPARARE where cod_bon=' "+entry_cod_bon.get()+" '")
            cursor.execute("commit");

            entry_cod_bon.delete(0, 'end')
            entry_cod_client.delete(0, 'end')
            entry_cod_met_plata.delete(0, 'end')
            entry_pret_cumparare.delete(0, 'end')
            entry_data_cumparare.delete(0, 'end')
            show()

            MessageBox.showinfo("Delete Status", "Deleted Successfully");
            con.close();

    def update():
        cod_bon1 = entry_cod_bon.get();
        cod_client1 = entry_cod_client.get();
        cod_met_plata1 = entry_cod_met_plata.get();
        pret_cumparare1 = entry_pret_cumparare.get();
        data_cumparare1 = entry_data_cumparare.get();

        if (cod_bon1=="" or cod_client1=="" or cod_met_plata1=="" or pret_cumparare1=="" or data_cumparare1==""):
            MessageBox.showinfo("Update Status", "All fields are required")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute(f"update CUMPARARE set cod_client='{cod_client1}', cod_met_plata='{cod_met_plata1}', pret_cumparare='{pret_cumparare1}', data_cumparare='{data_cumparare1}' where cod_bon='{cod_bon1}'")
            cursor.execute("commit");

            entry_cod_bon.delete(0, 'end')
            entry_cod_client.delete(0, 'end')
            entry_cod_met_plata.delete(0, 'end')
            entry_pret_cumparare.delete(0, 'end')
            entry_data_cumparare.delete(0, 'end')
            show()

            MessageBox.showinfo("Update Status Status", "Updated Successfully");
            con.close();

    def get ():

        entry_cod_client.delete(0, 'end')
        entry_cod_met_plata.delete(0, 'end')
        entry_pret_cumparare.delete(0, 'end')
        entry_data_cumparare.delete(0, 'end')

        if (entry_cod_bon.get() == ""):
            MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("select * from CUMPARARE where cod_bon='"+ entry_cod_bon.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                entry_cod_client.insert(0, row[1])
                entry_cod_met_plata.insert(0, row[2])
                entry_pret_cumparare.insert(0, row[3])
                entry_data_cumparare.insert(0, row[4])

            #MessageBox.showinfo("Fetch Status", "Fetched Successfully");
            con.close();

    def show ():
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CUMPARARE")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0]) + '    '+str(row[1])+'   '+str(row[3])
            list.insert(list.size()+1, insertData)

    def CUMPARARE_sortare_cod_bon():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CUMPARARE order by cod_bon")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[1])
            list1.insert(list1.size() + 1, insertData)

    def CUMPARARE_sortare_cod_client():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CUMPARARE order by cod_client")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[1])
            list1.insert(list1.size() + 1, insertData)

    def CUMPARARE_sortare_cod_met_plata():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CUMPARARE order by cod_met_plata")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[2])
            list1.insert(list1.size() + 1, insertData)

    def CUMPARARE_sortare_pret_cumparare():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CUMPARARE order by pret_cumparare")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[3])
            list1.insert(list1.size() + 1, insertData)

    def CUMPARARE_sortare_data_cumparare():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CUMPARARE order by data_cumparare")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[4])
            list1.insert(list1.size() + 1, insertData)

    insert = Button(newWindow, text="Insert", command=insert)
    insert.place(x=20, y=200)

    delete = Button(newWindow, text="Delete", command=delete)
    delete.place(x=100, y=200)

    update = Button(newWindow, text="Update", command=update)
    update.place(x=180, y=200)

    get = Button(newWindow, text="Get", command=get)
    get.place(x=260, y=200)

    sort = Button(newWindow, text="Sortare dupa cod bon", command=CUMPARARE_sortare_cod_bon)
    sort.place(x=280, y=30)

    sort1 = Button(newWindow, text="Sortare dupa client", command=CUMPARARE_sortare_cod_client)
    sort1.place(x=280, y=60)

    sort2 = Button(newWindow, text="Sortare dupa met plata", command=CUMPARARE_sortare_cod_met_plata)
    sort2.place(x=280, y=90)

    sort3 = Button(newWindow, text="Sortare dupa pret", command=CUMPARARE_sortare_pret_cumparare)
    sort3.place(x=280, y=120)

    sort4 = Button(newWindow, text="Sortare dupa data", command=CUMPARARE_sortare_data_cumparare)
    sort4.place(x=280, y=150)

    list = Listbox(newWindow)
    list.place(x=50, y=250)
    show()

    list1 = Listbox(newWindow)
    list1.place(x=200, y=250)
    show()

    #Label(newWindow, text="Cumparare").pack()

def openNewWindow_Curent():
    newWindow = Toplevel(master)
    newWindow.title("Curent")
    newWindow.geometry("450x350")

    cod_curent = Label(newWindow, text='Cod curent', font=('bold', 10))
    cod_curent.place(x=20, y=30);

    nume_curent = Label(newWindow, text='Nume curent', font=('bold', 10))
    nume_curent.place(x=20, y=60);

    entry_cod_curent = Entry(newWindow)
    entry_cod_curent.place(x=150, y=30)

    entry_nume_curent = Entry(newWindow)
    entry_nume_curent.place(x=150, y=60)

    def insert():
        cod_curent1 = entry_cod_curent.get();
        nume_curent1 = entry_nume_curent.get();

        if (cod_curent1=="" or nume_curent1==""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            #mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("insert into CURENT values ('"+ cod_curent1 +"','"+ nume_curent1+"')")
            cursor.execute("commit");

            entry_cod_curent.delete(0, 'end')
            entry_nume_curent.delete(0, 'end')
            show()

            MessageBox.showinfo("Insert Status","Inserted Successfully");
            con.close();

    def delete():

        if (entry_cod_curent.get()==""):
            MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            print ("SET FOREIGN_KEY_CHECKS=0; delete from CURENT where cod_curent="+entry_cod_curent.get()+"")
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute("delete from CURENT where cod_curent="+entry_cod_curent.get()+";")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_curent.delete(0, 'end')
            entry_nume_curent.delete(0, 'end')
            show()

            MessageBox.showinfo("Delete Status", "Deleted Successfully");
            con.close();

    def update():
        cod_curent1 = entry_cod_curent.get();
        nume_curent1 = entry_nume_curent.get();

        if (cod_curent1 == "" or nume_curent1 == ""):
            MessageBox.showinfo("Update Status", "All fields are required")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(f"update CURENT set nume_curent='{nume_curent1}' where cod_curent='{cod_curent1}';")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_curent.delete(0, 'end')
            entry_nume_curent.delete(0, 'end')
            show()

            MessageBox.showinfo("Update Status Status", "Updated Successfully");
            con.close();

    def get ():
        entry_nume_curent.delete(0, 'end')
        if (entry_cod_curent.get() == ""):
            MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("select * from CURENT where cod_curent='"+ entry_cod_curent.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                entry_nume_curent.insert(0, row[1])


            #MessageBox.showinfo("Fetch Status", "Fetched Successfully");
            con.close();

    def show ():
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CURENT")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0]) + '    '+row[1]
            list.insert(list.size()+1, insertData)

    def CURENT_sortare_cod_curent():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CURENT order by cod_curent")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[1])
            list1.insert(list1.size() + 1, insertData)

    def CURENT_sortare_nume_curent():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from CURENT order by nume_curent")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[1])
            list1.insert(list1.size() + 1, insertData)

    insert = Button(newWindow, text="Insert", command=insert)
    insert.place(x=20, y=100)

    delete = Button(newWindow, text="Delete", command=delete)
    delete.place(x=100, y=100)

    update = Button(newWindow, text="Update", command=update)
    update.place(x=180, y=100)

    get = Button(newWindow, text="Get", command=get)
    get.place(x=260, y=100)

    sort = Button(newWindow, text="Sortare dupa cod curent", command=CURENT_sortare_cod_curent)
    sort.place(x=280, y=30)

    sort1 = Button(newWindow, text="Sortare dupa nume curent", command=CURENT_sortare_nume_curent)
    sort1.place(x=280, y=60)

    list = Listbox(newWindow)
    list.place(x=50, y=150)
    show()

    list1 = Listbox(newWindow)
    list1.place(x=200, y=150)
    show()
    #Label(newWindow, text="Curent").pack()

def openNewWindow_Galerie():
    newWindow = Toplevel(master)
    newWindow.title("Galerie")
    newWindow.geometry("450x375")

    cod_galerie = Label(newWindow, text='Cod galerie', font=('bold', 10))
    cod_galerie.place(x=20, y=30);

    nume_galerie = Label(newWindow, text='Nume galerie', font=('bold', 10))
    nume_galerie.place(x=20, y=60);

    telefon = Label(newWindow, text='Telefon', font=('bold', 10))
    telefon.place(x=20, y=90);

    entry_cod_galerie = Entry(newWindow)
    entry_cod_galerie.place(x=150, y=30)

    entry_nume_galerie = Entry(newWindow)
    entry_nume_galerie.place(x=150, y=60)

    entry_telefon = Entry(newWindow)
    entry_telefon.place(x=150, y=90)

    def insert():
        cod_galerie1 = entry_cod_galerie.get();
        nume_galerie1 = entry_nume_galerie.get();
        telefon1 = entry_telefon.get();


        if (cod_galerie1=="" or nume_galerie1=="" or telefon1==""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            #mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("insert into GALERIE values ('"+ cod_galerie1 +"','"+ nume_galerie1+"','" + telefon1 + "')")
            cursor.execute("commit");

            entry_cod_galerie.delete(0, 'end')
            entry_nume_galerie.delete(0, 'end')
            entry_telefon.delete(0, 'end')
            show()


            MessageBox.showinfo("Insert Status","Inserted Successfully");
            con.close();

    def delete():

        if (entry_cod_galerie.get()==""):
            MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            print ("SET FOREIGN_KEY_CHECKS=0; delete from GALERIE where cod_galerie="+entry_cod_galerie.get()+"")
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute("delete from GALERIE where cod_galerie="+entry_cod_galerie.get()+";")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_galerie.delete(0, 'end')
            entry_nume_galerie.delete(0, 'end')
            entry_telefon.delete(0, 'end')
            show()

            MessageBox.showinfo("Delete Status", "Deleted Successfully");
            con.close();

    def update():
        cod_galerie1 = entry_cod_galerie.get();
        nume_galerie1 = entry_nume_galerie.get();
        telefon1 = entry_telefon.get();

        if (cod_galerie1 == "" or nume_galerie1 == "" or telefon1 == ""):
            MessageBox.showinfo("Update Status", "All fields are required")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(f"update GALERIE set nume_galerie='{nume_galerie1}', telefon = '{telefon1}' where cod_galerie='{cod_galerie1}';")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_galerie.delete(0, 'end')
            entry_nume_galerie.delete(0, 'end')
            entry_telefon.delete(0, 'end')
            show()

            MessageBox.showinfo("Update Status Status", "Updated Successfully");
            con.close();
    def get ():
        entry_nume_galerie.delete(0, 'end')
        entry_telefon.delete(0, 'end')
        if (entry_cod_galerie.get() == ""):
            MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("select * from GALERIE where cod_galerie='"+ entry_cod_galerie.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                entry_nume_galerie.insert(0, row[1])
                entry_telefon.insert(0, row[2])


            #MessageBox.showinfo("Fetch Status", "Fetched Successfully");
            con.close();

    def show ():
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from GALERIE")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0]) + '    '+row[1]
            list.insert(list.size()+1, insertData)

    def GALERIE_sortare_cod_galerie():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from GALERIE order by cod_galerie")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[1]
            list1.insert(list1.size() + 1, insertData)

    def GALERIE_sortare_nume_galerie():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from GALERIE order by nume_galerie")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[1]
            list1.insert(list1.size() + 1, insertData)

    def GALERIE_sortare_telefon():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from GALERIE order by telefon")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[2])
            list1.insert(list1.size() + 1, insertData)


    insert = Button(newWindow, text="Insert", command=insert)
    insert.place(x=20, y=125)

    delete = Button(newWindow, text="Delete", command=delete)
    delete.place(x=100, y=125)

    update = Button(newWindow, text="Update", command=update)
    update.place(x=180, y=125)

    get = Button(newWindow, text="Get", command=get)
    get.place(x=260, y=125)

    sort = Button(newWindow, text="Sortare dupa cod galerie", command=GALERIE_sortare_cod_galerie)
    sort.place(x=280, y=30)

    sort1 = Button(newWindow, text="Sortare dupa nume galerie", command=GALERIE_sortare_nume_galerie)
    sort1.place(x=280, y=60)

    sort2 = Button(newWindow, text="Sortare dupa telefon", command=GALERIE_sortare_telefon)
    sort2.place(x=280, y=90)

    list = Listbox(newWindow)
    list.place(x=50, y=175)
    show()

    list1 = Listbox(newWindow)
    list1.place(x=200, y=175)
    show()

    #Label(newWindow, text="Galerie").pack()

def openNewWindow_Metoda_Plata():
    newWindow = Toplevel(master)
    newWindow.title("Metoda de Plata")
    newWindow.geometry("475x350")

    cod_met_plata = Label(newWindow, text='Cod metoda plata', font=('bold', 10))
    cod_met_plata.place(x=20, y=30);

    metoda_plata = Label(newWindow, text='Metoda plata', font=('bold', 10))
    metoda_plata.place(x=20, y=60);

    entry_cod_met_plata = Entry(newWindow)
    entry_cod_met_plata.place(x=150, y=30)

    entry_metoda_plata = Entry(newWindow)
    entry_metoda_plata.place(x=150, y=60)

    def insert():
        cod_met_plata1 = entry_cod_met_plata.get();
        metoda_plata1 = entry_metoda_plata.get();


        if (cod_met_plata1=="" or metoda_plata1==""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            #mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("insert into METODA_PLATA values ('"+ cod_met_plata1 +"','"+ metoda_plata1+"')")
            cursor.execute("commit");

            entry_cod_met_plata.delete(0, 'end')
            entry_metoda_plata.delete(0, 'end')
            show()

            MessageBox.showinfo("Insert Status","Inserted Successfully");
            con.close();

    def delete():

        if (entry_cod_met_plata.get() == ""):
            MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            print("SET FOREIGN_KEY_CHECKS=0; delete from METODA_PLATA where cod_met_plata=" + entry_cod_met_plata.get() + "")
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute("delete from METODA_PLATA where cod_met_plata=" + entry_cod_met_plata.get() + ";")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_met_plata.delete(0, 'end')
            entry_metoda_plata.delete(0, 'end')
            show()

            MessageBox.showinfo("Delete Status", "Deleted Successfully");
            con.close();

    def update():
        cod_met_plata1 = entry_cod_met_plata.get();
        metoda_plata1 = entry_metoda_plata.get();

        if (cod_met_plata1 == "" or metoda_plata1 == ""):
            MessageBox.showinfo("Update Status", "All fields are required")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(f"update METODA_PLATA set metoda_plata='{metoda_plata1}' where cod_met_plata='{cod_met_plata1}';")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_met_plata.delete(0, 'end')
            entry_metoda_plata.delete(0, 'end')
            show()

            MessageBox.showinfo("Update Status Status", "Updated Successfully");
            con.close();

    def get ():
        entry_metoda_plata.delete(0, 'end')
        if (entry_cod_met_plata.get() == ""):
            MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("select * from METODA_PLATA where cod_met_plata='"+ entry_cod_met_plata.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                entry_metoda_plata.insert(0, row[1])


            #MessageBox.showinfo("Fetch Status", "Fetched Successfully");
            con.close();

    def show ():
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from METODA_PLATA")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0]) + '    '+row[1]
            list.insert(list.size()+1, insertData)

    def PLATA_sortare_cod_met_plata():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from METODA_PLATA order by cod_met_plata")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[1])
            list1.insert(list1.size() + 1, insertData)

    def PLATA_sortare_met_plata():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from METODA_PLATA order by metoda_plata")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[1])
            list1.insert(list1.size() + 1, insertData)

    insert = Button(newWindow, text="Insert", command=insert)
    insert.place(x=20, y=100)

    delete = Button(newWindow, text="Delete", command=delete)
    delete.place(x=100, y=100)

    update = Button(newWindow, text="Update", command=update)
    update.place(x=180, y=100)

    get = Button(newWindow, text="Get", command=get)
    get.place(x=260, y=100)

    sort = Button(newWindow, text="Sortare dupa cod metoda plata", command=PLATA_sortare_cod_met_plata)
    sort.place(x=280, y=30)

    sort1 = Button(newWindow, text="Sortare dupa metoda plata", command=PLATA_sortare_met_plata)
    sort1.place(x=280, y=60)

    list = Listbox(newWindow)
    list.place(x=50, y=150)
    show()

    list1 = Listbox(newWindow)
    list1.place(x=200, y=150)
    show()
    #Label(newWindow, text="Metoda de Plata").pack()

def openNewWindow_Pictura():
    newWindow = Toplevel(master)
    newWindow.title("Pictura")
    newWindow.geometry("450x500")

    cod_pictura = Label(newWindow, text='Cod pictura', font=('bold', 10))
    cod_pictura.place(x=20, y=30);

    cod_artist = Label(newWindow, text='Cod artist', font=('bold', 10))
    cod_artist.place(x=20, y=60);

    cod_galerie = Label(newWindow, text='Cod galerie', font=('bold', 10))
    cod_galerie.place(x=20, y=90);

    cod_curent = Label(newWindow, text='Cod curent', font=('bold', 10))
    cod_curent.place(x=20, y=120);

    cod_bon = Label(newWindow, text='Cod bon', font=('bold', 10))
    cod_bon.place(x=20, y=150);

    titlu = Label(newWindow, text='Titlu', font=('bold', 10))
    titlu.place(x=20, y=180);

    pret_vanzare = Label(newWindow, text='Pret vanzare', font=('bold', 10))
    pret_vanzare.place(x=20, y=210);

    entry_cod_pictura = Entry(newWindow)
    entry_cod_pictura.place(x=150, y=30)

    entry_cod_artist = Entry(newWindow)
    entry_cod_artist.place(x=150, y=60)

    entry_cod_galerie = Entry(newWindow)
    entry_cod_galerie.place(x=150, y=90)

    entry_cod_curent = Entry(newWindow)
    entry_cod_curent.place(x=150, y=120)

    entry_cod_bon = Entry(newWindow)
    entry_cod_bon.place(x=150, y=150)

    entry_titlu= Entry(newWindow)
    entry_titlu.place(x=150, y=180)

    entry_pret_vanzare = Entry(newWindow)
    entry_pret_vanzare.place(x=150, y=210)

    def insert():
        cod_pictura1 = entry_cod_pictura.get();
        cod_artist1 = entry_cod_artist.get();
        cod_galerie1 = entry_cod_galerie.get();
        cod_curent1 = entry_cod_curent.get();
        cod_bon1 = entry_cod_bon.get();
        titlu1 = entry_titlu.get();
        pret_vanzare1 = entry_pret_vanzare.get();

        if (cod_pictura1=="" or cod_artist1=="" or cod_galerie1=="" or cod_curent1=="" or cod_bon1=="" or titlu1=="" or pret_vanzare1==""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            #mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute("insert into PICTURA values (' "+cod_pictura1+" ',' "+cod_artist1+" ',' "+cod_galerie1+" ',' "+cod_curent1+" ',' "+cod_bon1+" ',' "+titlu1+" ',' "+pret_vanzare1+" ')")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_pictura.delete(0, 'end')
            entry_cod_artist.delete(0, 'end')
            entry_cod_galerie.delete(0, 'end')
            entry_cod_curent.delete(0, 'end')
            entry_cod_bon.delete(0, 'end')
            entry_titlu.delete(0, 'end')
            entry_pret_vanzare.delete(0, 'end')
            show()

            MessageBox.showinfo("Insert Status","Inserted Successfully");
            con.close();
    def delete():

        if (entry_cod_pictura.get() == ""):
            MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            #print("SET FOREIGN_KEY_CHECKS=0; delete from PICTURA where cod_pictura=" + entry_cod_pictura.get() + "")
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute("delete from PICTURA where cod_pictura=" + entry_cod_pictura.get() + ";")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_pictura.delete(0, 'end')
            entry_cod_artist.delete(0, 'end')
            entry_cod_galerie.delete(0, 'end')
            entry_cod_curent.delete(0, 'end')
            entry_cod_bon.delete(0, 'end')
            entry_titlu.delete(0, 'end')
            entry_pret_vanzare.delete(0, 'end')
            show()

            MessageBox.showinfo("Delete Status", "Deleted Successfully");
            con.close();

    def update():

        cod_pictura1 = entry_cod_pictura.get();
        cod_artist1 = entry_cod_artist.get();
        cod_galerie1 = entry_cod_galerie.get();
        cod_curent1 = entry_cod_curent.get();
        cod_bon1 = entry_cod_bon.get();
        titlu1 = entry_titlu.get();
        pret_vanzare1 = entry_pret_vanzare.get();

        if (cod_pictura1 == "" or cod_artist1 == "" or cod_galerie1 == "" or cod_curent1 == "" or cod_bon1 == "" or titlu1 == "" or pret_vanzare1 == ""):
            MessageBox.showinfo("Update Status", "All fields are required")
        else:
            # mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(f"update PICTURA set cod_pictura ='{cod_pictura1}', cod_artist = '{cod_artist1}', cod_galerie = '{cod_galerie1}', cod_curent = '{cod_curent1}', cod_bon = '{cod_bon1}', titlu = '{titlu1}', pret_vanzare = '{pret_vanzare1}' where cod_pictura='{cod_pictura1}';")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
            cursor.execute("commit");

            entry_cod_pictura.delete(0, 'end')
            entry_cod_artist.delete(0, 'end')
            entry_cod_galerie.delete(0, 'end')
            entry_cod_curent.delete(0, 'end')
            entry_cod_bon.delete(0, 'end')
            entry_titlu.delete(0, 'end')
            entry_pret_vanzare.delete(0, 'end')
            show()

            MessageBox.showinfo("Update Status Status", "Updated Successfully");
            con.close();

    def get():

        entry_cod_artist.delete(0, 'end')
        entry_cod_galerie.delete(0, 'end')
        entry_cod_curent.delete(0, 'end')
        entry_cod_bon.delete(0, 'end')
        entry_titlu.delete(0, 'end')
        entry_pret_vanzare.delete(0, 'end')

        if (entry_cod_pictura.get() == ""):
            MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
            cursor = con.cursor()
            cursor.execute("select * from PICTURA where cod_pictura='"+ entry_cod_pictura.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                entry_cod_artist.insert(0, row[1])
                entry_cod_galerie.insert(0, row[2])
                entry_cod_curent.insert(0, row[3])
                entry_cod_bon.insert(0, str(row[4]))
                entry_titlu.insert(0, row[5])
                entry_pret_vanzare.insert(0, row[6])


            #MessageBox.showinfo("Fetch Status", "Fetched Successfully");
            con.close();

    def show():
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from PICTURA")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0]) + '    '+str(row[1])+ '    '+row[5]
            list.insert(list.size()+1, insertData)

    def PICTURA_sortare_cod_pictura():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from PICTURA order by cod_pictura")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[1])
            list1.insert(list1.size() + 1, insertData)

    def PICTURA_sortare_cod_artist():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from PICTURA order by cod_artist")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[1])
            list1.insert(list1.size() + 1, insertData)

    def PICTURA_sortare_cod_galerie():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from PICTURA order by cod_galerie")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[2])
            list1.insert(list1.size() + 1, insertData)

    def PICTURA_sortare_cod_curent():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from PICTURA order by cod_curent")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[3])
            list1.insert(list1.size() + 1, insertData)

    def PICTURA_sortare_cod_bon():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from PICTURA order by cod_bon")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[4])
            list1.insert(list1.size() + 1, insertData)

    def PICTURA_sortare_titlu():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from PICTURA order by titlu")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + row[5]
            list1.insert(list1.size() + 1, insertData)

    def PICTURA_sortare_pret_vanzare():
        list1.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select * from PICTURA order by pret_vanzare")
        rows = cursor.fetchall()

        for row in rows:
            insertData = str(row[0]) + '    ' + str(row[5])
            list1.insert(list1.size() + 1, insertData)


    insert = Button(newWindow, text="Insert", command=insert)
    insert.place(x=20, y=250)

    delete = Button(newWindow, text="Delete", command=delete)
    delete.place(x=100, y=250)

    update = Button(newWindow, text="Update", command=update)
    update.place(x=180, y=250)

    get = Button(newWindow, text="Get", command=get)
    get.place(x=260, y=250)

    sort = Button(newWindow, text="Sortare dupa cod pictura ", command=PICTURA_sortare_cod_pictura)
    sort.place(x=280, y=30)

    sort1 = Button(newWindow, text="Sortare dupa cod artist ", command=PICTURA_sortare_cod_artist)
    sort1.place(x=280, y=60)

    sort2 = Button(newWindow, text="Sortare dupa cod galerie ", command=PICTURA_sortare_cod_galerie)
    sort2.place(x=280, y=90)

    sort3 = Button(newWindow, text="Sortare dupa cod curent ", command=PICTURA_sortare_cod_curent)
    sort3.place(x=280, y=120)

    sort4 = Button(newWindow, text="Sortare dupa cod bon ", command=PICTURA_sortare_cod_bon)
    sort4.place(x=280, y=150)

    sort5 = Button(newWindow, text="Sortare dupa titlu ", command=PICTURA_sortare_titlu)
    sort5.place(x=280, y=180)

    sort6 = Button(newWindow, text="Sortare dupa pret vanzare", command=PICTURA_sortare_pret_vanzare)
    sort6.place(x=280, y=210)

    list = Listbox(newWindow)
    list.place(x=50, y=300)
    show()

    list1 = Listbox(newWindow)
    list1.place(x=200, y=300)
    show()
    #Label(newWindow, text="Pictura").pack()


def openNewWindow_Subpunctul_c():

    newWindow = Toplevel(master)
    newWindow.title("Subpunctul c)")
    newWindow.geometry("375x350")

    cerinta = Label(newWindow, text='c) Sa se afiseze codul bonurilor si codul clientilor care', font=('bold', 10))
    cerinta.place(x=20, y=30);

    cerinta = Label(newWindow, text='au achizitionat o pictura avand pretul de cumparare > 76000', font=('bold', 10))
    cerinta.place(x=20, y=60);

    cerinta = Label(newWindow, text='si care se afla in galeria 303', font=('bold', 10))
    cerinta.place(x=20, y=90);



    def show ():
        list.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select cod_client, cod_bon, pret_cumparare from clienti join cumparare using (cod_client) join pictura using (cod_bon) where pret_cumparare>76000 and cod_galerie=303;")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0])+'    '+str(row[1])+ '   '+str(row[2])
            list.insert(list.size()+1, insertData)

    list = Listbox(newWindow)
    list.place(x=25, y=150)
    show()

def openNewWindow_Subpunctul_d():

    newWindow = Toplevel(master)
    newWindow.title("Subpunctul d)")
    newWindow.geometry("350x350")

    cerinta = Label(newWindow, text='d) Pentru galeriile in care pretul picturilor de vanzare', font=('bold', 10))
    cerinta.place(x=20, y=30);

    cerinta = Label(newWindow, text='depaseste 500000, sa se obtina codul, numele picturilor', font=('bold', 10))
    cerinta.place(x=20, y=60);

    cerinta = Label(newWindow, text='si pretul maxim pe galerie', font=('bold', 10))
    cerinta.place(x=20, y=90);

    def show ():
        list.delete(0, END)
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="Galerie_de_Arta")
        cursor = con.cursor()
        cursor.execute("select cod_galerie, titlu, max(pret_vanzare) from pictura join galerie using (cod_galerie) group by cod_galerie, titlu having max(pret_vanzare)>500000000 order by max(pret_vanzare) desc;;")
        rows = cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData = str(row[0]) + '    '+str(row[1])+ '   '+str(row[2])
            list.insert(list.size()+1, insertData)

    list = Listbox(newWindow)
    list.place(x=25, y=150)
    show()

label = Label(master, text="Galerie de Arta")
label.pack(pady=10)

btn1 = Button(master, text="Artisti", command=openNewWindow_Artisti)
btn1.pack(pady=10)

btn2 = Button(master, text="Clienti", command=openNewWindow_Clienti)
btn2.pack(pady=10)

btn3 = Button(master, text="Cumparare", command=openNewWindow_Cumparare)
btn3.pack(pady=10)

btn4 = Button(master, text="Curent", command=openNewWindow_Curent)
btn4.pack(pady=10)

btn5 = Button(master, text="Galerie", command=openNewWindow_Galerie)
btn5.pack(pady=10)

btn6 = Button(master, text="Metoda de Plata", command=openNewWindow_Metoda_Plata)
btn6.pack(pady=10)

btn7 = Button(master, text="Pictura", command=openNewWindow_Pictura)
btn7.pack(pady=10)




btn8 = Button(master, text="Subpunctul c)", command=openNewWindow_Subpunctul_c)
btn8.pack(pady=10)

btn9 = Button(master, text="Subpunctul d)", command=openNewWindow_Subpunctul_d)
btn9.pack(pady=10)


mainloop() 