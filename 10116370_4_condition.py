# NIM : 10116370
# Nama : Alexander M S
# Kelas : MOSI-8

import math 

class Simulate_case_4_2:
    def __init__(self):
            self.a = 7
            self.m = 128
            self.z0 = 12357
            self.lambd = 3
            self.count = 5

    
    def multiplicative_formula(self,zi_minus_1):
        return (self.a * zi_minus_1) % self.m

    def ui_generate(self, zi):
        return zi / self.m

    def find_F(self):
        return math.e ** (-1 * self.lambd)

    def rvg_poisson_distribution(self):
        _list = []
        count_true = 0
        i = 0
        while count_true < self.count:

            if i == 0:
                k = 1
                zi = self.multiplicative_formula(self.z0)
                ui = self.ui_generate(zi)
                Pk = ui
                F = self.find_F()
                if Pk < F:
                    X = k-1
                    status = 'TRUE'
                    k = 1
                    if X != 0:
                        count_true += 1
                else:
                    status = 'FALSE'
                    X = 0
                _list.append({'K': 1, 'Zi':zi, 'Ui':ui, 'Pk':Pk, 'status': status, 'X': X})
            
            elif i>0:
                zi = self.multiplicative_formula(_list[i-1]['Zi'])
                ui = self.ui_generate(zi)
                if k == 1:
                    Pk = ui
                else:
                    Pk = _list[i-1]['Pk'] * ui
                
                F = self.find_F()
                if Pk < F:
                    X = k-1
                    status = 'TRUE'
                    k = 1
                    if X != 0:
                        count_true += 1
                else:
                    status = 'FALSE'
                    X = 0
                    k=k+1

                _list.append({'K': k, 'Zi':zi, 'Ui':ui, 'Pk':Pk, 'status': status, 'X': X})
            i+=1
        return _list

    def print_table(self):
        _list = self.rvg_poisson_distribution()
        print('\n===Kasus 4===\n')
        print('| No.\t |  K\t\t | Zi\t\t | Ui\t\t | Pk\t\t | Pk< {:.4f}\t | Jumlah Order (X=k-1)\t |'.format(self.find_F()))
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        for i in range(len(_list)):
            print("| {}\t | {:.4f} \t | {:.4f} \t | {:.4f} \t | {:.4f} \t | {} \t | {:.4f} \t\t |".format(i+1, _list[i]['K'], _list[i]['Zi'], _list[i]['Ui'], _list[i]['Pk'], _list[i]['status'], _list[i]['X'] ))



test = Simulate_case_4_2()
test.print_table()