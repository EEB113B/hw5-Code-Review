from linked_list import Node, DoubleLinkedList

def combine(LL1, LL2):
    # <將你的程式碼寫在這邊>
    LL1_last = LL1.head.pre     #設定LL1_last為LL1的末項
    LL2_last = LL2.head.pre     #設定LL2_last為LL2的末項
    #第8行和第9行為外圈的鏈結(LL1首項接LL2末項)
    LL1.head.pre = LL2_last     #將LL1首項的前一項改為LL2的末項
    LL2_last.next = LL1.head    #將LL2末項的後一項改為LL1的首項
    #第11行和第12行為外圈的鏈結(LL1末項接LL2首項)
    LL1_last.next = LL2.head    #將LL1末項的後一項改為LL2的首項
    LL2.head.pre = LL1_last     #將LL2首項的前一項改為LL1的末項
    #完成內圈的鏈結

    #完成LL1與LL2的環狀雙向鏈結串列
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
