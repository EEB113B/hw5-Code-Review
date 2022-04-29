from linked_list import Node, DoubleLinkedList

def combine(l1, l2):
    # <將你的程式碼寫在這邊>
    #1.易懂，較長
    tmp=l1.head                        #令tmp為l1的首節點
    while tmp.next!=l1.head:           #當tmp所在節點的下一個節點為l1的首節點，不繼續執行
        tmp=tmp.next                   #反之，繼續執行，tmp繼續走訪下一個節點

    cur=l2.head                        #令cur為l2的首節點
    while cur.next!=l2.head:           #當cur所在節點的下一個節點為l2的首節點，不繼續執行
        cur=cur.next                   #反之，繼續執行，cur繼續走訪下一個節點

    tmp.next.pre=cur                   #l1首節點指向l1尾巴的指標轉指向l2
    cur.next.pre=tmp                   #l2首節點指向l2尾巴的指標轉指向l1
    cur.next=tmp.next                  #cur原指向l2首節點的指標轉指向l1首節點
    tmp.next=l2.head                   #tmp原指向l1首節點的指標轉指向l2首節點

    #2.不易懂，較簡潔
    # tmp=l1.head                        #令tmp為l1的首節點
    # cur=l2.head                        #令cur為l2的首節點
    # cur.pre.next=tmp                   #l2尾巴原指向l2頭的指標，改指向l1頭
    # tmp.pre.next=cur                   #l1尾巴原指向l1頭的指標，改指向l2頭
    # stagging=cur.pre                   #將stagging指向l2尾巴
    # cur.pre=tmp.pre                    #l2原指向尾巴的指標，改指向l1尾巴
    # tmp.pre=stagging                   #l1原指向尾巴的指標，改指向stagging(也就是原本l2尾巴)


if __name__=="__main__":
# 建立 LL1 環狀雙向鏈結串列 
    LL1 = DoubleLinkedList() 
    LL1.insertHead("元") 
    LL1.insert("元", "智") # 此時 LL1 為 ["元","智"] 的環狀雙向鏈結串列 
    
    # 建立 LL2 環狀雙向鏈結串列 
    LL2 = DoubleLinkedList() 
    LL2.insertHead("幼") 
    LL2.insert("幼", "稚") 
    LL2.insert("稚", "園") # 此時 LL2 為 ["幼","稚","園"] 的環狀雙向鏈結串列 
    
    # 使用 combine 函式合成2 個環狀雙向鏈結串列，並改變 LL1 物件本身 
    combine(LL1, LL2) 
    LL1.printForward()  # 順向印出(next) 
    LL1.printBackward() # 反向印出(pre)
