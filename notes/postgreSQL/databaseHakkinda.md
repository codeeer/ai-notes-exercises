# PostgreSQL servisini başlat
brew services start postgresql@15

# Veritabanı oluştur
createdb testdb

# PostgreSQL'e bağlan (test için)

* psql testdb

- Test tablosu oluşturun
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

- Test verisi ekleyin
INSERT INTO users (name, email) VALUES 
('John Doe', 'john@example.com'),
('Jane Smith', 'jane@example.com');

- Veriyi kontrol edin
* SELECT * FROM users;

- Çıkmak için
* \q

# test için

psql -U omer -d testdb