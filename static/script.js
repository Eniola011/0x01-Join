document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const btnLoginPopup = document.querySelector('.btnLogin-popup');
    const wrapper = document.querySelector('.wrapper');
    const loginLink = document.querySelector('.login-link');
    const registerLink = document.querySelector('.register-link');
    const iconClose = document.querySelector('.icon-close');
    
    // Show the login popup
    btnLoginPopup.addEventListener('click', function() {
        wrapper.classList.add('active-popup');
    });

    // Switch to the register form
    registerLink.addEventListener('click', function(e) {
        e.preventDefault();
        wrapper.classList.add('active');
    });

    // Switch back to the login form
    loginLink.addEventListener('click', function(e) {
        e.preventDefault();
        wrapper.classList.remove('active');
    });

    // Close the popup
    iconClose.addEventListener('click', function() {
        wrapper.classList.remove('active-popup');
        wrapper.classList.remove('active');
    });
});
