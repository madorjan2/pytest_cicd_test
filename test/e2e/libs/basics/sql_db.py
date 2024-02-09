import json
import os
import mysql

from mysql.connector import connect, errorcode

def read_sql_json():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	file_path = os.path.join(current_dir, 'db_info.json')
	with open(file_path, 'r') as json_file:
		return json.load(json_file)

class Query:

	def __init__(self):
		self.dict = read_sql_json()
		try:
			self.connection = connect(user=self.dict['username'],
									  password=self.dict['password'],
									  host=self.dict['host'],
									  database=self.dict['database'])
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your username or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)

	def __del__(self):
		self.connection.close()

	def get_dict(self, query):
		with self.connection.cursor(dictionary=True) as cursor:
			cursor.execute(query)
			return cursor.fetchall()

	def update_db(self, query):
		with self.connection.cursor() as cursor:
			cursor.execute(query)
			self.connection.commit()