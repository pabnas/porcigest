
function reset_select(select_id){
    var select = document.getElementById(select_id);
    var options = select.options;
    for (var i = 0; i < options.length; i++) {
      var option = options[i];
      if (option.value === '') {
        option.selected = true;
      } else {
        option.hidden = true;
      }
    }
  }

  function chainedSelect(
      selector_object,
      data_key_sent,
      data_key_recieve,
      url,
      target_object
    ){

    reset_select(select_id=target_object);

    $(selector_object).change(function () {
      var optionSelected = $(this).find("option:selected");
      var valueSelected  = optionSelected.val();
      if (valueSelected === '') {
        reset_select(select_id=target_object);
        return;
      }

      data = {};
      data[data_key_sent] = valueSelected;
      $.ajax( {
        url: url,
        type: 'POST',
        data: data,
        success: function(data) {
          const validIds = data[data_key_recieve];
          const selectElement = document.getElementById(target_object);
          const options = selectElement.options;

          for (let i = 0; i < options.length; i++) {
            const option = options[i];
            if (option.value === '') {
              continue;
            }
            if (validIds.includes(parseInt(option.value))) {
              option.hidden = false;
            } else {
              option.hidden = true;
            }
          }
        }
      });  
    });

  }


