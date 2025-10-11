// Wait for the entire document to load before running the script
$(document).ready(function() {

    // --- Helper function to get the CSRF token from the cookie ---
    // Django requires this for POST requests (security)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');


    // --- Main function to perform the AJAX request ---
    function performAction(button, actionUrl) {
        const postId = button.closest('.like-dislike-section').data('post-id');
        // Replace the '0' placeholder in the URL with the actual Post ID
        const finalUrl = actionUrl.replace('0', postId); 

        $.ajax({
            type: 'POST',
            url: finalUrl,
            headers: { 'X-CSRFToken': csrftoken }, // Attach the CSRF token
            
            success: function(response) {
                if (response.status === 'ok') {
                    // 1. Update the display counts
                    $('#like-count').text(response.like_count);
                    $('#dislike-count').text(response.dislike_count);

                    // 2. Update the button styles

                    // Handle LIKE button changes
                    const likeBtn = $('#like-button');
                    if (response.hasOwnProperty('is_liked')) { // Only process if the response is from a LIKE action
                        if (response.is_liked) {
                            likeBtn.removeClass('btn-outline-primary').addClass('btn-primary');
                            // If liked, make sure the dislike button is reset
                            $('#dislike-button').removeClass('btn-danger').addClass('btn-outline-danger');
                        } else {
                            likeBtn.removeClass('btn-primary').addClass('btn-outline-primary');
                        }
                    }
                    
                    // Handle DISLIKE button changes
                    const dislikeBtn = $('#dislike-button');
                    if (response.hasOwnProperty('is_disliked')) { // Only process if the response is from a DISLIKE action
                        if (response.is_disliked) {
                            dislikeBtn.removeClass('btn-outline-danger').addClass('btn-danger');
                            // If disliked, make sure the like button is reset
                            $('#like-button').removeClass('btn-primary').addClass('btn-outline-primary');
                        } else {
                            dislikeBtn.removeClass('btn-danger').addClass('btn-outline-danger');
                        }
                    }

                } else {
                    alert('An error occurred during voting.');
                }
            },
            error: function() {
                alert('Could not connect to the server or process the request.');
            }
        });
    }


    // --- Event listener for the LIKE button ---
    $('#like-button').on('click', function(e) {
        e.preventDefault();
        // The URL pattern from urls.py
        const likeUrl = "{% url 'like_post' pk=0 %}"; 
        performAction($(this), likeUrl);
    });

    // --- Event listener for the DISLIKE button ---
    $('#dislike-button').on('click', function(e) {
        e.preventDefault();
        // The URL pattern from urls.py
        const dislikeUrl = "{% url 'dislike_post' pk=0 %}"; 
        performAction($(this), dislikeUrl);
    });

});