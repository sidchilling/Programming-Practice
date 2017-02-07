// Define some variables. Variables (optionally) require a type declaration
var burger = 'hamburger', calories = 300, tasty = true;
function speak(food, energy, tasty) {
    console.log("Our " + food + ' has ' + energy + " calories ");
    if (tasty) {
        console.log("But, it's quite tasty!");
    }
    else {
        console.log("And it tastes bad :(");
    }
}
speak(burger, calories, tasty);
speak(burger, calories, false);
