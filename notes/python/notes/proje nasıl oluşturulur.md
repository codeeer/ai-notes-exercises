# FastAPI, PostgreSQL ve SQLAlchemy ile Proje Kurulumu

Bu rehber, FastAPI, PostgreSQL ve SQLAlchemy kullanarak modern bir Python web API projesinin temelini nasıl atacağınızı adım adım açıklamaktadır.

## 1. Proje Klasörünü Oluşturun

İlk olarak, projemiz için bir ana dizin oluşturup bu dizine geçiş yapalım.

```bash
mkdir python-user-api
cd python-user-api
```

## 2. Sanal Ortam (Virtual Environment) Oluşturun

Proje bağımlılıklarını sistem genelindeki Python paketlerinden izole etmek için bir sanal ortam oluşturmak en iyi pratiktir.

```bash
python3 -m venv venv
source venv/bin/activate
```
*   `python3 -m venv venv`: `venv` adında bir sanal ortam klasörü oluşturur.
*   `source venv/bin/activate`: Oluşturulan sanal ortamı aktif hale getirir. Komut satırınızın başında `(venv)` ifadesini görmelisiniz.

## 3. Gerekli Paketleri Kurun

Projemiz için gerekli olan Python kütüphanelerini `pip` kullanarak kuralım.

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

*   **fastapi**: Yüksek performanslı web framework'ümüz.
*   **uvicorn**: Projemizi çalıştıracak olan ASGI (Asynchronous Server Gateway Interface) sunucusu.
*   **sqlalchemy**: Veritabanı ile etkileşim kurmamızı sağlayan ORM (Object-Relational Mapper).
*   **psycopg2-binary**: Python'un PostgreSQL veritabanı ile konuşmasını sağlayan adaptör.
*   **python-dotenv**: `.env` dosyasından ortam değişkenlerini (örneğin veritabanı şifreleri) yüklemek için kullanılır.

## 4. Proje Yapısını Oluşturun

İyi organize edilmiş bir proje yapısı, kodun bakımı ve geliştirilmesini kolaylaştırır. Aşağıdaki komutlarla temel dosya ve klasör yapısını oluşturalım.

```bash
mkdir app
touch app/__init__.py app/main.py app/database.py app/models.py app/schemas.py app/crud.py
touch .env requirements.txt
```

Oluşturulan dosya ve klasörlerin görevleri:

*   `app/`: Ana uygulama kodlarımızın bulunacağı paket klasörü.
*   `app/__init__.py`: `app` klasörünün bir Python paketi olarak tanınmasını sağlar.
*   `app/main.py`: FastAPI uygulamasının oluşturulduğu ve API endpoint'lerinin tanımlandığı ana dosya.
*   `app/database.py`: Veritabanı bağlantısı ve oturum (session) yönetimi ayarlarını içerir.
*   `app/models.py`: SQLAlchemy ORM modellerinin (veritabanı tablolarına karşılık gelen Python sınıfları) tanımlandığı yer.
*   `app/schemas.py`: Pydantic modellerinin (API'ye gelen ve giden verilerin şeklini, türünü ve doğruluğunu kontrol eden şemalar) bulunduğu dosya.
*   `app/crud.py`: Veritabanı üzerinde temel CRUD (Create, Read, Update, Delete) işlemlerini gerçekleştiren fonksiyonları içerir.
*   `.env`: Veritabanı bağlantı bilgileri gibi hassas veya ortama özgü verileri saklamak için kullanılır. Bu dosya genellikle `.gitignore` dosyasına eklenerek versiyon kontrolüne dahil edilmez.
*   `requirements.txt`: Projenin bağımlı olduğu paketleri ve versiyonlarını listeleyen dosyadır. Bu, projenin başka bir ortamda kolayca kurulabilmesini sağlar.

### Bağımlılıkları Listeleme

Kurduğumuz paketleri `requirements.txt` dosyasına ekleyelim:

```bash
pip freeze > requirements.txt
```

## FastAPI Otomatik Dokümantasyon

FastAPI'nin en güçlü özelliklerinden biri, kodunuzdan otomatik olarak interaktif API dokümantasyonu oluşturmasıdır. Projenizi `uvicorn` ile başlattıktan sonra aşağıdaki adreslerden dokümantasyona erişebilirsiniz:

*   **Swagger UI**: http://localhost:8000/docs
    *   API endpoint'lerinizi interaktif olarak test etmenizi sağlayan bir arayüz.
*   **ReDoc**: http://localhost:8000/redoc
    *   Daha temiz ve sadece okunabilir bir dokümantasyon görünümü sunar.

# Proje Çalıştırma Komutları

## Virtual environment aktif edip paketleri kurun:

```bash
source venv/bin/activate
pip install -r requirements.txt
```
## Virtual enviroment deactive etmek için: 

```bash
deactivate
```

## Projemizi çalıştırın:

```bash
uvicorn app.main:app --reload --port 8000
```
    