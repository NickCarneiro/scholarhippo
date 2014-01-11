$(document).ready(function() {
    var $locationCombobox = $('#location-combobox');
    $locationCombobox.select2({width: 210});
    $locationCombobox.val(ne.state).trigger('change');

});