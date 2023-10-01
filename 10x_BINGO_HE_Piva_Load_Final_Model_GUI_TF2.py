import numpy as np
from numpy import loadtxt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from tkinter import Tk, Frame, Label, Radiobutton, Button, Entry, IntVar, messagebox, END

# predvidjanje ugiba
def predict():
    KA = ent_sila.get()
    T = ent_EMIP.get()
    NPV = ent_EMIO.get()
    #fundiranje = selected1.get()
    #raspon = ent_raspon.get()
    #tehnologija = selected2.get()
    
    # provera da li su unete sve vrednosti
    if (KA == ''):
        messagebox.showwarning('Upozorenje!', 'Niste uneli kotu akumulacije')
        ent_KA.focus()
    elif (T == ''):
        messagebox.showwarning('Upozorenje!', 'Niste uneli temperaturu')
        ent_T.focus()
    elif (NPV == ''):
        messagebox.showwarning('Upozorenje!', 'Niste uneli nivo podzemnih voda')
        ent_NPV.focus()
    #elif (raspon == ''):
        #messagebox.showwarning('Upozorenje!', 'Niste uneli raspon mosta')
        #ent_raspon.focus()
        
    # provera da li su unete vrednosti brojevi
    else:
        try:
            KA = float(KA)
        except ValueError:
            messagebox.showwarning('Upozorenje!', 'Uneli ste pogresnu vrednost za kotu akumulacije')
            ent_KA.focus()
        try:
            T = float(T)
        except ValueError:
            messagebox.showwarning('Upozorenje!', 'Uneli ste pogresnu vrednost za temperaturu')
            ent_T.focus()
        try:
             NPV = float(NPV)
        except ValueError:
            messagebox.showwarning('Upozorenje!', 'Uneli ste pogresnu vrednost za nivo podzemnih voda')
            ent_NPV.focus()
        #try:
            #raspon = float(raspon)
        #except ValueError:
            #messagebox.showwarning('Upozorenje!', 'Uneli ste pogresnu vrednost za raspon mosta')
            #ent_raspon.focus()
        
        # ukoliko su sve unete vrednosti ispravne, vrsi se predvidjanje
        #fundiranje = float(fundiranje)
        #tehnologija = float(tehnologija)
    
        # uneti niz
        user_input = np.array ([[KA, T, NPV]])
        
        # transformacija unetih vrednosti - skaliranje
        user_input_rescaled = scaler.transform(user_input.astype(np.float))
            
        # predvidjanje na osnovu unetih vrednosti
        prediction = model_loaded.predict(user_input_rescaled)
                
        # obrnuta transformacija predvidjenog ugiba
        inverse_prediction = prediction * maxDisplacement
        
        # pretvaranje rezultata u string        
        pomeranje = str(round(float(inverse_prediction), 2))
        
        # osvezavanje polja za rezultat
        lbl_rezultat.configure(text = "Predvidjeno pomeranje: " + pomeranje + " cm")
    

# brisanje unetih podataka
def erase():
    ent_sila.delete(0, END)
    ent_EMIP.delete(0, END)
    ent_EMIO.delete(0, END)
    #ent_raspon.delete(0, END)
    #fund_rad1.select()
    #tehn_rad1.select()
    lbl_rezultat.configure(text = "Predvidjeno pomeranje: ____ cm")
    

########################################
###### PROZOR GLAVNOG PROGRAMA #########
########################################

window = Tk()
window.title('Greda')
window.resizable(width="no", height="no")
window.minsize(width=700, height=600)
window.maxsize(width=1000, height=700)

frame_naslov = Frame(window)
frame_parametri = Frame(window, borderwidth="1", relief="ridge")
frame_dugme = Frame(window)
frame_rezultat = Frame(window, borderwidth="1", relief="ridge")

frame_naslov.grid(row=0, column=0, padx=20)
frame_parametri.grid(row=1, column=0, padx=20)
frame_dugme.grid(row=2, column=0, padx=20)
frame_rezultat.grid(row=3, column=0, padx=20)

# naslovni tekst
lbl_naslov = Label(frame_naslov, text='Za predvidjanje radijalnog pomeranja unesite trazene parametre i kliknite na dugme "Predvidi":')    
lbl_naslov.grid(row=0, column=0, sticky="EW", pady=20)

#razmak
lbl_razmak = Label(frame_parametri, text='', width=5, height=1).grid(row=0, column=0)

# sila
lbl_sila = Label(frame_parametri, text="KA (m): ", width=20, height=3)
lbl_sila.grid(row=1, column=0, sticky="W", padx=10)
ent_sila = Entry(frame_parametri, width=5)
ent_sila.grid(row=1, column=1, sticky="EW")
ent_sila.focus()

# EMI polje
lbl_EMIP = Label(frame_parametri, text="T (C): ", width=19, height=3)
lbl_EMIP.grid(row=2, column=0, sticky="W", padx=10)
ent_EMIP = Entry(frame_parametri, width=5)
ent_EMIP.grid(row=2, column=1, sticky="EW")

# EMI oslonaca
lbl_EMIO = Label(frame_parametri, text="NPV (m): ", width=20, height=3)
lbl_EMIO.grid(row=3, column=0, sticky="W", padx=10)
ent_EMIO = Entry(frame_parametri, width=5)
ent_EMIO.grid(row=3, column=1, sticky="EW")

# fundiranje
#lbl_fundiranje = Label(frame_parametri, text="Nacin fundiranja:", width=18, height=3)
#lbl_fundiranje.grid(row=4, column=0, sticky="W", padx=10)
#selected1 = IntVar()
#fund_rad1 = Radiobutton(frame_parametri, text='Plitko', value=0, variable=selected1, width=10)
#fund_rad2 = Radiobutton(frame_parametri, text='Duboko', value=1, variable=selected1, width=10)
#fund_rad3 = Radiobutton(frame_parametri, text='Kombinovano', value=2, variable=selected1, width=15)
#fund_rad1.grid(row=4, column=1, sticky="W", ipadx=1, padx=5)
#fund_rad2.grid(row=4, column=2, sticky="W", ipadx=1, padx=5)
#fund_rad3.grid(row=4, column=3, sticky="W", ipadx=1, padx=5)
#fund_rad1.select()

# raspon
#lbl_raspon = Label(frame_parametri, text="Raspon mosta (m): ", width=20, height=3)
#lbl_raspon.grid(row=5, column=0, sticky="W", padx=10)
#ent_raspon = Entry(frame_parametri, width=5)
#ent_raspon.grid(row=5, column=1, sticky="EW")

# tehnologija
#lbl_tehnologija = Label(frame_parametri, text="Tehnologija gradjenja:", width=21, height=3)
#lbl_tehnologija.grid(row=6, column=0, sticky="W", padx=10)
#selected2 = IntVar()
#tehn_rad1 = Radiobutton(frame_parametri,text='Fiksna skela', value=0, variable=selected2, width=15)
#tehn_rad2 = Radiobutton(frame_parametri,text='Pokretna skela', value=1, variable=selected2, width=15)
#tehn_rad1.grid(row=6, column=1, sticky="EW", ipadx=1, padx=5)
#tehn_rad2.grid(row=6, column=2, sticky="EW", ipadx=1, padx=5)
#tehn_rad1.select()

#razmak
lbl_razmak = Label(frame_parametri, text='', width=5, height=1).grid(row=7, column=0)

# dugme za predvidjanje pomeranja
btn_predict = Button(frame_dugme, text="Predvidi", command=predict, width=10, height=3)
btn_predict.grid(row=0, column=0, pady=15, padx=10, sticky="S")

# dugme za brisanje unosa
btn_erase = Button(frame_dugme, text="Izbrisi", command=erase, width=10, height=3)
btn_erase.grid(row=0, column=1, pady=15, padx=10, sticky="S")

# rezultat
lbl_rezultat = Label(frame_rezultat, text="Predvidjeno pomeranje: ____ cm", width=74, height=2)
lbl_rezultat.grid(row=0, column=0, sticky="N")


#####################
####### MODEL #######
#####################

# ucitavanje podataka iz datoteke
dataset = loadtxt('HE_Piva_data_Shuffle.csv', delimiter=',')

# podela na ulazne (X) i izlazne (y) promenljive
X = dataset[:,0:3]
y = dataset[:,3]

# definisanje skalera
#scaler = StandardScaler()
scaler = MinMaxScaler(feature_range=(0, 1))

# transformacija - skaliranje ulaznih podataka
scaler.fit_transform(X)


# pronalazenje najvece izlazne vrednosti (pomeranja)
# kasnije se koristi za obrnutu transformaciju 
# predvidjenog pomeranja
maxDisplacement = y.max()

# ucitavanje modela
model_loaded = load_model('BINGO_HE_Piva.h5')

####### GLAVNA PETLJA #######