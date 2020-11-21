from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.messagebox import *  # get standard dialogs

root = Tk()

titlefont= ('Ariel', 15, 'bold')
labelfont= ('Ariel', 12) #, 'bold')
buttonfont= ('Ariel', 12) #, 'bold')
entryfont= ('Ariel', 12) #, 'bold')

unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
elements = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr "
elements = elements + "Cs Cu Dy Er Es Eu F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr "
elements = elements + "La Li Lu M Mn Mo N Na Nb Nd Ne Ni Np O Os P Pa Pb Pd Pm Po Pr "
elements = elements + "Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti "
elements = elements + "Ti Tm U V W Xe Y Yb Zn Zr "

compound_values = "Al4C3 2HBr CaI Ca(OH)2 Ca3P2 CdS CH3CO2H CO CO2 CsF CuS FeCl2 FeCl3 GaBr3 "
compound_values = compound_values + "HgO Hg2O HNO2 HNO3 H2CO3 H2SO3 H2SO4 H3PO4 HC2H3O2 HCl HClO4"
compound_values = compound_values + "HF HI H2S LiCl K2SO4 Kbr KOH Mg3N2 NaCl NaOH Na2O NH3 "
compound_values = compound_values + "NO2 N2O4 N2O5 H2O ZnO ZnCO3"

element1 = StringVar()
#el1 = element1.get()
eci_qty = StringVar()
#eci_qty.set(element1)

def set_element1():
    element1 = StringVar()
    el1 = element1.get()
    eci_qty = StringVar()
    eci_qty.set(element1)
    #eci_qty = StringVar()
    #eci1_qty = element1
    #pass       # The following does not get or set element1
    #e1 = element1.get()
    print('In process Set_Element. Element 1 is: ', el1)

def makeform(root):
    element1 = StringVar()
    el1 = element1.get()
    #eci_qty = StringVar()
    #eci_qty.set(element1)
    #eci_qty = DoubleVar()
    #eci1_qty = eci_qty.get()

    lbl_Title = Label(root, text="Chemistry")
    lbl_Title.grid(row=0, column=3, columnspan=4)
    lbl_Title.config(font=titlefont)

    lbl_Element1 = Label(root, text="Element 1", width=8)
    lbl_Element1.grid(row=1, column=0)
    lbl_Element1.config(font=labelfont)
    cb_UseCompounds1 = Checkbutton(root, text='Use Compounds 1?', width=14)
    cb_UseCompounds1.grid(row=1, column=1, columnspan=2)
    cb_UseCompounds1.config(font=labelfont)
    cb_UseHistory = Checkbutton(root, text='Use History?', width=10)
    cb_UseHistory.grid(row=1, column=5, columnspan=2)
    cb_UseHistory.config(font=labelfont)
    lbl_Element1 = Label(root, text="Explanation", width=10)
    lbl_Element1.grid(row=1, column=9, padx=8)
    lbl_Element1.config(font=labelfont)

    lbl_Qty1 = Label(root, text="Quantity 1", width=8)
    lbl_Qty1.grid(row=2, column=0)
    lbl_Qty1.config(font=labelfont)
    lbl_Units1 = Label(root, text="Units 1", width=6)
    lbl_Units1.grid(row=2, column=1)
    lbl_Units1.config(font=labelfont)
    lbl_Element1 = Label(root, text="Element 1")
    lbl_Element1.grid(row=2, column=2)
    lbl_Element1.config(font=labelfont)
    lbl_Yield = Label(root, text="Yield", width=8)
    lbl_Yield.grid(row=2, column=4)
    lbl_Yield.config(font=labelfont)
    lbl_CompQty1 = Label(root, text="Quantity 1", width=8)
    lbl_CompQty1.grid(row=2, column=5, padx=4)
    lbl_CompQty1.config(font=labelfont)
    lbl_CompUnits1 = Label(root, text="Units 1", width=8)
    lbl_CompUnits1.grid(row=2, column=6, padx=4)
    lbl_CompUnits1.config(font=labelfont)
    lbl_Compound1 = Label(root, text="  Compound 1", width=10)
    lbl_Compound1.grid(row=2, column=7, padx=4)
    lbl_Compound1.config(font=labelfont)
    #n=0
    e_ElementQty1 = Entry(root, text=0, width=8)
    e_ElementQty1.grid(row=3, column=0, padx=4)
    e_ElementQty1.config(font=entryfont, textvariable=eci_qty)
    cb_Units1 = Combobox(root, values=unit_values, width=8)
    cb_Units1.grid(row=3, column=1, padx=4)
    cb_Units1.config(font=entryfont)
    #, textvariable = n)  #, command=set_element1())
    #elements = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr "
    cb_Elements1 = Combobox(root, values=elements, width=8)
    cb_Elements1.grid(row=3, column=2, padx=4)
    cb_Elements1 = Combobox(root, command=set_element1())
    cb_Elements1.config(font=entryfont, textvariable=element1)
    #element1 = cb_Elements1.get()
    #element1 = Combobox(cb_Elements1.get())
    e_Yield1 = Entry(root, text="Yield", width=8)
    e_Yield1.grid(row=3, column=4, padx=4)
    e_Yield1.config(font=entryfont)
    e_CompoundQty1 = Entry(root, text="CompoundQty 1", width=8)
    e_CompoundQty1.grid(row=3, column=5, padx=4)
    e_CompoundQty1.config(font=entryfont)
    cb_CompoundUnits1 = Combobox(root, values=unit_values, width=8)
    cb_CompoundUnits1.grid(row=3, column=6, padx=4)
    cb_CompoundUnits1.config(font=entryfont)
    cb_Compound1 = Combobox(root, values=compound_values, width=8)
    cb_Compound1.grid(row=3, column=7, padx=4)
    cb_Compound1.config(font=entryfont)
    #compound1 = cb_Compound1.get()
    txt_Explanation = Text(root, width=16, height=16) #, text='First text') #, textvariable = n)
    txt_Explanation.grid(row=3, column=9, rowspan=12, padx=10, pady=10)
    txt_Explanation.config(font=entryfont)
    #txt_Explanation.selection_get() #= Text(root, element1)
    btn_Compose = Button(root, text='Compose', command=set_element1())
    btn_Compose.grid(row=4, column=4)
    btn_Compose.config(font=buttonfont)

    e_ElementMoleQty1 = Entry(root, text="eemq1 ", width=8)
    e_ElementMoleQty1.grid(row=4, column=0, padx=4)
    e_ElementMoleQty1.config(font=entryfont)
    lbl_Moles1 = Label(root, text="Moles", width=8)
    lbl_Moles1.grid(row=4, column=1, padx=4)
    lbl_Moles1.config(font=entryfont)
    e_Element1 = Entry(root, text="ee1", width=8)
    e_Element1.grid(row=4, column=2, padx=4)
    e_Element1.config(font=entryfont)

    e_CompoundMoleQty1 = Entry(root, text="CompoundMoleQty 1", width=8)
    e_CompoundMoleQty1.grid(row=4, column=5, padx=4)
    e_CompoundMoleQty1.config(font=entryfont)
    lbl_CompoundMoles1 = Label(root, text="Moles", width=8)
    lbl_CompoundMoles1.grid(row=4, column=6, padx=4)
    lbl_CompoundMoles1.config(font=entryfont)
    cb_CompoundMole1 = Combobox(root, values=compound_values, width=8)
    cb_CompoundMole1.grid(row=4, column=7, padx=4)
    cb_CompoundMole1.config(font=entryfont)

    lbl_CompTemp1 = Label(root, text="Temp C", width=6)
    lbl_CompTemp1.grid(row=5, column=5)
    lbl_CompTemp1.config(font=labelfont)
    e_CompQty1 = Entry(root, text="ecq1", width=6)
    e_CompQty1.grid(row=5, column=6)
    e_CompQty1.config(font=labelfont)
    lbl_CompPress1 = Label(root, text=" Press ATM", width=10)
    lbl_CompPress1.grid(row=5, column=7, padx=5)
    lbl_CompPress1.config(font=labelfont)
    e_CompPressQty1 = Entry(root, text="", width=6)
    e_CompPressQty1.grid(row=5, column=8)
    e_CompPressQty1.config(font=labelfont)

    lbl_Temp2 = Label(root, text="Temp C", width=6)
    lbl_Temp2.grid(row=5, column=0)
    lbl_Temp2.config(font=labelfont)
    e_TempQty2 = Entry(root, text="etq2", width=6)
    e_TempQty2.grid(row=5, column=1)
    e_TempQty2.config(font=labelfont)
    lbl_Press2 = Label(root, text=" Press ATM", width=10)
    lbl_Press2.grid(row=5, column=2, padx=5)
    lbl_Press2.config(font=labelfont)
    e_PressQty2 = Entry(root, text="epq2", width=6)
    e_PressQty2.grid(row=5, column=3)
    e_PressQty2.config(font=labelfont)

    lbl_Element2 = Label(root, text="Element 2", width=8)
    lbl_Element2.grid(row=7, column=0)
    lbl_Element2.config(font=labelfont)
    cb_UseCompounds2 = Checkbutton(root, text='Use Compounds 2?', width=14)
    cb_UseCompounds2.grid(row=7, column=1, columnspan=2)
    cb_UseCompounds2.config(font=labelfont)
    btn_Compose = Button(root, text = 'Deompose')
    btn_Compose.grid(row=5, column=4)
    btn_Compose.config(font=buttonfont)

    lbl_Qty2 = Label(root, text="Quantity 2", width=8)
    lbl_Qty2.grid(row=8, column=0)
    lbl_Qty2.config(font=labelfont)
    lbl_Units2 = Label(root, text="Units 2", width=6)
    lbl_Units2.grid(row=8, column=1)
    lbl_Units2.config(font=labelfont)
    lbl_Element2 = Label(root, text="Element 2")
    lbl_Element2.grid(row=8, column=2)
    lbl_Element2.config(font=labelfont)
    btn_Compose = Button(root, text = 'Metathesis')
    btn_Compose.grid(row=6, column=4)
    btn_Compose.config(font=buttonfont)
    lbl_CompQty2 = Label(root, text="Quantity 2", width=8)
    lbl_CompQty2.grid(row=8, column=5, padx=4)
    lbl_CompQty2.config(font=labelfont)
    lbl_CompUnits2 = Label(root, text="Units 2", width=8)
    lbl_CompUnits2.grid(row=8, column=6, padx=4)
    lbl_CompUnits2.config(font=labelfont)
    lbl_Compound2 = Label(root, text="  Compound 2", width=8)
    lbl_Compound2.grid(row=8, column=7, padx=4)
    lbl_Compound2.config(font=labelfont)

    e_ElementQty2 = Entry(root, text="eeq2", width=8)
    e_ElementQty2.grid(row=9, column=0, padx=4)
    e_ElementQty2.config(font=entryfont)
    cb_Units2 = Combobox(root, values=unit_values, width=8)
    cb_Units2.grid(row=9, column=1, padx=4)
    cb_Units2.config(font=entryfont)
    cb_Elements2 = Combobox(root, values=elements, width=8)
    cb_Elements2.grid(row=9, column=2, padx=4)
    cb_Elements2.config(font=entryfont)

    e_ElementMoleQty2 = Entry(root, text="eemq2", width=8)
    e_ElementMoleQty2.grid(row=10, column=0, padx=4)
    e_ElementMoleQty2.config(font=entryfont)
    lbl_Moles2 = Label(root, text="Moles", width=8)
    lbl_Moles2.grid(row=10, column=1, padx=4)
    lbl_Moles2.config(font=entryfont)
    e_ElementMoles2 = Entry(root, text="eem2", width=8)
    e_ElementMoles2.grid(row=10, column=2, padx=4)
    e_ElementMoles2.config(font=entryfont)

    e_CompoundMolesQty2 = Entry(root, text="ecmq2", width=8)
    e_CompoundMolesQty2.grid(row=10, column=5, padx=4)
    e_CompoundMolesQty2.config(font=entryfont)
    lbl_CompoundMoles2 = Label(root, text="Moles", width=8)
    lbl_CompoundMoles2.grid(row=10, column=6, padx=4)
    lbl_CompoundMoles2.config(font=entryfont)
    e_CompoundMoles2 = Entry(root, text="ecm2", width=8)
    e_CompoundMoles2.grid(row=10, column=7, padx=4)
    e_CompoundMoles2.config(font=entryfont)

    btn_Compose = Button(root, text = 'Neutralize')
    btn_Compose.grid(row=7, column=4)
    btn_Compose.config(font=buttonfont)

    e_CompoundQty2 = Entry(root, text="CompoundQty ", width=8)
    e_CompoundQty2.grid(row=9, column=5, padx=4)
    e_CompoundQty2.config(font=entryfont)
    cb_CompoundUnits2 = Combobox(root, values=unit_values, width=8)
    cb_CompoundUnits2.grid(row=9, column=6, padx=4)
    cb_CompoundUnits2.config(font=entryfont)
    cb_Compound2 = Combobox(root, values=compound_values, width=8)
    cb_Compound2.grid(row=9, column=7, padx=4)
    cb_Compound2.config(font=entryfont)

    btn_Compose = Button(root, text = '    Other    ')
    btn_Compose.grid(row=8, column=4)
    btn_Compose.config(font=buttonfont)

    lbl_Temp2 = Label(root, text="Temp C", width=6)
    lbl_Temp2.grid(row=11, column=0)
    lbl_Temp2.config(font=labelfont)
    e_TempQty2 = Entry(root, text="etq2", width=6)
    e_TempQty2.grid(row=11, column=1)
    e_TempQty2.config(font=labelfont)
    lbl_Press2 = Label(root, text=" Press ATM", width=10)
    lbl_Press2.grid(row=11, column=2, padx=1)
    lbl_Press2.config(font=labelfont)
    e_PressQty2 = Entry(root, text="epq2", width=6)
    e_PressQty2.grid(row=11, column=3)
    e_PressQty2.config(font=labelfont)

    lbl_CompTemp2 = Label(root, text="Temp C", width=6)
    lbl_CompTemp2.grid(row=11, column=5)
    lbl_CompTemp2.config(font=labelfont)
    e_CompTempQty2 = Entry(root, text="ectq2", width=6)
    e_CompTempQty2.grid(row=11, column=6)
    e_CompTempQty2.config(font=labelfont)
    lbl_CompPress2 = Label(root, text=" Press ATM", width=10)
    lbl_CompPress2.grid(row=11, column=7, padx=5)
    lbl_CompPress2.config(font=labelfont)
    e_CompPressQty2 = Entry(root, text="ecpq2", width=6)
    e_CompPressQty2.grid(row=14, column=8)
    e_CompPressQty2.config(font=labelfont)

    lbl_Space1 = Label(root, text=" ", width=6)
    lbl_Space1.grid(row=12, column=0)
    lbl_Space1.config(font=labelfont)

    lbl_Element3 = Label(root, text="Element 3", width=8)
    lbl_Element3.grid(row=13, column=0)
    lbl_Element3.config(font=labelfont)
    cb_UseCompounds3 = Checkbutton(root, text='Use Compounds 3?', width=14)
    cb_UseCompounds3.grid(row=13, column=1, columnspan=2)
    cb_UseCompounds3.config(font=labelfont)

    lbl_Qty3 = Label(root, text="Quantity 3", width=8)
    lbl_Qty3.grid(row=14, column=0)
    lbl_Qty3.config(font=labelfont)
    lbl_Units3 = Label(root, text="Units 3", width=6)
    lbl_Units3.grid(row=14, column=1)
    lbl_Units3.config(font=labelfont)
    lbl_Element3 = Label(root, text="Element 3")
    lbl_Element3.grid(row=14, column=2)
    lbl_Element3.config(font=labelfont)

    lbl_CompQty3 = Label(root, text="Quantity 3", width=8)
    lbl_CompQty3.grid(row=14, column=5, padx=4)
    lbl_CompQty3.config(font=labelfont)
    lbl_CompUnits3 = Label(root, text="Units 3", width=8)
    lbl_CompUnits3.grid(row=14, column=6, padx=4)
    lbl_CompUnits3.config(font=labelfont)
    lbl_Compound3 = Label(root, text="  Compound 3", width=10)
    lbl_Compound3.grid(row=14, column=7, padx=4)
    lbl_Compound3.config(font=labelfont)

    e_ElementQty3 = Entry(root, text="eeq3", width=8)
    e_ElementQty3.grid(row=15, column=0, padx=4)
    e_ElementQty3.config(font=entryfont)
    cb_Units3 = Combobox(root, values=unit_values, width=8)
    cb_Units3.grid(row=15, column=1, padx=4)
    cb_Units3.config(font=entryfont)
    cb_Elements3 = Combobox(root, values=elements, width=8)
    cb_Elements3.grid(row=15, column=2, padx=4)
    cb_Elements3.config(font=entryfont)
    e_CompoundQty3 = Entry(root, text="ecq3", width=8)
    e_CompoundQty3.grid(row=15, column=5, padx=4)
    e_CompoundQty3.config(font=entryfont)
    cb_CompoundUnits3 = Combobox(root, values=unit_values, width=8)
    cb_CompoundUnits3.grid(row=15, column=6, padx=4)
    cb_CompoundUnits3.config(font=entryfont)
    cb_Compound3 = Combobox(root, values=compound_values, width=8)
    cb_Compound3.grid(row=15, column=7, padx=4)
    cb_Compound3.config(font=entryfont)
    e_ElementMoleQty3 = Entry(root, text="eemq3", width=8)
    e_ElementMoleQty3.grid(row=17, column=0, padx=4)
    e_ElementMoleQty3.config(font=entryfont)
    lbl_Moles3 = Label(root, text="Moles", width=8)
    lbl_Moles3.grid(row=17, column=1, padx=4)
    lbl_Moles3.config(font=entryfont)
    e_ElementMoles3 = Entry(root, text="eem3", width=8)
    e_ElementMoles3.grid(row=17, column=2, padx=4)
    e_ElementMoles3.config(font=entryfont)
    e_CompoundMolesQty3 = Entry(root, text="ecmq3", width=8)
    e_CompoundMolesQty3.grid(row=17, column=5, padx=4)
    e_CompoundMolesQty3.config(font=entryfont)
    lbl_CompoundMoles3 = Label(root, text="Moles", width=8)
    lbl_CompoundMoles3.grid(row=17, column=6, padx=4)
    lbl_CompoundMoles3.config(font=entryfont)
    e_CompoundMoles3 = Entry(root, text="ecm3", width=8)
    e_CompoundMoles3.grid(row=17, column=7, padx=4)
    e_CompoundMoles3.config(font=entryfont)

    lbl_Temp3 = Label(root, text="Temp C", width=6)
    lbl_Temp3.grid(row=18, column=0)
    lbl_Temp3.config(font=labelfont)
    e_TempQty3 = Entry(root, text="", width=6)
    e_TempQty3.grid(row=18, column=1)
    e_TempQty3.config(font=labelfont)
    lbl_Press3 = Label(root, text=" Press ATM", width=10)
    lbl_Press3.grid(row=18, column=2, padx=5)
    lbl_Press3.config(font=labelfont)
    e_PressQty3 = Entry(root, text="epq3", width=6)
    e_PressQty3.grid(row=18, column=3)
    e_PressQty3.config(font=labelfont)
    lbl_TempComp3 = Label(root, text="Temp C", width=6)
    lbl_TempComp3.grid(row=18, column=5)
    lbl_TempComp3.config(font=labelfont)
    e_TempCompQty3 = Entry(root, text="etcq3", width=6)
    e_TempCompQty3.grid(row=18, column=6)
    e_TempCompQty3.config(font=labelfont)
    lbl_CompPress3 = Label(root, text=" Press ATM", width=10)
    lbl_CompPress3.grid(row=18, column=7, padx=1)
    lbl_CompPress3.config(font=labelfont)
    e_CompPressQty3 = Entry(root, width=6)
    e_CompPressQty3.grid(row=18, column=8)
    e_CompPressQty3.config(font=labelfont)

    btn_Quit = Button(root, text = 'Quit')
    btn_Quit.grid(row=19, column=9)
    btn_Quit.config(font=buttonfont)

if __name__ == '__main__':
    #make_Title_Frame('Chemistry')

    #root = Tk()
    root.title('Chemistry')
    makeform(root)
    root.bind('<Return>', lambda event: set_element1())
    mainloop()