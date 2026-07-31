// =====================================
// JBOD Validation Platform
// Login Page
// =====================================

document.addEventListener("DOMContentLoaded", function () {

    const passwordInput = document.getElementById("id_password");
    const togglePassword = document.getElementById("togglePassword");

    if (togglePassword && passwordInput) {

        togglePassword.addEventListener("click", function () {

            const type =
                passwordInput.getAttribute("type") === "password"
                    ? "text"
                    : "password";

            passwordInput.setAttribute("type", type);

            this.classList.toggle("fa-eye");
            this.classList.toggle("fa-eye-slash");

        });

    }

});