import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('IceCream')

response = table.delete_item(Key = {'Brand': 'Breyers', 'Flavor': 'Chocolate'})

print(response)
