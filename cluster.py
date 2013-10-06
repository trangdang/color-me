import math, random, json

class Color:
    def __init__(self, rgb_vals):
        if not isinstance(rgb_vals, tuple):
            raise TypeError, 'not a tuple'
        elif len(rgb_vals) != 3:
            raise ValueError, 'there should be 3 values'
        else:
            for i in rgb_vals:
                if not isinstance(i, int):
                    raise TypeError, 'not an int'
                elif i<0 or i>255:
                    raise ValueError, 'not a valid rgb value'
            self.rgb = rgb_vals

    @classmethod
    def from_hex(cls, hex_string):
        if not isinstance(hex_string, unicode):
            raise TypeError, 'not a unicode string'
        elif len(hex_string) != 6:
            raise ValueError, 'hex code should be 6 characters long'
        else:
            rgb_vals = tuple(int(hex_string[i:i+2], 16) for i in range(0,6,2))
            return cls(rgb_vals)

    def to_hex(self):
        return '%02x%02x%02x' % self.rgb
    
    def dist(self, other_color):
        return math.sqrt(sum((self.rgb[i]-other_color.rgb[i])**2 for i in xrange(3)))

    def avg(self, other_color):
        return Color(tuple(int((self.rgb[i]+other_color.rgb[i])/2) for i in xrange(3)))

def compute_distances(colors_list):
    distances = {}
    for colors in [(x, y) for x in colors_list for y in colors_list]:
        if colors[::-1] in distances:
            distances[colors] = distances[colors[::-1]]
        else:
            distances[colors] = colors[0].dist(colors[1])
    return distances

def get_clusters(medoid_candidates, colors_list, distances):
    clusters = {}
    for m in medoid_candidates:
        clusters[m] = []

    for c in colors_list:
        best_medoid = medoid_candidates[0]
        best_distance = distances[(best_medoid, c)]
        for m in medoid_candidates:
            d = distances[(m,c)]
            if d < best_distance:
                best_distance = d
                best_medoid = m
        clusters[best_medoid].append((c,best_distance))

    return clusters

def total_cost(medoid_candidates, colors_list, distances):
    clusters = get_clusters(medoid_candidates, colors_list, distances)
    return sum([sum( [ point[1] for point in clusters[m]] ) for m in clusters.keys()])


def k_medoids(colors_list, k):
    dists = compute_distances(colors_list)

    medoids = random.sample(colors_list, k)
    cost = total_cost(medoids, colors_list, dists)
    while True:
        swap_med = random.choice(medoids)
        temp_med_list = medoids
        temp_cost = cost
        other_points = list(set(colors_list) - set(medoids))
        for o in other_points:
            trial_med_list = medoids[:]
            trial_med_list.remove(swap_med)
            trial_med_list.append(o)
            trial_cost = total_cost(trial_med_list, colors_list, dists)
            if trial_cost < temp_cost:
                temp_cost = trial_cost
                temp_med_list = trial_med_list

        if temp_cost >= cost:
            break
        else:
            medoids = temp_med_list
            cost = temp_cost

    return medoids
    
def color_strings(result):
    return [c.to_hex() for c in result]

def process(input_color_strings, num_clusters):
    colors_list = [Color.from_hex(s) for s in input_color_strings]
    cluster_result = k_medoids(colors_list, num_clusters)
    return color_strings(cluster_result)
