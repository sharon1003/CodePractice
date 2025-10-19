# Review

### Description
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

---

### 解題思路
這題的重點應該就是要額外設置兩個`dummy`pointer，去記錄合併的list跟剩下的list。
有兩個list，我們會一次走兩個list，相互比較彼此的 `.val` ，並且利用我們的pointer去做紀錄，最後去看那一個list還有剩下的數字，就直接把tail指過去。

---

```python
while list1 and list2:
	if list1.val > list2.val:
		tail.next = list1
		list1 = list1.next
	else:
		tail.next = list2
		list2 = list2.next
	tail = tail.next

if list1:
	tail.next = list1
else:
	tail.next = list2 
```

### 解題紀錄
| Date         | time  |
|--------------|-------|
| 2025/10/19   | td    | 
