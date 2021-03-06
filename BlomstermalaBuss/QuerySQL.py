import dbConnector

class QuerySQL(object):
    """description of class"""
    db_connection = dbConnector.dbConnector()

    #Get all data in specific table
    def get_all_data(self, table):
        query = 'SELECT * from %s' % (table)
        result = self.db_connection.get_data(query)
        return result

    #Get all data from table Person
    def get_all_data_person(self):
        query = 'SELECT * from Person'
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['FirstName']=record[1]
            resline['LastName']=record[2]
            resline['PersonalNumber']=record[3]
            reslist.append(resline)
        return reslist

    #Add person
    def add_user(self, new_person):
        query = 'INSERT INTO Person (FirstName, LastName, PersonalNumber) VALUES (\'%s\', \'%s\', \'%s\')' % (new_person.first_name, new_person.last_name, new_person.personal_number)
        self.db_connection.add_data(query)

    #Delete person
    def delete_user(self, id):                 
        query = 'DELETE FROM Person WHERE ID=%s CONSTRAINT Address_ibfk_1 FOREIGN KEY (ID) REFERENCES Address_ibfk_1 (ID) ON DELETE CASCADE' % (id)
        self.db_connection.remove_data(query)


    #Delete bus
    def delete_bus(self, id):
        query = 'DELETE FROM Bus WHERE ID=%s' % (id)
        self.db_connection.remove_data(query)


    #Add bus
    def add_bus(self, new_bus):
        query = 'INSERT INTO Bus (Name, Seats) VALUES (\'%s\', \'%s\')' % (new_bus.name, new_bus.seats)
        self.db_connection.add_data(query)

    #Add city
    def add_city(self, new_city):
        query = 'INSERT INTO City (Name, Country) VALUES (\'%s\', \'%s\')' % (new_city.name, new_city.country)
        self.db_connection.add_data(query)

    #Delete city
    def delete_city(self, id):
        query = 'DELETE FROM City WHERE ID=%s' % (id)
        self.db_connection.remove_data(query)

    #Get info about specific person
    def get_person(self, id):
        query = 'SELECT * FROM Person WHERE ID=%s' % (id)
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['FirstName']=record[1]
            resline['LastName']=record[2]
            resline['PersonalNumber']=record[3]
            reslist.append(resline)
        return reslist

    #Update information about person
    def update_person(self, id, new_person):
        query = 'UPDATE Person SET FirstName=\'%s\', LastName=\'%s\', PersonalNumber=\'%s\' WHERE ID=\'%s\'' % (new_person.first_name, new_person.last_name, new_person.personal_number, id)
        self.db_connection.add_data(query)

    #Get information about all buses
    def get_buses(self):
        query = 'SELECT ID, Name, Seats FROM Bus'
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['Name']=record[1]
            resline['Seats']=record[2]
            reslist.append(resline)
        return reslist

    #Get info about specific bus
    def get_bus(self, id):
        query = 'SELECT ID, Name, Seats FROM Bus WHERE ID=%s' % (id)
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['Name']=record[1]
            resline['Seats']=record[2]
            reslist.append(resline)
        return reslist

    #Update information about bus
    def update_bus(self, id, new_bus):
        query = 'UPDATE Bus SET Name=\'%s\', Seats=\'%s\' WHERE ID=\'%s\'' % (new_bus.name, new_bus.seats, id)
        self.db_connection.add_data(query)

    #Update information about person
    def update_person(self, id, new_person):
        query = 'UPDATE Person SET FirstName=\'%s\', LastName=\'%s\', PersonalNumber=\'%s\' WHERE ID=\'%s\'' % (new_person.first_name, new_person.last_name, new_person.personal_number, id)
        self.db_connection.add_data(query)

    #Search trip on depart from
    def search_trip(self, search):
        query = 'SELECT Trip.ID, Start, Ends, Weekday, Price, a.Name AS DepartsFrom, b.Name AS ArrivesAt FROM Trip INNER JOIN City a ON Trip.DepartsFrom=a.ID INNER JOIN City b ON Trip.ArrivesAt=b.ID WHERE Trip.DepartsFrom=(SELECT ID FROM City WHERE ID=\'%s\')' % (search)
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['Start']=record[1]
            resline['Ends']=record[2]
            resline['Weekday']=record[3]
            resline['Price']=record[4]
            resline['DepartsFrom']=record[5]
            resline['ArrivesAt']=record[6]
            reslist.append(resline)
        return reslist

    #See all trips
    def get_all_trips(self):
        query = 'SELECT Trip.ID, Start, Ends, Weekday, Price, a.Name AS DepartsFrom, b.Name AS ArrivesAt FROM Trip INNER JOIN City a ON Trip.DepartsFrom=a.ID INNER JOIN City b ON Trip.ArrivesAt=b.ID '
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['Start']=record[1]
            resline['Ends']=record[2]
            resline['Weekday']=record[3]
            resline['Price']=record[4]
            resline['DepartsFrom']=record[5]
            resline['ArrivesAt']=record[6]
            reslist.append(resline)
        return reslist

    #Add trip
    def add_trip(self, trip):
        query = 'INSERT INTO Trip (Start, Ends, Weekday, Price, DepartsFrom, ArrivesAt, BusID) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (trip.start_time, trip.end_time, trip.weekday, trip.price, trip.departs_from, trip.arrives_at, trip.bus)
        self.db_connection.add_data(query)

    #Get person id from firstnme and lastname
    def get_person_id(self, first_name, last_name):
        query = 'SELECT * FROM Person WHERE FirstName=\'%s\' AND LastName=\'%s\'' % (first_name, last_name)
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['FirstName']=record[1]
            resline['LastName']=record[2]
            resline['PersonalNumber']=record[3]
            reslist.append(resline)
        return reslist

    #Add booking
    def add_booking(self, new_booking):
        query = 'INSERT INTO Booking (Date, TripID, PersonID) VALUES (\'%s\', \'%s\', \'%s\')' % (new_booking.date, new_booking.trip, new_booking.person)
        self.db_connection.add_data(query)

    #Get id of last person added
    def get_last_person_id(self):
        query = 'SELECT ID FROM Person ORDER BY ID DESC LIMIT 1'
        result = self.db_connection.get_data(query)
        reslist = []
        for record in result:
            resline = {}
            resline['ID']=record[0]
            reslist.append(resline)
        return reslist
        
    # add address
    def add_adress(self, new_address):
        query = 'INSERT INTO Address (Town, Zipcode, Street, PersonID, Country) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (new_address.town, new_address.zipcode, new_address.street, new_address.person_id, new_address.country)
        self.db_connection.add_data(query)

    #Add phone number
    def add_phone(self, new_phone):
        query = 'INSERT INTO Phone (PersonID, PhoneNumber) VALUES (\'%s\', \'%s\')' % (new_phone.person_id, new_phone.phone_number)
        self.db_connection.add_data(query)

    #Get information about all cities
    def get_cities(self):
        query = 'SELECT ID, Name, Country FROM City'
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['Name']=record[1]
            resline['Country']=record[2]
            reslist.append(resline)
        return reslist

    #Get information about all bookings
    def get_all_bookings(self):
        query = """
            select 
             b.ID,
             b.Date,
             t.Start,
             t.Ends,
             t.Price,
             dc.Name as FromCity,
             dc.Country as FromCountry,
             ac.Name as ToCity,
             ac.Country as ToCountry,
             bus.Name as BusName,
             p.FirstName,
             p.LastName,
             p.PersonalNumber
             from Booking as b
            join Trip as t
             on t.id = b.TripID
            join Person as p
             on p.id = b.PersonID
            join City as dc
             on t.DepartsFrom = dc.ID
            join City as ac
             on t.ArrivesAt = ac.ID
            join Bus as bus
             on t.BusID = bus.id"""
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['Date']=record[1]
            resline['Start']=record[2]
            resline['Ends']=record[3]
            resline['Price']=record[4]
            resline['FromCity']=record[5]
            resline['FromCountry']=record[6]
            resline['ToCity']=record[7]
            resline['ToCountry']=record[8]
            resline['BusName']=record[9]
            resline['FirstName']=record[10]
            resline['LastName']=record[11]
            resline['PersonalNumber']=record[12]
            reslist.append(resline)
        
        return reslist

    #Get list of citys that belongs to a trip via DepartsFrom
    def get_depart_cities(self):
        query = """
            SELECT DISTINCT City.ID, City.Name, City.Country 
            FROM City 
            JOIN Trip
            ON Trip.DepartsFrom=City.ID
            """
        result = self.db_connection.get_data(query)
        reslist=[]
        for record in result:
            resline={}
            resline['ID']=record[0]
            resline['Name']=record[1]
            resline['Country']=record[2]
            reslist.append(resline)

        return reslist

