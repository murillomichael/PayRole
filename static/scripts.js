function validateForm() {
  var nameField = document.getElementById("name");
  var payField = document.getElementById("pay");
  var hoursField = document.getElementById("hours");
  var nameError = document.getElementById("name-error");
  var payError = document.getElementById("pay-error");
  var hoursError = document.getElementById("hours-error");

  if (nameField.value == "") {
    nameError.style.display = "inline-block";
    return false;
  } else {
    nameError.style.display = "none";
  }

  if (payField.value == "") {
    payError.style.display = "inline-block";
    return false;
  } else {
    payError.style.display = "none";
  }

  if (hoursField.value == "") {
    hoursError.style.display = "inline-block";
    return false;
  } else {
    hoursError.style.display = "none";
  }

  return true;
}
