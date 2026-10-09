# ✖️ Binary Çarpan Turing Makinesi

İki binary sayıyı **kaydır-ve-topla (shift-and-add)** yöntemiyle çarpan, her adımı bant üzerinde canlı olarak gösteren bir Turing makinesi simülasyonu.

> `101 * 11 =` → `1111` (5 × 3 = 15)

## 🎯 Özellikler

- ✅ Kullanıcıdan alınan iki binary sayının çarpımı
- ✅ Adım adım izleme: durum, okunan/yazılan sembol, kafa hareketi ve bant içeriği
- ✅ Okunan bitlerin `X` / `Y` ile işaretlenmesi ve işlem sonunda geri yazılması
- ✅ Sonucun hem binary hem decimal olarak gösterilmesi
- ✅ Hatalı girdi kontrolü (yalnızca `0` ve `1`)

## 🛠️ Teknik Detaylar

- **Bant Formatı:** Girdiler bant üzerinde `M*N=` biçiminde tutulur; sonuç `=` işaretinin sağına yazılır.
- **Kaydır-ve-Topla Algoritması:** Çarpanın (`N`) bitleri sağdan sola okunur. Bit `1` ise çarpılan (`M`) sonuca eklenir, ardından `M` bir basamak sola kaydırılır. Bit `0` ise yalnızca kaydırma yapılır. Elle çarpma yaparken kullandığımız yöntemin binary karşılığıdır.
- **İşaretleme:** Okunan her bit `0 → X`, `1 → Y` olarak işaretlenir; böylece makine hangi bitlerin işlendiğini kaybetmez. `q_cleanup` durumunda bant eski hâline döndürülür.
- **Makro Adımlar:** Toplama ve kaydırma işlemleri, simülasyonu okunabilir tutmak için `q_macro_add` ve `q_macro_shift` durumlarında tek adımda gerçekleştirilir.

## 🔄 Durumlar

| Durum | Okunan | Ne yapar? | Sonraki durum |
|---|---|---|---|
| `q_start` | `0`, `1`, `*` | Sağa ilerler | `q_start` |
| `q_start` | `=` | Çarpanı okumaya başlar | `q_read_N` |
| `q_read_N` | `1` | `Y` ile işaretler | `q_macro_add` |
| `q_read_N` | `0` | `X` ile işaretler | `q_macro_shift` |
| `q_macro_add` | – | Toplar ve kaydırır | `q_read_N` |
| `q_macro_shift` | – | Yalnızca kaydırır | `q_read_N` |
| `q_read_N` | `*` | Tüm bitler okundu | `q_cleanup` |
| `q_cleanup` | `X`, `Y` | Bitleri geri yazar | `q_cleanup` |
| `q_cleanup` | `=` | İşlem biter | `q_accept` ✅ |

## 🚀 Çalıştırma

```bash
python main.py
```

## 📸 Örnek Çıktı

```
Birinci sayiyi (binary) giriniz: 101
Ikinci sayiyi (binary) giriniz: 11

Olusturulan Baslangic Bant Formati: 101*11=

Turing Makinesi Simulasyonu Basliyor...

----------------------------------------
Adim 1:
  - Mevcut Durum  : q_start
  - Okunan Sembol : '1'
  - Yazilan Sembol: '1'
  - Kafa Hareketi : Sag (R)
  - Bant Icerigi  : 101*11=
----------------------------------------
...
ISLEM TAMAMLANDI (Kabul Durumu)!
Sonuc (Binary) : 1111
Sonuc (Decimal): 15
```
