function speak(food) {
    console.log("You're eating " + food.name + " that contains " + food.calories
        + " calories.");
}
var iceCream = {
    name: 'vanilla icecream',
    calories: 200
};
speak(iceCream);
