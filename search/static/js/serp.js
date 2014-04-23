function submitRefine() {
    //construct object representing form state
    var refineForm = {};
    refineForm.q = ne.keyword;
    var $locationCombobox = $('#location-combobox-refine');
    refineForm.l = $locationCombobox.val();

    refineForm.ne = $('#refine-no-essay-required').prop('checked');
    var deadline = $('#refine-deadline').prop('checked');
    refineForm.d = deadline;
    refineForm.e = $('#refine-ethnicity').val();
    refineForm.g = $('#refine-gender').val();
    var url = $.param(refineForm);
    window.location.href = '?' + url;
}
function resultClick() {
    var loggingParameters = {
        "schol_key": $(this).data('scholkey')
    }
    mixpanel.track("search#resultclick", loggingParameters);
}
$(function() {
    //make refine form match page state
    $('#refine-ethnicity').val(ne.ethnicity_restriction);
    $('#refine-gender').val(ne.gender_restriction);

    var $locationCombobox = $('#location-combobox-refine');
    $locationCombobox.select2({width: 180});
    $locationCombobox.val(ne.state).trigger('change');

    // wire up clickables
    $('#refine-submit').on('click', submitRefine);
    $('.result-link').on('click', resultClick);

    // ne gets defined in footer_script.html
    mixpanel.track('search', window['ne']);
});