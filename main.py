import tkmacosx

from naivebayes import NaiveBayes
from tkinter import *
import tkinter as tk

class Main:
    @staticmethod
    def main():
        nb = NaiveBayes()
        nb.load_data_training()
        nb.mulai_training()

        def process():
            nilai1 = ent1.get()
            nilai2 = ent2.get()
            nilai3 = ent3.get()

            hasil_prediksi = nb.prediksi(nilai_outlook=nilai1,
                                         nilai_temperature=nilai2,
                                         nilai_humidity=nilai3)

            result = tk.Label(text="Hasil akhir prediksi = \n" +
                                   hasil_prediksi['hasil'] +
                                   ", dengan peluang sebesar "+
                                   str(hasil_prediksi['peluang'])+" %")
            result.place(x=10, y=180)

            print('=====================================')

            print('Hasil akhir prediksi = {}, dengan peluang sebesar {}%'.format(hasil_prediksi['hasil'],
                                                                                 hasil_prediksi['peluang']))

        window = tk.Tk()
        window.geometry("400x250")
        window.title('Prediksi Main Golf')
        judul = tk.Label(text="Jadi Main Golf atau tidak?")
        judul.pack()
        label1 = tk.Label(text="Masukan Outlook          : ")
        label1.place(x = 10, y = 30)
        ent1 = tk.Entry()
        ent1.place(x = 170, y = 30)
        label2 = tk.Label(text="Masukan Temperature : ")
        label2.place(x=10, y=60)
        ent2 = tk.Entry()
        ent2.place(x=170, y=60)
        label3 = tk.Label(text="Masukan Humidity        : ")
        label3.place(x=10, y=90)
        ent3 = tk.Entry()
        btn_cek = tkmacosx.Button(text = "cek", command = process)
        btn_cek.place(x=150, y=130)
        ent3.place(x=170, y=90)




        window.mainloop()

        # # TODO: [LANGKAH-10] Cobalah untuk melakukan prediksi!
        # hasil_prediksi = nb.prediksi(nilai_outlook='sunny',
        #                              nilai_temperature='hot',
        #                              nilai_humidity='high')
        # print('=====================================')
        #
        # print('Hasil akhir prediksi = {}, dengan peluang sebesar {}%'.format(hasil_prediksi['hasil'],
        #                                                                      hasil_prediksi['peluang']))


Main.main()
