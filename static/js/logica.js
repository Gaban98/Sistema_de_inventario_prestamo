
    function filterElements(categoria) {
        // Redireccionar a la URL con el parámetro de filtro seleccionado
        window.location.href = "{% url 'inventario:view' %}?filtro=" + categoria;
    }

