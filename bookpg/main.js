document.addEventListener('DOMContentLoaded', () => {
    const book = document.querySelector('.book-3d');
    const hero = document.querySelector('.hero');

    // 1. Mouse Follow Effect (The "Premium" touch)
    hero.addEventListener('mousemove', (e) => {
        const { clientX, clientY } = e;
        const { innerWidth, innerHeight } = window;
        
        // Calculate tilt based on mouse position
        const yRotation = ((clientX / innerWidth) - 0.5) * 40; // Horizontal tilt
        const xRotation = ((clientY / innerHeight) - 0.5) * -40; // Vertical tilt
        
        // Combine with base rotation of -25deg
        book.style.transform = rotateX(${xRotation}deg) rotateY(${yRotation - 25}deg);
    });

    // 2. Reset on Mouse Leave
    hero.addEventListener('mouseleave', () => {
        book.style.transition = "transform 0.6s ease";
        book.style.transform = rotateY(-25deg) rotateX(0deg);
    });
    
    // Smooth transition back to follow mode after reset
    hero.addEventListener('mouseenter', () => {
        setTimeout(() => { book.style.transition = "transform 0.1s ease-out"; }, 600);
    });
});
