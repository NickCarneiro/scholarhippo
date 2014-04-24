$(document).ready(function() {
    var $locationCombobox = $('#location-combobox');
    $locationCombobox.select2({width: 244});
    $locationCombobox.val(ne.state).trigger('change');

});