import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table (
    TableName ='IceCream',
       KeySchema = [
           {
               'AttributeName': 'Brand',
               'KeyType': 'HASH'
           },
           {
               'AttributeName': 'Flavor',
               'KeyType': 'RANGE'
           }
           ],
           AttributeDefinitions = [
               {
                   'AttributeName': 'Brand',
                   'AttributeType': 'S'
               },
               {
                   'AttributeName':'Flavor',
                   'AttributeType': 'S'
               }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits':10,
                'WriteCapacityUnits':10
            }
          
    )
print(table)
