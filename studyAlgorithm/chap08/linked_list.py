class Node:
    def __init__(self, key): # self는 해당 메소드를 호출하는 객체를 의미한다.
        self.key = key
        self.next = None
    
    def __str__(self):
        return str(self.key)

class Singlylinkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size   

    def __iterator__(self): # iterator == 반복자, yield가 존재하는 함수를 generator라고 한다.
        new_node = self.head # ex) for x in L: print(x) 와 같이 사용이 가능하게 하는 함수
        while new_node != None:
            yield new_node # yield == return 과 유사하다
            new_node = new_node.next
        # while문이 종료될 경우 StopIterator Error message 같은 오류를 내보내 for 문을 종료한다

    def push_front(self, key):
        new_node = Node(key) # 해당 메소드를 호출할 때 새로운 노드를 생성하고,
        new_node.next = self.head # 새로운 노드의 link에 기존 노드의 head를 연결하고
        self.head = new_node # 새로운 노드를 head에 붙였으니까 head의 위치를 새로운 노드로 옮기고
        self.size += 1 # 노드가 추가되었기 때문에 사이즈를 1 증가시킨다.
        
    def push_back(self, key):
        new_node = Node(key)
        if len(self) == 0: # 만약 빈 리스트일 경우에는 push_back을 해도 해당 노드가 head도 되기 때문에 head로 저장
            self.head = new_node
        else:
            tail = self.head # tail에 접근하기 위해서는 head값의 이동으로 tail.next가 None일 때 tail임을 확인할 수 있다.
            while tail.next != None: # tail의 다음이 없을 때 까지
                tail = tail.next # 포인터가 이동한다.
            tail.next = new_node # tail.next가 None일 떄(tail에 도달했을 때) new_node가 새로운 tail이 된다.
        self.size += 1 # 공통적으로 사이즈 1 증가
    
    def pop_front(self):
        if len(self) == 0:
            return
        else: # 하나 이상의 노드가 존재할 경우
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key

    def pop_back(self):
        if len(self) == 0:
            return
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1: # 만약 노드가 1개 있어서 head이자 tail일 경우
                self.head = None
            else:
                prev.next = tail.next # == prev.next = None
            key = tail.key
            del tail
            self.size -= 1
            return key
    
    def search(self, key):
        # key 값의 노드를 리턴, 없으면 None 리턴
        new_node = self.head
        while new_node != None:
            if new_node.key == key:
                return new_node
            new_node = new_node.next
        return None # or return new_node = (None)