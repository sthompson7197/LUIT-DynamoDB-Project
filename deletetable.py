import boto3

client = boto3.client('dynamodb')

try:
    resp = client.delete_table(
        TableName="IceCream",
    )
    print("You have successfully deleted the table.!")
except Exception as x:
    print("There was en error deleting the table. Please review error:")
    #prints error message
    print(x)
