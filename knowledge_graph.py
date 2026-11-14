# Knowledge graph for the academic prototype.
# Edge format: (source, relationship, destination)

NODES = [
    "Mathematics",
    "Software",
    "Hardware",
    "Probability",
    "Linear Algebra",
    "Discrete Mathematics",
    "Programming in C",
    "Data Structures",
    "Algorithms",
    "Machine Learning",
    "DBMS",
    "Operating Systems",
    "Computer Networks",
    "Digital Logic",
    "Computer Architecture",
]

EDGES = [
    # Prerequisite relationships (11)
    ("Programming in C", "prerequisite_of", "Data Structures"),
    ("Data Structures", "prerequisite_of", "Algorithms"),
    ("Algorithms", "prerequisite_of", "Machine Learning"),
    ("Probability", "prerequisite_of", "Machine Learning"),
    ("Linear Algebra", "prerequisite_of", "Machine Learning"),
    ("Discrete Mathematics", "prerequisite_of", "Algorithms"),
    ("Data Structures", "prerequisite_of", "DBMS"),
    ("Data Structures", "prerequisite_of", "Operating Systems"),
    ("Operating Systems", "prerequisite_of", "Computer Networks"),
    ("Digital Logic", "prerequisite_of", "Computer Architecture"),
    ("Data Structures", "prerequisite_of", "Computer Architecture"),

    # Domain membership relationships (12)
    ("Probability", "belongs_to", "Mathematics"),
    ("Linear Algebra", "belongs_to", "Mathematics"),
    ("Discrete Mathematics", "belongs_to", "Mathematics"),
    ("Programming in C", "belongs_to", "Software"),
    ("Data Structures", "belongs_to", "Software"),
    ("Algorithms", "belongs_to", "Software"),
    ("Machine Learning", "belongs_to", "Software"),
    ("DBMS", "belongs_to", "Software"),
    ("Operating Systems", "belongs_to", "Software"),
    ("Computer Networks", "belongs_to", "Software"),
    ("Digital Logic", "belongs_to", "Hardware"),
    ("Computer Architecture", "belongs_to", "Hardware"),
]

# Directed adjacency list, retaining relationship labels.
GRAPH = {node: [] for node in NODES}
for source, relation, destination in EDGES:
    GRAPH[source].append((relation, destination))

ALIASES = {
    "c programming": "Programming in C",
    "programming": "Programming in C",
    "c": "Programming in C",
    "ds": "Data Structures",
    "data structure": "Data Structures",
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "linear algebra": "Linear Algebra",
    "discrete maths": "Discrete Mathematics",
    "discrete math": "Discrete Mathematics",
    "os": "Operating Systems",
    "operating system": "Operating Systems",
    "computer network": "Computer Networks",
    "networks": "Computer Networks",
    "dbms": "DBMS",
    "digital logic": "Digital Logic",
    "computer architecture": "Computer Architecture",
    "probability": "Probability",
    "maths": "Mathematics",
    "math": "Mathematics",
    "software": "Software",
    "hardware": "Hardware",
}

# Supplementary educational content (Definitions, Roadmaps, Examples)
EDUCATIONAL_CONTENT = {
    "Mathematics": {
        "definition": "The foundational domain covering formal logic, discrete structures, linear spaces, and probability theory used in computing.",
        "roadmap": [
            "Start with Discrete Mathematics for logic, sets, and graph theory.",
            "Learn Linear Algebra for vectors, matrices, and transformations.",
            "Study Probability for statistical reasoning and uncertainty modeling."
        ],
        "examples": "Graph theory in network routing, matrices in computer graphics, and Bayes' theorem in spam filtering."
    },
    "Software": {
        "definition": "The domain encompassing programming, data organization, algorithms, system software, databases, networking, and AI.",
        "roadmap": [
            "Master procedural coding with Programming in C.",
            "Organize data efficiently using Data Structures and Algorithms.",
            "Specialize in systems (OS, DBMS, Networks) or intelligence (Machine Learning)."
        ],
        "examples": "Operating systems like Linux, relational databases like PostgreSQL, and ML recommendation engines."
    },
    "Hardware": {
        "definition": "The physical and logical layer of computing systems, from boolean gates to processor organization.",
        "roadmap": [
            "Begin with Digital Logic (gates, flip-flops, combinational/sequential circuits).",
            "Progress to Computer Architecture (ALU, CPU pipelining, memory hierarchy)."
        ],
        "examples": "Logic gates inside microchips, CPU instruction pipelines, and cache memory."
    },
    "Probability": {
        "definition": "The branch of mathematics that quantifies uncertainty and models random events and distributions.",
        "roadmap": [
            "Learn basic counting, permutations, combinations, and conditional probability.",
            "Understand random variables, expectation, and variance.",
            "Study common distributions (Binomial, Normal, Poisson) and Bayes' theorem."
        ],
        "examples": "Predicting weather outcomes, Naive Bayes spam classifiers, and A/B testing in web apps."
    },
    "Linear Algebra": {
        "definition": "The study of vectors, vector spaces, matrices, and linear transformations.",
        "roadmap": [
            "Master vector operations, dot products, and matrix multiplication.",
            "Learn determinants, matrix inversion, and solving systems of linear equations.",
            "Study eigenvalues, eigenvectors, and Singular Value Decomposition (SVD)."
        ],
        "examples": "Representing datasets as feature matrices in Machine Learning and 3D rotations in game engines."
    },
    "Discrete Mathematics": {
        "definition": "The study of countable, distinct mathematical structures including logic, sets, relations, combinatorics, and graphs.",
        "roadmap": [
            "Learn propositional and predicate logic along with proof techniques.",
            "Master sets, functions, and equivalence/partial-order relations.",
            "Study trees, graphs, traversals, and recurrence relations."
        ],
        "examples": "Representing this Q&A system as a directed graph and verifying circuit logic with boolean algebra."
    },
    "Programming in C": {
        "definition": "A foundational procedural programming language offering low-level memory control via pointers and structured syntax.",
        "roadmap": [
            "Learn variables, data types, operators, and control flow (loops, conditionals).",
            "Master functions, recursion, arrays, and strings.",
            "Understand pointers, dynamic memory allocation (malloc/free), and structs."
        ],
        "examples": "Writing embedded firmware, implementing linked lists from scratch, and building Linux kernel modules."
    },
    "Data Structures": {
        "definition": "Specialized formats for organizing, storing, and retrieving data efficiently in computer memory.",
        "roadmap": [
            "Start with linear structures: Arrays, Linked Lists, Stacks, and Queues.",
            "Learn hierarchical structures: Binary Trees, BSTs, AVL Trees, and Heaps.",
            "Master Hash Tables and Graph representations (adjacency lists and matrices)."
        ],
        "examples": "Using a Stack for browser back-button history, a Queue for print jobs, and a Graph for social networks."
    },
    "Algorithms": {
        "definition": "Step-by-step computational procedures designed to solve problems accurately and within optimal time and space.",
        "roadmap": [
            "Learn asymptotic complexity analysis (Big-O, Big-Theta, Big-Omega).",
            "Master searching and sorting algorithms (Binary Search, Merge Sort, Quick Sort).",
            "Study design paradigms: Divide & Conquer, Greedy, Dynamic Programming, and Graph algorithms (BFS/DFS, Dijkstra)."
        ],
        "examples": "Google Maps using shortest-path algorithms and e-commerce sites using binary search and sorting."
    },
    "Machine Learning": {
        "definition": "A field of AI where statistical models learn patterns from data to make predictions without explicit rule programming.",
        "roadmap": [
            "Build foundations in Linear Algebra, Probability, and Algorithms.",
            "Learn data preprocessing and supervised learning (Linear/Logistic Regression, Decision Trees).",
            "Explore unsupervised learning (K-Means, PCA), model evaluation, and neural networks."
        ],
        "examples": "UPI fraud detection, movie recommendations on streaming apps, and voice assistants."
    },
    "DBMS": {
        "definition": "Database Management Systems—software used to store, query, secure, and manage structured data reliably.",
        "roadmap": [
            "Understand Entity-Relationship (ER) modeling and the relational model.",
            "Master SQL queries (SELECT, JOIN, GROUP BY, subqueries).",
            "Learn normalization (1NF to BCNF), indexing (B+ Trees), and ACID transaction properties."
        ],
        "examples": "Banking systems maintaining account balances via ACID transactions and IRCTC managing train bookings."
    },
    "Operating Systems": {
        "definition": "System software that manages hardware resources (CPU, memory, storage) and provides services to user programs.",
        "roadmap": [
            "Understand processes, threads, and CPU scheduling algorithms.",
            "Learn process synchronization, mutexes, semaphores, and deadlock handling.",
            "Study memory management (paging, virtual memory) and file systems."
        ],
        "examples": "Running multiple apps simultaneously via time-sliced CPU scheduling and virtual memory paging."
    },
    "Computer Networks": {
        "definition": "Interconnected computing devices that exchange data using standardized communication protocols.",
        "roadmap": [
            "Learn the OSI and TCP/IP layered network models.",
            "Understand IP addressing, subnetting, and routing protocols.",
            "Study transport protocols (TCP vs UDP) and application protocols (HTTP, DNS)."
        ],
        "examples": "Loading a webpage via DNS resolution and HTTP over TCP/IP, or streaming video using UDP."
    },
    "Digital Logic": {
        "definition": "The foundation of hardware design using binary values (0 and 1) and Boolean logic gates to process signals.",
        "roadmap": [
            "Learn number systems (binary, octal, hexadecimal) and Boolean algebra.",
            "Design combinational circuits (adders, multiplexers, decoders) using K-maps.",
            "Build sequential circuits using latches, flip-flops, registers, and counters."
        ],
        "examples": "A half-adder circuit adding two binary bits and flip-flops storing single bits in registers."
    },
    "Computer Architecture": {
        "definition": "The structural design and functional organization of a computer system, including CPU, memory, and I/O.",
        "roadmap": [
            "Understand Instruction Set Architecture (ISA) and assembly language basics.",
            "Study ALU design, control units, and instruction pipelining.",
            "Learn memory hierarchy (registers, L1/L2 cache, RAM) and I/O interfacing."
        ],
        "examples": "ARM processors in smartphones executing pipelined instructions and CPU caches speeding up memory access."
    },
}


def get_domain_members(domain):
    """Return all nodes connected to a domain by belongs_to."""
    return [
        source for source, relation, destination in EDGES
        if relation == "belongs_to" and destination.lower() == domain.lower()
    ]


def get_topic_domains(topic):
    """Return domain(s) a topic belongs to."""
    return [
        destination for source, relation, destination in EDGES
        if relation == "belongs_to" and source.lower() == topic.lower()
    ]


def get_prerequisites(topic):
    """Return direct prerequisites of a topic."""
    return [
        source for source, relation, destination in EDGES
        if relation == "prerequisite_of" and destination.lower() == topic.lower()
    ]


def get_next_topics(topic):
    """Return topics that have this topic as a direct prerequisite."""
    return [
        destination for source, relation, destination in EDGES
        if relation == "prerequisite_of" and source.lower() == topic.lower()
    ]


def get_related_topics(topic):
    """Return all connected concepts from the graph (prerequisites, next topics, and sibling topics in the same domain)."""
    prereqs = get_prerequisites(topic)
    next_topics = get_next_topics(topic)
    domains = get_topic_domains(topic)

    same_domain = []
    for d in domains:
        for member in get_domain_members(d):
            if member != topic and member not in prereqs and member not in next_topics:
                same_domain.append(member)

    return {
        "prerequisites": prereqs,
        "next_topics": next_topics,
        "domains": domains,
        "same_domain": same_domain,
    }


def bfs_path(start, target):
    """Find one shortest directed prerequisite path using BFS."""
    if start not in GRAPH or target not in GRAPH:
        return None

    queue = [(start, [start])]
    visited = {start}

    while queue:
        current, path = queue.pop(0)
        if current == target:
            return path

        for relation, neighbor in GRAPH[current]:
            if relation == "prerequisite_of" and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None