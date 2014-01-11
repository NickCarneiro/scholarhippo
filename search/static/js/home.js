$(function() {
    var $locationCombobox = $('#location-combobox');
    $locationCombobox .select2({width: 200});
    if (window['geoip_region']) {
        var stateCode = geoip_region();
        if ($.type(stateCode) === 'string') {
            // disable geo IP for now
            //$locationCombobox.val(stateCode).trigger('change');
        }
    }
    $('#what').focus();
    mixpanel.track('homepage');
});
