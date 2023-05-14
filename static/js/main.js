
    // Aktif sayfayı belirleme
    var currentPage = window.location.pathname.split("/").pop();

    // Navbar'ın bağlantılarını seçme
    var navLinks = document.querySelectorAll(".navbar-nav a");

    // Navbar'ın bağlantılarını döngüye sokma
    for (var i = 0; i < navLinks.length; i++) {
        // Bağlantının adresindeki sayfa adını alın
        var linkPage = navLinks[i].getAttribute("href").split("/").pop();

        // Eğer bağlantı, aktif sayfayla aynıysa "active" sınıfını ekle
        if (linkPage === currentPage) {
            navLinks[i].classList.add("active");
        }
    }
