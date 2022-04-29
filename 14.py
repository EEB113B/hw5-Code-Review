from pickle import TRUE
from xml.etree.ElementTree import TreeBuilder
from linked_list import Node, DoubleLinkedList


def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    # 0 1 2 3 # 10 11 12 13 
    tmp2 = l2.head
    tmp1 = l1.head
    while True:
        l1.insert(tmp1.pre.data, tmp2.data)
        tmp2 = tmp2.next
        if tmp2.data == l2.head.data:
            break
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

    LL1 = DoubleLinkedList()
    LL1.insertHead('元')
    LL1.insert('元', '智')

    # 建立 LL2 環狀雙向鏈結串列
    LL2 = DoubleLinkedList()
    LL2.insertHead('幼')
    LL2.insert('幼', '兒')
    LL2.insert('兒','園')


    # 使用 combine 函式合成2個環狀雙向鏈結串列，並改變 LL1 物件本身
    combine(LL1, LL2)
    LL1.printForward()  # 順向印出(next)
    LL1.printBackward() # 反向印出(pre)

    # Forward : 0 1 2 3 10 11 12 13
    # Backward : 13 12 11 10 3 2 1 0
