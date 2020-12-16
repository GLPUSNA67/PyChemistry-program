import shelve

class Compound:
    def __init__(self, formula, alphas='', name='', m_mass='', bond='', electronegativity='', density='', melting='', boiling='',
                 Vanderwaals_radius='', Ionic_radius='', Isotopes='', electronic_shell='', Energy_of_first_ionization='',
                 energy_of_second_ionization='', standard_potential='', structure=''):
        self.formula = formula
        self.alphas = alphas
        self.name = name
        self.m_mass  = m_mass
        self.bond  = bond
        self.electronegativity  = electronegativity
        self.density = density
        self.melting = melting
        self.boiling = boiling
        self.Vanderwaals_radius  = Vanderwaals_radius
        self.Ionic_radius = Ionic_radius
        self.Isotopes = Isotopes
        self.electronic_shell = electronic_shell
        self.Energy_of_first_ionization  = Energy_of_first_ionization
        self.energy_of_second_ionization  = energy_of_second_ionization
        self.standard_potential = standard_potential
        self.structure = structure

class Ion:
    def __init__(self, formula, alphas='', name='', charge="", m_mass='', bond='', electronegativity='', density='', melting='', boiling='',
                 Vanderwaals_radius='', Ionic_radius='', Isotopes='', electronic_shell='', Energy_of_first_ionization='',
                 energy_of_second_ionization='', standard_potential='', structure=''):
        self.formula = formula
        self.alphas = alphas
        self.name = name
        self.charge = charge
        self.m_mass  = m_mass
        self.bond  = bond
        self.electronegativity  = electronegativity
        self.density = density
        self.melting = melting
        self.boiling = boiling
        self.Vanderwaals_radius  = Vanderwaals_radius
        self.Ionic_radius = Ionic_radius
        self.Isotopes = Isotopes
        self.electronic_shell = electronic_shell
        self.Energy_of_first_ionization  = Energy_of_first_ionization
        self.energy_of_second_ionization  = energy_of_second_ionization
        self.standard_potential = standard_potential
        self.structure = structure
'''
    P"Al4C3BCl3BeH22HBrCaICa(OH)2CdSCH3CO2HCOCO2CsFCuSFeCl2FeCl3GaBr3HgOHg2OHNO2HNO3H2CO3H2SO3H2SO4H3PO4HC2H3O2HClHClO4HFHIH2SLiClK2SO4KBrKOHMg3N2NaClNaOHNa2ONH3NONO2N2O4N2O5H2OZZnCO3"
    "Al4C3 BCl3 BeH2 2HBr CaICa(OH)2CdSCH3CO2HCOCO2CsFCuSFeCl2FeCl3GaBr3HgOHg2OHNO2HNO3H2CO3H2SO3H2SO4H3PO4HC2H3O2HClHClO4HFHIH2SLiClK2SO4KBrKOHMg3N2NaClNaOHNa2ONH3NONO2N2O4N2O5H2OZZnCO3"
    "AlC BCl BeH HBr CaI Ca(OH) CaP CdS CHCOH CO CO CsF CuS FeCl FeCl GaBr HgO HgO HNO HNO HCO HSO HSO HPO HCHO
                                    HCl HClO HF HI HS LiCl KSO Kbr KOH MgN NaCl NaOH NaO NH NO NO NO NO HO ZnO ZnCO3"
    "CuS FeCl2 FeCl3 GaBr3 HgO Hg2O HNO2 HNO3 H2CO3 H2SO3 H2SO4 H3PO4 HC2H3O2 Hcl HclO4 HF HI H2S LiCl K2SO4
                                    Kbr KOH Mg3N2 NaCl NaOH Na2O NH3 NO NO2 N2O4 N2O5 H2O ZnO ZnCO3"
    "AcAgAlAmArAsAtAuBBaBeBiBkBrCCaCdCeCfClCmCoCrCsCuDyErEsEuFFeFmFrGaGdGeHHeHfHgHoIInIrKKrLaLiLuMgMnMoNNaNbNdNeNiNpOOsPPaPbPdPmPoPrPtPuRaRbReRhRnRuSSbScSeSiSmSnSrTaTbTcTeThTiTlTmUVWXeYYbZnZr"

'''


if __name__ == '__main__':
    Al4C3 = Compound('Al4C3', 'AlC','aluminum_carbide')
    Ar2He2Kr2Ne2Xe2Rn2 = Compound('Ar2He2Kr2Ne2Xe2Rn2', 'ArHeKrNeXeRn', 'air')
    BCl3 = Compound('BCl3', 'BCl','boron_trichloride')
    CH4 = Compound('CH4', 'CH', 'methane', melting=-182.5, boiling=-161.5)
    C2H6 = Compound('C2H6', 'CH', 'ethane', melting=-183.2, boiling=-88.6)
    C3H8 = Compound('C3H8', 'CH', 'propane', melting=-187.7, boiling=-42.1)
    C4H10 = Compound('C4H10', 'CH', 'butane', melting=-138.3, boiling=-0.5)
    C4H10_M = Compound('C4H10_M', 'CH', '2-methylpropane', melting='', boiling='')
    C5H12 = Compound('C5H12', 'CH', 'pentane', melting=-129.7, boiling=36.1)
    C6H14 = Compound('C6H14', 'CH', 'hexane', melting=-95.3, boiling=68.7)
    C7H16 = Compound('C7H16', 'CH', 'heptane', melting=-90.6, boiling=98.4)
    C8H18 = Compound('C8H18', 'CH', 'octane', melting=-56.8, boiling=125.7)
    C9H20 = Compound('C9H20', 'CH', 'nonane', melting=-53.6, boiling=150.8)
    C10H22 = Compound('C10H22', 'CH', 'decane', melting=-29.7, boiling=174.0)
    C14H30 = Compound('C14H30', 'CH', 'tetradecane', melting=5.9, boiling=253.5)
    C18H38 = Compound('C18H38', 'CH', 'octadecane', melting=28.2, boiling=316.1)

    CaH2PO4 = Compound('Ca(H2PO4)2', 'CaHOP','calcium_dihydrogen_phosphate')
    CaI = Compound('CaI', 'CaI','calcium_iodide')
    CaOH2 = Compound('Ca(OH)2', 'CaHO','calcium_hydroxide')
    Ca3P2 = Compound('Ca3P2', 'CaP','calcium_phosphide')
    CdS = Compound('CdS', 'CdS','cadmium_sulfide')
    CsF = Compound('CsF', 'CsF','cesium_fluoride')
    C6H8O7 = Compound('C6H8O7', 'CHO','citric_acid')
    CH3CO2H = Compound('CH3CO2H', 'CHO','acetic_acid')
    C2H4COH = Compound('C2H4COH', 'CHO','acetic_acid')
    CO = Compound('CO', 'CO','carbon_monoxide')
    CO2 = Compound('CO2', 'CO','carbon_dioxide')
    HBr_g = Compound('HBr_g', 'BrH','hydrogen_bromide')
    HBr_aq = Compound('HBr_aq', 'BrH','hydrobromic_acid')
    HC2H3O2 = Compound('HC2H3O2', 'CHO','acetic_acid')
    HCl = Compound('HCl', 'ClH','hydrogen_chloride')
    HCl_g = Compound('HCl_g', 'ClH','hydrogen_chloride_g')
    HCl_aq = Compound('HCl_aq', 'ClH','hydrochloric_acid')
    HClO4 = Compound('HClO4', 'ClHO','perchloric_acid')
    HCN = Compound('HCN', 'CHN','hydrogen_cyanide')
    H2CO3 = Compound('H2CO3', 'CHO','carbonic_acid')

    HF_g = Compound('HF_g', 'FH', 'hydrogen_fluoride')
    HF_aq = Compound('HF_aq', 'FH', 'hydrofluoric_acid')
    HI_g = Compound('HI_g', 'HI','hydrogen_iodide')
    HI_aq = Compound('HI_aq', 'HI','hydroiodic_acid')
    HNO2 = Compound('HNO2', 'HNO','nitrous_acid')
    HNO3 = Compound('HNO3', 'HNO','nitric_acid')
    H3PO4 = Compound('H3PO4', 'HOS','phosphoric_acid')
    H2S_g = Compound('H2S_g', 'HS','hydrogen_suflide')
    H2S_aq = Compound('H2S_aq', 'HS','hydrosulfuric_acid')
    H2SO3 = Compound('H2SO3', 'HOS','sulfurous_acid')
    H2SO4 = Compound('H2SO4', 'HOS','sulfuric_acid')
    IF7 = Compound('IF7', 'FI','iodine_heptafluoride')
    KBr = Compound('KBr', 'BrK','potassium_bromide')
    KOH = Compound('KOH', 'HKO','potassium_hydroxide')
    LiCl = Compound('LiCl', 'ClLi','lithium_chloride')
    Mg3N2 = Compound('Mg3N2', 'MgN','magnesium_nitride')
    NaCl = Compound('NaCl', 'ClNa','sodium_chloride')
    NaHCO3 = Compound('NaHCO33', 'CHNaO)','bicarbonate_of_soda')
    Na2O = Compound('Na2O', 'NaO','sodium_oxide')
    NaOH = Compound('NaOH', 'HNaO','sodium_hydroxide')
    NH3 = Compound('NH3', 'HN','ammonia')
    N2H4 = Compound('N2H4', 'HN','hydrazine')
    NO = Compound('NO', 'NO','nitric_oxide')
    NO2 = Compound('NO2', 'NO','nitorgen_dioxide')
    N2O4 = Compound('N2O4', 'NO','dinitrogen_tetroxide')
    N2O = Compound('N2O', 'NO','nitrous_oxide')
    N2O5 = Compound('N2O5', 'NO','dinitrogen_pentoxide')
    PF5 = Compound('PF5', 'FP','phosphorus_pentafluoride')
    SO2 = Compound('SO2', 'OS','sulfur_dioxide')
    SO3 = Compound('SO3', 'OS','sulfur_trioxide')

    # Ions follow
    C2H3O2 = Ion('C2H3O2-', 'CHO','acetate', '-')
    ClO2 = Ion('ClO2-', 'ClO','chlorite', '-')
    ClO3 = Ion('ClO3-', 'ClO','chlorate', '-')
    ClO4 = Ion('ClO4-', 'ClO','perchlorate', '-')
    CN = Ion('CN-', 'CN','cyanide', '-')
    CO32 = Ion('CO32-', 'CO','carbonate', '-')
    CuS = Ion('CuS+', 'CuS','copper_(II)_sulfide', '+')
    FeCl2 = Ion('FeCl2+', 'ClFe','iron_(II)_chloride', '+')
    FeCl3 = Ion('FeCl3+', 'ClFe','iron_(III)_chloride', '+')
    H2PO4 = Ion('H2PO4-', 'dihydrogen_phosphate', '-')
    HCO3 = Ion('HCO3-', 'CHO','hydrogen_carbonate', '-')
    Hg2O = Ion('HgO+', 'HgO','mercury_(I)_oxide', '+')
    HgO = Ion('HgO+', 'HgO','mercury_(II)_oxide', '+')
    H3O = Ion('H3O+', 'HO','hydronium', '+')
    HPO42 = Ion('HPO42-', 'HOP','hydrogen phosphate', '-')
    HSO4 = Ion('HSO4-', 'HOS','hydrogen_sulfate', '-')
    OH = Ion('OH-', 'HO','hydroxide', '-')
    NH4 = Compound('NH4+', 'HN','ammonium')
    NO3 = Ion('NO3-', 'NO','nitrate', '-')
    NO2 = Ion('NO2-', 'NO','nitrite', '-')
    MNO4 = Ion('MNO4-', 'MNO','permanganate', '-')
    O22 = Ion('O22-', 'O','peroxide', '-')
    SO42 = Ion('SO42-', 'OS','sulfate', '-')
    SO32 = Ion('SO32-', 'So','sulfite', '-')
    PO43 = Ion('PO43-', 'PO','phosphate', '-')
    # ***

    db = shelve.open('chem-compounds')
    db['air'] = Ar2He2Kr2Ne2Xe2Rn2
    db['Al4C3'] = Al4C3
    db['BCl3'] = BCl3
    db['CH4'] = CH4
    db['C2H6'] = C2H6
    db['C3H8'] = C3H8
    db['C4H10'] = C4H10
    db['C4H10_M'] = C4H10_M
    db['C5H12'] = C5H12
    db['C6H14'] = C6H14
    db['C7H16'] = C7H16
    db['C8H18'] = C8H18
    db['C9H20'] = C9H20
    db['C10H22'] = C10H22
    db['C14H30'] = C14H30
    db['C18H38'] = C18H38

    db['CaH2PO4'] = CaH2PO4
    db['CaI'] = CaI
    db['CaOH2'] = CaOH2
    db['Ca3P2'] = Ca3P2
    db['CdS'] = CdS
    db['C6H8O7'] = C6H8O7
    db['CH3CO2H'] = CH3CO2H
    db['C2H4COH'] = C2H4COH
    db['CO'] = CO
    db['CO2'] = CO2
    db['HBr_g'] = HBr_g
    db['HBr_aq'] = HBr_aq
    db['HC2H3O2'] = HC2H3O2
    db['HCl'] = HCl
    db['HCl_g'] = HCl_g
    db['HCl_aq'] = HCl_aq
    db['HClO4'] = HClO4
    db['H2CO3'] = H2CO3

    '''

    '''
    db.close()
    # formula, alphas='', name
    print(Al4C3.formula, Al4C3.alphas, Al4C3.name, BCl3.formula, BCl3.alphas, BCl3.name, CaH2PO4.formula, CaH2PO4.alphas, CaH2PO4.name)

    db = shelve.open('chem-ions')
    db['C2H3O2'] = C2H3O2
    db['ClO2'] = ClO2
    db['ClO3'] = ClO3
    db['CN'] = CN
    db['CuS'] = CuS
    db['FeCl2'] = FeCl2
    db['FeCl3'] = FeCl3
    db['Hg2O'] = Hg2O
    db['HgO'] = HgO
    db['H3O'] = H3O
    db['H3O'] = H3O
    db['HSO4'] = HSO4

    db['H2PO4'] = H2PO4
    db['HCO3'] = HCO3
    db['NO2'] = NO2
    db['NO2'] = NO2
    db['NO3'] = NO3
    db['OH'] = OH

    db.close()
    print(CuS.formula, CuS.alphas, CuS.name, CuS.charge)
    print(FeCl2.formula, FeCl2.alphas, FeCl2.name, FeCl2.charge)
    print(FeCl3.formula, FeCl3.alphas, FeCl3.name, FeCl3.charge)
    # desn refers to dictionary, element(symbol/formula), symbol, name. When an item is selected in a combo box, 
    # the desn can be used look up the associated symbol/formula or name and fill in the associated combo box.
    desn = {"Al4C3": "aluminum_carbide", "Ar2He2Kr2Ne2Xe2Rn2": "air", "BCl3": "boron_trichloride",
            "CH4":  "methane", "C2H6": "ethane", "C3H8": "propane", "C4H10": "butane",
            "C4H10_M": "2-methylpropane", "C5H12": "pentane", "C6H14": "hexane", "C7H16": "heptane",
            "C8H18": "octane", "C9H20": "nonane", "C10H22": "decane", "C14H30": "tetradecane",
            "C18H38": "octadecane", "CaH2PO4": "calcium_dihydrogen_phosphate", "CaI": "calcium_iodide",
            "CaOH2": "calcium_hydroxide", "Ca3P2": "calcium_phosphide", "CdS": "cadmium_sulfide",
            "CsF": "cesium_fluoride", "C6H8O7": "citric_acid", "CH3CO2H": "acetic_acid",
            "C2H4COH": "acetic_acid", "CO": "carbon_monoxide", "CO2": "carbon_dioxide",
            "HBr_g": "hydrogen_bromide", "HBr_aq": "hydrobromic_acid", "HC2H3O2": "acetic_acid",
            "HCl": "hydrogen_chloride", "HCl_g": "hydrogen_chloride", "HCl_aq": "hydrochloric_acid",
            "HClO4": "perchloric_acid", "HCN": "hydrogen_cyanide", "H2CO3": "carbonic_acid",
            "HF_g": "hydrogen_fluoride", "HF_aq": "hydrofluoric_acid", "HI_g": "hydrogen_iodide",
            "HI_aq": "hydroiodic_acid", "HNO2": "nitrous_acid", "HNO3": "nitric_acid",
            "H3PO4": "phosphoric_acid", "H2S_g": "hydrogen_suflide", "H2S_aq": "hydrosulfuric_acid",
            "H2SO3": "sulfurous_acid", "H2SO4": "sulfuric_acid", "IF7": "iodine_heptafluoride",
            "KBr": "potassium_bromide", "KOH": "potassium_hydroxide", "LiCl": "lithium_chloride",
            "Mg3N2": "magnesium_nitride", "NaCl": "sodium_chloride", "NaHCO3": "bicarbonate_of_soda",
            "Na2O": "sodium_oxide", "NaOH": "sodium_hydroxide", "NH3": "ammonia", "N2H4": "hydrazine",
            "NO": "nitric_oxide", "NO2": "nitorgen_dioxide", "N2O4": "dinitrogen_tetroxide",
            "N2O": "nitrous_oxide", "N2O5": "dinitrogen_pentoxide", "PF5": "phosphorus_pentafluoride",
            "SO2": "sulfur_dioxide", "SO3": "sulfur_trioxide"}

    des_list = {"AlC": "[Al4C3]", "Ar2He2Kr2Ne2Xe2Rn2": "[Ar2He2Kr2Ne2Xe2Rn2]", "BCl": "[BCl3]",
                "CH": ["CH4", "C2H6", "C3H8", "C4H10", "C4H10_M", "C5H12", "C6H14", "C7H16", "C8H18",
                "C9H20", "C10H22", "C14H30", "C18H38"]}

    compound_symbols_list= "Al4C3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 CH4 C2H6 C3H8 C4H10 C4H10_M C5H12 C6H14 C7H16 C8H18 C9H20 C10H22 C14H30 C18H38 CaH2PO4 CaI CaOH2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H4COH CO CO2 HBr_g HBr_aq HC2H3O2 HCl HCl_g HCl_aq HClO4 HCN H2CO3 HF_g HF_aq HI_g HI_aq HNO2 HNO3 H3PO4 H2S_g H2S_aq H2SO3 H2SO4 IF7 KBr KOH LiCl Mg3N2 NaCl NaHCO3 Na2O NaOH NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3"

    for key in desn.keys():
        compound_symbols_list = compound_symbols_list  + "'"+ key + "' "

    #compound_names_list = "aluminum carbide air boron trichloride methane ethane propane butane 2-methylpropane pentane hexane heptane octane nonane decane tetradecane octadecane calcium dihydrogen phosphate calcium iodide calcium hydroxide calcium phosphide cadmium sulfide cesium fluoride citric acid acetic acid acetic acid carbon monoxide carbon dioxide hydrogen bromide hydrobromic acid acetic acid hydrogen chloride hydrogen chloride hydrochloric acid Perchloric acid hydrogen cyanide Carbonic acid hydrogen fluoride hydrofluoric acid hydrogen iodide hydroiodic acid nitrous acid nitric acid phosphoric acid hydrogen suflide hydrosulfuric acid sulfurous acid sulfuric acid iodine heptafluoride potassium bromide potassium hydroxide lithium chloride magnesium nitride sodium chloride bicarbonate of soda sodium oxide sodium hydroxide ammonia hydrazine nitric oxide nitorgen dioxide dinitrogen tetroxide nitrous oxide dinitrogen pentoxide phosphorus pentafluoride sulfur dioxide sulfur trioxide"
    compound_names_list = ""

    for value in desn.values():
        compound_names_list = compound_names_list + value + " "

    print (compound_symbols_list)
    print(compound_names_list)
    print(des_list)

    '''
    #alphabetic list of compounds that have similar alphabetic element lists
    "AlC": "[Al4C3]",
    "Ar2He2Kr2Ne2Xe2Rn2": "[Ar2He2Kr2Ne2Xe2Rn2]",
    "BCl": "[BCl3]",
    "CH": "["CH4", "C2H6", "C3H8", "C4H10", "C4H10_M", "C5H12", "C6H14", "C7H16", "C8H18",
        "C9H20", "C10H22", "C14H30", "C18H38"]"

    H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
    He = Element('He','Helium',  2,  4.002602,  '8A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
    Li = Element('Li', 'Lithium',  3,  6.941,  '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')

    H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', '_1s', '_2s', '_2p', '_3s', '_3p', '_3d', '_4s', '_4p', '_4d', '_4f', 'reserved')

    db = shelve.open('class-element-shelve')
    db['H'] = H
    db['He'] = He
    db['Li'] = Li
    db.close()
    print(H.name, H.group, He.name, He.group, Li.name, Li.group)
    '''
