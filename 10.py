from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    newl1 = l1.head               #設一個新的變數保存原本l1的值
    newl2 = l2.head               #設一個新的變數保存原本l2 的值
    lastl1 = l1.head.pre          #設一個變數=l1後面要加入的值
    lastl2 = l2.head.pre          #設一個變數=l2後面要加入的值

    l1.head.pre.next = newl2      #將l2接上newl1
    l2.head.pre.next = newl1      #將l1接上newl2
    l1.head.pre= lastl2           #l2後面要加入的值變成newl1
    l2.head.pre = lastl1          #l1後面要加入的值變成newl2



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
