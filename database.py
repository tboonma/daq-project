import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

class Database:
    """Encapsulates an Amazon DynamoDB table."""
    
    def __init__(self, table_name: str):
        """
        :param table_name: The table name of object.
        """
        self.dyn_resource = boto3.resource('dynamodb')
        self.__create_table_if_not_exists(table_name)
    
    def __create_table_if_not_exists(self, table_name: str):
        """
        Determines whether a table exists. As a side effect, stores the table in
        a member variable.
        :param table_name: The name of the table to check.
        """
        try:
            table = self.dyn_resource.Table(table_name)
            table.load()
            self.table = table
        except ClientError as err:
            if err.response['Error']['Code'] == 'ResourceNotFoundException':
                self.__create_table(table_name)
            else:
                logger.error(
                    "Couldn't check for existence of %s. Here's why: %s: %s",
                    table_name,
                    err.response['Error']['Code'], err.response['Error']['Message'])
                raise

    def __create_table(self, table_name: str):
        """
        Creates an Amazon DynamoDB table that can be used to store movie data.
        The table uses the release year of the movie as the partition key and the
        title as the sort key.
        :param table_name: The name of the table to create.
        :return: The newly created table.
        """
        try:
            self.table = self.dyn_resource.create_table(
                TableName=table_name,
                ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10})
            self.table.wait_until_exists()
        except ClientError as err:
            logger.error(
                "Couldn't create table %s. Here's why: %s: %s", table_name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
        else:
            return self.table
    
    def create(self, items):
        """
        Adds items to the table.

        :param items: THe dictionary of items to add into table.
        """
        try:
            self.table.put_item(Item=items)
        except ClientError as err:
            logger.error(
                "Couldn't add items to table %s. Here's why: %s: %s",
                self.table.name,
                err.response['Error']['Code'],
                err.response['Error']['Message'])
            raise

    def query(self, condition):
        try:
            response = self.table.query(KeyConditionExpression=condition)
        except ClientError as err:
            logger.error(
                "Couldn't query Here's why: %s: %s",
                err.response['Error']['Code'],
                err.response['Error']['Message'])
            raise
        else:
            return response['Items']
    
    def get(self):
        """
        Gets all items in the table.
        :return: The list of items in the table.
        """
        try:
            response = self.table.scan()
        except ClientError as err:
            logger.error(
                "Couldn't get from table %s. Here's why: %s: %s",
                self.table.name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
        else:
            return response['Items']

    def getByField(self, field):
        """
        Get an item by specified field
        :param field: A Dictionary of specified field value to get.
        :return: An item with specified field value.
        """
        try:
            response = self.table.get_item(Key=field)
        except ClientError as err:
            logger.error(
                "Couldn't get from table %s. Here's why: %s: %s",
                self.table.name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
        else:
            return response['Item']

    def delete(self, field):
        """
        Delete an item by specified field
        :param field: A Dictionary of specified field value to get.
        :return: An item with specified field value.
        """
        try:
            self.table.delete_item(Key=field)
        except ClientError as err:
            logger.error(
                "Couldn't delete. Here's why: %s: %s",
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
