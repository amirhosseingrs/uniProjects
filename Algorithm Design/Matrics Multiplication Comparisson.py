import random
import os
import time
import xlsxwriter
import matplotlib.pyplot as plt
# project of algorithm design class PROVIDED BY AMIR HOSSEIN GAROUSI
class zarbing:
    def zarb_sade(self, m1, m2):
        n = len(m1[0])
        # print('-------------------------------')
        # for i in range(n):
        #     print(m1[i], '   |   ', m2[i])
        
        result = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += m1[i][k] * m2[k][j]
        
        return result
        
    def make_matrix(self, n):
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(random.randint(1, 100))
            matrix.append(row)
        # print(f'new mat = {matrix}')
        return matrix

    def add_matrix(self, m1, m2):
        result = [[0 for j in range(len(m1))] for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2)):
                result[i][j] = m1[i][j] + m2[i][j]
        return result    


    def devide_conquer(self, m1, m2):
        n = len(m1[0])
        if n == 1:
            return [[m1[0][0] * m2[0][0]]]

        if n % 2 != 0:
            m1 = self.add_one(m1)
            m2 = self.add_one(m2)
            n = len(m1)

        c = [[0 for i in range(n)] for j in range(n)]
        mid = n // 2

        a11, a12, a21, a22 = self.partition(m1, mid)
        b11, b12, b21, b22 = self.partition(m2, mid)


        c11 = self.add_matrix(self.devide_conquer(a11, b11), self.devide_conquer(a12, b21))
        c12 = self.add_matrix(self.devide_conquer(a11, b12), self.devide_conquer(a12, b22))
        c21 = self.add_matrix(self.devide_conquer(a21, b11), self.devide_conquer(a22, b21))
        c22 = self.add_matrix(self.devide_conquer(a21, b12), self.devide_conquer(a22, b22))


        # combine result to c
        for i in range(mid):
            for j in range(mid):
                c[i][j] = c11[i][j]
                c[i][j + mid] = c12[i][j]
                c[i + mid][j] = c21[i][j]
                c[i + mid][j + mid] = c22[i][j]
        return c

    def partition(self, m, n):
        a11 = [[m[i][j] for j in range(n)] for i in range(n)]
        a12 = [[m[i][j] for j in range(n, len(m))] for i in range(n)]
        a21 = [[m[i][j] for j in range(n)] for i in range(n, len(m))]
        a22 = [[m[i][j] for j in range(n, len(m))] for i in range(n, len(m))]
        return (a11, a12, a21, a22)

    
    def add_one(self, m1):
        # print(m1)
        m = []
        for i in m1:
            mrow = [x for x in i]
            mrow.append(0)
            m.append(mrow)

        m.append([0 for x in range(len(m[0]))])
        return m 
        

    def strassen(self, m1, m2):
        n = len(m1[0])
        if n == 1:
            return [[m1[0][0] * m2[0][0]]]
        
        if n % 2 != 0:
            m1 = self.add_one(m1)
            m2 = self.add_one(m2)
            n = len(m1)
        
        c = [[0 for i in range(n)] for j in range(n)]
        mid = n // 2

        a11, a12, a21, a22 = self.partition(m1, mid)
        b11, b12, b21, b22 = self.partition(m2, mid)
        
        p1 = self.strassen(self.add_matrix(a11, a22), self.add_matrix(b11, b22))
        p2 = self.strassen(self.add_matrix(a21, a22), b11)
        p3 = self.strassen(a11, self.subtract_matrix(b12, b22))
        p4 = self.strassen(a22, self.subtract_matrix(b21, b11))
        p5 = self.strassen(self.add_matrix(a11, a12), b22)
        p6 = self.strassen(self.subtract_matrix(a21, a11), self.add_matrix(b11, b12))
        p7 = self.strassen(self.subtract_matrix(a12, a22), self.add_matrix(b21, b22))


        c11 = self.add_matrix(self.subtract_matrix(self.add_matrix(p1, p4), p5), p7)
        c12 = self.add_matrix(p3, p5)
        c21 = self.add_matrix(p2, p4)
        c22 = self.add_matrix(self.subtract_matrix(self.add_matrix(p1, p3), p2), p6)
    

        for i in range(mid):
            for j in range(mid):
                c[i][j] = c11[i][j]
                c[i][j + mid] = c12[i][j]
                c[i + mid][j] = c21[i][j]
                c[i + mid][j + mid] = c22[i][j]
        
        return c

    def subtract_matrix(self, m1, m2):
        result = [[0 for i in range(len(m1))] for j in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m1)):
                result[i][j] = m1[i][j] - m2[i][j]
        return result


    def time_run(self, func, m1, m2):
        pass

    def run(self):
        b = []
        d = []
        s = []
        for i in range(2, 50):
            m1 = self.make_matrix(i)
            m2 = self.make_matrix(i)


            # for i in range(len(m1)):
            #     print(m1[i], '   |   ', m2[i])
            # print()



            s_t = time.perf_counter()
            res = self.zarb_sade(m1, m2)
            e_t = time.perf_counter()
            b.append(round(e_t - s_t, 5))

            # for i in range(len(m1)):
            #     print(m1[i] , '   |   ', m2[i])
            # print()



            s_t = time.perf_counter()
            res = self.devide_conquer(m1, m2)
            e_t = time.perf_counter()
            d.append(round(e_t - s_t, 5))

            s_t = time.process_time()
            res = self.strassen(m1, m2)
            e_t = time.perf_counter()
            s.append(round(e_t - s_t, 5))
        # print(b)
        # print('-------------')
        # print(d)
        # print('---------------')
        # print(s)
        t = [i for i in range(2,50)]
        self.write_excel(b, d, s, t)
        self.write_plot(b, d, s, t)


    def write_excel(self, b, d, s, t):
        length = len(t)
        desktop_path = os.path.expanduser("~/Desktop/line_chart.xlsx") 
        workbook = xlsxwriter.Workbook(desktop_path)

        worksheet = workbook.add_worksheet()
        data = {'X': b, 'Y': t}
        worksheet.write_row(0, 0, ['time(simple)', 'run(simple)'])
        for i, (x, y) in enumerate(zip(data['X'], data['Y'])):
            worksheet.write_row(i + 1, 0, [x, y])
        chart = workbook.add_chart({'type': 'line'})
        chart.add_series({
            'name': 'Y',
            'categories': f'=Sheet1!$B$2:$B${length}',
            'values': f'=Sheet1!$A$2:$A$19{length}',
        })
        chart.set_title({'name': 'Ordinary'})
        chart.set_x_axis({'name': 'X'})
        chart.set_y_axis({'name': 'Y'})
        worksheet.insert_chart('H1', chart)




        data = {'D': d, 'T': t}
        worksheet.write_row(0, 2, ['time(D&C)', 'run(D&C)'])
        for i, (x, y) in enumerate(zip(data['D'], data['T'])):
            worksheet.write_row(i + 1, 2, [x, y])
        chart = workbook.add_chart({'type': 'line'})
        chart.add_series({
            'name': 'T',
            'categories': f'=Sheet1!$D$2:$D${length}',
            'values': f'=Sheet1!$C$2:$C${length}',
        })
        chart.set_title({'name': 'Devide and Conquer'})
        chart.set_x_axis({'name': 'D'})
        chart.set_y_axis({'name': 'T'})
        worksheet.insert_chart('H16', chart)


        data = {'A': s, 'B': t}
        worksheet.write_row(0, 4, ['time(Strassen)', 'run(Strassen)'])
        for i, (x, y) in enumerate(zip(data['A'], data['B'])):
            worksheet.write_row(i + 1, 4, [x, y])
        chart = workbook.add_chart({'type': 'line'})
        chart.add_series({
            'name': 'B',
            'categories': f'=Sheet1!$F$2:$F${length}',
            'values': f'=Sheet1!$E$2:$E${length}',
        })
        chart.set_title({'name': 'Strassen'})
        chart.set_x_axis({'name': 'A'})
        chart.set_y_axis({'name': 'B'})
        worksheet.insert_chart('P1', chart)


        workbook.close()

    def write_plot(self, b, d, s, t):
        plt.figure(figsize=(15, 5))

        # Chart 1
        plt.subplot(1, 3, 1)
        plt.plot(t, b, marker='o')
        plt.title('Basic multiplication')
        plt.xlabel('Run')
        plt.ylabel('Time (seconds)')

        # Chart 2
        plt.subplot(1, 3, 2)
        plt.plot(t, d, marker='o')
        plt.title('Divide & Conquer')
        plt.xlabel('Run')
        plt.ylabel('Time (seconds)')

        # Chart 3
        plt.subplot(1, 3, 3)
        plt.plot(t, s, marker='o')
        plt.title('Strassen')
        plt.xlabel('Run')
        plt.ylabel('Time (seconds)')

        plt.tight_layout()
        # plt.savefig('three_charts.png')
        plt.show()







        
z = zarbing()
print()
# print(z.add_one(z.make_matrix(3)))
# print(z.zarb_sade(z.make_matrix(3), z.make_matrix(3)))
# print(z.add_matrix(z.make_matrix(2), z.make_matrix(2)))
# print(z.devide_conquer(z.make_matrix(4), z.make_matrix(4)))
# print(z.strassen(z.make_matrix(4), z.make_matrix(4)))
m1 = [[78, 29, 15, 92], [77, 4, 9, 2], [24, 39, 66, 79], [54, 73, 45, 26]]
m2 = [[98, 57, 89, 8], [64, 62, 21, 59], [14, 43, 27, 59], [31, 16, 67, 6]]
# print(z.zarb_sade(m1,m2))
# print('------------------------------------------------')
# print(z.devide_conquer(m1, m2))
# print('------------------------------------------------')
# print(z.strassen(m1, m2))        

z.run()        