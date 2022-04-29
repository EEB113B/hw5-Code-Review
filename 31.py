from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    l1tail = l1.head.pre #(找出l1尾端)
    l2tail = l2.head.pre #(找出l2尾端)
    l1tail.next = l2.head #l1尾端的下一項是l2的頭(將l1與l2正向連接)
    l2tail.next = l1.head #l2尾端的下一項是l1的頭(形成l1+l2正向循環)
    l2.head.pre = l1tail  #l2頭的前一項是l1尾端(將l1與l2反向連接)
    l1.head.pre = l2tail  #l1頭的前一項是l2尾端(形成l1+l2反向循環)




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
