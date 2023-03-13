from .models import Photo, PropertyType, Property

def init_property_types(db):
    if PropertyType.query.count() == 0:
        apartment = PropertyType(name='Apartment')
        house = PropertyType(name='House')
        # cottage = PropertyType(name='Cottage')
        # studio = PropertyType(name='Studio')
        # suite = PropertyType(name='Suite')
        # cabin = PropertyType(name='Cabin')
        # db.session.add_all([apartment, house, cottage, studio, suite, cabin])
        db.session.add_all([apartment, house])
        db.session.commit()

def init_properties(db):
    if Property.query.count() == 0:
        prop1= Property(id = 621,title='Sunny Beach Apartment - Two Bedrooms',description='A modern and bright apartment with a stunning sea view. This spacious and airy two-bedroom apartment is the perfect beachfront property for a family or a couple.',rooms=2,bathrooms=1,price=120000.00,property_type_id='1',location='123 Sunny Beach Road, Miami', main_photo_id = 1236)
        prop2= Property(id = 622,title='Downtown Loft - One Bedroom',description='A stylish and contemporary loft in the heart of the city. This beautiful one-bedroom apartment is perfect for a young professional or couple looking for a modern and convenient living space.',rooms=1,bathrooms=1,price=200000.00,property_type_id='1',location='456 Downtown Avenue, New York', main_photo_id=1235)
        prop3= Property(id = 623,title='Charming Victorian House - Four Bedrooms',description='A stunning and historic Victorian house with plenty of character. This beautiful four-bedroom home features original woodwork, stained glass windows, and a wrap-around porch.',rooms=4,bathrooms=2,price=600000.00,property_type_id='2',location='789 Victorian Lane, San Francisco', main_photo_id =1232)
        prop4= Property(id = 624,title='Cozy Mountain Cabin - Two Bedrooms',description='A cozy and rustic cabin in the heart of the mountains. This two-bedroom retreat is the perfect getaway for anyone looking to escape the hustle and bustle of city life.',rooms=2,bathrooms=1,price=300000.00,property_type_id='2',location='101 Cabin Road, Denver', main_photo_id = 1231)
        prop5= Property(id = 625,title='Luxury Waterfront House - Five Bedrooms',description='A luxurious and modern waterfront property with breathtaking views. This five-bedroom house features a gourmet kitchen, infinity pool, and private boat dock.',rooms=5,bathrooms=4,price=2500000.00,property_type_id='2',location='1111 Waterfront Drive, Miami', main_photo_id=1234)
        prop6= Property(id = 626,title='Spacious City House - Three Bedrooms',description='A spacious and elegant city house with plenty of natural light. This three-bedroom home features a large backyard, perfect for entertaining or relaxing.',rooms=3,bathrooms=2,price=800000.00,property_type_id='2',location='222 City Street, Los Angeles', main_photo_id = 1233)
        
        db.session.add_all([prop1, prop2, prop3, prop4, prop5, prop6])
        db.session.commit()

def intit_photos(db):
    if Photo.query.count() == 0:
        photo1= Photo(id= 1231, name='cabin.jpg')
        photo2= Photo(id= 1232,name='victorian.png')
        photo3= Photo(id= 1233,name='housecity.jpg')
        photo4= Photo(id= 1234,name='luxbeachhouse.jpg')
        photo5= Photo(id= 1235,name='Modern-Open-Loft.jpg')
        photo6= Photo(id= 1236,name='sunnyapt1.jpg')

        db.session.add_all([photo1,photo2,photo3,photo4,photo5,photo6])
        db.session.commit()