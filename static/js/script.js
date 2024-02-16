$(document).ready(function () {
    $('.upload-input').on('change', function () {
        var file = $(this)[0].files[0];

        // Check if the uploaded file is a PDF
        if (file.type === 'application/pdf') {
            var reader = new FileReader();

            reader.onload = function (e) {
                // Create elements for displaying PDF icon and file name
                var pdfIcon = $('<img>').attr('src', '../static/img/pdf-icon.png').addClass('pdf-icon');
                var fileName = $('<span>').addClass('file-name').text(file.name);

                // Append elements to the dropzone
                $('.dropzone').find('.pdf-icon, .file-name').remove(); // Remove previous elements if any
                $('.dropzone').prepend(pdfIcon, fileName); // Add the new elements

                $('.upload-icon').hide();
            }

            reader.readAsDataURL(file);
        } else {
            alert('Please upload a PDF file.');
            // Reset the file input
            $(this).val('');
        }
    });
});



const form = document.querySelector('form');

// Get the loading element
const loading = document.getElementById('loading');
const title =

    // Add event listener to form submission
    form.addEventListener('submit', (event) => {
        // Prevent default form submission behavior
        event.preventDefault();

        // Display the loading animation
        loading.style.display = 'block';
        loading.style.marginBottom = '25px';
        form.style.display = 'none';

        document.getElementById('info-title').innerHTML = "Generating Your Audio Book Please Wait!"
        document.getElementById('info-title').style.color = "white"
        // Submit the form
        form.submit();
    });