import QuerySQL

class Address(object):
    """description of class"""

    #add
    def add_address(self, town, zipcode, street, person_id, country):
        new_address = Address()
        new_address.town = town
        new_address.zipcode = zipcode
        new_address.street = street
        new_address.person_id = person_id
        new_address.country = country

        QuerySQL.QuerySQL().add_adress(new_address)



    

        #edit
    def edit_bus(self, id, name, seats):
        new_bus = Bus()        
        new_bus.name = name
        new_bus.seats = seats

        QuerySQL.QuerySQL().update_bus(id, new_bus)

    ##Edit a user with a specific id
    #def edit_person(self, id, first_name, last_name, personal_number):
    #    new_person = Person()
    #    new_person.first_name = first_name
    #    new_person.last_name = last_name
    #    new_person.personal_number = personal_number
        
    #    QuerySQL.QuerySQL().update_person(id, new_person)

        #remove 
    def remove_bus(self, id):
        QuerySQL.QuerySQL().delete_bus(id)
        print 'delete bus'
        

        
    