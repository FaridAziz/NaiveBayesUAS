import pandas as pd
from probaspek import ProbAspek


class NaiveBayes:

    def __init__(self):
        pass

        # TODO: [LANGKAH-2] Buat property untuk menampung data dari file CSV
        self.data_training = None

        # TODO: [Langkah-3] Buat variabel dictionary untuk menampung matriks Probabilitas untuk semua aspek
        self.aspek_outlook = {'sunny': None, 'overcast': None, 'rainy': None}
        self.aspek_temperature = {'hot': None, 'mild': None, 'cool': None}
        self.aspek_humidity = {'high': None, 'normal': None}
        # self.aspek_windy = {'False': None, 'True': None}

        # TODO: [Langkah-4] Buat variabel untuk menampung Prior Probability
        self.prior_probability = {'no': 0, 'yes': 0}

    # TODO: [LANGKAH-5] Load data training dari file CSV
    def load_data_training(self):
        self.data_training = pd.read_csv('golf_df.csv', sep=',')
        print(self.data_training)

    # TODO: [LANGKAH-6] Membuat object ProbAspek untuk semua nilai pada aspek, sekaligus menghitung jumlah masuk dan bolosnya
    def buat_prob_aspek(self, nama_aspek: str, nilai_aspek: str) -> ProbAspek:
        prob_aspek = ProbAspek(nama_aspek, nilai_aspek)
        data_tidak_main = self.data_training.loc[(self.data_training[nama_aspek] == nilai_aspek) &
                                                 (self.data_training['Play'] == 'no')]
        data_main = self.data_training.loc[(self.data_training[nama_aspek] == nilai_aspek) &
                                           (self.data_training['Play'] == 'yes')]
        self.tidak_main = len(data_tidak_main)
        self.main = len(data_main)
        self.total = self.tidak_main + self.main
        prob_aspek.jml_no = len(data_tidak_main)
        prob_aspek.jml_yes = len(data_main)

        return prob_aspek

    # TODO: [LANGKAH-7] Mengisi semua nilai pada matris probabilitas aspek
    def mulai_training(self):
        # Aspek Outlook
        pc_sunny = self.buat_prob_aspek('Outlook', 'sunny')
        pc_overcast = self.buat_prob_aspek('Outlook', 'overcast')
        pc_rainy = self.buat_prob_aspek('Outlook', 'rainy')
        # Jadikan array
        arr_pc = [pc_sunny, pc_overcast, pc_rainy]
        # Hitung total masing-masing nilai aspek berapa kali muncul di bolos dan masuk
        total_c = ProbAspek.hitung_jml_total_aspek(arr_pc)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        pc_sunny.hitung_p_aspek_no(total_c['no']).hitung_p_aspek_yes(total_c['yes'])
        pc_overcast.hitung_p_aspek_no(total_c['no']).hitung_p_aspek_yes(total_c['yes'])
        pc_rainy.hitung_p_aspek_no(total_c['no']).hitung_p_aspek_yes(total_c['yes'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_pc)
        self.aspek_outlook['sunny'] = pc_sunny
        self.aspek_outlook['overcast'] = pc_overcast
        self.aspek_outlook['rainy'] = pc_rainy
        #     # TODO: [SOAL-1] Lengkapi fungsi ini untuk semua aspek!

        # Aspek Temperature

        ps_hot = self.buat_prob_aspek('Temperature', 'hot')
        ps_mild = self.buat_prob_aspek('Temperature', 'mild')
        ps_cool = self.buat_prob_aspek('Temperature', 'cool')
        arr_ps = [ps_hot, ps_mild, ps_cool]
        total_s = ProbAspek.hitung_jml_total_aspek(arr_ps)
        ps_hot.hitung_p_aspek_no(total_s['no']).hitung_p_aspek_yes(total_s['yes'])
        ps_mild.hitung_p_aspek_no(total_s['no']).hitung_p_aspek_yes(total_s['yes'])
        ps_cool.hitung_p_aspek_no(total_s['no']).hitung_p_aspek_yes(total_s['yes'])
        ProbAspek.print_matrix_probabilitas(arr_ps)
        self.aspek_temperature['hot'] = ps_hot
        self.aspek_temperature['mild'] = ps_mild
        self.aspek_temperature['cool'] = ps_cool

        # Aspek Humidity

        pt_high = self.buat_prob_aspek('Humidity', 'high')
        pt_normal = self.buat_prob_aspek('Humidity', 'normal')
        arr_pt = [pt_high, pt_normal]
        total_t = ProbAspek.hitung_jml_total_aspek(arr_pt)
        pt_high.hitung_p_aspek_no(total_t['no']).hitung_p_aspek_yes(total_t['yes'])
        pt_normal.hitung_p_aspek_no(total_t['no']).hitung_p_aspek_yes(total_t['yes'])
        ProbAspek.print_matrix_probabilitas(arr_pt)
        self.aspek_humidity['high'] = pt_high
        self.aspek_humidity['normal'] = pt_normal

    # TODO: [LANGKAH-8] Menghitung prior probability
    def hitung_prior_probability(self):
        pp_no = self.buat_prob_aspek('Play', 'no')
        pp_yes = self.buat_prob_aspek('Play', 'yes')
        arr_pp = [pp_yes, pp_no]
        total_p = ProbAspek.hitung_jml_total_aspek(arr_pp)
        self.prior_probability['no'] = total_p['no'] / (total_p['no'] + total_p['yes'])
        self.prior_probability['yes'] = total_p['yes'] / (total_p['no'] + total_p['yes'])

    #     # TODO: [SOAL-2] Prior Probability-nya masih 0, hitunglah prior probability yang sebenarnya!

    # TODO: [LANGKAH-9] Membuat method untuk memprediksi hasil akhir berdasarkan nilai aspek
    def prediksi(self, nilai_outlook: str, nilai_temperature: str, nilai_humidity: str):
        self.hitung_prior_probability()
        predict_tidak_main = self.prior_probability['no'] * \
                             self.aspek_outlook[nilai_outlook].p_aspek_no * \
                             self.aspek_temperature[nilai_temperature].p_aspek_no * \
                             self.aspek_humidity[nilai_humidity].p_aspek_no
        # self.aspek_windy[nilai_windy].p_aspek_no
        print('Peluang Tidak Main Golf: {}'.format(predict_tidak_main))
        predict_main = self.prior_probability['yes'] * \
                       self.aspek_outlook[nilai_outlook].p_aspek_yes * \
                       self.aspek_temperature[nilai_temperature].p_aspek_yes * \
                       self.aspek_humidity[nilai_humidity].p_aspek_yes
        # self.aspek_windy[nilai_windy].p_aspek_yes
        print('Peluang Main Golf: {}'.format(predict_main))

        # TODO: [SOAL-3] hasil prediksi masih '???' dan peluangnya masih 0. Bagaimana agar nilainya benar?
        if predict_main > predict_tidak_main:
            hasil = 'Main Golf'
            peluang = predict_main
        else:
            hasil = 'Tidak Main Golf'
            peluang = predict_tidak_main

        return {'hasil': hasil, 'peluang': peluang * 100}
