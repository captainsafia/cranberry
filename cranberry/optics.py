from queue import PriorityQueue
from distances import euclidean_distance

class OPTICS():
	def __init__(self, epsilon, min_samples, distance = euclidean_distance):
		self.epsilon = epsilon
		self.min_samples = min_samples
		self.distance = distance
		self.reachability= {}
		self.processed = []
		self.clusters = []
		self.ordered = []

	def get_neighbors(self, point, epsilon, data):
		"""
		Returns the neighbors of point in data limited by epsilon.

		Keyword arguments: 

		point -- the point whose neighbors to find
		epsilon -- the 
		data -- the data set that clustering will be applied on
		"""
		neighbors = []
		for id_ in xrange(len(data)):
			print point, data[id_]
			if point != data[id_] and self.distance(point, data[id_]):
				neighbors.append(id_)
		return neighbors

	def core_distance(self, epsilon, min_samples, point, data):
		"""
		Returns distance from point to the min_samples-th closest
		point in data.

		Keyword arguments:
		epsilon -- the limit of distance value considered approximate
		min_samples -- the minimum number of samples in a cluster
		point -- the point whose proximity to determine
		data -- the data clustering will be applied to
		"""
		for candidate in xrange(0, epsilon):
			neighbors = self.get_neighbors(data[candidate], epsilon, data)
			if len(neighbors) >= min_samples:
				return candidate
		return None

	def reachability_distance(self, epsilon, min_samples, point_x, point_y):
		"""
		Returns the distance between point_x and point_y or the distance from 
		point_y to the nearest min_samples-th cluster.

		Keyword arguments:
		epsilon -- the limit of distance value considered approximate
		min_samples -- the minimum number of samples in a cluster
		point_x -- the first point
		point_y -- the second point
		"""
		print point_x, point_y
		max(self.core_distance(epsilon, min_samples, point_y), 
			self.distance(point_x, point_y))

	def update(self, queue, neighbors, point, epsilon, min_samples):
		distance = self.core_distance(epsilon, min_samples, point)
		for neighbor in neighbors:
			if neighbor not in self.processed:
				new_distance = max(distance, self.distance(point, neighbor))
				if not self.reachability[neighbor]:
					self.reachability[neighbor] = new_distance
					queue.put((neighbor, new_distance))
				elif new_distance < self.reachability[neighbor]:
					self.reachability[neighbor] = new_distance
					queue.prioritize((neighbor, new_distance))

	def fit(self, data):
		for x, y in data:
			self.reachability[(x,y)] = None
			unprocessed = list(set(data) - set(self.processed))
			for t, u in unprocessed:
				neighbors = self.get_neighbors((t,u), self.epsilon, data)
				self.processed.append((t, u))
				self.clusters.append((t, u))
				if self.core_distance(self.epsilon, self.min_samples, (x,y), data):
					seeds = PriorityQueue()
					seeds = self.update(seeds, neighbors, (x,y),
										self.epsilon, self.min_samples)
					for seed in seeds.get():
						seed_neighbors = get_neighbors(seed, self.epsilon, data)
						processed.append(seed)
						self.ordered.append(seed)
						if self.core_distance(self.epsilon, 
												self.min_samples,
												seed,
												data) != None:
							seeds = self.update(seeds,
												seed_neighbors, 
												seed, 
												self.epsilon, 
												self.min_samples)
			return self.clusters