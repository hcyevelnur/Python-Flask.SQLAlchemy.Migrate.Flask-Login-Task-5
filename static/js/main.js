
    var currentPage = window.location.pathname.split("/").pop();

    var navLinks = document.querySelectorAll(".navbar-nav a");

    for (var i = 0; i < navLinks.length; i++) {
        var linkPage = navLinks[i].getAttribute("href").split("/").pop();

        if (linkPage === currentPage) {
            navLinks[i].classList.add("active");
        }
    }
