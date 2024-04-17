let listElements = document.querySelectorAll('.list_button--click');



listElements.forEach(listElement => {
    listElement.addEventListener('click', ()=>{
        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;

        if(menu.clientHeight == 0){ /*Si el arto que tiene el menu en el momento es igual a cero*/
            height = menu.scrollHeight;   /*Height apropiado para que todos los elementos existan*/
        }

        menu.style.height = height +"px";
    })
});

var ultimoClicado = null;
function fondoClick(elemento){
    
        if(ultimoClicado !== null){
            ultimoClicado.classList.remove('clicked');
        }
        
        elemento.classList.add('clicked')
        ultimoClicado = elemento;
    }
  

