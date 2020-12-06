import json

def write_game(id,jsobj):
	with open(str(id )+ '.json','w') as f:
		json.dump(jsobj, f)

def read_game(id):
	with open(str(id) + '.json') as f:
		return json.loads(f.read())