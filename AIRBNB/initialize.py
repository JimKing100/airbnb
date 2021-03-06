from AIRBNB.models import DB, amenities, neighborhoods, property_types


def init_db():
    DB.session.add(amenities(id=1, amenity='TV'))
    DB.session.add(amenities(id=2, amenity='Internet'))
    DB.session.add(amenities(id=3, amenity='WiFi'))
    DB.session.add(amenities(id=4, amenity='Kitchen'))
    DB.session.add(amenities(id=5, amenity='Pets'))
    DB.session.add(amenities(id=6, amenity='Breakfast'))
    DB.session.add(amenities(id=7, amenity='Free Parking'))
    DB.session.add(amenities(id=8, amenity='Hot Tub'))
    DB.session.add(amenities(id=9, amenity='Air Conditioning'))
    DB.session.add(amenities(id=10, amenity='Private Entrance'))

    DB.session.add(property_types(id=1, property_type='Guesthouse'))
    DB.session.add(property_types(id=2, property_type='House'))
    DB.session.add(property_types(id=3, property_type='Apartment'))
    DB.session.add(property_types(id=4, property_type='Guest suite'))
    DB.session.add(property_types(id=5, property_type='Condominium'))
    DB.session.add(property_types(id=6, property_type='Townhouse'))
    DB.session.add(property_types(id=7, property_type='Bungalow'))
    DB.session.add(property_types(id=8, property_type='Loft'))
    DB.session.add(property_types(id=9, property_type='Bed and breakfast'))
    DB.session.add(property_types(id=10, property_type='Other'))
    DB.session.add(property_types(id=11, property_type='Cabin'))
    DB.session.add(property_types(id=12, property_type='Cottage'))
    DB.session.add(property_types(id=13, property_type='Campsite'))
    DB.session.add(property_types(id=14, property_type='Tent'))
    DB.session.add(property_types(id=15, property_type='Villa'))
    DB.session.add(property_types(id=16, property_type='Camper/RV'))
    DB.session.add(property_types(id=17, property_type='Nature lodge'))
    DB.session.add(property_types(id=18, property_type='Tiny house'))
    DB.session.add(property_types(id=19, property_type='Chalet'))
    DB.session.add(property_types(id=20, property_type='Farm stay'))
    DB.session.add(property_types(id=21, property_type='Boat'))
    DB.session.add(property_types(id=22, property_type='Serviced apartment'))
    DB.session.add(property_types(id=23, property_type='Boutique hotel'))
    DB.session.add(property_types(id=24, property_type='Bus'))
    DB.session.add(property_types(id=25, property_type='Tipi'))
    DB.session.add(property_types(id=26, property_type='Treehouse'))
    DB.session.add(property_types(id=27, property_type='Barn'))
    DB.session.add(property_types(id=28, property_type='Hostel'))
    DB.session.add(property_types(id=29, property_type='Yurt'))
    DB.session.add(property_types(id=30, property_type='Houseboat'))
    DB.session.add(property_types(id=31, property_type='Resort'))
    DB.session.add(property_types(id=32, property_type='Dome house'))
    DB.session.add(property_types(id=33, property_type='Aparthotel'))
    DB.session.add(property_types(id=34, property_type='Hotel'))
    DB.session.add(property_types(id=35, property_type='Casa particular (Cuba)'))
    DB.session.add(property_types(id=36, property_type='Earth house'))
    DB.session.add(property_types(id=37, property_type='Hut'))

    DB.session.add(neighborhoods(id=1, neighborhood='East Downtown'))
    DB.session.add(neighborhoods(id=2, neighborhood='SW Williamson Co.'))
    DB.session.add(neighborhoods(id=3, neighborhood='Travis Heights'))
    DB.session.add(neighborhoods(id=4, neighborhood='Zilker'))
    DB.session.add(neighborhoods(id=5, neighborhood='East Riverside'))
    DB.session.add(neighborhoods(id=6, neighborhood='West Campus'))
    DB.session.add(neighborhoods(id=7, neighborhood='Balcones Civic Association'))
    DB.session.add(neighborhoods(id=8, neighborhood='Clarksville'))
    DB.session.add(neighborhoods(id=9, neighborhood='Brentwood'))
    DB.session.add(neighborhoods(id=10, neighborhood='Old West Austin'))
    DB.session.add(neighborhoods(id=11, neighborhood='Cherry Creek'))
    DB.session.add(neighborhoods(id=12, neighborhood='Scofield Ridge'))
    DB.session.add(neighborhoods(id=13, neighborhood='Bouldin Creek'))
    DB.session.add(neighborhoods(id=14, neighborhood='Tarrytown'))
    DB.session.add(neighborhoods(id=15, neighborhood='Northwest Hills'))
    DB.session.add(neighborhoods(id=16, neighborhood='McKinney'))
    DB.session.add(neighborhoods(id=17, neighborhood='South Congress'))
    DB.session.add(neighborhoods(id=18, neighborhood='Hyde Park'))
    DB.session.add(neighborhoods(id=19, neighborhood='Barton Hills'))
    DB.session.add(neighborhoods(id=20, neighborhood='Dawson'))
    DB.session.add(neighborhoods(id=21, neighborhood='Upper Boggy Creek'))
    DB.session.add(neighborhoods(id=22, neighborhood='Rosedale'))
    DB.session.add(neighborhoods(id=23, neighborhood='Angus Valley'))
    DB.session.add(neighborhoods(id=24, neighborhood='South Lamar'))
    DB.session.add(neighborhoods(id=25, neighborhood='Govalle'))
    DB.session.add(neighborhoods(id=26, neighborhood='Holly'))
    DB.session.add(neighborhoods(id=27, neighborhood='South Manchaca'))
    DB.session.add(neighborhoods(id=28, neighborhood='Steiner Ranch'))
    DB.session.add(neighborhoods(id=29, neighborhood='Westgate'))
    DB.session.add(neighborhoods(id=30, neighborhood='Rosewood'))
    DB.session.add(neighborhoods(id=31, neighborhood='Downtown'))
    DB.session.add(neighborhoods(id=32, neighborhood='Galindo'))
    DB.session.add(neighborhoods(id=33, neighborhood='Allendale'))
    DB.session.add(neighborhoods(id=34, neighborhood='Windsor Park'))
    DB.session.add(neighborhoods(id=35, neighborhood='West Austin'))
    DB.session.add(neighborhoods(id=36, neighborhood='Barton Creek'))
    DB.session.add(neighborhoods(id=37, neighborhood='Highland'))
    DB.session.add(neighborhoods(id=38, neighborhood='Wooten'))
    DB.session.add(neighborhoods(id=39, neighborhood='University of Texas'))
    DB.session.add(neighborhoods(id=40, neighborhood='Rollingwood'))
    DB.session.add(neighborhoods(id=41, neighborhood='Copperfield'))
    DB.session.add(neighborhoods(id=42, neighborhood='St. Edwards'))
    DB.session.add(neighborhoods(id=43, neighborhood='West Congress'))
    DB.session.add(neighborhoods(id=44, neighborhood='East Congress'))
    DB.session.add(neighborhoods(id=45, neighborhood='Long Canyon'))
    DB.session.add(neighborhoods(id=46, neighborhood='Georgian Acres'))
    DB.session.add(neighborhoods(id=47, neighborhood='South First'))
    DB.session.add(neighborhoods(id=48, neighborhood='Westlake Hills'))
    DB.session.add(neighborhoods(id=49, neighborhood='Parker Lane'))
    DB.session.add(neighborhoods(id=50, neighborhood='MLK & 183'))
    DB.session.add(neighborhoods(id=51, neighborhood='Oak Hill'))
    DB.session.add(neighborhoods(id=52, neighborhood='Mesa Park'))
    DB.session.add(neighborhoods(id=53, neighborhood='Hancock'))
    DB.session.add(neighborhoods(id=54, neighborhood='Circle C'))
    DB.session.add(neighborhoods(id=55, neighborhood='Pleasant Valley'))
    DB.session.add(neighborhoods(id=56, neighborhood='North Loop'))
    DB.session.add(neighborhoods(id=57, neighborhood='Montopolis'))
    DB.session.add(neighborhoods(id=58, neighborhood='North Shoal Creek'))
    DB.session.add(neighborhoods(id=59, neighborhood='Pecan Spings'))
    DB.session.add(neighborhoods(id=60, neighborhood='Mueller'))
    DB.session.add(neighborhoods(id=61, neighborhood='Sunset Valley'))
    DB.session.add(neighborhoods(id=62, neighborhood='Old Enfield'))
    DB.session.add(neighborhoods(id=63, neighborhood='St. Johns'))
    DB.session.add(neighborhoods(id=64, neighborhood='Crestview'))
    DB.session.add(neighborhoods(id=65, neighborhood='Walnut Creek'))
    DB.session.add(neighborhoods(id=66, neighborhood='Bull Creek'))
    DB.session.add(neighborhoods(id=67, neighborhood='Cat Mountain'))
    DB.session.add(neighborhoods(id=68, neighborhood='Balcony Woods'))
    DB.session.add(neighborhoods(id=69, neighborhood='Gateway'))
    DB.session.add(neighborhoods(id=70, neighborhood='Anderson Mill'))
    DB.session.add(neighborhoods(id=71, neighborhood='Bryker Woods'))
    DB.session.add(neighborhoods(id=72, neighborhood='Canyon Mesa'))
    DB.session.add(neighborhoods(id=73, neighborhood='Windsor Hills'))
    DB.session.add(neighborhoods(id=74, neighborhood='Rainey Street'))
    DB.session.add(neighborhoods(id=75, neighborhood='Gracywoods'))
    DB.session.add(neighborhoods(id=76, neighborhood='Lamplight Village'))
    DB.session.add(neighborhoods(id=77, neighborhood='Milwood'))
    DB.session.add(neighborhoods(id=78, neighborhood='University Hills'))

    DB.session.commit()
