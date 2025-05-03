document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    const dotsContainer = document.querySelector('.dots-container');
    const prevBtn = document.querySelector('.prev-slide');
    const nextBtn = document.querySelector('.next-slide');
    let currentSlide = 0;
    
    // Initialize slider
    function initSlider() {
        // Create dots
        slides.forEach((_, idx) => {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            dot.addEventListener('click', () => goToSlide(idx));
            dotsContainer.appendChild(dot);
        });
        
        updateSlider();
    }
    
    function updateSlider() {
        slides.forEach((slide, idx) => {
            if (idx === currentSlide) {
                slide.style.transition = "transform 0.6s ease, opacity 0.6s ease";
                slide.style.transform = "translateX(0)";
                slide.style.opacity = "1";
                slide.style.zIndex = "2";
            } else if (idx < currentSlide) {
                slide.style.transition = "none";
                slide.style.transform = "translateX(-100%)";
                slide.style.opacity = "0";
                slide.style.zIndex = "1";
            } else {
                slide.style.transition = "none";
                slide.style.transform = "translateX(100%)";
                slide.style.opacity = "0";
                slide.style.zIndex = "1";
            }
        });
    
        const dots = document.querySelectorAll('.dot');
        dots.forEach((dot, idx) => {
            dot.classList.toggle('active', idx === currentSlide);
        });
    }
    
    
    function goToSlide(index) {
        currentSlide = index;
        updateSlider();
    }
    
    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        updateSlider();
    }
    
    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        updateSlider();
    }
    
    // Event listeners
    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);
    
    // Auto-rotate
    let slideInterval = setInterval(nextSlide, 5000);
    
    // Pause on hover
    const slider = document.querySelector('.hero-slider');
    slider.addEventListener('mouseenter', () => clearInterval(slideInterval));
    slider.addEventListener('mouseleave', () => {
        slideInterval = setInterval(nextSlide, 5000);
    });
    
    // Initialize
    initSlider();
});