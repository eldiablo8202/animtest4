from os import path

from data import constants

class Map:
	def __init__(self, filename):
		self.mapData = []
		with open (filename, 'r+') as inFile:
			for line in inFile:
				self.mapData.append(line.strip())

			self.tileCountX = len(self.mapData[0])					#get count of chars on first line
			self.tileCountY = len(self.mapData)						#get line count of map file	
			self.mapWidth = self.tileCountX * constants.TILE_SIZE	#calculate map width
			self.mapHeight = self.tileCountY * constants.TILE_SIZE	#calculate map height
