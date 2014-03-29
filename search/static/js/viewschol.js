function trackApplyClick() {
    var loggingParameters = {
        "schol_key": $('#apply-now').data('scholkey')
    }
    mixpanel.track("view_schol#applynow", loggingParameters);
}

$(function() {
     // wire up clickables
    $('#apply-now').on('click', trackApplyClick);
    $('#report-link').on('click', showReportOptions);
    $('#report-cancel').on('click', cancelReport);
    $('#report-submit').on('click', submitReport)
    // ne gets defined in footer_script.html
    mixpanel.track('view_schol', window['ne']);

    // tell the report view to send us back here
    $('#report-form-next').val(document.location.pathname + document.location.search);
});

function showReportOptions(e) {
    $('#report-choices').show();
    $(this).hide();
    $("html, body").animate({ scrollTop: $(document).height() }, "slow");
    e.preventDefault();
}

function cancelReport() {
    $('#report-choices').hide();
    $('#report-link').show();
}

function submitReport() {
    $('#report-submit').prop('disabled', true);
    $('#report-cancel').prop('disabled', true);
    var problem = $('#report-select').val();
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var explanation = $('#report-explanation').val();
    var payload = {
        problem: problem,
        csrfToken: csrfToken,
        explanation: explanation,
        sk: window['sk']
    };
    var options = {
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(payload),
        success: function(res) {
            $('#report-container').html('Thanks for the report!')
        },
        error: function(e) {
            $('#report-submit').prop('disabled', false);
            $('#report-cancel').prop('disabled', false);
            $('#report-error').html('Something went wrong. Please try again.');
        }
    };
    $.ajax('/report', options);
}

