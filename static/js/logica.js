function updateClock() {
    const currentTime = new Date();
    const hours = currentTime.getHours();
    const minutes = currentTime.getMinutes();

    const timeString = hours + ":" + minutes ;
    document.getElementById("current-time").innerText = timeString;
}

// Actualizar la hora cada segundo
setInterval(updateClock, 1000);

function mostrarFormulario(tipo) {
    if (tipo === 'sede') {
        document.getElementById('formularioSede').style.display = 'block';
        document.getElementById('formularioCategoria').style.display = 'none';
    } else if (tipo === 'categoria') {
        document.getElementById('formularioSede').style.display = 'none';
        document.getElementById('formularioCategoria').style.display = 'block';
    }
}


$(document).ready(function() {
    // Cuando se hace clic en "Agregar Sede"
    $("#sede-modal-trigger").click(function() {
        loadModalContent("{% url 'inventario:sede-create' %}", "Agregar Sede");
    });

    // Cuando se hace clic en "Agregar Categoría"
    $("#categoria-modal-trigger").click(function() {
        loadModalContent("{% url 'inventario:categoria-create' %}", "Agregar Categoría");
    });

    // Función para cargar contenido en el modal
    function loadModalContent(url, title) {
        $.get(url, function(data) {
            $(".modal-body").html(data);
            $(".modal-title").html(title);
            $("#myModal").modal("show");
        });
    }
});
