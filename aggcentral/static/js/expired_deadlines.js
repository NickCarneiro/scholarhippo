$(function() {

$('tr:first-child').on('click', function() {
    $('tr').removeClass('highlighted');
    $(this).addClass('highlighted');
});

$('.expire-button').on('click', function() {
    var scholarshipId = $(this).data('scholarship-id');
    var settings = {
        type: 'post',
        context: this,
        data: JSON.stringify({'scholarshipId': scholarshipId}),
        success: function(res) {
            // delete the row
            $(this).parent().parent().addClass('expired');

        },
        error: function(e) {
            console.log(e);
        }
    };
    $.ajax('/private/aggcentral/expire', settings)
});

$('.deadline').on('click', function(e) {
    $(this).hide();
    var deadlineSpan = this;
    var deadlineNumber = $(this).data('deadline');
    var deadlineInput = '<input class="deadline-input" type="text" value="'+ $(this).text() + '" />';
    //remove padding from this td so there's no jump when input element appears
    $(deadlineSpan).parent().css('padding-top', 0);
    $(deadlineSpan).parent().css('padding-bottom', 0);
    $(this).after(deadlineInput);
    var $deadlineInput = $(this).next();
    $($deadlineInput).on('keypress', function(e) {
        if (e.which !== 13) {
            return;
        }
        var newDeadline = $(this).val();
        var scholarshipId = $(this).closest('tr').data('scholarship-id');
        var settings = {
            'type': 'post',
            'context': this,
            'data': JSON.stringify({newDeadline: newDeadline,
                deadlineNumber: deadlineNumber,
                scholarshipId: scholarshipId}),
            'success': function(res) {
                $(this).remove();
                if (newDeadline === '') {
                    newDeadline = 'none';
                }
                $(deadlineSpan).text(newDeadline);
                $(deadlineSpan).show();
            },
            'error': function(e) {
                $(this).css('background', '#C95D5D');
                console.log(e);
                $deadlineInput.prop('disabled', false);
            }
        };
        $deadlineInput.prop('disabled', true);
        $.ajax('/private/aggcentral/deadline', settings);
    });
});


});