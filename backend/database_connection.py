from sqlite3 import Error
from constants import TABLE_NAME
from bitcoin_timestamp import BitcoinTimestamp
from custom_util import create_database

class DatabaseConnection:

    def __init__(self):
        """
        class constructor: generates a database connection object
        """
        self.__db = create_database()

    def insert_timestamp(self, bitcoin: BitcoinTimestamp):
        """
        inserts a bitcoin timestamp into the database

        :param bitcoin_timestamp:
            the bitcoin timestamp
        :type bitcoin_timestamp:
            BitcoinTimestamp
        :return:
            boolean indicating if the operation was successful or not
        :rtype:
            bool
        """
        try:
            # get cursor
            cursor = self.__db.cursor()
        except Error as e:
            print(e)
            return False

        try:
            # TODO (5.3.2)  
            # insert sql query
            sql = "INSERT INTO {} ({}, {});".format(TABLE_NAME, bitcoin.timestamp, bitcoin.price)
            # execute sql query
            cursor.execute(sql)
            # commit to db
            self.__db.commit()
            # close
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
      
    def get_all_timestampes(self):
        """
        gets all bitcoin timestamps in the database

        :return:
            a list of bitcoin timestamps
        :rtype:
            list[BitcoinTimestamp]
        """
        try:
            output = []
            
            # TODO (5.3.1)
            # get cursor
            cursor = self.__db.cursor()
            
            # insert sql query
            sql = "SELECT * from {}".format(TABLE_NAME)

            # execute sql query
            cursor.execute(sql)

            # fetch all results obtained
            results = cursor.fetchall()
            # close
            cursor.close()
            # convert results to BitcoinTimestamp objects and append to output
            for result in results:
                output.append(BitcoinTimestamp(result[0], result[1]))
            return output
        except Error as e:
            print(e)
            return []