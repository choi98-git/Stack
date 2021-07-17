# 클래스와 함수 선언
class Node():
    def __init__ (self):
        self.data = None #노드의 데이터 값
        self.link = None # 앞의 노드를 가르킴

# 출력        
def printStack(top):
    current = top
    # 스택이 비었을 때
    if current == None:
        return
    print(current.data, end = ' ')

    # 앞노드가 있을 때
    while current.link != None:
        current = current.link
        print(" ")
        print(current.data, end = ' ')       
    print()

# 삽입
def push(top, new_data):
    
    newNode = Node()
    newNode.data = new_data 
    
    # 첫 번째 노드일 때
    if top == None:
        top = newNode # top이 새로운 노드를 가르
        return top
    
    newNode.link = top # 기존 top의 값을 새로운 노드가 가리킴
    top = newNode # top이 새로운 노드를 가르킴
    return top

# 삭제
def pop(top):
    # 스택이 비어있을 때
    if top == None:
        print("스택이 비어있습니다!!")
        return top

    delete_node = top # delete 노드 값으로 top을 가르킴
    top = top.link # top값이 삭제되기 때문에 top의 앞 노드가 top이 됨.
    
    print("%s를 삭제했습니다 \n" % delete_node.data)
    del(delete_node)
    return top
    
    
    
    
## 전역 변수 선언 부분 ##
top = None

## 메인 코드 부분 ##
if __name__ == "__main__" :
    
    while True:
        print("==================================================\n")
        print(" [0: 종료] [1: push] [2: pop] [3: 출력] \n")
        print("==================================================\n")
        menu = int(input("메뉴 입력: "))

        # 종료
        if menu == 0:
            quit()
            
        # push(삽입)
        elif menu == 1:
            add_data = (input('입력할 자료: '))

            top = push(top,add_data)
            printStack(top)
            
        # pop(삭제)
        elif menu == 2:
            top = pop(top)
            printStack(top)       

        # 출력
        elif menu == 3:
            printStack(top)

        # 오류
        else:
            print("[Error]다시 입력!!")
            

