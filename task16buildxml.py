#!/usr/bin/python3
#build xml file in mysql table 
import xml.etree.ElementTree as ET
import pymysql
class  siva1:
	def __init__(self):
		self.tree = ET.parse('s.xml')
		self.root = self.tree.getroot()
		self.db=pymysql.connect("localhost","root","srm","siva1")
		self.cur = self.db.cursor()
	def buildxml(self):	
		self.cur.execute("select * from xml1")
		columns=[i[0] for i in self.cur.description]
		allrows=self.cur.fetchall()
		buildxml=open("pymysqlxml.xml","w")
		buildxml.write('#build xml file in mysql data in python')
		buildxml.write("\n")
		buildxml.write('<empdata>')
		buildxml.write("\n")
		for rows in allrows:
			buildxml.write('<data>')
			buildxml.write("\n")
			c=0
			for col in columns:
				data=rows[c]
			#	if data == None:
			#		data=''
				buildxml.write('<{}>{}</{}>'.format(col,data,col))
				buildxml.write("\n")
				c +=1
			buildxml.write('</data>')
			buildxml.write("\n")
		buildxml.write('</empdata>')
		buildxml.write("\n")
		buildxml.close()

obj=siva1()
obj.buildxml()

		
