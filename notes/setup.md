# macOS için Yapay Zeka Geliştirme Ortamı Kurulumu ve Notlar

Bu rehber, macOS üzerinde bir yapay zeka geliştirme ortamı kurmak için gerekli adımları ve araçları özetlemektedir.

## 1. Temel Geliştirme Araçlarının Kurulumu

Geliştirme sürecinde ihtiyaç duyacağımız temel araçları [Homebrew](https://brew.sh/) paket yöneticisi ile kuracağız.

```bash
# Belirli bir Python versiyonunu kurar
brew install python@3.11

# Versiyon kontrol sistemi olan Git'i kurar
brew install git

# Visual Studio Code metin editörünü kurar
brew install --cask visual-studio-code
```

## 2. Önerilen Visual Studio Code Eklentileri

Verimliliği artırmak için VS Code'a aşağıdaki eklentileri kurmanız önerilir:

-   **Python (Microsoft):** Python dil desteği, kod tamamlama, linting ve hata ayıklama özellikleri sunar.
-   **Jupyter (Microsoft):** VS Code içinde Jupyter Notebook'ları oluşturma ve çalıştırma imkanı sağlar.
-   **Python Docstring Generator:** Fonksiyonlarınız için kolayca dokümantasyon metinleri (docstrings) oluşturmanıza yardımcı olur.
-   **GitLens:** Kodunuzun her satırını kimin, ne zaman değiştirdiğini göstererek Git entegrasyonunu güçlendirir.
-   **Thunder Client:** VS Code'dan ayrılmadan API istekleri göndermenizi ve test etmenizi sağlayan hafif bir REST istemcisi.

## 3. n8n Kurulumu ve Yapılandırması

[n8n](https://n8n.io/), farklı servisleri birbirine bağlayarak iş akışları (workflow) otomasyonu yapmanızı sağlayan bir araçtır.

### Kurulum

n8n, Node.js tabanlı olduğu için öncelikle Node.js ve npm'i kurmamız gerekiyor.

```bash
# Node.js ve npm paket yöneticisini kurar
brew install node
```

### Kalıcı ve Güvenli Çalıştırma

n8n'i her başlattığınızda iş akışlarınızın kaybolmaması ve güvenli (HTTPS) bir şekilde çalışması için bir `.env` dosyası ile yapılandırmak en iyi yöntemdir.

1.  **`.env` Dosyası Oluşturun:**
    Aşağıdaki içeriğe sahip bir `.env` dosyası oluşturun ve `<kullanıcı_adın>` kısımlarını kendi kullanıcı adınızla güncelleyin.

    ```bash
    # .env
    
    # Üretim ortamı için ayarlar
    NODE_ENV=production
    
    # HTTPS'i etkinleştirir
    N8N_PROTOCOL=https
    N8N_PORT=5678
    N8N_SECURE_COOKIE=true
    
    # Sertifika dosyalarının yolları (Lütfen kendi sertifika yollarınızla değiştirin)
    N8N_SSL_KEY=/Users/<kullanıcı_adın>/n8n-local-certs/key.pem
    N8N_SSL_CERT=/Users/<kullanıcı_adın>/n8n-local-certs/cert.pem
    
    # n8n verilerinin (iş akışları, kimlik bilgileri vb.) saklanacağı klasör
    # Bu ayar verilerinizin kalıcı olmasını sağlar.
    N8N_USER_FOLDER=/Users/<kullanıcı_adın>/n8n-local-data
    ```

2.  **n8n'i Başlatın:**
    `.env` dosyasının bulunduğu dizinde aşağıdaki komutu çalıştırarak n8n'i başlatabilirsiniz. `npx`, paketi lokal olarak indirip çalıştırır.

    ```bash
    npx n8n
    ```

## 4. AI Destekli Sosyal Medya Otomasyonu için Faydalı Servisler

Aşağıda, yapay zeka destekli bir Twitter gönderi otomasyonu projesinde kullanılabilecek bazı servisler ve API'ler listelenmiştir.

-   **SerpApi:** serpapi.com
    -   Google Trends gibi arama motoru sonuçlarını programatik olarak çekmek için kullanılır. Popüler konuları belirlemede faydalıdır.
-   **OpenAI API:** api.openai.com/v1
    -   Metin üretme, özetleme gibi görevler için GPT modellerine erişim sağlar. Tweet içeriklerini oluşturmak için idealdir.
-   **Twitter API:** developer.x.com
    -   Twitter'a programatik olarak gönderi (tweet) atmak, veri çekmek ve diğer işlemleri yapmak için kullanılır.
-   **Perplexity AI:** perplexity.ai
    -   Araştırma yapmak ve içerik fikirleri bulmak için kullanılabilecek, kaynakları belirten bir yapay zeka arama motoru.
-   **Google Cloud Console (Google Sheets API):** console.cloud.google.com
    -   Oluşturulacak tweet'leri, fikirleri veya performans verilerini bir Google E-Tablosu'nda saklamak ve yönetmek için kullanılabilir.