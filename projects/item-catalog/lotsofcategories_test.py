from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(username="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

User2 = User(username="Papo Barista", email="tinnypapo@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()

User3 = User(username="Papo Robo", email="robopapo@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User3)
session.commit()

print "Successfully created users"

# Create base Categories
# 1
outdoor = Category(user_id=1, category_name="Outdoor", description="outdoor fun", parent_id=None)
session.add(outdoor)
session.commit()

# 2
electronics = Category(user_id=2, category_name="Electronics", description="All electronic equipments", parent_id=None)
session.add(electronics)
session.commit()

# 3
home = Category(user_id=3, category_name="Home", description="All home equipments", parent_id=None)
session.add(home)
session.commit()

# 4
sports = Category(user_id=1, category_name="Sports", description="All sporting equipments", parent_id=1)
session.add(sports)
session.commit()

# 5
camping = Category(user_id=1, category_name="Camping", description="All camping equipments", parent_id=1)
session.add(camping)
session.commit()

# 6
computers = Category(user_id=2, category_name="Computers", description="All computing equipments", parent_id=2)
session.add(computers)
session.commit()

# 7
cellphones = Category(user_id=2, category_name="Cell Phones", description="All cellphone equipments", parent_id=2)
session.add(cellphones)
session.commit()

# 8
kitchen = Category(user_id=3, category_name="Kitchen", description="All kitchen equipments", parent_id=3)
session.add(kitchen)
session.commit()

# 9
furniture = Category(user_id=3, category_name="Furniture", description="All home furniture", parent_id=3)
session.add(furniture)
session.commit()


print "Successfully added categories"

# Create items

# user_id = 1, category_id = 4

sport_1 = Item(user_id=1, category_id=4, item_name="Soccer Ball", 
       description="Ball used to play Soccer", price="$15.00", picture="SOCCER" )
session.add(sport_1)
session.commit()

sport_2 = Item(user_id=1, category_id=4, item_name="Tennis Balls", 
       description="Ball used to play Tennis", price="$10.00", picture="Tennis" )
session.add(sport_2)
session.commit()

sport_3 = Item(user_id=1, category_id=4, item_name="Tennis Racquet", 
       description="Racquet used to play Tennis", price="$60.00", picture="Tennis")
session.add(sport_3)
session.commit()

sport_4 = Item(user_id=1, category_id=4, item_name="Cleats", 
       description="Soccer shoes", price="$40.00", picture="Scoccer Shoes" )
session.add(sport_4)
session.commit()

sport_5 = Item(user_id=1, category_id=4, item_name="Shin guards", 
       description="Soccer shin protector", price="$20.00", picture="Scoccer shin guards" )
session.add(sport_5)
session.commit()

sport_6 = Item(user_id=1, category_id=4, item_name="Baseball bat", 
       description="Baseball bat for kids", price="$60.00", picture="Baseball" )
session.add(sport_6)
session.commit()

# user_id = 1, category_id = 5

camp_1 = Item(user_id=1, category_id=5, item_name="Tent", 
       description="Tent for camping", price="$60.00", picture="Tent" )
session.add(camp_1)
session.commit()

camp_2 = Item(user_id=1, category_id=5, item_name="Sleeping Bag", 
       description="Sleeping bags used for sleeping", price="$50.00", picture="Sleeping Bags" )
session.add(camp_2)
session.commit()

camp_3 = Item(user_id=1, category_id=5, item_name="Rods", 
       description="Used to hold up tent", price="$10.00", picture="Rods")
session.add(camp_3)
session.commit()

camp_4 = Item(user_id=1, category_id=5, item_name="Swiss Knife", 
       description="Swiss knife for random stuff", price="$25.00", picture="Knife" )
session.add(camp_4)
session.commit()

camp_5 = Item(user_id=1, category_id=5, item_name="Camping fire fuel", 
       description="Fuel for starting a camping fire", price="$20.00", picture="picture" )
session.add(camp_5)
session.commit()

camp_6 = Item(user_id=1, category_id=5, item_name="Mosquito Repellant", 
       description="Used to protect against mosquitos", price="$12.00", picture="mosquitos" )
session.add(camp_6)
session.commit()


# user_id = 2, category_id = 6

comp_1 = Item(user_id=2, category_id=6, item_name="PC", 
       description="Windos 10", price="$1200.00", picture="Dell" )
session.add(comp_1)
session.commit()

comp_2 = Item(user_id=2, category_id=6, item_name="Hard Drive", 
       description="SSD", price="$250.00", picture="Samsung" )
session.add(comp_2)
session.commit()

comp_3 = Item(user_id=2, category_id=6, item_name="RAM", 
       description="8 GB DDR3", price="$80.00", picture="Corshair")
session.add(comp_3)
session.commit()

comp_4 = Item(user_id=2, category_id=6, item_name="Processor", 
       description="Intel I7", price="$450.00", picture="Intel" )
session.add(comp_4)
session.commit()

comp_5 = Item(user_id=2, category_id=6, item_name="Monitor", 
       description="LG 24 inch", price="$225.00", picture="Oled" )
session.add(comp_5)
session.commit()

comp_6 = Item(user_id=2, category_id=6, item_name="Battery", 
       description="Keep yuor laptop charged", price="$120.00", picture="Samsung" )
session.add(comp_6)
session.commit()


# user_id = 2, category_id = 7

cell_1 = Item(user_id=2, category_id=7, item_name="Samsung Galaxy S9", 
       description="Android", price="$720.00", picture="Samsung" )
session.add(cell_1)
session.commit()

cell_2 = Item(user_id=2, category_id=7, item_name="Apple Iphone X", 
       description="IOS", price="$1000.00", picture="Apple" )
session.add(cell_2)
session.commit()

cell_3 = Item(user_id=2, category_id=7, item_name="Google Pixel XL", 
       description="Pure Android", price="$800.00", picture="Google")
session.add(cell_3)
session.commit()

cell_4 = Item(user_id=2, category_id=7, item_name="Cell case", 
       description="Samsung Galaxy S9 case", price="$25.00", picture="Cases" )
session.add(cell_4)
session.commit()

cell_5 = Item(user_id=2, category_id=7, item_name="Charger", 
       description="universal charger for Android phones", price="$35.00", picture="charger" )
session.add(cell_5)
session.commit()

cell_6 = Item(user_id=2, category_id=7, item_name="Car charger", 
       description="Keep your cell charged in long drives", price="$30.00", picture="cars" )
session.add(cell_6)
session.commit()


# user_id = 3, category_id = 8

kit_1 = Item(user_id=3, category_id=8, item_name="Blender", 
       description="Vitamix", price="$720.00", picture="Vitamix" )
session.add(kit_1)
session.commit()

kit_2 = Item(user_id=3, category_id=8, item_name="Juicer", 
       description="Omega", price="$500.00", picture="Omega" )
session.add(kit_2)
session.commit()

kit_3 = Item(user_id=3, category_id=8, item_name="Toaster", 
       description="Toast some bread", price="$30.00", picture="Toaster")
session.add(kit_3)
session.commit()

kit_4 = Item(user_id=3, category_id=8, item_name="Knife", 
       description="Chefs knife", price="$45.00", picture="Knife" )
session.add(kit_4)
session.commit()

kit_5 = Item(user_id=3, category_id=8, item_name="Grater", 
       description="grates stuff", price="$20.00", picture="grater" )
session.add(kit_5)
session.commit()

kit_6 = Item(user_id=3, category_id=8, item_name="Spoons", 
       description="Drink your soups", price="$45.00", picture="spoons" )
session.add(kit_6)
session.commit()

# user_id = 3, category_id = 9

fur_1 = Item(user_id=3, category_id=9, item_name="Bed", 
       description="Queen size", price="$500.00", picture="Ikea" )
session.add(fur_1)
session.commit()

fur_2 = Item(user_id=3, category_id=9, item_name="Table", 
       description="computer table", price="$230.00", picture="table" )
session.add(fur_2)
session.commit()

fur_3 = Item(user_id=3, category_id=9, item_name="Couch", 
       description="LEather couch", price="$900.00", picture="Living Spaces")
session.add(fur_3)
session.commit()

fur_4 = Item(user_id=3, category_id=9, item_name="Dinning Table", 
       description="Dinning for 4", price="$450.00", picture="Dinning" )
session.add(fur_4)
session.commit()

fur_5 = Item(user_id=3, category_id=9, item_name="TV Mount", 
       description="TV stand for new TVs", price="$200.00", picture="mount" )
session.add(fur_5)
session.commit()

fur_6 = Item(user_id=3, category_id=9, item_name="Coffee Table", 
       description="Coffe table for yuor coffes", price="$150.00", picture="Coffee" )
session.add(fur_6)
session.commit()

print "added menu items!"