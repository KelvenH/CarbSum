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
  $('.modal').modal();
  $('select').formSelect();
});

// Quick Calc Functions

//Calculate base carbs (carb per gram) 

/* --Defect : despite setting input step value to 1 decimal place, calculated results can still display float to multiple decimal places
Status : Resolved - '.toFixed(1)' added to float being parsed to limit to 1 decimal place */

//Plan to Revisit to Simplify

function carbPerGram(selectObject) {
  if (selectObject.includes("-item1")) {
    let baseWeight = parseFloat(document.getElementById("qc-base-weight-item1").value, 10);
    let baseCarbs = parseFloat(document.getElementById("qc-base-carbs-item1").value, 10);
    let result = baseCarbs / baseWeight;
    document.getElementById("qc-carb-per-g-item1").value = parseFloat(result).toFixed(1);
  }
  if (selectObject.includes("-item2")) {
    let baseWeight = parseFloat(document.getElementById("qc-base-weight-item2").value, 10);
    let baseCarbs = parseFloat(document.getElementById("qc-base-carbs-item2").value, 10);
    let result = baseCarbs / baseWeight;
    document.getElementById("qc-carb-per-g-item2").value = parseFloat(result).toFixed(1);
  }
  if (selectObject.includes("-item3")) {
    let baseWeight = parseFloat(document.getElementById("qc-base-weight-item3").value, 10);
    let baseCarbs = parseFloat(document.getElementById("qc-base-carbs-item3").value, 10);
    let result = baseCarbs / baseWeight;
    document.getElementById("qc-carb-per-g-item3").value = parseFloat(result).toFixed(1);
  }
  if (selectObject.includes("-item4")) {
    let baseWeight = parseFloat(document.getElementById("qc-base-weight-item4").value, 10);
    let baseCarbs = parseFloat(document.getElementById("qc-base-carbs-item4").value, 10);
    let result = baseCarbs / baseWeight;
    document.getElementById("qc-carb-per-g-item4").value = parseFloat(result).toFixed(1);
  }
}


//Calculate portion carbs

/* --Defect :
Status : Outstanding - consider invoking both functions to capture changes. */

function qcItemCarbs(selectObject) {
  if (selectObject.includes("-item1")) {
    let portionSize = parseFloat(document.getElementById("qc-portion-weight-item1").value, 10);
    let carbsPerG = parseFloat(document.getElementById("qc-carb-per-g-item1").value, 10);
    let result = portionSize * carbsPerG;
    document.getElementById("qc-carbs-item1").value = parseFloat(result).toFixed(1);
    document.getElementById("qc-carbs-big-item1").value = parseFloat(result).toFixed(1);
  }
  if (selectObject.includes("-item2")) {
    let portionSize = parseFloat(document.getElementById("qc-portion-weight-item2").value, 10);
    let carbsPerG = parseFloat(document.getElementById("qc-carb-per-g-item2").value, 10);
    let result = portionSize * carbsPerG;
    document.getElementById("qc-carbs-item2").value = parseFloat(result).toFixed(1);
    document.getElementById("qc-carbs-big-item2").value = parseFloat(result).toFixed(1);
  }
  if (selectObject.includes("-item3")) {
    let portionSize = parseFloat(document.getElementById("qc-portion-weight-item3").value, 10);
    let carbsPerG = parseFloat(document.getElementById("qc-carb-per-g-item3").value, 10);
    let result = portionSize * carbsPerG;
    document.getElementById("qc-carbs-item3").value = parseFloat(result).toFixed(1);
    document.getElementById("qc-carbs-big-item3").value = parseFloat(result).toFixed(1);
  }
  if (selectObject.includes("-item4")) {
    let portionSize = parseFloat(document.getElementById("qc-portion-weight-item4").value, 10);
    let carbsPerG = parseFloat(document.getElementById("qc-carb-per-g-item4").value, 10);
    let result = portionSize * carbsPerG;
    document.getElementById("qc-carbs-item4").value = parseFloat(result).toFixed(1);
    document.getElementById("qc-carbs-big-item4").value = parseFloat(result).toFixed(1);
  }
  qcItemCount()
}

//Update Item Count & Total Carbs


function qcItemCount() {
  let items = [];                                         // create empty array
  $('input[id*=qc-carbs-big]').each(function(index) {     // find inputs with partial id match (i.e. all 4)
  items.push(+$(this).val())  // push associated value into array (note'+' after push converted string to number)
  });

  let count = items.filter(String).length;                // count no of array items with a string value
  document.getElementById("qc-total-items").innerHTML = parseInt(count);
  console.log(count);
  
  let total=0;                                             //loop through array values and count 
  for (let item in items)
  { total += items[item]; };
  document.getElementById("qc-calc-result").innerHTML = parseInt(total);
  console.log(total);

};
