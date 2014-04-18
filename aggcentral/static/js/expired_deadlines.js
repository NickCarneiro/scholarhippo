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
    var deadlineNumber = $(this).data('deadline');
    var deadlineInput = '<input class="deadline-input" type="text" value="'+ $(this).text() + '" />';
    $(this).after(deadlineInput);
    var $deadlineInput = $(this).after();
    $($deadlineInput).on('keypress', function(e) {
        if (e.which !== 13) {
            return false;
        }
        var newDeadline = $(this).val();
        updateDeadline(newDeadline, deadlineNumber)
    });
});

//var updateDeadline = function(newDeadline, deadlineNumber) {
//    var settings = {
//        'type': 'post',
//    }
//    $.ajax('/private/aggservice/deadline', settings);
//};