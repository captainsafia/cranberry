class PriorityQueue():
	def __init__(self):
		self.data = {}

	def put(self, item, priority = None):
		if not priority:
			max_key = self.highest_priority()
			self.data[max_key + 1] = item
		elif priority in self.data.keys():
			raise Exception("Priority value already in queue!")
		else:
			self.data[priority] = item

	def pop(self, priority = None):
		if not priority:
			if len(self.data) > 0:
				max_key = self.highest_priority()
				item = self.data[max_key]
				del self.data[max_key]
				return item
			else:
				raise Exception("Queue is empty!")
		elif priority not in self.data.keys():
			raise Exception("Priority value is not in queue!")
		else:
			item = self.data[priority]
			del self.data[priority]
			return item

	def highest_priority(self):
		return max(self.data.keys()) if len(self.data) > 0 else 0

	def prioritize(self, item):
		if item not in self.data.values():
			raise Exception("Item is not in priority queue!")
		else:
			lookup = {value: key for key, value in self.data.iteritems()}
			new_priority = lookup[item] + 1
			if new_priority in self.data.keys():
				raise Exception("Incremeneted priority already in queue!")
			else:
				self.data[new_priority] = item