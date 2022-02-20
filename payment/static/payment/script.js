function toggleButton() {
    var x = document.getElementsByClassName("amount")[0];
   
      x.style.display = "block";
  }
 
  function manage(txt) {
    var bt = document.getElementsByClassName('btn')[0];
    var btext = document.getElementsByClassName('btn-text')[0]; 
    
    if (txt.value != '') {
        bt.disabled = false;
        bt.style.cursor="pointer";
        btext.style.cursor="pointer";
    }
    else {
        bt.disabled = true;
        bt.style.cursor="no-drop";
        btext.style.cursor="no-drop";
        
        
    }
}
