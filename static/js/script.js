$(document).ready(function () {
  $('.sidenav').sidenav({edge: "right"});
  $(".dropdown-trigger").dropdown();
  $('.collapsible').collapsible();
  //toggle show/hide password (Acknowledgement Stack Overflow: https://stackoverflow.com/questions/51552661/how-to-show-and-hide-password-when-click-on-eye-icon-using-jquery)
  $(document).on('click', '.toggle-password', function () {
    $(this).toggleClass("fa-eye fa-eye-slash");
    var input = $("#password");
    input.attr('type') === 'password' ? input.attr('type', 'text') : input.attr('type', 'password')
  });
});

// Quick Calc Function

//Calculate base carbs (carb per gram) 

/* --Defect : despite setting input step value to 2 decimal places, calculated results can still display float to multiple decimal places
Status : Resolved - '.toFixed(2)' added to float being parsed to limit to 2 decimal places */

function carbPerGram() {
  let baseWeight = parseFloat(document.getElementById("qc-base_weight").value, 10);
  let baseCarbs = parseFloat(document.getElementById("qc-base_carbs").value, 10);
  let result = baseCarbs / baseWeight;
  document.getElementById("qc-carb-per-g").value = parseFloat(result).toFixed(2);
}

//Calculate portion carbs

function qcItemCarbs() {
  let portionSize = parseFloat(document.getElementById("qc-portion_weight").value, 10);
  let carbsPerG = parseFloat(document.getElementById("qc-carb-per-g").value, 10);
  let result = portionSize * carbsPerG;
  document.getElementById("qc-item-carbs").value = parseFloat(result).toFixed(2);
  document.getElementById("qc-item-carbs-big").value = parseFloat(result).toFixed(2);
}






 