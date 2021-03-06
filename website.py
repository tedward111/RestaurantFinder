#!/usr/bin/env python3
'''
    website.py
    Jeff Ondich, 25 April 2016
    Nicki Polyakov + Teddy Willard 
'''
import sys
import flask
import json
import config
import psycopg2
import urllib

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/') 
def get_main_page():
    ''' This is the only route intended for human users '''
    return flask.render_template('homePage.html')

@app.route('/searchresults/')
def get_search_results():
    url = ""
    #GET parameters
    city = flask.request.args.get('city')
    state = flask.request.args.get('state')
    name = flask.request.args.get('name')
    category_list = flask.request.args.getlist('category')
    rating = flask.request.args.get('rating')
    credit_cards = flask.request.args.get('credit_cards')
    dogs_allowed = flask.request.args.get('dogs_allowed')
    wheelchair = flask.request.args.get('wheelchair_accessible')
    good_for_kids = flask.request.args.get('good_for_kids')
    outdoor_seating = flask.request.args.get('outdoor_seating')
    reservations = flask.request.args.get('reservations')
    delivery = flask.request.args.get('delivery')
    take_out = flask.request.args.get('take_out')
    garage = flask.request.args.get('garage')
    street = flask.request.args.get('street')
    validated = flask.request.args.get('validated')
    lot = flask.request.args.get('lot')
    valet = flask.request.args.get('valet')
    
    #Build URL to call API
    if (state != None):
        url += "state=" + state + "&"
    
    if (city != None):
        url += "city=" + city + "&"

    if (rating != None):
        url += "rating=" + rating + "&";
    
    if (reservations == '1'):
        url += "reservations=1&"
    
    if (delivery == '1'):
        url += "delivery=1&"
    
    if (take_out == '1'):
        url += "take_out=1&"
    
    if (credit_cards == '1'):
        url += "credit_cards=1&"
    
    if (good_for_kids == '1'):
        url += "good_for_kids=1&"
        
    if (dogs_allowed == '1'):
        url += "dogs_allowed=1&"
    
    if (outdoor_seating == '1'):
        url += "outdoor_seating=1&"
    
    if (wheelchair == '1'):
        url += "wheelchair_accessible=1&"
    
    if (validated == '1'):
        url += "validated=1&"
    
    if (street == '1'):
        url += "street=1&"
    
    if (valet == '1'):
        url += "valet=1&"
    
    if (lot == '1'):
        url += "lot=1&"
        
    if (garage == '1'):
        url += "garage=1&"
        
    for item in category_list:
        item = item.replace(" ", "_")
        url += "category=" + item + "&"
        
    url = url[:-1] #deletes the last "&" in the url
    searchUrl = "http://localhost:8080/restaurants/?"+url
    
    #Call API and read json results generated by API
    json_results = urllib.request.urlopen(searchUrl).read()
    string_from_server = json_results.decode('utf-8')
    string_from_server = string_from_server.replace('false', 'False')
    string_from_server = string_from_server.replace('true', 'True')
    string_from_server = string_from_server.replace('null', 'None')
    #Evaluate string as List
    restaurantList = eval(string_from_server)
    
    #If ourData is empty, return a search results page that tells the user that no results were found
    if len(restaurantList)==0: 
        return flask.render_template('searchresults.html',tableBody="Sorry, no restaurants were found. If you want to try again, hit the back button and enter a new set of criteria.")

    #initializes the tableBody
    tableBody="""<tr><th>Name</th><th>City</th><th>State</th><th>Address</th><th>Rating</th><th>Reservations</th><th>Delivers</th><th>Takeout</th><th>Accepts Credit Card</th><th>Good For Kids</th><th>Dogs Allowed</th><th>Outdoor Seating</th><th>Wheelchair Accessible</th><th>Validated Parking</th><th>Street Parking</th><th>Valet Parking</th><th>Lot Parking</th><th>Garage Parking</th><th>Categories</th></tr>"""
    
    #this is the code we will use if we can't get the key thing to work
    #        if garageParking=="None":
#            garageParking="N/A"
#        elif garageParking=="True":
#            garageParking="Yes"
#        elif garageParking=="False":
#            garageParking="No"
    
    #for every restaurant, extract the relevant data and add it to the table in our website
    for restaurant in restaurantList:
        name=str(restaurant['Name'])
        city=str(restaurant['City'])
        state=str(restaurant['State'])
        address=str(restaurant['Address'])
        rating=str(restaurant['Rating'])
        for key in ['Reservations', 'Delivers', 'Takeout', 'Accepts Credit Card', 'Good For Kids', 'Dogs Allowed', 'Outdoor Seating', 'Wheelchair Accessible', 'Validated Parking', 'Street Parking', 'Valet Parking', 'Lot Parking', 'Garage Parking']:
            if str(restaurant[key]) == 'False':
                restaurant[key] = 'No'
            if str(restaurant[key]) == 'True':
                restaurant[key] = 'Yes'
            if str(restaurant[key]) == 'None':
                restaurant[key] = 'N/A'
        reservations=str(restaurant['Reservations'])
        delivers=str(restaurant['Delivers'])
        takeout=str(restaurant['Takeout'])
        creditCard=str(restaurant['Accepts Credit Card'])
        goodForKids=str(restaurant['Good For Kids'])
        dogsAllowed=str(restaurant['Dogs Allowed'])
        outdoorSeating=str(restaurant['Outdoor Seating'])
        wheelchairAccess=str(restaurant['Wheelchair Accessible'])
        validatedParking=str(restaurant['Validated Parking'])
        streetParking=str(restaurant['Street Parking'])
        valetParking=str(restaurant['Valet Parking'])
        lotParking=str(restaurant['Lot Parking'])
        garageParking=str(restaurant['Garage Parking'])
        categoryList = str(restaurant['Categories'])
            
        #adds a new table entry with the data for this restaurant
        newTableEntry="<tr><td>"+name+"</td><td>"+city+"</td><td>"+state+"</td><td>"+address+"</td><td>"+rating+"</td><td>"+reservations+"</td><td>"+delivers+"</td><td>"+takeout+"</td><td>"+creditCard+"</td><td>"+goodForKids+"</td><td>"+dogsAllowed+"</td><td>"+outdoorSeating+"</td><td>"+wheelchairAccess+"</td><td>"+validatedParking+"</td><td>"+streetParking+"</td><td>"+valetParking+"</td><td>"+lotParking+"</td><td>"+garageParking+"</td><td>" + categoryList + "</td></tr>"
        tableBody+=newTableEntry    
    
    return flask.render_template('searchresults.html',tableBody=tableBody)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=int(port), debug=True)