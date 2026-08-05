// ======================================================
// JBOD Validation Platform
// Login UI v2.0
// File : static/js/login.js
// ======================================================

document.addEventListener("DOMContentLoaded", function () {

    // ==================================================
    // Password Show / Hide
    // ==================================================

    const passwordInput = document.querySelector(
        "input[type='password']"
    );

    const toggleButton = document.getElementById(
        "togglePassword"
    );

    if (passwordInput && toggleButton) {

        toggleButton.addEventListener("click", function () {

            const icon = this.querySelector("i");

            if (passwordInput.type === "password") {

                passwordInput.type = "text";

                icon.classList.remove("fa-eye");

                icon.classList.add("fa-eye-slash");

            } else {

                passwordInput.type = "password";

                icon.classList.remove("fa-eye-slash");

                icon.classList.add("fa-eye");

            }

        });

    }

    // ==================================================
    // Login Button Loading
    // ==================================================

    const loginForm = document.querySelector("form");

    const loginButton = document.querySelector(".btn-login");

    if (loginForm && loginButton) {

        loginForm.addEventListener("submit", function () {

            loginButton.disabled = true;

            loginButton.innerHTML = `
                <span class="spinner-border spinner-border-sm me-2"></span>
                Signing In...
            `;

        });

    }

    // ==================================================
    // Input Focus Effect
    // ==================================================

    const inputs = document.querySelectorAll(".form-control");

    inputs.forEach(function (input) {

        input.addEventListener("focus", function () {

            this.parentElement.classList.add("shadow-sm");

        });

        input.addEventListener("blur", function () {

            this.parentElement.classList.remove("shadow-sm");

        });

    });

    // ==================================================
    // Press Enter Login
    // ==================================================

    document.addEventListener("keydown", function (event) {

        if (event.key === "Enter") {

            if (loginForm) {

                loginForm.submit();

            }

        }

    });

    // ==================================================
    // Remember Username
    // ==================================================

    const remember = document.getElementById("remember");

    const username = document.querySelector(
        "input[name='username']"
    );

    if (remember && username) {

        const savedUsername = localStorage.getItem(
            "jvp_username"
        );

        if (savedUsername) {

            username.value = savedUsername;

            remember.checked = true;

        }

        loginForm.addEventListener("submit", function () {

            if (remember.checked) {

                localStorage.setItem(
                    "jvp_username",
                    username.value
                );

            } else {

                localStorage.removeItem(
                    "jvp_username"
                );

            }

        });

    }

});