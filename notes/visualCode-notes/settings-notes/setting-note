# Visual Studio Code Ayarları Açıklamalı Rehber

Bu dosya, `settings.json` dosyasında bulunan Visual Studio Code ayarlarının ne anlama geldiğini ve ne işe yaradığını açıklamaktadır.

---

## Genel Editör Ayarları

Bu ayarlar, metin editörünün genel davranışını ve görünümünü kontrol eder.

```json
"editor.fontSize": 14,
"editor.tabSize": 4,
"editor.insertSpaces": true,
"editor.wordWrap": "on",
"editor.minimap.enabled": true,
"editor.guides.bracketPairs": "active",
"editor.bracketPairColorization.enabled": true,
```
-   `"editor.fontSize"`: Editördeki yazı tipi boyutunu belirler.
-   `"editor.tabSize"`: `Tab` tuşuna basıldığında kaç boşluk bırakılacağını ayarlar.
-   `"editor.insertSpaces"`: `Tab` tuşuna basıldığında boşluk karakterleri eklenmesini sağlar.
-   `"editor.wordWrap"`: Uzun satırların ekran dışına taşmasını engeller ve alt satıra kaydırır.
-   `"editor.minimap.enabled"`: Kodun genel bir önizlemesini gösteren sağdaki mini haritayı etkinleştirir.
-   `"editor.guides.bracketPairs"`: Birbiriyle eşleşen parantezlerin (`()`, `{}`, `[]`) arasına bir kılavuz çizgisi çizer.
-   `"editor.bracketPairColorization.enabled"`: İç içe geçmiş parantezleri farklı renklerde göstererek okunabilirliği artırır.

### Kod Tamamlama ve Öneriler

```json
"editor.suggestSelection": "first",
"editor.acceptSuggestionOnCommitCharacter": false,
"editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
},
```
-   `"editor.suggestSelection"`: Öneri listesi açıldığında ilk önerinin seçili gelmesini sağlar.
-   `"editor.acceptSuggestionOnCommitCharacter"`: `;` veya `.` gibi karakterlere basıldığında öneriyi otomatik olarak kabul etmeyi devre dışı bırakır.
-   `"editor.quickSuggestions"`: Kod yazarken (`other`), yorum satırlarında (`comments`) ve metinlerde (`strings`) otomatik önerilerin çıkıp çıkmayacağını kontrol eder.

---

## Dosya ve Kaydetme Ayarları

```json
"files.autoSave": "afterDelay",
"files.autoSaveDelay": 1000,
"editor.formatOnSave": true,
"editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
},
```
-   `"files.autoSave"`: Dosyaların belirli bir gecikmeden sonra otomatik olarak kaydedilmesini sağlar.
-   `"files.autoSaveDelay"`: Otomatik kaydetme için beklenecek süreyi milisaniye cinsinden belirler (1000ms = 1 saniye).
-   `"editor.formatOnSave"`: Dosya her kaydedildiğinde, tanımlı formatlayıcı (Prettier, Black vb.) ile kodun otomatik olarak biçimlendirilmesini sağlar.
-   `"editor.codeActionsOnSave"`: Kaydetme sırasında `import` ifadelerinin otomatik olarak organize edilmesini (gereksizleri silme, sıralama) sağlar.

---

## Git Entegrasyonu

```json
"git.autofetch": true,
"git.confirmSync": false,
"git.enableSmartCommit": true,
```
-   `"git.autofetch"`: Uzak depodaki (remote) değişiklikleri periyodik olarak otomatik çeker.
-   `"git.confirmSync"`: "Sync Changes" (Değişiklikleri Eşitle) butonuna basıldığında ek bir onay istemeden işlemi gerçekleştirir.
-   `"git.enableSmartCommit"`: Değişiklik yapılmamış dosyaları "stage" alanına ekleyerek boş commit'ler yapmayı engeller.

---

## Dile Özgü Ayarlar

### Java ve Spring Boot

```json
/* "java.jdt.ls.java.home": "/opt/homebrew/opt/openjdk@17",
"java.configuration.runtimes": [
    { "name": "JavaSE-17", "path": "/opt/homebrew/opt/openjdk@17" }
],*/
"java.compile.nullAnalysis.mode": "automatic",
"java.format.settings.url": "https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-java-google-style.xml",
"spring-boot.ls.problem.application-properties.unknown-property": "warning",
```
-   `java.jdt.ls.java.home` ve `java.configuration.runtimes` (yorum satırında): VS Code'un Java projeleri için hangi JDK'yı kullanacağını belirtir.
-   `"java.compile.nullAnalysis.mode"`: Null-pointer hatalarını önlemek için kod analizini otomatik olarak yapar.
-   `"java.format.settings.url"`: Java kodu formatlaması için Google'ın stil rehberini kullanır.
-   `"spring-boot.ls.problem...unknown-property"`: `application.properties` dosyasında Spring Boot tarafından tanınmayan bir özellik kullanıldığında hata yerine uyarı gösterir.

### Python

```json
"python.defaultInterpreterPath": "/opt/homebrew/bin/python3",
"python.formatting.provider": "black",
"python.linting.enabled": true,
"python.linting.pylintEnabled": true,
"python.linting.flake8Enabled": false,
"python.analysis.typeCheckingMode": "standard",
"[python]": {
    "editor.tabSize": 4,
    "editor.formatOnSave": true
}
```
-   `"python.defaultInterpreterPath"`: Projeler için varsayılan Python yorumlayıcısının yolunu belirtir.
-   `"python.formatting.provider"`: Python kodunu formatlamak için `black` kütüphanesini kullanır.
-   `"python.linting..."`: Kod analizi (linting) için `pylint`'i etkinleştirir, `flake8`'i devre dışı bırakır.
-   `"python.analysis.typeCheckingMode"`: Python için standart seviyede tip kontrolü yapar.
-   `"[python]"`: Sadece `.py` uzantılı dosyalarda geçerli olacak şekilde `tab` boyutunu 4 yapar ve kaydetmede formatlamayı etkinleştirir.

### JavaScript, React, TypeScript

```json
"emmet.includeLanguages": { "javascript": "javascriptreact" },
"emmet.triggerExpansionOnTab": true,
"eslint.validate": ["javascript", "javascriptreact", "typescript", "typescriptreact"],
"prettier.singleQuote": true,
"prettier.semi": true,
"prettier.trailingComma": "es5",
"[javascript]": { "editor.tabSize": 2, "editor.formatOnSave": true },
"[javascriptreact]": { "editor.tabSize": 2, "editor.formatOnSave": true },
"[typescript]": { "editor.tabSize": 2, "editor.formatOnSave": true },
"[typescriptreact]": { "editor.tabSize": 2, "editor.formatOnSave": true },
"[json]": { "editor.tabSize": 2 }
```
-   `"emmet..."`: HTML benzeri kısayolların (Emmet) JSX/TSX dosyalarında da çalışmasını ve `Tab` tuşu ile tetiklenmesini sağlar.
-   `"eslint.validate"`: `ESLint` kod denetleyicisinin hangi dosya türlerinde çalışacağını belirtir.
-   `"prettier..."`: `Prettier` formatlayıcısı için kuralları belirler: tek tırnak (`'`) kullan, satır sonlarına noktalı virgül (`;`) ekle ve obje/dizi sonlarına virgül ekle.
-   `"[javascript]"` ve diğerleri: Bu dillere özel olarak `tab` boyutunu 2 yapar ve kaydetmede formatlamayı etkinleştirir.

---

## Arayüz ve Diğer Ayarlar

```json
"terminal.integrated.fontSize": 13,
"workbench.iconTheme": "material-icon-theme",
"workbench.colorTheme": "One Dark Pro",
"files.exclude": {
    "**/node_modules": true,
    "**/target": true,
    "**/__pycache__": true
},
"diffEditor.codeLens": true
```
-   `"terminal.integrated.fontSize"`: VS Code içindeki terminalin yazı tipi boyutunu ayarlar.
-   `"workbench.iconTheme"` ve `"workbench.colorTheme"`: Arayüzün renk temasını ve dosya/klasör ikon setini belirler.
-   `"files.exclude"`: Dosya gezgininde `node_modules` (JavaScript), `target` (Java/Maven), `__pycache__` (Python) gibi otomatik oluşturulan ve genellikle görmek istemediğiniz klasörleri gizler.
-   `"diffEditor.codeLens"`: İki dosya arasındaki farkları gösteren ekranda ek bilgiler (CodeLens) sunar.

