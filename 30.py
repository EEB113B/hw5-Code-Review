from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    tmp = l1.head #l1首節點
    while(tmp.next != l1.head): #找出l1結尾
        tmp=tmp.next
    tmp.next = l2.head #指向l2首節點
    l2.head.pre =  tmp #l2前節點往回指向l1
    cur = l2.head #l2首節點
    while(cur.next != l2.head): #找出l2結尾
        cur=cur.next
    cur.next = l1.head #指向l1首節點
    l1.head.pre =  cur #l1前節點往回指向l2


 




if __name__=="__main__":
    # 建立 LL1 環狀雙向鏈結串列 
    LL1 = DoubleLinkedList() 
    LL1.insertHead(0) 
    LL1.insert(0, 1) 
    LL1.insert(1, 2) 
    LL1.insert(2, 3) # 此時 LL1 為 [0 1 2 3] 的環狀雙向鏈結串列 
 
    # 建立 LL2 環狀雙向鏈結串列 
    LL2 = DoubleLinkedList() 
    LL2.insertHead(10) 
    LL2.insert(10, 11) 
    LL2.insert(11, 12) 
    LL2.insert(12, 13) # 此時 LL2 為 [10 11 12 13] 的環狀雙向鏈結串列 
 
    # 使用 combine 函式合成 2 個環狀雙向鏈結串列，並改變 LL1 物件本身 
    combine(LL1, LL2)
    LL1.printForward()  # 順向印出(next) 
    LL1.printBackward() # 反向印出(pre)
