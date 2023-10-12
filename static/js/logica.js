$(document).ready(function() {
    $('#id_categoria').change(function() {
        var categoriaId = $(this).val();
        var url = '/usuarios/api/elementos_por_categoria/' + categoriaId; // URL fija
        $.ajax({
            url: url,
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

$(document).ready(function(){
    $('.delete-btn').on('click', function(e){
        var objectType = $(this).data('object-type');
        if(!confirm('¿Estás seguro de que quieres eliminar este ' + objectType + '?')){
            e.preventDefault();
        }
    });
});

$(document).ready(function() {
    $('.select2').select2();
});