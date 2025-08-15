# PostgreSQL Kurulum ve Temel Komutlar (macOS)

Bu rehber, [Homebrew](https://brew.sh/) ile macOS üzerine kurulan PostgreSQL veritabanının nasıl yönetileceğini ve temel komutların nasıl kullanılacağını açıklamaktadır.

## 1. PostgreSQL Servisini Başlatma

PostgreSQL sunucusunu bilgisayarınızda bir servis olarak başlatmak için aşağıdaki komutu kullanın. Bu komut, servisi arka planda çalıştırır ve bilgisayarınız her yeniden başladığında otomatik olarak başlamasını sağlar.

```bash
brew services start postgresql@15
```

## 2. Yeni Veritabanı Oluşturma

Yeni bir veritabanı oluşturmak için `createdb` komutunu ve ardından veritabanı adını kullanabilirsiniz.

```bash
createdb testdb
```
Bu komut, `testdb` adında yeni ve boş bir veritabanı oluşturur.

## 3. Veritabanına Bağlanma ve Temel İşlemler

`psql`, PostgreSQL ile etkileşime geçmek için kullanılan komut satırı aracıdır.

### a. Veritabanına Bağlanma

Oluşturduğunuz `testdb` veritabanına bağlanmak için:

```bash
psql testdb
```

### b. Temel SQL Komutları

Bağlantı kurulduktan sonra `psql` terminali üzerinden SQL komutları çalıştırabilirsiniz.

*   **Test Tablosu Oluşturma:**
    ```sql
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE
    );
    ```
*   **Test Verisi Ekleme:**
    ```sql
    INSERT INTO users (name, email) VALUES 
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com');
    ```
*   **Veriyi Kontrol Etme:**
    ```sql
    SELECT * FROM users;
    ```

### c. psql'den Çıkış

`psql` interaktif terminalinden çıkmak için `\q` komutunu kullanın.

```sql
\q
```

## 4. Belirli Bir Kullanıcı ile Bağlanma

Eğer veritabanına belirli bir kullanıcı adı ile bağlanmanız gerekiyorsa, `-U` (user) ve `-d` (database) parametrelerini kullanabilirsiniz.

```bash
psql -U omer -d testdb
```
Bu komut, `omer` kullanıcısı ile `testdb` veritabanına bağlanmaya çalışır.
