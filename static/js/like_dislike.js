// Run after DOM ready (ensure jQuery loads BEFORE this file)
$(function () {
  // CSRF helper
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim(); // native trim
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');

  function performAction($button, actionUrl) {
    const $section = $button.closest('.like-dislike-section');

    $.ajax({
      type: 'POST',
      url: actionUrl,                       // already a full URL from data-*
      headers: { 'X-CSRFToken': csrftoken },
      success: function (response) {
        if (response.status === 'ok') {
          // Update only within this section
          $section.find('.like-count').text(response.like_count);
          $section.find('.dislike-count').text(response.dislike_count);

          const $likeBtn = $section.find('.like-button');
          const $dislikeBtn = $section.find('.dislike-button');

          if (Object.prototype.hasOwnProperty.call(response, 'is_liked')) {
            if (response.is_liked) {
              $likeBtn.removeClass('btn-outline-primary').addClass('btn-primary');
              $dislikeBtn.removeClass('btn-danger').addClass('btn-outline-danger');
            } else {
              $likeBtn.removeClass('btn-primary').addClass('btn-outline-primary');
            }
          }

          if (Object.prototype.hasOwnProperty.call(response, 'is_disliked')) {
            if (response.is_disliked) {
              $dislikeBtn.removeClass('btn-outline-danger').addClass('btn-danger');
              $likeBtn.removeClass('btn-primary').addClass('btn-outline-primary');
            } else {
              $dislikeBtn.removeClass('btn-danger').addClass('btn-outline-danger');
            }
          }
        } else {
          alert('An error occurred during voting.');
        }
      },
      error: function () {
        alert('Could not connect to the server or process the request.');
      }
    });
  }

  // Delegated events (works even if content is injected later)
  $(document).on('click', '.like-button', function (e) {
    e.preventDefault();
    const $section = $(this).closest('.like-dislike-section');
    const likeUrl = $section.data('like-url');
    performAction($(this), likeUrl);
  });

  $(document).on('click', '.dislike-button', function (e) {
    e.preventDefault();
    const $section = $(this).closest('.like-dislike-section');
    const dislikeUrl = $section.data('dislike-url');
    performAction($(this), dislikeUrl);
  });
});
