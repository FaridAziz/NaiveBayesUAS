class ProbAspek:

    def __init__(self, nama_aspek: str, nilai_aspek: str):
        pass
    # TODO: [LANGKAH-1] Buat class untuk menampung nilai matriks probabilitas

        self.nama_aspek = nama_aspek
        self.nilai_aspek = nilai_aspek
        self.jml_no = 0
        self.jml_yes = 0
        self.p_aspek_no = 0
        self.p_aspek_yes = 0

    def hitung_p_aspek_no(self, jml_total_no_aspek):
        self.p_aspek_no = self.jml_no / jml_total_no_aspek
        return self

    def hitung_p_aspek_yes(self, jml_total_yes_aspek):
        self.p_aspek_yes = self.jml_yes / jml_total_yes_aspek
        return self

    def print(self):
        print('Aspek    : {}'.format(self.nama_aspek))
        print('Nilai    : {}'.format(self.nilai_aspek))
        print('Jml No   : {}'.format(self.jml_no))
        print('Jml Yes  : {}'.format(self.jml_yes))
        print('P({}|No) : {}'.format(self.nilai_aspek, self.p_aspek_no))
        print('P({}|Yes): {}'.format(self.nilai_aspek, self.p_aspek_yes))
        print('------------------------------------------')

    @staticmethod
    def hitung_jml_total_aspek(pa_list: list) -> dict:
        jumlah = {'no': 0, 'yes': 0}
        for pa in pa_list:
            jumlah['no'] += pa.jml_no
            jumlah['yes'] += pa.jml_yes
        return jumlah

    @staticmethod
    def print_matrix_probabilitas(pa_list: list):
        for pa in pa_list:
            pa.print()
