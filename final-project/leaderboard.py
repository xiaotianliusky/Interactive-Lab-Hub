from decimal import Decimal
import json
import boto3
from botocore.config import Config




def writeLeaderboard(leaderBoard):
    dynamodb = getDDB()

    table = dynamodb.Table('SnakeJoystickLeaderBoard')
    table.put_item(Item=leaderBoard)

def getDDB():
    dynamodb = boto3.resource('dynamodb',config=Config(region_name="us-west-2"))
    return dynamodb

def getLeaderboard(gameID):

    dynamodb = getDDB()

    table = dynamodb.Table('SnakeJoystickLeaderBoard')

    try:
        response = table.get_item(Key={'GameID': gameID})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']

def key(e):
    return e['score']

def addToLeaderBoard(name, score):
    leaderboard = getLeaderboard("snakeJoystick")
    leaders = leaderboard["leaders"]
    leaders.append({"name":name, "score": score})
    leaders.sort(key=key)
    leaders.reverse()
    leaders.pop()
    leaderboard["leaders"] = leaders
    writeLeaderboard(leaderboard)
    return leaderboard






if __name__ == '__main__':
    addToLeaderBoard("cjh", 1)
    leaderBoard = getLeaderboard("snakeJoystick")
    if leaderBoard:
        print("Get leaderboard succeeded:")
        print(leaderBoard)
