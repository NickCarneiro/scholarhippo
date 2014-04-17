$('td').on('click', function() {
    $('tr').removeClass('highlighted');
    $(this).parent().addClass('highlighted');
});