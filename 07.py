from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    l1_head = l1.head      #將l1的head命名
    l1_end = l1_head.pre   #將l1鏈結串列中的最後一個data命名
    l2_head = l2.head      #將l2的head命名
    l2_end = l2_head.pre   #將l2鏈結串列中的最後一個data命名
    
    #------------l1尾巴連接l2的head------------
    l2_head.pre = l1_end   #連接l2的開頭與l1的結尾(逆向)
    l1_end.next = l2_head  #連接l2的開頭與l1的結尾(順向)
    
    #------------l2尾巴連接l1的head------------    
    l1_head.pre = l2_end   #連接l2的開頭與l1的結尾(逆向)
    l2_end.next = l1_head  #連接l2的開頭與l1的結尾(順向)
    
    

  




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
