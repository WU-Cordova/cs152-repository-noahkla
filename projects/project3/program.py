from datastructures.circularqueue import CircularQueue


def main():
    print('hello world')
    q = CircularQueue(5)
    print("Hello, World!")
    q.enqueue(8)
    q.enque(78)
    print(q.dequeue())
    q.front()



if __name__ == '__main__':
    main()
