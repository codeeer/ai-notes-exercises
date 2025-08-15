# VS Code ile Spring Boot Projesi Oluşturma Rehberi

Bu rehber, Visual Studio Code kullanarak [Spring Initializr](https://start.spring.io/) aracılığıyla yeni bir Spring Boot projesinin nasıl oluşturulacağını adım adım açıklamaktadır.

## Adım 1: Spring Initializr'ı Başlatma

VS Code içerisinde Komut Paleti'ni (Command Palette) açın:

*   **macOS:** `Cmd + Shift + P`
*   **Windows/Linux:** `Ctrl + Shift + P`

Açılan palete `Spring Initializr` yazın ve **"Spring Initializr: Create a Maven Project"** seçeneğini seçin.

## Adım 2: Proje Ayarlarını Yapılandırma

Spring Initializr sizden projeniz için temel bilgileri girmenizi isteyecektir. Aşağıdaki adımları takip edin:

1.  **Spring Boot Version:** En son stabil sürümü (örneğin, `3.x.x`) seçin. Genellikle varsayılan olarak gelen önerilen sürüm uygundur.
2.  **Project Language:** `Java` seçin.
3.  **Group Id:** Projenizin paket yapısını belirten benzersiz bir kimlik girin. Genellikle ters alan adı formatı kullanılır (örn: `com.example`).
4.  **Artifact Id:** Projenizin adını girin (örn: `demo` veya `user-api`). Bu, oluşturulacak Jar dosyasının adı olacaktır.
5.  **Packaging Type:** `Jar` seçeneğini seçin. Bu, projenizin tek bir çalıştırılabilir dosya olarak paketlenmesini sağlar.
6.  **Java Version:** Projenizde kullanmak istediğiniz Java sürümünü seçin. Genellikle en son LTS (Long-Term Support) sürümü olan `17` veya `21` tercih edilir.

## Adım 3: Bağımlılıkları (Dependencies) Seçme

Son olarak, projenizin ihtiyaç duyacağı kütüphaneleri (bağımlılıkları) seçmeniz istenecektir. Aşağıdaki temel bağımlılıkları seçerek başlayabilirsiniz:

*   **Spring Web:**
    *   RESTful API'ler ve web uygulamaları oluşturmak için gereklidir.
    *   Apache Tomcat'i gömülü sunucu olarak içerir.
*   **Spring Data JPA:**
    *   Veritabanı işlemlerini kolaylaştırmak için kullanılır.
    *   Java Persistence API (JPA) standartlarını kullanarak veritabanı tablolarını Java nesneleri (Entity) ile eşlemenizi sağlar.
*   **PostgreSQL Driver:**
    *   Uygulamanızın PostgreSQL veritabanı ile iletişim kurmasını sağlayan JDBC sürücüsüdür.
*   **Spring Boot DevTools:**
    *   Geliştirme sürecini hızlandıran araçlar sunar.
    *   Kodunuzda bir değişiklik yaptığınızda uygulamanın otomatik olarak yeniden başlatılması (live reload) gibi özellikler sağlar.

Seçimleri tamamladıktan sonra, projenin oluşturulacağı klasörü seçin. Spring Initializr, gerekli tüm dosyaları ve `pom.xml` dosyasını bağımlılıklarınızla birlikte oluşturacaktır.