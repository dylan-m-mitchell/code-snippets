# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeDuplicates(nums: list[int]) -> int:
    l, r = 0, 0
    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
        r += 1
    return l+1

def removeNthFromEnd( head, n: int):
    if not head.next:
        return None
    l, r = head, head
    count = 0
    while r.next:
        r = r.next
        count += 1
    
    for i in range(count-n):
        l = l.next
    
    if count+1 == n:
        return head.next
        
    l.next = l.next.next
    return head

def validPalindrome(s: str) -> bool:
    i = 0
    j = len(s)-1
    while i<j:
        if not s[i].isalpha() and not s[i].isnumeric():
            i += 1
        elif not s[j].isalpha() and not s[j].isnumeric():
            j -= 1
        else:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
    return True

# this is sort of two pointers but it is really a bucket sort problem
def sortColors(nums: list[int]) -> None:
    # given an array containing 0s, 1s, 2s, in random spots, sort the array in place
    l = 0
    bucket = [0,0,0]
    while l < len(nums):
        bucket[nums[l]] += 1
        l += 1
    
    i = 0
    k = 0
    while i < len(nums):
        for j in range(bucket[k]):
            nums[i] = k
            i += 1
        k += 1

if __name__ == "__main__":
    print(validPalindrome("racecar"))
    print(validPalindrome("a man, a plan, a canal: panama"))
    print('.,'.isalpha())
    
    ListNode
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    node = removeNthFromEnd(node1, 5)
    # node = node1
    while node:
        print(node.val)
        node = node.next
        
    rem_dup_check = [0,0,1,1,1,2,2,3,3,4]
    rem_chk_2 = [0,1,2,3,4]
    rem_chk_3 = [1,1,2]
    
    tests = [rem_dup_check, rem_chk_2, rem_chk_3]
    
    for test in tests:
        print(test)
        removeDuplicates(test)
        print(test)
    
    test = [2,0,2,1,1,0]
    print(test)
    sortColors(test)
    print(test)