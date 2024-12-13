import tkinter as tk
from tkinter import messagebox

NODES_INTRODUCTION = {
    'BC Place': 'A multi-purpose stadium, home to major sporting events and concerts, known for its iconic retractable roof.',
    'Steam Clock': 'A famous clock located in Gastown, powered by steam, known for its hourly whistle and steam release.',
    'Canada Place': 'A prominent waterfront landmark, home to a convention center and known for its white sail-like roof.',
    'Vancouver Art Gallery': 'A major public art museum in downtown Vancouver, featuring exhibitions of local and international artists.',
    'Granville Island': 'A vibrant shopping district on a small peninsula, known for its public market, artisan shops, and waterfront views.',
    'Vancouver Aquatic Center': 'A large swimming facility offering indoor pools and a variety of aquatic programs.',
    'Stanley Park': 'A 1,000-acre urban park offering scenic views, nature trails, and landmarks like the Seawall and Vancouver Aquarium.',
    'Engine 374 Pavilion': 'A railway museum showcasing the historic Engine 374, the first transcontinental train to arrive in Vancouver.',
    'English Bay Beach': 'A popular beach located near Stanley Park, ideal for swimming, sunbathing, and scenic views of the city.',
    'Inukshuk': 'A stone sculpture located at English Bay, symbolizing friendship and human connection, often associated with the Inuit people.',
    'Orpheum': 'A historic theater in downtown Vancouver, known for its stunning architecture and hosting live performances and concerts.',
    'Vancouver City Center': 'The central business district of Vancouver, featuring major shopping malls, offices, and entertainment venues.',
    'Northeastern University': 'A leading research university, with a campus offering innovative programs and a strong community presence in Vancouver.',
    'Roedde House Museum': 'A Victorian-era house museum that offers insight into the life of a prominent Vancouver family from the late 19th century.',
    'Yaletown Roundhouse': 'A historical landmark in the Yaletown district, originally a railway roundhouse, now a community center and cultural venue.',
    'David Lam Park': 'A beautiful park located in Yaletown, offering green space, walking paths, and views of False Creek.',
    'Robson Square': 'A public plaza and cultural hub in downtown Vancouver, often hosting events and festivals.',
    'Vancouver Lookout': 'An observation deck offering panoramic views of Vancouver, the surrounding mountains, and the Pacific Ocean.',
    'Sunset Beach': 'A tranquil beach located near downtown Vancouver, ideal for watching sunsets and enjoying scenic views of the city and ocean.',
    'Cathedral Square': 'A historic public square in the heart of Vancouver, often used for events and featuring beautiful cathedral architecture.',
    'Rogers Arena': 'A major indoor arena in downtown Vancouver, home to the Vancouver Canucks and hosting concerts and sports events.',
    'Devonian Harbour Park': 'A peaceful urban park located near Stanley Park, offering beautiful waterfront views and a relaxing environment.'
}

NODES_WITH_NAMES = [
    'BC Place',
    'Canada Place',
    'Cathedral Square',
    'David Lam Park',
    'Devonian Harbour Park',
    'Engine 374 Pavilion',
    'English Bay Beach',
    'Granville Island',
    'Inukshuk',
    'Northeastern University',
    'Orpheum',
    'Robson Square',
    'Rogers Arena',
    'Roedde House Museum',
    'Stanley Park',
    'Sunset Beach',
    'Vancouver Aquatic Center',
    'Vancouver Art Gallery',
    'Vancouver City Center',
    'Vancouver Lookout',
    'Yaletown Roundhouse',
    'Steam Clock',
]


nodes = {
    'BC Place': {'latitude': 49.277588, 'longitude': -123.114054},
    'Steam Clock': {'latitude': 49.284329, 'longitude': -123.108806},
    'Canada Place': {'latitude': 49.287669, 'longitude': -123.113786},
    'Vancouver Art Gallery': {'latitude': 49.283199, 'longitude': -123.121008},
    'Granville Island': {'latitude': 49.271489, 'longitude': -123.134705},
    'Vancouver Aquatic Center': {'latitude': 49.277041, 'longitude': -123.134893},
    'Stanley Park': {'latitude': 49.292158, 'longitude': -123.142980},
    'Engine 374 Pavilion': {'latitude': 49.273773, 'longitude': -123.121006},
    'English Bay Beach': {'latitude': 49.286350, 'longitude': -123.142491},
    'Inukshuk': {'latitude': 49.284452, 'longitude': -123.142764},
    'Orpheum': {'latitude': 49.279849, 'longitude': -123.120725},
    'Vancouver City Center': {'latitude': 49.282495, 'longitude': -123.118159},
    'Northeastern University': {'latitude': 49.280781, 'longitude': -123.115508},
    'Roedde House Museum': {'latitude': 49.286846, 'longitude': -123.131517},
    'Yaletown Roundhouse': {'latitude': 49.274556, 'longitude': -123.122175},
    'David Lam Park': {'latitude': 49.273039, 'longitude': -123.123053},
    'Robson Square': {'latitude': 49.281587, 'longitude': -123.121516},
    'Vancouver Lookout': {'latitude': 49.284458, 'longitude': -123.112576},
    'Sunset Beach': {'latitude': 49.282367, 'longitude': -123.140683},
    'Cathedral Square': {'latitude': 49.282661, 'longitude': -123.114030},
    'Rogers Arena': {'latitude': 49.278374, 'longitude': -123.108260},
    'Devonian Harbour Park': {'latitude': 49.293685, 'longitude': -123.135379},
    '1': {'latitude': 49.290365, 'longitude': -123.145649},
    '2': {'latitude': 49.292930, 'longitude': -123.141940},
    '3': {'latitude': 49.293395, 'longitude': -123.138445},
    '4': {'latitude': 49.294409, 'longitude': -123.136675},
    '5': {'latitude': 49.288594, 'longitude': -123.142877},
    '6': {'latitude': 49.290391, 'longitude': -123.140213},
    '7': {'latitude': 49.293515, 'longitude': -123.135198},
    '8': {'latitude': 49.289373, 'longitude': -123.138605},
    '9': {'latitude': 49.291481, 'longitude': -123.135437},
    '10': {'latitude': 49.292581, 'longitude': -123.133782},
    '11': {'latitude': 49.284805, 'longitude': -123.142297},
    '12': {'latitude': 49.283019, 'longitude': -123.139576},
    '13': {'latitude': 49.284078, 'longitude': -123.138064},
    '14': {'latitude': 49.286570, 'longitude': -123.134291},
    '15': {'latitude': 49.287255, 'longitude': -123.133209},
    '69': {'latitude': 49.286497, 'longitude': -123.132031},
    '16': {'latitude': 49.287899, 'longitude': -123.129962},
    '17': {'latitude': 49.290308, 'longitude': -123.130168},
    '18': {'latitude': 49.289591, 'longitude': -123.127430},
    '19': {'latitude': 49.289031, 'longitude': -123.128242},
    '20': {'latitude': 49.277588, 'longitude': -123.135439},
    '21': {'latitude': 49.278988, 'longitude': -123.133275},
    '22': {'latitude': 49.280028, 'longitude': -123.131700},
    '23': {'latitude': 49.282508, 'longitude': -123.127998},
    '24': {'latitude': 49.283583, 'longitude': -123.126430},
    '25': {'latitude': 49.284622, 'longitude': -123.124838},
    '26': {'latitude': 49.276394, 'longitude': -123.134149},
    '27': {'latitude': 49.282283, 'longitude': -123.124443},
    '28': {'latitude': 49.283313, 'longitude': -123.122808},
    '29': {'latitude': 49.284428, 'longitude': -123.121137},
    '30': {'latitude': 49.286590, 'longitude': -123.117802},
    '31': {'latitude': 49.287147, 'longitude': -123.117030},
    '32': {'latitude': 49.288120, 'longitude': -123.115474},
    '33': {'latitude': 49.286562, 'longitude': -123.115862},
    '34': {'latitude': 49.283779, 'longitude': -123.120110},
    '35': {'latitude': 49.282960, 'longitude': -123.122285},
    '36': {'latitude': 49.282666, 'longitude': -123.121826},
    '37': {'latitude': 49.281866, 'longitude': -123.123869},
    '38': {'latitude': 49.282043, 'longitude': -123.120807},
    '39': {'latitude': 49.280930, 'longitude': -123.122459},
    '40': {'latitude': 49.274721, 'longitude': -123.131815},
    '41': {'latitude': 49.274123, 'longitude': -123.130845},
    '42': {'latitude': 49.274549, 'longitude': -123.128717},
    '43': {'latitude': 49.273100, 'longitude': -123.125894},
    '44': {'latitude': 49.273405, 'longitude': -123.123654},
    '45': {'latitude': 49.274025, 'longitude': -123.121399},
    '46': {'latitude': 49.276544, 'longitude': -123.115574},
    '47': {'latitude': 49.277734, 'longitude': -123.117448},
    '48': {'latitude': 49.279690, 'longitude': -123.120456},
    '49': {'latitude': 49.280736, 'longitude': -123.118859},
    '50': {'latitude': 49.279794, 'longitude': -123.117408},
    '51': {'latitude': 49.279487, 'longitude': -123.116919},
    '52': {'latitude': 49.280599, 'longitude': -123.115218},
    '53': {'latitude': 49.281240, 'longitude': -123.116195},
    '54': {'latitude': 49.282347, 'longitude': -123.114500},
    '55': {'latitude': 49.283080, 'longitude': -123.113395},
    '56': {'latitude': 49.284037, 'longitude': -123.111929},
    '57': {'latitude': 49.284693, 'longitude': -123.110915},
    '58': {'latitude': 49.283865, 'longitude': -123.106433},
    '59': {'latitude': 49.281067, 'longitude': -123.107570},
    '60': {'latitude': 49.278655, 'longitude': -123.107640},
    '61': {'latitude': 49.281266, 'longitude': -123.108486},
    '62': {'latitude': 49.281547, 'longitude': -123.109993},
    '63': {'latitude': 49.280471, 'longitude': -123.111581},
    '64': {'latitude': 49.279345, 'longitude': -123.113277},
    '65': {'latitude': 49.278719, 'longitude': -123.112267},
    '66': {'latitude': 49.277815, 'longitude': -123.110699},
    '67': {'latitude': 49.279848, 'longitude': -123.110615},
    '68': {'latitude': 49.278652, 'longitude': -123.108738},
    '70': {'latitude': 49.287388, 'longitude': -123.113041},
    '71': {'latitude': 49.286639, 'longitude': -123.113894},
    '72': {'latitude': 49.285945, 'longitude': -123.114895},
    '73': {'latitude': 49.281852, 'longitude': -123.117143},
    '74': {'latitude': 49.283142, 'longitude': -123.119146},
    '75': {'latitude': 49.278847, 'longitude': -123.115914},
    '76': {'latitude': 49.276509, 'longitude': -123.125228},
    '77': {'latitude': 49.277790, 'longitude': -123.127204},
    '78': {'latitude': 49.279088, 'longitude': -123.129211},
    '79': {'latitude': 49.275471, 'longitude': -123.126820},
    '80': {'latitude': 49.276753, 'longitude': -123.128803},
    '81': {'latitude': 49.278033, 'longitude': -123.130780},
    '82': {'latitude': 49.279342, 'longitude': -123.132801},
    '83': {'latitude': 49.280403, 'longitude': -123.131205},
    '84': {'latitude': 49.276115, 'longitude': -123.127768},
    '85': {'latitude': 49.277136, 'longitude': -123.126223},
    '86': {'latitude': 49.280311, 'longitude': -123.121439},
    '87': {'latitude': 49.281365, 'longitude': -123.119848},
}

edges = [
    ('26', '81', 881.93),
    ('21', '82', 56.89),
    ('82', '22', 129.25),
    ('82', '81', 238.24),
    ('81', '78', 185.76),
    ('78', '27', 564.25),
    ('78', '83', 235.54),
    ('78', '77', 236.55),
    ('81', '80', 233.04),
    ('40', '80', 356.74),
    ('80', '77', 188.52),
    ('77', '39', 560.71),
    ('77', '85', 116.02),
    ('79', '42', 218.11),
    ('79', '76', 187.81),
    ('79', '84', 112.37),
    ('79', '44', 373.52),
    ('80', '84', 121.37),
    ('80', '81', 233.04),
    ('80', '40', 356.74),
    ('83', '22', 59.54),
    ('83', '23', 378.62),
    ('33', '72', 113.8),
    ('84', '41', 362.7),
    ('84', '85', 182.54),
    ('85', '76', 116.94),
    ('85', '86', 565.5),
    ('86', 'Orpheum', 84.16),
    ('86', '87', 188.03),
    ('86', '39', 119.42),
    ('87', '38', 114.24),
    ('87', '49', 116.35),
    ('87', 'Vancouver City Center', 199.84),
    ('38', '74', 196.27),
    ('Stanley Park', '1', 315.97),
    ('Stanley Park', '2', 124.72),
    ('2', '3', 389.41),
    ('3', '4', 206.11),
    ('1', '5', 326.29),
    ('5', '6', 315.53),
    ('Stanley Park', '6', 325.68),
    ('6', '7', 588.72),
    ('6', '8', 189.09),
    ('8', '9', 374.61),
    ('9', '10', 195.67),
    ('English Bay Beach', '8', 469.26),
    ('Inukshuk', 'English Bay Beach', 119.24),
    ('Inukshuk', '11', 56.15),
    ('10', '17', 424.67),
    ('17', '18', 307.36),
    ('18', '19', 96.43),
    ('19', '16', 203.12),
    ('16', 'Roedde House Museum', 387.37),
    ('Roedde House Museum', '69', 60.92),
    ('69', '15', 138.77),
    ('15', '14', 127.23),
    ('14', '13', 445.76),
    ('13', '12', 179.92),
    ('12', 'Sunset Beach', 129.24),
    ('Sunset Beach', '20', 651.05),
    ('20', 'Vancouver Aquatic Center', 69.18),
    ('Vancouver Aquatic Center', '26', 91.54),
    ('20', '21', 255.07),
    ('23', '24', 186.07),
    ('24', '25', 187.83),
    ('24', '27', 234.49),
    ('27', '37', 68.63),
    ('27', '28', 192.15),
    ('28', '25', 239.18),
    ('28', '35', 61.95),
    ('28', '29', 197.65),
    ('29', '34', 120.74),
    ('29', '30', 393.16),
    ('30', '31', 92.21),
    ('31', '32', 182.72),
    ('31', '33', 134.57),
    ('33', '34', 501.39),
    ('34', '36', 202.31),
    ('34', 'Vancouver City Center', 230.4),
    ('36', '38', 119.39),
    ('36', '35', 54.04),
    ('Vancouver Art Gallery', '34', 105.82),
    ('Vancouver Art Gallery', '36', 96.49),
    ('35', '37', 188.14),
    ('37', '39', 166.68),
    ('39', 'Robson Square', 112.13),
    ('Robson Square', '38', 83.51),
    ('32', 'Canada Place', 189.57),
    ('14', '23', 741.55),
    ('English Bay Beach', '13', 510.95),
    ('English Bay Beach', '5', 142.92),
    ('11', '12', 321.25),
    ('Inukshuk', 'Sunset Beach', 263.67),
    ('8', '14', 508.73),
    ('9', '16', 646.14),
    ('17', '19', 227.65),
    ('12', '21', 741.78),
    ('13', '22', 748.77),
    ('14', '23', 741.55),
    ('Roedde House Museum', '24', 599.02),
    ('16', '25', 603.18),
    ('19', '29', 837.56),
    ('18', '30', 1085.32),
    ('7', '10', 167.27),
    ('Devonian Harbour Park', '7', 22.61),
    ('Devonian Harbour Park', '4', 150.58),
    ('40', '26', 278.56),
    ('40', '41', 113.75),
    ('41', 'Granville Island', 457.81),
    ('41', '42', 237.89),
    ('42', '43', 325.81),
    ('43', '44', 249.61),
    ('44', '45', 253.4),
    ('44', 'David Lam Park', 70.39),
    ('45', '46', 665.13),
    ('Engine 374 Pavilion', '45', 46.28),
    ('45', 'Yaletown Roundhouse', 92.06),
    ('Yaletown Roundhouse', '47', 559.61),
    ('46', '47', 220.42),
    ('46', 'BC Place', 180.41),
    ('47', '48', 354.73),
    ('48', 'Orpheum', 31.41),
    ('48', '49', 188.49),
    ('49', '73', 202.37),
    ('49', '50', 171.09),
    ('50', 'Northeastern University', 219.48),
    ('50', '51', 57.45),
    ('51', '52', 200.72),
    ('BC Place', '65', 210.12),
    ('52', 'Northeastern University', 34.07),
    ('52', '64', 228.73),
    ('Northeastern University', '53', 81.27),
    ('53', '73', 111.71),
    ('53', '54', 199.99),
    ('54', '63', 343.79),
    ('54', 'Cathedral Square', 55.6),
    ('Cathedral Square', '55', 75.01),
    ('55', '56', 172.96),
    ('55', '62', 389.33),
    ('56', '57', 119.51),
    ('56', 'Vancouver Lookout', 76.31),
    ('Vancouver Lookout', '73', 531.6),
    ('Vancouver Lookout', '72', 273.05),
    ('57', '71', 351.49),
    ('57', 'Steam Clock', 235.4),
    ('Steam Clock', '58', 265.2),
    ('Steam Clock', '62', 214.28),
    ('58', '59', 211.68),
    ('59', '60', 146.61),
    ('59', '61', 102.5),
    ('60', '68', 122.02),
    ('Rogers Arena', '68', 55.73),
    ('61', '62', 168.33),
    ('61', '67', 251.76),
    ('62', '63', 188.17),
    ('63', '64', 200.48),
    ('63', '67', 113.81),
    ('64', '65', 118.5),
    ('65', '66', 182.68),
    ('65', '67', 195.95),
    ('66', '68', 223.76),
    ('67', '68', 220.86),
    ('70', 'Canada Place', 84.53),
    ('70', '71', 105.13),
    ('71', '72', 118.95),
    ('72', '74', 502.11),
    ('73', 'Vancouver City Center', 119.46),
    ('74', 'Vancouver City Center', 116.5),
    ('74', '34', 113.89),
    ('75', '51', 118.25),
    ('75', 'BC Place', 220.37),
    ('75', '47', 183.37),
    ('76', 'Yaletown Roundhouse', 359.4)
]


# Create the graph, add nodes and edges
graph = {node: [] for node in nodes}
for edge in edges:
    node1, node2, weight = edge
    graph[node1].append((node2, weight))
    graph[node2].append((node1, weight))

# Latitude and longitude to pixel coordinates conversion
canvas_width = 900
canvas_height = 850

min_latitude = 49.25
max_latitude = 49.35
min_longitude = -123.20
max_longitude = -123.05


def lat_lon_to_pixels(lat, lon):
    '''
    Converts latitude and longitude to pixel coordinates on the canvas.
    '''
    x = (lon - min_longitude) / (max_longitude - min_longitude) * canvas_width
    y = (max_latitude - lat) / (max_latitude - min_latitude) * canvas_height
    return x, y

# PART 2. SHORTEST PATH


def shortest_path(graph, start, end):
    '''
    Finds the shortest path between two nodes in a graph using Dijkstra's algorithm.

    Parameters:
        graph (dict): The graph represented as an adjacency list (dictionary of nodes and edges).
        start (str): The starting node.
        end (str): The ending node.

    Returns:
        tuple: The shortest distance and the list of nodes in the shortest path.
    '''
    # Initialization:

    # Priority queue: stores tuples (current_distance, current_node)
    # It's used to point out the node with the smallest distance
    pq = [(0, start)]
    # Initialize a shortest distance table (0 for start node, inf for others)
    # This step is because at the start, all nodes are initialized as "infinitely far away."
    # It can be float('inf') or any large number that is larger than the longest path in the graph
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Predecessor table for reconstructing the path
    # It stores the previous node of the current node
    predecessors = {node: None for node in graph}

    # pop until the priority queue is empty
    while pq:
        # we use Bubble Sort in this case to make sure the node with the smallest distance is at the front
        for i in range(len(pq)):  # get each node in pq
            for j in range(i + 1, len(pq)):  # compare it with the rest of the nodes
                if pq[i][0] > pq[j][0]:  # if larger
                    pq[i], pq[j] = pq[j], pq[i]  # Swap

        # Pop the element with the smallest distance and get its distance and node
        current_distance, current_node = pq.pop(0)

        # edge case handling: If the distance is greater than the recorded shortest distance, skip
        if current_distance > distances[current_node]:
            continue  # continue to the next node and bubble sort again

        # if the distance is smaller, update the distance and predecessor of the neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Update distance
                predecessors[neighbor] = current_node
                # Add updated distance & node to the queue
                pq.append((distance, neighbor))

    # retrieve the nodes in the shortest path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()

    return distances[end], path

# PART 3. PLOT


def draw_node(node_id, latitude, longitude, canvas):
    '''
    Draws nodes onto canvas.

    Parameters:
        node_id (str): The name of the node.
        latitude (float): The latitude of the node.
        longitude (float): The longitude of the node.
        canvas (tk.Canvas): The canvas on which the node will be drawn.
    '''
    x, y = lat_lon_to_pixels(latitude, longitude)

    if node_id == 'Northeastern University':
        radius = 4
        canvas.create_oval(x-8, y-8, x+8, y+8,
                           fill="red", outline="")
        canvas.create_text(x, y, text=node_id, font=("Arial", 9))

    elif node_id in NODES_WITH_NAMES:
        radius = 3
        canvas.create_oval(x-8, y-8, x+8, y+8,
                           fill="blue", outline="")
        canvas.create_text(x, y, text=node_id, font=("Arial", 9))

    else:
        radius = 1
        canvas.create_oval(x-3, y-3, x+3, y+3, fill="yellow", outline="")
        canvas.create_text(x, y, text=node_id, font=("Arial", 6))


def draw_edge(node1, node2, canvas):
    '''
    Draws an edge between two nodes on the canvas.

    Parameters:
        node1 (str): The first node.
        node2 (str): The second node.
        canvas (tk.Canvas): The canvas on which the edge will be drawn.
    '''
    lat1, lon1 = nodes[node1]['latitude'], nodes[node1]['longitude']
    lat2, lon2 = nodes[node2]['latitude'], nodes[node2]['longitude']

    x1, y1 = lat_lon_to_pixels(lat1, lon1)
    x2, y2 = lat_lon_to_pixels(lat2, lon2)

    canvas.create_line(x1, y1, x2, y2, fill="black")


def draw_shortest_path(shortest_path_edges, canvas):
    '''
    Draws the shortest path on the canvas in red color.

    Parameters:
        shortest_path_edges (list): List of edges in the shortest path.
        canvas (tk.Canvas): The canvas on which the path will be drawn.
    '''
    for node1, node2 in shortest_path_edges:
        lat1, lon1 = nodes[node1]['latitude'], nodes[node1]['longitude']
        lat2, lon2 = nodes[node2]['latitude'], nodes[node2]['longitude']

        x1, y1 = lat_lon_to_pixels(lat1, lon1)
        x2, y2 = lat_lon_to_pixels(lat2, lon2)

        canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

# PART 4. INTERFACE


class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Visualization with Latitude and Longitude")

        # Create the Canvas widget
        self.canvas = tk.Canvas(
            self.root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack()

        # Bind mouse wheel event for zoom
        self.canvas.bind("<MouseWheel>", self.on_zoom)

        # Bind arrow keys for moving the canvas
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)

        # Dropdown menus for selecting start and end nodes from nodes_with_names list
        self.start_node_var = tk.StringVar(self.root)
        self.start_node_var.set(NODES_WITH_NAMES[9])

        self.end_node_var = tk.StringVar(self.root)
        self.end_node_var.set(NODES_WITH_NAMES[1])

        # Update dropdown menus to show only nodes in nodes_with_names
        self.start_menu = tk.OptionMenu(
            self.root, self.start_node_var, *NODES_WITH_NAMES)
        self.start_menu.pack()

        self.end_menu = tk.OptionMenu(
            self.root, self.end_node_var, *NODES_WITH_NAMES)
        self.end_menu.pack()

        # A calculate button for calculation
        self.calc_button = tk.Button(
            self.root, text="Calculate Shortest Path", command=self.calculate_shortest_path)
        self.calc_button.pack(pady=10)

        # A label for introduction
        self.description_label = tk.Label(
            self.root, text="", wraplength=canvas_width - 20)
        self.description_label.pack(pady=10)

        # Draw all nodes and edges on the canvas initially
        self.draw_all()

    def draw_all(self):
        '''Draw all nodes and edges on the canvas.'''
        for node_id, coords in nodes.items():
            latitude = coords['latitude']
            longitude = coords['longitude']
            draw_node(node_id, latitude, longitude, self.canvas)

        for node1, node2, weight in edges:
            draw_edge(node1, node2, self.canvas)

    def calculate_shortest_path(self):
        '''Calculate the shortest path based on user input and update the canvas with the shortest path.'''
        start = self.start_node_var.get()
        end = self.end_node_var.get()
        distance, shortest_path_nodes = shortest_path(graph, start, end)
        shortest_path_edges = list(
            zip(shortest_path_nodes[:-1], shortest_path_nodes[1:]))

        # Clear and redraw everything
        self.canvas.delete("all")
        self.draw_all()

        # Draw the shortest path on the canvas
        draw_shortest_path(shortest_path_edges, self.canvas)

        # Display the landmark description in the label
        description = NODES_INTRODUCTION.get(end, "No description available.")
        self.description_label.config(
            text=f"Description of {end}: {description}")

        # Show a message box with the shortest path, distance, and estimated walking time
        path_str = " -> ".join(shortest_path_nodes)
        estimated_time_seconds = distance  # Assume 1 second per meter
        estimated_time_minutes = estimated_time_seconds / 60  # Convert to minutes
        estimated_time = f"Estimated walking time: {
            estimated_time_minutes:.2f} minutes"

        messagebox.showinfo(
            "Shortest Path",
            f"Shortest distance: {distance:.2f} meters\n\n{
                estimated_time}\n\nPath: {path_str}"
        )

    def on_zoom(self, event):
        '''Zoom in or out when mouse wheel is used'''
        scale_factor = 0.9 if event.delta > 0 else 1.1
        self.zoom(scale_factor)

    def zoom(self, scale_factor):
        '''Adjust canvas scale based on zoom factor'''
        global canvas_width, canvas_height, min_latitude, max_latitude, min_longitude, max_longitude

        # Calculate new latitude and longitude ranges
        lat_diff = max_latitude - min_latitude
        lon_diff = max_longitude - min_longitude

        # Apply scaling to the ranges
        new_lat_diff = lat_diff * scale_factor
        new_lon_diff = lon_diff * scale_factor

        # Update boundaries
        min_latitude += (lat_diff - new_lat_diff) / 2
        max_latitude -= (lat_diff - new_lat_diff) / 2
        min_longitude += (lon_diff - new_lon_diff) / 2
        max_longitude -= (lon_diff - new_lon_diff) / 2

        # Redraw canvas with updated view
        self.canvas.delete("all")
        self.draw_all()

    def move_left(self, event):
        '''Move canvas to the left'''
        self.shift_view(0, -0.01)

    def move_right(self, event):
        '''Move canvas to the right'''
        self.shift_view(0, 0.01)

    def move_up(self, event):
        '''Move canvas up'''
        self.shift_view(0.01, 0)

    def move_down(self, event):
        '''Move canvas down'''
        self.shift_view(-0.01, 0)

    def shift_view(self, delta_lat, delta_lon):
        '''Shift canvas view by changing latitude and longitude range'''
        global min_latitude, max_latitude, min_longitude, max_longitude

        min_latitude += delta_lat
        max_latitude += delta_lat
        min_longitude += delta_lon
        max_longitude += delta_lon

        # Redraw canvas with new view
        self.canvas.delete("all")
        self.draw_all()


# Main function to run the app


def main():
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()


# Run the main function
if __name__ == "__main__":
    main()
