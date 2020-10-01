from db.run_sql import run_sql
from models.human import Human
from models.zombie import Zombie
from models.zombie_type import ZombieType
import repositories.zombie_repository as zombie_repository
import repositories.zombie_type_repository as zombie_type_repository

def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    biting.id = id

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for result in results:
        biting = Biting(result["name"], result["zombie"])
        bitings.append(biting)
    return bitings


def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)
    

def select(id):
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    biting = Biting(result["human"], result["zombie"])
    return biting


def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(biting):
    sql = "UPDATE bitings SET human = %s WHERE id = %s"
    values = [biting.human, biting.id ]
    run_sql(sql ,values)