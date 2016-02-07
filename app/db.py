from app import connection



conn = connection.theabbytapes
players = conn.players



def get_first_row():

	return players.find({"_id": { "$gt": 0, "$lt": 4} } )
	
	

def get_second_row():
	return players.find({"_id": { "$gt": 3, "$lt": 7} } )

def get_places():
	return players.find({"_id": { "$gt": 6, "$lt": 11 } } )

def get_downloads():
	return players.find({"_id": {"$gte": 11, "$lte": 15}})