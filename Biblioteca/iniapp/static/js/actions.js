jQuery(document).ready(function(){
    jQuery("#name_category").change(function(){
        enableBtnAddEdition("name_category","description_category")
    });

    jQuery("#description_category").change(function(){
        enableBtnAddEdition("description_category","name_category")
    });

    jQuery('#find').keyup(function(){
        var find = $(this).val();
        if(find.length >= 5){
            jQuery('.spinner-border').removeClass('d-none');
            var categories = $('.categories');
            var item='';
            for( var i = 0; i < categories.length; i++ ){
                item = jQuery(categories[i]).html().toLowerCase();
                for(var x = 0; x < item.length; x++ ){
                    if( find.length == 0 || item.indexOf( find ) > -1 ){
                        jQuery(categories[i]).parents('.book-item').show(); 
                    }else{
                        jQuery(categories[i]).parents('.book-item').hide();
                    }
                }
            }
            setTimeout(function(){jQuery('.spinner-border').addClass('d-none');}, 2000);
        }
     });

     jQuery("#btnEdition").click(function(){
        if(jQuery(this).attr('typeevent') == 0){
            jQuery("#divAddEdition").removeClass("d-none");
            jQuery(this).removeClass("btn-warning");
            jQuery(this).addClass("btn-danger");
            jQuery(this).text("Cancelar");
            jQuery(this).attr('typeevent','1');
        }
        else{
            jQuery("#divAddEdition").addClass("d-none");
            jQuery(this).addClass("btn-warning");
            jQuery(this).removeClass("btn-danger");
            jQuery(this).text("Edición");
            jQuery(this).attr('typeevent','0');
        }
    });

     var forms = document.getElementsByClassName('needs-validation');
     for (let form of forms) {       
       form.addEventListener('submit', (evt) => {
        console.log(form);
        for(element = 0; element < form.length; element++){
            form[element].value = form[element].value.trim();
        }
         if (!form.checkValidity()) {
           evt.preventDefault();
           evt.stopPropagation();
           console.log('Mal capturado el formulario');
         } else {
           evt.preventDefault();
           console.info('Todo el formulario esta validado');
           form.submit();
         }
         
         form.classList.add('was-validated');
       });
     }
})

enableBtnAddEdition = function(elementUsed, otherElement){
    if(jQuery("#"+elementUsed).val().length >= jQuery("#"+elementUsed).attr('minlength')){
        if(jQuery("#"+otherElement).val().length >= jQuery('#'+otherElement).attr('minlength')){
            jQuery("#btnAdd").removeAttr('disabled');
        }
        else{
            jQuery("#btnAdd").attr('disabled','disabled');
        }
    }
    else{
        jQuery("#btnAdd").attr('disabled','disabled');
    }
}