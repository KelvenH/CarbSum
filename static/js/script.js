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

//navigation purposes to go back to previous page

function goBack() {
  window.history.back();
}

// Quick Calc Functions

//Calculate base carbs (carb per gram) 

/* --Defect : despite setting input step value to 1 decimal place, calculated results can still display float to multiple decimal places
Status : Resolved - '.toFixed(1)' added to float being parsed to limit to 1 decimal place */

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

//create array on partial id match for each of the 4 carb items & push associated value into array
function qcItemCount() {
  let items = [];
  $('input[id*=qc-carbs-big]').each(function(index) {     
    items.push(+$(this).val())  // note'+' after push converts string to number
    //console.log("ITMSB", items);     
    }
  );

  // Count: no of array items with a value > 0
  let count = 0;
  //console.log("COUNTA", count);
  items.forEach(item =>{
    if(item !="0"){
      count+=1;
    //console.log("COUNTB", count);
    }
  });
  document.getElementById("qc-total-items").innerHTML = parseInt(count);
  //console.log("COUNTC", count);


  //Sum: loop through array values and sum total
  let total=0;                                            
  for (let item in items){
    total += items[item];
  };
  document.getElementById("qc-calc-result").innerHTML = (parseInt(total) + "g");
  //console.log(total);

};

// Food Card Calculations - Note as base carbs is pulled from db (unlike Add New Food Card) only the carbs per portion needs to be calculated. Second calc uses the preset portion sizes as alternative for user

function calcFoodCardCarbs() {
  
    let portionSize = parseFloat(document.getElementById("food-card-portion-data").value, 10);
    let carbsPerG = parseFloat(document.getElementById("food-base-carbs").value, 10);
    let result = portionSize * carbsPerG;
    document.getElementById("food-calc-result").innerHTML = (parseFloat(result).toFixed(1) + "g");
    //clears out any values in alternative option of calc carbs (preset)
    document.getElementById("food-card-portion-carbs").value = 0;
};

function calcFoodCardPresetCarbs() {
  
  let portionCarbs = parseFloat(document.getElementById("testcalc").value, 10);
  console.log("portionCarbs", portionCarbs);
  let portionNo = parseFloat(document.getElementById("food-card-portion-no").value, 10);
  console.log("portionNo", portionNo);
  let result = portionCarbs * portionNo;
  console.log(result);
  document.getElementById("food-card-portion-carbs").value = (parseFloat(result).toFixed(1) + "g");
  document.getElementById("food-calc-result").innerHTML = (parseFloat(result).toFixed(1) + "g");
  //clears out any values in alternative option of calc carbs (manual portion size)
  document.getElementById("food-card-portion-data").value = 0;
};

// Add Food Card Calculations

function calcAddFoodCarbs() {
  
  let portionSize = parseFloat(document.getElementById("add-portion-size").value, 10);
  let carbsPerPortion = parseFloat(document.getElementById("add-carbs-per-portion").value, 10);
  /*--divide carbs by portion for carb per g--*/
  let carbPerG = carbsPerPortion / portionSize;
  document.getElementById("add-carbs-per-gram").value = parseFloat(carbPerG).toFixed(2);
  let carbPer100 = carbPerG * 100;
  document.getElementById("add-carbs-per100").value = parseFloat(carbPer100).toFixed(1);
};


// Edit Food Card Calculations

function calcEditFoodCarbs() {
  
  let portionSize = parseFloat(document.getElementById("edit-portion-size").value, 10);
  let carbsPerPortion = parseFloat(document.getElementById("edit-carbs-per-portion").value, 10);
  /*--divide carbs by portion for carb per g--*/
  let carbPerG = carbsPerPortion / portionSize;
  console.log("Port Size:", portionSize);
  console.log("Carb per Port:", carbsPerPortion);
  console.log("CarbPerG", carbPerG);
  document.getElementById("edit-carbs-per-gram").value = parseFloat(carbPerG).toFixed(2);
  let carbPer100 = carbPerG * 100;
  console.log("carbPer100", carbPer100);
  document.getElementById("edit-carbs-per100").value = parseFloat(carbPer100).toFixed(1);
};