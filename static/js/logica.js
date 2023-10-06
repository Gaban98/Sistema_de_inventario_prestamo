$(document).ready(function() {
    $('#id_categoria').change(function() {
        var categoriaId = $(this).val();
        $.ajax({
            url: '/api/elementos_por_categoria/' + categoriaId,
            method: 'GET',
            success: function(data) {
                var elementoSelect = $('#id_elemento');
                elementoSelect.empty();

                $.each(data, function(index, elemento) {
                    elementoSelect.append(new Option(elemento.nombre, elemento.id));
                });
            }
        });
    });
});