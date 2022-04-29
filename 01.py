from linked_list import Node, DoubleLinkedList

def combine(L1, L2):
    # <將你的程式碼寫在這邊>
    #把L1的前一項貼到L1_pre
    L1_pre = L1.head.pre
    #L1.head貼到L1_head(避免更改到初始值)
    L1_head = L1.head
    #把L2的前一項貼到L2_pre
    L2_pre = L2.head.pre
    #L2.head貼到L2_head(避免更改到初始值)
    L2_head = L2.head

    #L1_head指向L2尾端
    L1_head.pre = L2_pre
    #L1尾端指向L2_head
    L1_pre.next = L2_head
    #L2_head指向L1尾端
    L2_pre.next = L1_head
    #L2尾端指向L1_head
    L2_head.pre = L1_pre

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

    # 使用 combine 函式合成2個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward()  # 順向印出(next)
    LL1.printBackward() # 反向印出(pre)
    # Forward : 0 1 2 3 10 11 12 13
    # Backward : 13 12 11 10 3 2 1 0
