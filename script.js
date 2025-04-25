// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollTop = 0;
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Toggle event details
function toggleDetails(button) {
    const details = button.nextElementSibling;
    const isHidden = details.style.display === 'none' || !details.style.display;
    
    // Hide all other details first
    document.querySelectorAll('.event-details').forEach(detail => {
        detail.style.display = 'none';
    });
    
    // Toggle the clicked details
    details.style.display = isHidden ? 'block' : 'none';
    button.textContent = isHidden ? 'Hide Details' : 'View Details';
}

// Form submission handler
function handleSubmit(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    
    // Here you would typically send this data to a server
    console.log('Form submitted:', { name, email, message });
    
    // Show success message
    alert('Thank you for your message! We will get back to you soon.');
    
    // Clear form
    event.target.reset();
}

// Login form handler
function handleLogin(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Here you would typically validate with a server
    console.log('Login attempt:', { username, password });
    
    // Simulate successful login
    alert('Login successful!');
    window.location.href = 'index.html';
}

// Register form handler
function handleRegister(event) {
    event.preventDefault();
    
    const username = document.getElementById('regUsername').value;
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    
    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }
    
    // Here you would typically send this data to a server
    console.log('Registration:', { username, email, password });
    
    // Simulate successful registration
    alert('Registration successful! Please login.');
    toggleRegister();
}

// Toggle between login and register forms
function toggleRegister() {
    const loginContainer = document.querySelector('.login-container');
    const registerContainer = document.querySelector('.register-container');
    
    if (loginContainer.style.display === 'none') {
        loginContainer.style.display = 'block';
        registerContainer.style.display = 'none';
    } else {
        loginContainer.style.display = 'none';
        registerContainer.style.display = 'block';
    }
}

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero');
    const scrolled = window.pageYOffset;
    hero.style.backgroundPositionY = scrolled * 0.5 + 'px';
});