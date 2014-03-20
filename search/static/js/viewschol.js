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

