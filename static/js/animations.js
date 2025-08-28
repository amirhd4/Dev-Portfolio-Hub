import { gsap } from "gsap";

document.addEventListener("DOMContentLoaded", () => {
    if (document.querySelector('.hero-title')) {
        const tl = gsap.timeline();

        tl.from(".hero-greeting", {
            duration: 0.8,
            y: 30,
            opacity: 0,
            ease: "power3.out",
            delay: 0.2
        })
        .from(".hero-title", {
            duration: 1,
            y: 50,
            opacity: 0,
            ease: "power3.out"
        }, "-=0.6") // Start 0.6s before the previous animation ends
        .from(".hero-subtitle", {
            duration: 1,
            y: 50,
            opacity: 0,
            ease: "power3.out"
        }, "-=0.8") // Overlap by 0.8s
        .from(".hero-cta", {
            duration: 0.8,
            y: 20,
            opacity: 0,
            ease: "power3.out",
            stagger: 0.2 // Animate each CTA button with a 0.2s delay
        }, "-=0.5");
    }
});