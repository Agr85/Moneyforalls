$(document).ready(function() {
  $('#pais').select2({
    placeholder: 'Selecciona un país',
    minimumInputLength: 2,
    ajax: {
      url: 'http://127.0.0.1:8000/app/obtener_paises/',  // Reemplaza 'ruta/al/endpoint' por la URL real
      dataType: 'json',
      processResults: function(data) {
        return {
          results: data
        };
      },
      cache: true
    }
  });
});