class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    contacts = {}
    result = []
    for query in queries:
        if query.type == 'add':
            contacts[query.number] = query.name
        elif query.type == 'del':
            contacts.pop(query.number, None)
        elif query.type == 'find':
            name = contacts.get(query.number, 'not found')
            result.append(name)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))