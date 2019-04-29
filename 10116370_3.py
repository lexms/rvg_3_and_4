# NIM : 10116370
# Nama : Alexander M S
# Kelas : MOSI-8

import math 

class Simulate_case_3:
    def __init__(self):
            self.a = 7
            self.m = 128
            self.z0 = 12357
            self.mean = 56.27
            self.standard_deviation = 17.5749
            self.count = 5

    def multiplicative_formula(self,zi_minus_1):
        return (self.a * zi_minus_1) % self.m

    def ui_generate(self, zi):
        return zi / self.m

    def method_ln(self, ui):
        return (-2 * math.log(ui))**(1/2)
    
    def method_sin(self, ui_plus_satu):
        return math.sin(2* math.pi * ui_plus_satu)

    def find_Z(self, ln, sin):
        return ln * sin

    def find_X(self, Z):
        return self.mean + self.standard_deviation * Z
    
    def rvg_normal_distribution(self):
        _list = []
        for i in range(0,self.count):
            if i == 0:
                zi = self.multiplicative_formula(self.z0)
                zi_plus_satu = self.multiplicative_formula(zi)
                ui = self.ui_generate(zi)
                ui_plus_satu = self.ui_generate(zi_plus_satu)

                ln = self.method_ln(ui)
                sin = self.method_sin(ui_plus_satu)
                Z = self.find_Z(ln, sin)
                X = self.find_X(Z)
                _list.append({'Zi' : zi, 'Zi+1' : zi_plus_satu, 'ui': ui, 'ui+1': ui_plus_satu, 'ln': ln, 'sin': sin, 'Z': Z, 'X': X})
            elif i>0:
                zi = _list[i-1]['Zi+1']
                zi_plus_satu = self.multiplicative_formula(zi)
                ui = self.ui_generate(zi)
                ui_plus_satu = self.ui_generate(zi_plus_satu)

                ln = self.method_ln(ui)
                sin = self.method_sin(ui_plus_satu)
                Z = self.find_Z(ln, sin)
                X = self.find_X(Z)
                _list.append({'Zi' : zi, 'Zi+1' : zi_plus_satu, 'ui': ui, 'ui+1': ui_plus_satu, 'ln': ln, 'sin': sin, 'Z': Z, 'X': X})
        return _list

    def print_table(self):
        _list = self.rvg_normal_distribution()
        print('\n===Kasus 3===\n')
        print('| No.\t |  Zi\t\t | Zi+1\t\t | Ui\t\t | Ui+1\t\t | (-2lnUi)^(1/2)\t | sin(2 pi (Ui+1))\t | Z\t\t | X\t\t |')
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        for i in range(0,len(_list)):
            print("| {}\t | {:.4f} \t | {:.4f} \t | {:.4f} \t | {:.4f} \t | {:.4f} \t\t | {:.4f} \t\t | {:.4f} \t | {:.4f} \t |".format(i+1, _list[i]['Zi'], _list[i]['Zi+1'], _list[i]['ui'], _list[i]['ui+1'], _list[i]['ln'], _list[i]['sin'], _list[i]['Z'], _list[i]['X'] ))


test = Simulate_case_3()
test.print_table()