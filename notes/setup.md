# macOS Yapay Zeka Notlari

## Homebrew ile Python ve gerekli araçları kurun
* brew install python@3.11
* brew install git
* brew install --cask visual-studio-code

----
## VS Code Extensions (Eklentiler):
- Python (Microsoft)
- Jupyter (Microsoft)
- Python Docstring Generator
- GitLens
- Thunder Client (API testleri için)

----
## n8n install
* `brew install node` --> node ve npm i kurar.
* `https` olarak kalkması için aşağıdaki komutları çalıştırın:
  ```bash
  export N8N_SSL_KEY=~/n8n-certs/key.pem
  export N8N_SSL_CERT=~/n8n-certs/cert.pem
  export N8N_PORT=5678
  export N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
  export N8N_RUNNERS_ENABLED=true
  export N8N_SECURE_COOKIE=true
  npx n8n
  ```
* .env dosyası oluşturulmaz ise her seferinde workflowlar silinir.
```bash
  touch .env
  # HTTPS aktif
  N8N_PROTOCOL=https
  N8N_PORT=5678
  NODE_ENV=production

  # Sertifika yolları
  N8N_SSL_KEY=/Users/<kullanıcı_adın>/n8n-local-certs/key.pem
  N8N_SSL_CERT=/Users/<kullanıcı_adın>/n8n-local-certs/cert.pem

  # Verilerin kaybolmaması için
  N8N_USER_FOLDER=/Users/<kullanıcı_adın>/n8n-local-data
 ```
---
## Twitter post atmak için adım adım yapılması gerekenler.
---
### google trend için serpapi kullan

* https://serpapi.com/search

### open api kullan 

* https://api.openai.com/v1 

### twitter api kullan 
* https://developer.x.com/en/portal/dashboard

### perplexity ai
* https://www.perplexity.ai/

### console cloud google for sheet excel
* https://console.cloud.google.com/