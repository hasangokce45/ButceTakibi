# ButceTakibi
Flask ile Bütçe Takip uygulaması

Bütçe takip uygulamasını flask ile geliştirdim. Html dosyalarını Bootstrap CSS framework’ünü kullanarak geliştirdim. Uygulamam kısaca girilen verileri hesaplayıp net bütçeyi hesaplıyor.
/gelirekle ve /giderekle url’lerinin metotlarını POST olarak belirledim. Diğer tüm url’ler varsayılan olarak GET metodu ile çalışıyor. Yani url kısmına elle /gelirekle ve /giderekle yazarak erişemiyoruz.
Girilen veriyi gelirEkle fonksiyonu gelir olarak, giderEkle fonksiyonu gider olarak veri tabanına kaydetmemizi sağlıyor. Veri tabanındaki bilgileri çekip hesapla fonksiyonu ile net bütçeyi hesaplıyoruz. Seçili veriyi silme işlemini dinamik bir url yapısına sahip olan islemSil fonksiyonu gerçekleştiriyor. Tüm verileri hepsiniSil fonksiyonuyla silebiliyoruz.
