from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    tmp_1 = l1.head #將兩組鏈結串列的頭用變數tmp_1、tmp_2取代
    tmp_2 = l2.head
    while True: #用迴圈的方式找出該串列之末項(首項的前一個)
        if tmp_1.next == l1.head:
            break
        tmp_1 = tmp_1.next 
    tmp_2.pre = tmp_1 #將第二個串列首項的前一個鏈結欄位指向第一個串列末項的節點
    tmp_1.next = tmp_2 #將第一個串列末項的後一個鏈結欄位指向第二個串列首項的節點
    while True:
        if tmp_2.next == l2.head: #用迴圈的方式找出該串列之末項(首項的前一個)
            break
        tmp_2 = tmp_2.next
    tmp_2.next = l1.head #將第二個串列末項的後一個鏈結欄位指向第一個串列首項的節點
    l1.head.pre = tmp_2 #將第一個串列首項的前一個鏈結欄位指向第二個串列末項的節點





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
