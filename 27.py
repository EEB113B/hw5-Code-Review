from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    tmp1 = l1.head               #指定儲存位置
    while tmp1.next != None:     #若有指向
        tmp1 = tmp1.next         #將儲存位置替代為下一個儲存格
        if tmp1.next == l1.head: #繞一圈後
            break                #離開迴圈
    tmp2 = l2.head
    while tmp2.next != None:
        tmp2 = tmp2.next
        if tmp2.next == l2.head:
            break
        
    tmp2.next = l1.head          #正向鏈接串列
    l2.head.pre = tmp1
    tmp1.next = l2.head          #反向鏈接串列
    l1.head.pre = tmp2



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
    
