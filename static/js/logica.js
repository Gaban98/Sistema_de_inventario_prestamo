$(document).on('click', '.editar-categoria', function(){
    var id = $(this).data('id');
    $.ajax({
        url: "/actualizar_categoria/" + id,  // Asegúrate de que esta URL dirige a la vista de edición de la categoría
        success: function(data){
            $("#editarCategoriaModal .modal-body").html(data);
        }
    });
});
