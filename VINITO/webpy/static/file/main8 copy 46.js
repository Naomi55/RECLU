$(document).ready(function(){
    tablaPersonas = $("#tablaPersonas").DataTable({
       "columnDefs":[{
        "targets": -1,
        "data":null,
        "defaultContent": "<div class='text-center'><div class='btn-group'><button class='btn btn-primary btnEditar'>Responder</button><button class='btn btn-danger btnBorrar'>Rechazar</button><button class='btn btn-info btnDetalle'>Detalles</button></div></div>"  
       }],
        
        //Para cambiar el lenguaje a español
    "language": {
            "lengthMenu": "Mostrar _MENU_ registros",
            "zeroRecords": "No se encontraron resultados",
            "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "infoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sSearch": "Buscar:",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast":"Último",
                "sNext":"Siguiente",
                "sPrevious": "Anterior"
             },
             "sProcessing":"Procesando...",
        }
    });
    
    $(document).on("click", ".btnEditar", function(){
    $("#formPersonas").trigger("reset");
    $(".modal-header").css("background-color", "#28a745");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("¿Seguro que deseas responder?");            
    $("#modalCRUD").modal("show");  
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(10)').text(); 
    $("#nombre").val(nombre);  
    id=null;
    opcion = 1; //alta

});    
    
var fila; //capturar la fila para editar o borrar el registro
    
//botón EDITAR    
$(document).on("click", ".btnEdita", function(){
    fila = $(this).closest("tr");
    id = parseInt(fila.find('td:eq(0)').text());
    nombre = fila.find('td:eq(1)').text();
    pais = fila.find('td:eq(2)').text();
    edad = parseInt(fila.find('td:eq(3)').text());
    $("#nombre").val(nombre);
    $("#pais").val(pais);
    $("#edad").val(edad);
    opcion = 2; //editar
    
    $(".modal-header").css("background-color", "#007bff");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("Editar Persona");            
    $("#modalCRUD").modal("show");  
    
});

//botón BORRAR
$(document).on("click", ".btnBorrar", function(){
    $("#formPersonas2").trigger("reset");
    $(".modal-header2").css("background-color", "#ff4500");
    $(".modal-header2").css("color", "white");
    $(".modal-title2").text("¿Seguro que deseas rechazar?");            
    $("#modalCRUD2").modal("show");  
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(10)').text(); 
    $("#nombre2").val(nombre);     
    id=null;
    opcion = 1; //alta
})

$(document).on("click", ".btnDetalle", function(){    
    $("#formPersonas3").trigger("reset");
    $(".modal-header3").css("background-color", "#4b8edb");
    $(".modal-header3").css("color", "white");
    $(".modal-title3").text("Detalles del Postulante");            
    $("#modalCRUD3").modal("show");  
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(9)').text(); 
    $("#nombre3").val(nombre); 
    expe = fila.find('td:eq(12)').text(); 
    $("#nombre4").val(expe);  
    id=null;
    opcion = 1; //alta
       
});
    
/*$("#formPersonas").submit(function(e){
    e.preventDefault();    
    nombre = $.trim($("#nombre").val());
    pais = $.trim($("#pais").val());
    edad = $.trim($("#edad").val());    
    $.ajax({
        url: "bd/crud.php",
        type: "POST",
        dataType: "json",
        data: {nombre:nombre, pais:pais, edad:edad, id:id, opcion:opcion},
        success: function(data){  
            console.log(data);
            id = data[0].id;            
            nombre = data[0].nombre;
            pais = data[0].pais;
            edad = data[0].edad;
            if(opcion == 1){tablaPersonas.row.add([id,nombre,pais,edad]).draw();}
            else{tablaPersonas.row(fila).data([id,nombre,pais,edad]).draw();}            
        }        
    });
    $("#modalCRUD").modal("hide");    
    
}); */   
fila = $(this).closest("tr");
var estatus = fila.find('td:eq(12)').text(); 
var nombre = document.getElementById('nombre').style.backgroundColor = estatus


    

});