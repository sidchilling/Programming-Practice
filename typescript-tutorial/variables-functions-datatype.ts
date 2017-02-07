
// Define some variables. Variables (optionally) require a type declaration
var burger: string = 'hamburger',
    calories: number = 300,
    tasty: boolean = true;

function speak(food: string, energy: number, tasty: boolean): void {
    console.log("Our " + food + ' has ' + energy + " calories ");
    if (tasty) {
	console.log("But, it's quite tasty!");
    } else {
	console.log("And it tastes bad :(")
    }
}

speak(burger, calories, tasty);
speak(burger, calories, false);