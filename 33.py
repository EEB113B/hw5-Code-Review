from linked_list import Node, DoubleLinkedList


def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    tmp_1_last = l1.head.pre    #設l1的最後一個數為tmp_1_last
    tmp_2_last = l2.head.pre    #設l2的最後一個數為tmp_2_last

    tmp_1_last.next = l2.head   #將l1最後一個數的next指到l2的第一個數
    l2.head.pre = tmp_1_last    #將l2第一個數的pre指到l1的最後一個數

    tmp_2_last.next = l1.head   #將l2最後一個數的next指到l1的第一個數
    l1.head.pre = tmp_2_last    #將l1第一個數的pre指到l2的最後一個數


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
    LL1.printForward() # 順向印出(next)
    LL1.printBackward() # 反向印出(pre

