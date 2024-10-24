document.addEventListener("DOMContentLoaded", function() {
    // Move Sonic on the racecourse as the user progresses through questions
    const sonic = document.querySelector('.sonic');
    let progress = 0;  // Start at position 0 (start of the racecourse)

    // Event listener to simulate Sonic's movement based on quiz progress
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        moveSonic();
    });

    function moveSonic() {
        // Increment progress with each question
        progress += 10;  // Moves by 10% of the racecourse for each question

        // Update Sonic's position visually
        if (sonic) {
            sonic.style.left = `${progress}%`;
        }

        // Check if Sonic has reached the finish line (10 questions completed)
        if (progress >= 100) {
            setTimeout(function() {
                window.location.href = "/result";  // Redirect to result page
            }, 1000);  // Small delay before redirect
        }
    }

    // Background music control
    let audio = document.querySelector('audio');
    if (audio) {
        audio.volume = 0.5;  // Adjust volume if needed
        audio.play();  // Play background music on page load
    }
});
