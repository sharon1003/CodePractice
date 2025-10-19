# Review

### Description
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

---

### 解題思路
用Bitwise去進行思考
Tips: Brian kernighan's Algorithm
> 只有 2 的次方，才可以滿足 n & (n-1) == 0

---

```bash
n = 8 		(1000)
n-1 = 7 	(0111)
n & (n-1) =  0000
```

### 複習Bitwise
| a         | b     |  a & b (類似乘法) | a \| b (類似加法) | a ^ b (位元互斥)| 
|-----------|-------|--------|--------|-------|
| 0         |   0   |    0   |    0   |   0   | 
| 0         |   1   |    0   |    1   |   1   | 
| 1         |   0   |    0   |    1   |   1   | 
| 1         |   1   |    1   |    1   |   0   | 

---

| 運算子	| 中文名稱	  |  結果（二進位 | 結果（十進位) |說明
|-------| ------------|-------------|-------------|-----
| ^	XOR	| 位元互斥	  |  0110		| 6	      	  | 只有一邊是 1（不相等）時結果為 1
| ~	NOT	| 位元反相	  |  1010		| -6		  | （在 Python 為補數）	把 1 → 0、0 → 1
| <<	| Left Shift  |  10100		| 20		  | 往左移一位，相當於 ×2
| >>	| Right Shift |	 0010		| 2			  | 往右移一位，相當於 ÷2

---

### 解題紀錄
| Date         | time  |
|--------------|-------|
| 2025/10/19   | td    | 
