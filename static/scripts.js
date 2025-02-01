<script>
    document.addEventListener("DOMContentLoaded", function () {
        let words = document.querySelectorAll(".animated-header span");
        words.forEach((word, index) => {
            word.style.animationDelay = `${index * 0.5}s`;  // Delay each word
            word.querySelector("::before")?.style.setProperty("animation-delay", `${index * 0.5}s`);
        });
    });
</script>
