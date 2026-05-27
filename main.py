import time

class TuringMachine:
    def __init__(self, tape_string):
        self.tape = list(tape_string) + ['_'] * 100
        self.head_position = 0
        self.current_state = 'q_start'
        self.step_count = 1

    def print_step(self, read_sym, write_sym, direction):
        # Bantin okunabilir kismini temizle ve birlestir
        current_tape = "".join(self.tape).split('_')[0]
        if not current_tape:
            current_tape = "".join(self.tape).rstrip('_')
            
        print(f"Adim {self.step_count}:")
        print(f"  - Mevcut Durum  : {self.current_state}")
        print(f"  - Okunan Sembol : '{read_sym}'")
        print(f"  - Yazilan Sembol: '{write_sym}'")
        print(f"  - Kafa Hareketi : {'Sag (R)' if direction == 'R' else 'Sol (L)' if direction == 'L' else '-'}")
        print(f"  - Bant Icerigi  : {current_tape}")
        print("-" * 40)
        self.step_count += 1

    def get_transition(self, state, read_sym):
        # Baslangicta esittir isaretine kadar git
        if state == 'q_start':
            if read_sym in ['0', '1', '*']: return ('q_start', read_sym, 'R')
            if read_sym == '=': return ('q_read_N', '=', 'L')

        # Carpanin (N) bitlerini oku ve isaretle
        if state == 'q_read_N':
            if read_sym in ['X', 'Y', '=']: return ('q_read_N', read_sym, 'L')
            if read_sym == '0': return ('q_macro_shift', 'X', 'L')
            if read_sym == '1': return ('q_macro_add', 'Y', 'L')
            if read_sym == '*': return ('q_cleanup', '*', 'R')

        # Carpma bittikten sonra isaretlenen bitleri orijinal haline dondur
        if state == 'q_cleanup':
            if read_sym == 'X': return ('q_cleanup', '0', 'R')
            if read_sym == 'Y': return ('q_cleanup', '1', 'R')
            if read_sym == '*': return ('q_cleanup', '*', 'R')
            if read_sym == '=': return ('q_accept', '=', 'R')

        return ('q_reject', read_sym, 'R')

    def execute_macro_shift(self):
        # 0 okundugunda sadece kaydirma yapilir
        tape_str = "".join(self.tape).split('_')[0]
        m_part, rest = tape_str.split('*')
        n_part, r_part = rest.split('=')

        # Birinci sayinin (M) sonuna 0 ekleyerek sola kaydirma simulasyonu
        new_m = m_part + '0'
        new_tape_str = new_m + '*' + n_part + '=' + r_part

        self.tape = list(new_tape_str) + ['_'] * 100
        self.head_position = self.tape.index('=')
        self.current_state = 'q_read_N'
        self.print_step('-', '-', '-')

    def execute_macro_add(self):
        # 1 okundugunda once toplama, sonra kaydirma yapilir
        tape_str = "".join(self.tape).split('_')[0]
        m_part, rest = tape_str.split('*')
        n_part, r_part = rest.split('=')

        if not r_part: r_part = '0'

        # Binary Toplama Islemi
        m_val = int(m_part, 2)
        r_val = int(r_part, 2)
        new_r_bin = bin(m_val + r_val)[2:]

        # Birinci sayinin (M) sonuna 0 ekleyerek sola kaydirma simulasyonu
        new_m = m_part + '0'
        new_tape_str = new_m + '*' + n_part + '=' + new_r_bin

        self.tape = list(new_tape_str) + ['_'] * 100
        self.head_position = self.tape.index('=')
        self.current_state = 'q_read_N'
        self.print_step('-', '-', '-')

    def run(self):
        print("Turing Makinesi Simulasyonu Basliyor...\n")
        print("-" * 40)
        
        while self.current_state not in ['q_accept', 'q_reject']:
            # Makro durumlari kontrol et
            if self.current_state == 'q_macro_add':
                self.execute_macro_add()
                continue
            if self.current_state == 'q_macro_shift':
                self.execute_macro_shift()
                continue

            read_symbol = self.tape[self.head_position]
            transition = self.get_transition(self.current_state, read_symbol)
            
            if transition[0] == 'q_reject':
                print(f"HATA: Tanimsiz gecis! Durum: {self.current_state}, Okunan: {read_symbol}")
                break
                
            new_state, write_symbol, direction = transition
            
            # Banti guncelle ve adimi yazdir
            self.tape[self.head_position] = write_symbol
            self.print_step(read_symbol, write_symbol, direction)
            
            # Durum ve kafa pozisyonu guncellemesi
            self.current_state = new_state
            if direction == 'R':
                self.head_position += 1
            elif direction == 'L':
                self.head_position -= 1

        if self.current_state == 'q_accept':
            self.print_result()
        else:
            print("\nISLEM BASARISIZ (Red Durumu)!")

    def print_result(self):
        final_tape_str = "".join(self.tape).split('_')[0]
        if '=' in final_tape_str:
            binary_result = final_tape_str.split('=')[1]
            if not binary_result:
                binary_result = '0'
            print(f"\nISLEM TAMAMLANDI (Kabul Durumu)!")
            print(f"Sonuc (Binary) : {binary_result}")
            print(f"Sonuc (Decimal): {int(binary_result, 2)}")

def is_binary(string):
    return set(string).issubset({'0', '1'})

def main():
    num1 = input("Birinci sayiyi (binary) giriniz: ")
    num2 = input("Ikinci sayiyi (binary) giriniz: ")

    if not is_binary(num1) or not is_binary(num2):
        print("Hata: Girdilerin yalnizca 0 ve 1 icerdigini dogrulayiniz.")
        return

    tape_input = f"{num1}*{num2}="
    print(f"\nOlusturulan Baslangic Bant Formati: {tape_input}\n")
    
    tm = TuringMachine(tape_string=tape_input)
    tm.run()

if __name__ == "__main__":
    main()