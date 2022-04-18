
var LunchArray = [{name:'Cheeseburger', price:1.99}, {name:'Hamburger', price:1.50}, {name:'Chicken Strips',price:2.75}];

var SidesArray = [{name:'French Fries', price:1.00},{name:'Onion Rings', price:1.25},{name:'Corn Nuggets', price:1.50}];

// @ts-check
function selectLunch() {
    if (input == "Cheeseburger")
        return console.log(`You have selected Cheeseburger. The price is:\$ ${LunchArray[0].price}`)

    if (input == "Hamburger")
        return console.log(`You have selected Hamburger. The price is:\$ ${LunchArray[1].price}`)

     if (input == "Chicken Strips")
        return console.log(`You have selected Chicken Strips. The price is:\$ ${LunchArray[2].price}`)

    else
        return console.log(`You've Made an Invalid Selection! ${input} Try again.`)
}

function selectSide() {
    if (inputTwo == "French Fries")
        return console.log(`You have selected French Fries. The price is:\$ ${SidesArray[0].price}`)

    if (inputTwo == "Onion Rings")
        return console.log(`You have selected Onion Rings. The price is:\$ ${SidesArray[1].price}`)

     if (inputTwo == "Corn Nuggets")
        return console.log(`You have selected Corn Nuggets The price is:\$ ${SidesArray[2].price}`)

    else
        return console.log(`You've Made an Invalid Selection! ${inputTwo} Try again.`)
}

function calculateTotal() {
    if (input == "Cheeseburger")
        a = LunchArray[0].price
    if (input =="Hamburger")
        a = LunchArray[1].price
    if (input == "Chicken Strips")
        a = LunchArray[2].price
    if (inputTwo == "French Fries")
        b = SidesArray[0].price
    if (inputTwo == "Onion Rings")
        b = SidesArray[1].price
    if (inputTwo == "Corn Nuggets")
        b = SidesArray[2].price
    // else
    //     console.log('You have entered an invalid item. Unable to calculate total.')
    total = a + b
    return console.log(`Your total is: \$ ${total}`)
}

const prompt = require("prompt-sync")();
const input = prompt("Please Enter: Cheesburger, Hamburger, or Chicken Strips: ");
selectLunch();
const inputTwo = prompt("Please Enter: French Fries, Onion Rings, or Corn Nuggets: ");
selectSide();
a = ''
b = ''
calculateTotal();
