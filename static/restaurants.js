function onSearchButton() {
    
    //Checks what state/country the user selected and sets it to the stateValue
    var stateSelectElement = document.getElementById("stateSelect");
    var stateValue = stateSelectElement.options[stateSelectElement.selectedIndex].value;   

    //Checks what city the user entered and sets it to cityValue
    var cityValue = document.getElementById("citySelect").value;
    
    //Checks what rating the user selected and sets it to ratingValue
    var ratingSelectElement = document.getElementById("ratingSelect");
    var ratingValue = ratingSelectElement.options[ratingSelectElement.selectedIndex].value;
    
    //Checks which features the user put a checkmark next to
    var reservationsValue = document.getElementById("Reservations").checked;
    var deliversValue = document.getElementById("Delivers").checked;
    var takeOutValue = document.getElementById("takeOut").checked;
    var creditCardsValue = document.getElementById("creditCards").checked;
    var goodForKidsValue = document.getElementById("goodForKids").checked;
    var dogsAllowedValue = document.getElementById("dogsAllowed").checked;
    var outdoorSeatingValue = document.getElementById("outdoorSeating").checked;
    var wheelchairAccessValue = document.getElementById("wheelchairAccess").checked;

    //Checks which parking attributes the user put a checkmark next to
    var validatedParkingValue = document.getElementById("validatedParking").checked;
    var streetParkingValue = document.getElementById("streetParking").checked;
    var valetParkingValue = document.getElementById("valetParking").checked;
    var lotParkingValue = document.getElementById("lotParking").checked;
    var garageParkingValue = document.getElementById("garageParking").checked;
    
    //Checks what cuisine type the user selected and sets it to the cuisineValue
    var cuisineSelectElement = document.getElementById("cuisineSelect");
    var cuisineValue = cuisineSelectElement.options[cuisineSelectElement.selectedIndex].value;
    
    //Checks which menu items the user put a checkmark next to
    var pizzaValue = document.getElementById("Pizza").checked;
    var burgersValue = document.getElementById("Burgers").checked;
    var chickenWingsValue = document.getElementById("Chicken Wings").checked;
    var sushiValue = document.getElementById("Sushi").checked;
    var tacosValue = document.getElementById("Tacos").checked;
    var gelatoValue = document.getElementById("Gelato").checked;
    var cupcakesValue = document.getElementById("Cupcakes").checked;
    var wafflesValue = document.getElementById("Waffles").checked;
    var sandwichValue = document.getElementById("Sandwiches").checked;
    var saladValue = document.getElementById("Salad").checked;
    var noodlesValue = document.getElementById("Noodles").checked;
    
    //Creates our search url by checking which values the user selected
    var url="";
    if (stateValue!="-"){
        url+="state="+stateValue+"&";
    }
    if (cityValue!=""){
        url+="city="+cityValue+"&";
    }
    if (ratingValue!="-"){
        url+="rating="+ratingValue+"&";
    }
    if (reservationsValue==true){
        url+="reservations=1&";
    }
    if (deliversValue==true){
        url+="delivery=1&";
    }
    if (takeOutValue==true){
        url+="take_out=1&";
    }
    if (creditCardsValue==true){
        url+="credit_cards=1&";
    }
    if (goodForKidsValue==true){
        url+="good_for_kids=1&";
    }
    if (dogsAllowedValue==true){
        url+="dogs_allowed=1&";
    }
    if (outdoorSeatingValue==true){
        url+="outdoor_seating=1&";
    }
    if (wheelchairAccessValue==true){
        url+="wheelchair_accessible=1&";
    }
    if (validatedParkingValue==true){
        url+="validated=1&";
    }
    if (streetParkingValue==true){
        url+="street=1&";
    }
    if (valetParkingValue==true){
        url+="valet=1&";
    }
    if (lotParkingValue==true){
        url+="lot=1&";
    }
    if (garageParkingValue==true){
        url+="garage=1&";
    }
    if (cuisineValue != "-"){
        url += "category=" + cuisineValue + "&";
    }
    if (pizzaValue == true){
        url += "category=Pizza&";
    }
    if (burgersValue == true){
        url += "category=Burgers&";
    }
    if (chickenWingsValue == true){
        url += "category=Chicken_Wings&";
    }
    if (sushiValue == true){
        url += "category=Sushi_Bars&";
    }
    if (tacosValue == true){
        url += "category=Tacos&";
    }
    if (gelatoValue == true){
        url += "category=Gelato&";
    }
    if (cupcakesValue == true){
        url += "category=Cupcakes&";
    }
    if (wafflesValue == true){
        url += "category=Waffles&";
    }
    if (sandwichValue == true){
        url += "category=Sandwiches&";
    }
    if (saladValue == true){
        url += "category=Salad&";
    }
    if (noodlesValue == true){
        url += "category=Noodles&";
    }

    
<<<<<<< HEAD
    url=url.substring(0,url.length-1); //deletes the last "&" in the url
    searchUrl="http://localhost:8080/restaurants/?"+url;
    window.location=searchUrl;

=======
    url = url.substring(0,url.length-1); //deletes the last "&" in the url
    searchUrl = "http://localhost:8081/searchresults/?"+url;    
    window.location.href = searchUrl;
>>>>>>> 523f1b55b84b0f62eee40b99ec4ef57fcae1d138
}

//When the user presses the back button, the website goes back to the home page
function goBack() {
<<<<<<< HEAD
    window.location="http://localhost:8080/";
=======
    window.location = "http://localhost:8081/";
>>>>>>> 523f1b55b84b0f62eee40b99ec4ef57fcae1d138
}