# bot_comentador_instagram

#bot

#PARA USAR:

#0. CONFIGURAR ARCHIVO lista_nombres.py

#1. ABRIR LA PAGINA DE INSTAGRAM

#2. CORRER EL CODIGO 

#3. TIENES 5 SEGUNDOS PARA POSICIONAR EL CURSOR EN EL CUADRO DE COMENTARIOS

#4. ESPERAR QUE EL BOT TERMINE DE COMENTAR



------------------------------------------------------------------------------------

#CODIGO PARA OBTENER LISTA DE USERNAMES Y NOMBRES DE IG



// Selecciona todos los span con el atributo data-bloks-name="bk.components.Text"
var spans = document.querySelectorAll('span[data-bloks-name="bk.components.Text"]');

// Crea una lista para almacenar los nombres de usuario
var usernames = [];

// Itera sobre los span seleccionados y extrae el texto
spans.forEach(span => {
    usernames.push(span.textContent.trim());
});

// Muestra la lista de nombres de usuario en la consola
console.log(usernames);
