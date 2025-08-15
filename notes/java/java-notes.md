# Spring Boot Projesini Maven ile Yönetme ve Çalıştırma

Bu rehber, bir Spring Boot projesini yönetmek için kullanılan temel Maven komutlarını açıklamaktadır. Komutlar, projenin kök dizininde (`pom.xml` dosyasının bulunduğu yerde) çalıştırılmalıdır.

## Maven Wrapper (`mvnw`) Hakkında

Spring Initializr ile oluşturulan projeler genellikle bir "Maven Wrapper" (`mvnw`) içerir. Bu araç, sisteminize ayrıca Maven kurmanıza gerek kalmadan, projenin gerektirdiği doğru Maven sürümünü kullanarak komutları çalıştırmanızı sağlar.

*   **macOS/Linux için:** `./mvnw`
*   **Windows için:** `mvnw.cmd`

Aşağıdaki örneklerde macOS/Linux uyumlu `./mvnw` komutu kullanılacaktır.

---

## 1. Projeyi Temizleme (`clean`)

`clean` komutu, önceki derlemelerden kalan ve derlenmiş sınıfları, test sonuçlarını ve paketlenmiş dosyaları içeren `target` klasörünü siler. Bu, projenin "temiz" bir durumda yeniden derlenmesini garanti eder.

```bash
./mvnw clean
```

## 2. Projeyi Derleme ve Paketleme (`package`)

`package` komutu, proje kodunu derler, testleri çalıştırır ve `pom.xml` dosyasında belirtilen paketleme türüne (genellikle `Jar`) göre `target` klasörü içinde çalıştırılabilir bir dosya oluşturur. Bu komut genellikle `clean` ile birlikte kullanılır:

```bash
./mvnw clean package
```

## 3. Projeyi Geliştirme Ortamında Çalıştırma (`run`)

`spring-boot:run` komutu, uygulamayı derler ve Spring Boot'un gömülü sunucusunda (genellikle Tomcat) çalıştırır. Bu, geliştirme sırasında hızlı testler yapmak için idealdir. `spring-boot-devtools` bağımlılığı varsa, kodda yapılan değişikliklerde uygulamanın otomatik olarak yeniden başlatılmasını sağlar.

```bash
./mvnw spring-boot:run
```