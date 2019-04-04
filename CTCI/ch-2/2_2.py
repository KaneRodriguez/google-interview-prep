class Node:
  def __init__(self, val):
    self.next = None
    self.val = val

def kthToLast(head, k):
  if head is None:
    return head

  if k is 0:
    while head.next != None:
      head = head.next
    
    return head
    
  pT = pB = pF = head
  diff = 0
  
  while pF != None:
    pT = pF
    # print("forward pointer at  " + str(pF.val) )
    for i in range(k):
      pF = pF.next
      if pF is None:
        diff += i + 1
        break
      elif i == k - 1:
        diff += k
  
    if diff >= 2*k:
      pB = pT
      diff -= k
      # print("moving up back pointer to " + str(pB.val) )
  
  # print("diff " + str(diff))
  if diff < k:
    return head
  else:
    for i in range(diff - k):
      pB = pB.next
    
    return pB
    
current = head = Node(9)

for i in range(8, 0, -1):
  current.next = Node(i)
  current = current.next

for i in range(1, 8):
  current = head
  ans = kthToLast(current, i)

  if ans is not None:
    print("Answer: " + str(i) + " Result: " + str(ans.val))
