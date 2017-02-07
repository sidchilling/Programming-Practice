interface Food {
    name: string;
    calories: number;
}

function speak(food: Food): void {
    console.log("You're eating " + food.name + " that contains " + food.calories
	       + " calories.")
}

var iceCream = {
    name: 'vanilla icecream',
    calories: 200
}

speak(iceCream);