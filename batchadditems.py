import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('IceCream')

with table.batch_writer() as batch:
    batch.put_item(Item={"Brand": "Ben & Jerry's", "Flavor": "Half Baked"})
    batch.put_item(Item={"Brand": "Breyers", "Flavor": "Vanilla"})
    batch.put_item(Item={"Brand": "Breyers", "Flavor": "Chocolate"})
    batch.put_item(Item={"Brand": "Ben & Jerry's", "Flavor": "Cherry Garcia"})
    batch.put_item(Item={"Brand": "Edys", "Flavor": "Chocolate"})
    batch.put_item(Item={"Brand": "Edys", "Flavor": "Vanilla"})
    batch.put_item(Item={"Brand": "Edys", "Flavor": "Coffee"})
    batch.put_item(Item={"Brand": "Blue Bell", "Flavor": "Vanilla"})
    batch.put_item(Item={"Brand": "Blue Bell", "Flavor": "Chocolate"})
    batch.put_item(Item={"Brand": "Ben & Jerry's", "Flavor": "Chocolate Fudge Brownie"})
print(batch)

 
