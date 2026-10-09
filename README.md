Turing Makinesi ile Binary Çarpma

İki binary sayıyı çarpan bir Turing makinesi simülasyonu. Python ile yazıldı. Makine, çarpmayı kaydır ve topla (shift-and-add) yöntemiyle yapıyor ve her adımda bandın durumunu ekrana yazdırıyor.

Nasıl çalışır?

Girdiler bant üzerinde M*N= biçiminde tutulur. Makine:

= işaretine kadar sağa ilerler.
Çarpanın (N) bitlerini sağdan sola tek tek okur ve okuduğu biti işaretler (0 → X, 1 → Y).
Okunan bit 1 ise M sonuca eklenir ve M bir basamak sola kaydırılır. Bit 0 ise yalnızca kaydırma yapılır.
Tüm bitler okununca işaretler eski hâline döndürülür ve makine kabul durumuna geçer.
Toplama ve kaydırma işlemleri, simülasyonu sade tutmak için makro adımlar olarak uygulanmıştır.

Durumlar
Durum	Görevi
q_start	= işaretine kadar sağa ilerler
q_read_N	Çarpanın sıradaki bitini okur
q_macro_add	Toplama + kaydırma (bit = 1)
q_macro_shift	Yalnızca kaydırma (bit = 0)
q_cleanup	İşaretli bitleri geri yazar
q_accept / q_reject	Kabul / red
Çalıştırma
python main.py
Birinci sayiyi (binary) giriniz: 101
Ikinci sayiyi (binary) giriniz: 11
...
ISLEM TAMAMLANDI (Kabul Durumu)!
Sonuc (Binary) : 1111
Sonuc (Decimal): 15

Yalnızca 0 ve 1 içeren girdiler kabul edilir.
