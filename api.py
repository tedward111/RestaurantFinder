#!/usr/bin/env python3
'''
    api.py
    Nicki Polyakov and Teddy Willard, 15 May 2017
'''
from flask import Flask, render_template, request, redirect, url_for
import sys
import flask
import json
import config
import psycopg2
import urllib
import re

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

def _fetch_all_rows_for_query(query):
    '''
    Returns a list of rows obtained from the books database
    by the specified SQL query. If the query fails for any reason,
    an empty list is returned.
    '''
    try:
        connection = psycopg2.connect(database=config.database, user=config.user, password=config.password)
    except Exception as e:
        print('Connection error:', e, file=sys.stderr)
        return []

    rows = []
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchmany(10) # This can be trouble if your query results are really big.
    except Exception as e:
        print('Error querying database:', e, file=sys.stderr)

    connection.close()
    return rows

@app.route('/') 
def get_main_page():
    ''' This is the only route intended for human users '''
    return flask.render_template('homePage.html')

@app.route('/restaurants/') 
def restaurants():
    '''
    Returns a list of dictionaries of information about the restaurants in our database that match all the given criteria.
    '''
    
    #First part of the query that must be used
    query1 = '''SELECT restaurants.business_id FROM restaurants, categories, restaurants_categories''' 
    #Later part of the query that must be used
    query2 = ''' WHERE restaurants.id=restaurants_categories.restaurant_id AND categories.id=restaurants_categories.category_id AND categories.category='Restaurants\''''
    
    #GET parameters
    city = flask.request.args.get('city')
    state = flask.request.args.get('state')
    name = flask.request.args.get('name')
    category_list = flask.request.args.getlist('category')
    category_list.append('Restaurants')
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
    restaurants_list = []
    
    #For each parameter, if the parameter has been given by the user, add neccessary strings to the first and second parts of the query string
    if city != None:
        query1 += ', cities, restaurants_cities'
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.id=restaurants_cities.restaurant_id AND cities.id=restaurants_cities.city_id'
        query2 += ' AND cities.city=\'{0}\''.format(city)
    if state != None:
        query1 += ', states, restaurants_states'
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.id=restaurants_states.restaurant_id AND states.id=restaurants_states.states_id'
        query2 += ' AND states.state=\'{0}\''.format(state)    
    if name != None:
        query1 += ', names, restaurants_names'
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.id=restaurants_names.restaurant_id AND names.id=restaurants_names.name_id'
        query2 += ' AND names.name=\'{0}\''.format(name)
    if rating != None:
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.rating>={0}'.format(rating)
    if credit_cards == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.credit_card=\'t\''
    if dogs_allowed == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.dogs_allowed=\'t\''
    if wheelchair == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.wheelchair=\'t\''
    if good_for_kids == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.good_for_kids=\'t\''
    if outdoor_seating == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.outdoor_seating=\'t\''
    if reservations == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.reservations=\'t\''
    if delivery == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.delivers=\'t\''
    if take_out == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.takeout=\'t\''
    if garage == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.garage_parking=\'t\''
    if street == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.street_parking=\'t\''
    if validated == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.validated_parking=\'t\''
    if lot == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.lot_parking=\'t\''
    if valet == '1':
        if query2 != ' WHERE ':
            query2 += ' AND '
        query2 += 'restaurants.valet_parking=\'t\''
    #Part of the query that allows for multiple categories
    number_categories = len(category_list)
    for i in range(number_categories):
        category_list[i] = category_list[i].replace('_', ' ')
    query2 += ''' AND restaurants.id IN (SELECT restaurant_id FROM (
        SELECT restaurant_id, count(category_id) as cat_count
        FROM restaurants_categories, categories
        WHERE categories.id=category_id
        AND (categories.category='Restaurants\''''
    category_list.remove('Restaurants')
    for i in range(number_categories - 1):
        query2 += ''' OR categories.category='{0}\''''.format(category_list[i])
    query2 += ''')
            GROUP BY restaurant_id
            ) AS cat_counts WHERE cat_count = {0})'''.format(number_categories)
    restaurant_list = []
    
    #Concatenates the two halves of the query to form a full query
    query = query1 + query2
    #Makes list of dictionaries of restaurant business_ids that match search criteria
    for row in _fetch_all_rows_for_query(query):
        restaurant = {'business_id':row[0]}
        restaurant_list.append(restaurant)
    for item in restaurant_list:
        business_id = item.keys()
        for id in business_id:
            final_id = item.get(id)
            
        #Query to extract all info from each restaurant based on business_id
        query_final = '''SELECT names.name, cities.city, states.state, restaurants.address, restaurants.rating, restaurants.reservations, restaurants.delivers, restaurants.takeout, restaurants.credit_card, restaurants.good_for_kids, restaurants.dogs_allowed, restaurants.outdoor_seating, restaurants.wheelchair, restaurants.validated_parking, restaurants.street_parking, restaurants.valet_parking, restaurants.lot_parking, restaurants.garage_parking FROM names, restaurants, restaurants_names, cities, restaurants_cities, states, restaurants_states WHERE restaurants.id=restaurants_names.restaurant_id AND names.id=restaurants_names.name_id AND restaurants.id=restaurants_cities.restaurant_id AND cities.id=restaurants_cities.city_id AND restaurants.id=restaurants_states.restaurant_id AND states.id=restaurants_states.states_id AND restaurants.business_id={0}'''.format('\'' + final_id + '\'')
        
        #Build a query to get all categories for a given business_id
        query_categories = '''SELECT category FROM restaurants, categories, restaurants_categories WHERE restaurants.id=restaurants_categories.restaurant_id AND categories.id=restaurants_categories.category_id AND business_id={0}'''.format('\'' + final_id + '\'')
        
        categoryList=""
        #Add categories to categoryList for each restaurant
        for category in _fetch_all_rows_for_query(query_categories):
            category = str(category)
            category = category[2:-3]
            if (category!='Restaurants'):
                categoryList += " " + category + ", "
        if (categoryList.endswith(', ')):
            categoryList = categoryList[:-2]
        for row in _fetch_all_rows_for_query(query_final):
            restaurant = {'Name':row[0], 'City':row[1], 'State':row[2], 'Address':row[3], 'Rating': row[4], 'Reservations': row[5], 'Delivers': row[6], 'Takeout': row[7], 'Accepts Credit Card': row[8], 'Good For Kids': row[9], 'Dogs Allowed': row[10], 'Outdoor Seating': row[11], 'Wheelchair Accessible': row[12], 'Validated Parking': row[13], 'Street Parking': row[14], 'Valet Parking': row[15], 'Lot Parking': row[16], 'Garage Parking': row[17]}
            restaurant['Categories'] = categoryList
            restaurants_list.append(restaurant)
    return json.dumps(restaurants_list)
    
if __name__ == '__main__':
    app.run(host='localhost', port=8080)