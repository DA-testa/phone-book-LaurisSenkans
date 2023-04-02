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
    result = []
    phone_book = {}
    for query in queries:
        q = query.split()
        if q[0] == 'add':
            phone_book[q[1]] = q[2]
        elif q[0] == 'del':
            if q[1] in phone_book:
                del phone_book[q[1]]
        else:
            result.append(phone_book.get(q[1], 'not found'))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))