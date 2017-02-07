
interface FoodItem {
    itemName: string;
    isAvailable: boolean;
    price: number;
}

class Menu {
    // these are the properties
    
    items: Array<FoodItem>;
    pages: number;

    constructor(itemList: Array<FoodItem>, numPages: number) {
	this.items = itemList;
	this.pages = numPages;
    }

    list(): void {
	console.log("We have " + this.pages + " pages in our menu. Enjoy!");
	for(var i = 0; i < this.items.length; i++) {
	    var foodItem: FoodItem = this.items[i];
	    var printString = foodItem.itemName + " is ";
	    if (foodItem.isAvailable) {
		printString += "available";
	    } else {
		printString += "unavailable";
	    }
	    printString += ". And the price is $" + foodItem.price;
	    console.log(printString);
	}
    }

}

var itemList: Array<FoodItem> = [];
itemList.push({itemName: 'Wada Pao', isAvailable: true, price: 3.50});
itemList.push({itemName: 'Idli Sambhar', isAvailable: false, price: 2});
var menu = new Menu(itemList, 4);
menu.list();