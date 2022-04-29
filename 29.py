from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    l1.last = l1.head.next                     #l1的串列
    l2.last = l2.head.next  

    while l1.last.next != l1.head:             #當l1串列的最後 的下一個節點 不等於串列的頭時 繼續往下找
        l1.last = l1.last.next
    l1.last.next = l2.head                     #當l1串列的最後 的下一個節點 等於串列的頭時 它的下一個就跟l2的頭'連接'
                      
    while l2.last.next != l2.head:             #當l2串列的最後 的下一個節點 不等於串列的頭時 繼續往下找
        l2.last = l2.last.next
    l2.last.next = l1.head                     #當l2串列的最後 的下一個節點 等於串列的頭時 它的下一個就跟l1的頭連接
    l2.head.pre = None                         #設l2的頭的前一個節點為none
    l2.head.pre = l1.last                      #l2的頭的前一個節點跟l1的最後'連接'
       
    if l1.head.pre == l1.last:                 #backward
        l1.head.pre = l2.last                  #將l1頭 的前一個節點和l2的後面'連接'


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

    # 使用 combine 函式合成2 個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward() # 順向印出(next)
    LL1.printBackward() # 反向印出(pre)