document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const fileInput = document.querySelector('input[type="file"]');
    const submitButton = document.querySelector('button');

    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    });

    form.addEventListener('submit', function() {
        submitButton.innerHTML = 'Processing...';
        submitButton.disabled = true;
    });

    // Get the modal
    var modal = document.getElementById("histogramModal");

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    var img = document.getElementById("color-histogram");
    var modalImg = document.getElementById("histogramImg");
    var captionText = document.getElementById("caption");
    img.onclick = function(){
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    }

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() { 
        modal.style.display = "none";
    }
});

