

# JSONPlaceholder API Test Otomasyonu Projem
**Bu doküman Türkçe versiyondur. İngilizce için lütfen tıklayın [README.md](README.md).**

Bu proje, [JSONPlaceholder](https://jsonplaceholder.typicode.com/) sahte API servisi üzerinde RESTful istekleri test etmek amacıyla geliştirilmiş bir **API Test Otomasyon** sistemidir. Projede Python, `pytest` ve `requests` kütüphanesi kullanılarak GET, POST, PUT, PATCH ve DELETE istekleri test edilmiştir.

## Özellikler

- GET istekleri ile veri doğrulama
- POST isteği ile veri gönderimi ve doğrulama
- PUT ve PATCH ile veri güncelleme testleri
- DELETE ile silme işlemi testi
- `pytest` ile test senaryoları
- Test sonuçlarının `log` dosyasına yazılması
- POM (Page Object Model) benzeri yapı ile temiz kod organizasyonu

## Proje Yapısı

```bash

├── api_json.py               # API işlemlerini yöneten sınıf (GET, POST, PUT, PATCH, DELETE)
├── test_api_response.py      # API test senaryoları
├── test_post_operations.py   # POST, PUT, PATCH, DELETE testleri
├── test_log.log              # Test loglarının tutulduğu dosya
├── conftest.py               # Pytest log yapılandırma ayarları
└── README.md                 # Bu dosya
````

## Kurulum

> Bu projeyi çalıştırmadan önce Python 3 kurulu olmalıdır.


```pip install requests pytest ```

## Testleri Çalıştırma

Tüm testleri çalıştırmak için terminalden aşağıdaki komutu kullanabilirsin:


```pytest```


Log dosyasına yazılan çıktıların bulunduğu dosya: `test_log.log`

## Örnek Testlerden Bazıları

* `GET /posts/1` → ID'ye göre gönderi içeriğini doğrulama
* `GET /posts/1/comments` → Gönderiye ait yorumları kontrol etme
* `POST /posts` → Yeni gönderi oluşturma
* `PUT /posts/1` → Tüm içeriği güncelleme
* `PATCH /posts/1` → Sadece belirli alanı güncelleme
* `DELETE /posts/1` → Belirli gönderiyi silme

## Kullanılan Teknolojiler

* Python
* Requests
* Pytest
* JSONPlaceholder (Fake REST API)

## Notlar
* Bu proje gerçek bir API’ye değil, test amaçlı hazırlanmış sahte bir REST servisine istek gönderir.**
* JSONPlaceholder, verileri sunucu tarafında gerçekten değiştirmez (POST, PUT, DELETE işlemleri simülasyon olarak çalışır).



**Adınız:** Erkut Elik
**GitHub:** https://github.com/erkutelk




