# Imports the Google Cloud client library
from google.cloud import datastore
import datetime
 


def create_client(project_id):
    return datastore.Client(project_id)

def add_player(client, name, description):
    key = client.key('player')

    player = datastore.Entity(
        key, exclude_from_indexes=['description'])

    player.update({
        'created': datetime.datetime.utcnow(),
        'description': description,
        'done': False,
        'name': name
    })

    client.put(player)

    return player.key


def mark_done(client, player_id):
    with client.transaction():
        key = client.key('player', player_id)
        player = client.get(key)

        if not player:
            raise ValueError(
                'Task {} does not exist.'.format(player_id))

        player['done'] = True

        client.put(player)


def delete_player(client, player_id):
    key = client.key('Player', player_id)
    client.delete(key)


def list_players(client):
    query = client.query(kind='player')
    query.order = ['created']

    return list(query.fetch(limit=1))


