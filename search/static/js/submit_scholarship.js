$(function() {
    $('#scholarship-submit-button').on('click', function() {
        $(this).prop('disabled', true);
        var title = $('#scholarship-title').val();
        var url = $('#scholarship-url').val();
        var fields = {
            title: title,
            url: url
        };
        var email = $('#scholarship-email').val();
        if (email !== '') {
            fields['email'] = email;
        }
        var payload = JSON.stringify(fields);
        var settings = {
            type: 'post',
            data: payload,
            contentType: 'application/json',
            success: function() {
                $('#submit-scholarship-form').html('<h2>Thanks! <a href="">Submit another?</a></h2>');
            },
            error: function() {
                $('#submit-scholarship-form').html('<h2>Something went really wrong on our end. Try again later.</h2>');
            }
        };
        $.ajax('/submit-scholarship', settings);
    });
});