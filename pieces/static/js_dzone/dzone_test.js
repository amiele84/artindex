





//from: https://www.w3schools.com/js/js_whereto.asp //

//changes text on click
function myFunction() {
    document.getElementById("upload-widget").innerHTML = "Paragraph changed.";
  }

//changes text on click
function myFunction2() {
    document.getElementById("srt-message").innerHTML = "Paragraph changed.";
  }

//overwrites everything and prints
//11
function myFunction3() {
    document.write(5+6)
}

//brings up window
function myFunction4() {
    window.alert(5 + 6);
}




// Create an object:
const car = {type:"Fiat", model:"500", color:"white"};

var price1 = 69;

const person = {
    firstName: "John",
    lastName : "Doe",
    id     :  5566
  };


// Display some data from the objects:
function myFunction5() {
    document.getElementById("demo").innerHTML = "The car type is " + car.type + price1;

    // Display some data from the object:
    document.getElementById("demo2").innerHTML = person.firstName + " " + person.lastName;
}


let x = myFunction6(4, 3);   // Function is called, return value will end up in x

function myFunction6(a, b) {
  return a * b;             // Function returns the product of a and b
}