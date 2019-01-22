import unittest

class Test(unittest.TestCase):

#Note: We don't know for sure if we should use the ids listed or the serial ids that will be generated when we generate our tables.
    def testMarioLocation(self):
        id="Q8qsbFqIE7lwA-zkv07fxA"
        query_result = id.search()
        name = "Mario's Pizza & Italian Restaurant"
        address = "2945 Matthews Weddington Road"
        city = "Matthews"
        state = "NC"
        self.assertEqual(query_result.name, name)
        self.assertEqual(query_result.address, address)
        self.assertEqual(query_result.city, city)
        self.assertEqual(query_result.state=state)
        
    def testMarioParking(self):
        id="Q8qsbFqIE7lwA-zkv07fxA"
        query_result = id.search()
        validated_parking=0
        street_parking=0
        valet_parking=0
        lot_parking=1
        garage_parking=0
        self.assertEqual(query_result.lot_parking, lot_parking)
        self.assertEqual(query_result.valet_parking, valet_parking)
        self.assertEqual(query_result.street_parking,  street_parking)
        self.assertEqual(query_result.validated_parking, validated_parking)
        self.assertEqual(query_result.garage_parking, garage_parking)
        
    def testMarioCategories(self):
        id="Q8qsbFqIE7lwA-zkv07fxA"
        query_result = id.category_search()
        categories=["Pizza","Restaurants","Italian"]
        self.assertEqual(query_result, categories)
        
    def testMarioHours(self):
        id="Q8qsbFqIE7lwA-zkv07fxA"
        query_result = id.search()
        hours=["Monday 11:0-22:0","Friday 11:0-23:0","Saturday 11:0-23:0","Sunday 11:0-22:0"]
        self.assertEqual(query_result.hours, hours)
        
    def testMarioPriceAndReviews(self):
        id="Q8qsbFqIE7lwA-zkv07fxA"
        query_result = id.search()
        price=2
        rating=3.5
        review_count=76
        self.assertEqual(query_result.price=price)
        self.assertEqual(query_result.review_count=review_count)
        self.assertEqual(query_result.rating=rating)
    
    def testMarioOtherBools(self):
        id="Q8qsbFqIE7lwA-zkv07fxA"
        query_result = id.search()
        delivers=1
        takeout=1
        credit_card=1
        good_for_kids=1
        outdoor_seating=1
        wheelchair=1
        self.assertEqual(query_result.delivers=delivers)
        self.assertEqual(query_result.wheelchair=wheelchair)
        self.assertEqual(query_result.takeout, takeout)       self.assertEqual(query_result.hours, hours)
        self.assertEqual(query_result.credit_card, credit_card)
        self.assertEqual(query_result.good_for_kids, good_for_kids)
                
            
    def resultsList(self):
        city = "Charlotte"
        state = "NC"
        wheelchair=1
        id = "IAjw9w6ASayV3Nhaq6bosQ"
        self.AssertIn(id,query(city,state,wheelchair))
        
    def resultsList1(self):
        city = "Toronto"
        state = "ON"
        credit_card=1;
        garage_parking=0;
        id = "EDqCEAGXVGCH4FJXggtjgg"
        url = "http://restaurantfinder.com/restaurants?city=" + city + "&state=" + state + "&credit_card=" \
              + credit_card +"&garage_parking=" + garage_parking
        json_string = urllib.request.open(url).read()
        query_result = json.loads(json_string)
        self.AssertIn(id, query_result)


if __name__ == '__main__':
    unittest.main()
