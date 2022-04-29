from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    #建立新的變數來存節點欄位(簡化程式版面)
    l1_tmp = l1.head   #l1的值
    l1_back = l1.head.pre#l1的後端
    l2_tmp = l2.head   #l2的值
    l2_back = l2.head.pre#l2的後端
    
    l1_back.next = l2_tmp #把新的l1後端接到l2上
    
    l2_back.next = l1_tmp #把新的l2後端接到l1上

    l2.head.pre = l1_back     #把新的l2的頭的前一個節點設成原本l1的後端
    
    l1.head.pre = l2_back     #把新的l1的頭的前一個節點設成原本l2的後端
    


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
