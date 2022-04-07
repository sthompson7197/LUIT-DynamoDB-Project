import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('IceCream')

response = table.query(KeyConditionExpression=Key('Brand').eq('Breyers'))

print("The query returned the following items:")
#use for loop to look through table to list each item that matches the specified key
for item in response['Items']:
    print(item)
