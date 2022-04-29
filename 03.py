from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    l1_pre = l1.head.pre
    l2_pre = l2.head.pre
    l1.head.pre.next = l2.head #將新l1的尾巴接上l2的頭
    l2.head.pre.next = l1.head #將新l2尾巴接上l1的頭
    l1.head.pre = l2_pre #將新l1頭的前一個設為原l2的尾巴
    l2.head.pre = l1_pre #將新l2頭的前一個設為原l1的尾巴




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
