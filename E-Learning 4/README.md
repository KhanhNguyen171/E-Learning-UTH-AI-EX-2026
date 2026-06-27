Làm theo nhóm:

Cho game Wumpus với Map số 9.

Xây dựng cơ sở tri thức và bằng thuật toán Resolution hãy

1. Suy diễn vị trí của Wumpus.
2. Suy diễn từng bước đi để đến phòng có Vàng.

Cho bản đồ Wumpus World số 9:

```text
+-----+-----+-----+-----+
|  P  |     |     |     |
+-----+-----+-----+-----+
|     |  P  |  G  |     |
+-----+-----+-----+-----+
|     |     |  W  |     |
+-----+-----+-----+-----+
|     |     |     |  P  |
+-----+-----+-----+-----+
```

Câu 1: Suy diễn vị trí của Wumpus.
- Agent xuất phát từ vị trí (1, 1), và không cảm nhận được Stench.

$R_1: S_{1, 1} \Leftrightarrow (W_{1, 2} \vee W_{2, 1})$

$R_2: \neg S_{1, 1}$

Từ $R_1$ và $R_2$ ta có:
$$\neg (W_{1, 2} \vee W_{2, 1})$$
$$\Leftrightarrow \neg W_{1, 2} \wedge \neg W_{2, 1}$$

$R_3: \neg W_{1, 2}$

$R_4: \neg W_{2, 1}$

- Di chuyển đến vị trí (2, 1), không có Stench.

$R_5: S_{2, 1} \Leftrightarrow (W_{1, 1} \vee W_{2, 2} \vee W_{3, 1})$

$R_6: \neg S_{2, 1}$

Từ $R_5$ và $R_6$ ta có:
$$\neg (W_{1, 1} \vee W_{2, 2} \vee W_{3, 1})$$
$$\neg W_{1, 1} \wedge \neg W_{2, 2} \wedge \neg W_{3, 1}$$

$R_7: \neg W_{1, 1}$

$R_8: \neg W_{2, 2}$

$R_9: \neg W_{3, 1}$ 

- Di chuyển đến vị trí (3, 1), có Stench.

$R_{10}: S_{3, 1} \Leftrightarrow (W_{2, 1} \vee W_{3, 2} \vee W_{4, 1})$

$R_{11}: S_{3, 1}$

Từ $R_{10}$ và $R_{11}$ ta có:

$R_{12}: (W_{2, 1} \vee W_{3, 2} \vee W_{4, 1})$

- Di chuyển đến vị trí (2, 2), có Stench.

$R_{13}: S_{2, 2} \Leftrightarrow (W_{1, 2} \vee W_{2, 1} \vee W_{3, 2} \vee W_{2, 3})$

$R_{14}: S_{2, 2}$

Từ $R_{13}$ và $R_{14}$ ta có:

$R_{15}: (W_{1, 2} \vee W_{2, 1} \vee W_{3, 2} \vee W_{2, 3})$

- Di chuyển đến vị trí (1, 2), không có Stench.

$R_{16}: S_{1, 2} \Leftrightarrow (W_{1, 1}) \vee (W_{1, 3}) \vee (W_{2, 2})$

$R_{17}: \neg S_{1, 2}$

Từ $R_{16}$ và $R_{17}$ ta có:

$$\neg (W_{1, 1} \vee W_{1, 3} \vee W_{2, 2})$$

$$\neg W_{1, 1} \wedge \neg W_{1, 3} \wedge \neg W_{2, 2}$$

$R_{18}: \neg W_{1, 3}$

- Di chuyển đến vị trí (1, 3), không có Stench.

$R_{19}: S_{1, 3} \Leftrightarrow (W_{1, 4} \vee W_{2, 3} \vee W_{1, 2})$

$R_{20}: \neg S_{1, 3}$

Từ $R_{19}$ và $R_{20}$ ta có:

$$\neg (W_{1, 4} \vee W_{2, 3} \vee W_{1, 2})$$

$$\neg W_{1, 4} \wedge \neg W_{2, 3} \wedge \neg W_{1, 2}$$

$R_{21}: \neg W_{1, 4}$

$R_{22}: \neg W_{2, 3}$


Vậy $KB = R_{15} \wedge R_3 \wedge R_4 \wedge R_{22}$ 

$\alpha = \neg W_{3, 2}$

$KB \wedge \neg \alpha$:

$$(W_{1, 2} \vee W_{2, 1} \vee W_{3, 2} \vee W_{2, 3}) \wedge (\neg W_{1, 2}) \wedge (\neg W_{2, 1}) \wedge (\neg W_{2, 3}) \wedge (\neg W_{3, 2})$$


---

Câu 2: Suy diễn từng bước đi để đến phòng có Vàng.

- Ban đầu Agent Bắt đầu tại vị trí (1, 1). Agent cảm nhận được không có Breeze và không có Stench:

$R_1: \neg B_{1, 1}$

$R_2: \neg S_{1, 1}$

$R_3: B_{1, 1} \Leftrightarrow (P_{1,2} \vee P_{2, 1})$

$R_4: S_{1, 1} \Leftrightarrow (W_{1,2} \vee W_{2, 1})$

Từ $R_3$ áp dụng CNF ta có:

$$(\neg B_{1, 1} \vee P_{1, 2} \vee P_{2, 1}) \wedge (\neg P_{1, 2} \vee B_{1, 1}) \wedge (\neg P_{2, 1} \vee B_{1, 1})$$

$R_5: \neg B_{1, 1} \vee P_{1, 2} \vee P_{2, 1}$

$R_6: \neg P_{1, 2} \vee B_{1, 1}$

$R_7: \neg P_{2, 1} \vee B_{1, 1}$

Từ $R_4$ áp dụng CNF ta có:

$$(\neg S_{1, 1} \vee W_{1, 2} \vee W_{2, 1}) \wedge (\neg W_{1, 2} \vee S_{1, 1}) \wedge (\neg W_{2, 1} \vee S_{1, 1})$$

$R_8: \neg S_{1, 1} \vee W_{1, 2} \vee W_{2, 1}$

$R_9: \neg W_{1, 2} \vee S_{1, 1}$

$R_{10}: \neg W_{2, 1} \vee S_{1, 1}$

Áp dụng Resolution giữa $R_1$ và $R_6$ ta có:
$$(\neg P_{1, 2} \vee B_{1, 1}) \wedge (\neg B_{1, 1})$$

$R_{11}: \neg P_{1, 2}$

Áp dụng Resolution giữa $R_1$ và $R_7$ ta có:
$$(\neg P_{2, 1} \vee B_{1, 1}) \wedge (\neg B_{1, 1})$$

$R_{12}: \neg P_{2, 1}$

Từ $R_2$ và $R_9$ ta có:
$$(\neg W_{1, 2} \vee S_{1, 1}) \wedge (\neg S_{1, 1})$$

$R_{13}: \neg W_{1, 2}$

Áp dụng Resolution giữa $R_2$ và $R_{10}$ ta có:
$$(\neg W_{2, 1} \vee S_{1, 1}) \wedge (\neg S_{1, 1})$$

$R_{14}: \neg W_{2, 1}$

Do $\neg P_{1, 2} \wedge \neg W_{1, 2}$ và $\neg P_{2, 1} \wedge \neg W_{2, 1}$ nên:

$$Safe(1, 2), Safe(2, 1)$$

Vậy Agent có thể di chuyển đến 2 ô (1, 2) và (2, 1), giả sử Agent di chuyển đến ô (2, 1):

- Agent di chuyển đến ô (2, 1), Không có Breeze và không có Stench.

$R_{15}: \neg B_{2, 1}$

$R_{16}: \neg S_{2, 1}$

$R_{17}: B_{2, 1} \Leftrightarrow (P_{1, 1} \vee P_{2, 2} \vee P_{3, 1})$

Từ $R_{17}$ áp dụng CNF ta có:
$$(\neg B_{2, 1} \vee P_{1, 1} \vee P_{2, 2} \vee P_{3, 1}) \wedge (\neg P_{1, 1} \vee B_{2, 1}) \wedge (\neg P_{2, 2} \vee B_{2, 1}) \wedge (\neg P_{3, 1} \vee B_{2, 1})$$

$R_{18}: \neg P_{2, 2} \vee B_{2, 1}$

$R_{19}: \neg P_{3, 1} \vee B_{2, 1}$

Áp dụng Resolution giữa $R_{15}$ và $R_{18}$ ta có:

$$(\neg P_{2, 2} \vee B_{2, 1}) \wedge (\neg B_{2, 1})$$

$R_{20}: \neg P_{2, 2}$

Áp dụng Resolution giữa $R_{15}$ và $R_{19}$ ta có:

$$(\neg P_{3, 1} \vee B_{2, 1}) \wedge (\neg B_{2, 1})$$

$R_{21}: \neg P_{3, 1}$

$R_{22}: S_{2, 1} \Leftrightarrow (W_{1, 1} \vee W_{2, 2} \vee W_{3, 1})$

Từ $R_{22}$ áp dụng CNF ta có:
$$(\neg S_{2, 1} \vee W_{1, 1} \vee W_{2, 2} \vee W_{3, 1}) \wedge (\neg W_{1, 1} \vee S_{2, 1}) \wedge (\neg W_{2, 2} \vee S_{2, 1}) \wedge (\neg W_{3, 1} \vee S_{2, 1})$$

$R_{23}: \neg W_{2, 2} \vee S_{2, 1}$

$R_{24}: \neg W_{3, 1} \vee S_{2, 1}$

Áp dụng Resolution giữa $R_{16}$ và $R_{23}$ ta có:
$$(\neg W_{2, 2} \vee S_{2, 1}) \wedge (\neg S_{2, 1})$$

$R_{25}: \neg W_{2, 2}$

Áp dụng Resolution giữa $R_{16}$ và $R_{24}$ ta có:
$$(\neg W_{3, 1} \vee S_{2, 1}) \wedge (\neg S_{2, 1})$$

$R_{26}: \neg W_{3, 1}$

Từ $R_{20} \wedge R_{25}$ và $R_{21} \wedge R_{26}$ suy ra:
$$Safe(2, 2), Safe(3, 1)$$

- Agent di chuyển đến ô (2, 2), cảm nhận được có Breeze và có Stench.

$R_{27}: B_{2, 2}$

$R_{28}: S_{2, 2}$

$R_{29}: B_{2, 2} \Leftrightarrow (P_{1, 2} \vee P_{2, 1} \vee P_{3, 2} \vee P_{2, 3})$

Từ $R_{29}$ áp dụng CNF ta có:
$$(\neg B_{2, 2} \vee P_{1, 2} \vee P_{2, 1} \vee P_{3, 2} \vee P_{2, 3}) \wedge (\neg P_{1, 2} \vee B_{2, 2}) \wedge (\neg P_{2, 1} \vee B_{2, 2}) \wedge (\neg P_{3, 2} \vee B_{2, 2}) \wedge (\neg P_{2, 3} \vee B_{2, 2})$$

$$C_1 = \neg B_{2, 2} \vee P_{1, 2} \vee P_{2, 1} \vee P_{3, 2} \vee P_{2, 3}$$

Từ $C_1, R_{11}, R_{12}$ và $R_{27}$ áp dụng ReSolution ta có:
$$(\neg B_{2, 2} \vee P_{1, 2} \vee P_{2, 1} \vee P_{3, 2} \vee P_{2, 3}) \wedge  (\neg P_{1, 2}) \wedge  (\neg P_{2, 1}) \wedge  (B_{2, 2})$$

$R_{30}: P_{3, 2} \vee P_{2, 3}$

$R_{31}: S_{2, 2} \Leftrightarrow (W_{1, 2} \vee W_{2, 1} \vee W_{3, 2} \vee W_{2, 3})$

Từ $R_{31}$ áp dụng CNF ta có:

$$(\neg S_{2, 2} \vee W_{1, 2} \vee W_{2, 1} \vee W_{3, 2} \vee W_{2, 3}) \wedge (\neg W_{1, 2} \vee S_{2, 2}) \wedge (\neg W_{2, 1} \vee S_{2, 2}) \wedge (\neg W_{3, 2} \vee S_{2, 2}) \wedge (\neg W_{2, 3} \vee S_{2, 2})$$

$$C_2 = (\neg S_{2, 2} \vee W_{1, 2} \vee W_{2, 1} \vee W_{3, 2} \vee W_{2, 3})$$

Từ $C_2, R_{13}, R_{14}$ và $R_{28}$ áp dụng ReSolution ta có:

$(\neg S_{2, 2} \vee W_{1, 2} \vee W_{2, 1} \vee W_{3, 2} \vee W_{2, 3}) \wedge (\neg W_{1, 2}) \wedge (\neg W_{2, 1}) \wedge (S_{2, 2})$

$R_{32}: W_{3, 2} \vee W_{2, 3}$

Trong $R_{32}, R_{30}$ Agent biết: Có Pit trong (3, 2), (2, 3) và có Wumpus trong (3, 2), (2, 3)

- Agent di chuyển đến ô (1, 2), cảm nhận được không có Breeze và không có Stench.

$R_{33}: \neg B_{1, 2}$

$R_{34}: \neg S_{1, 2}$

$R_{35}: B_{1, 2} \Leftrightarrow (P_{1, 1} \vee P_{1, 3} \vee P_{2, 2})$

Từ $R_{35}$ áp dụng CNF ta có:
$$(\neg B_{1, 2} \vee P_{1, 1} \vee P_{1, 3} \vee P_{2, 2}) \wedge (\neg P_{1, 1} \vee B_{1, 2}) \wedge (\neg P_{1, 3} \vee B_{1, 2}) \wedge (\neg P_{2, 2} \vee B_{1, 2})$$

$R_{36}: (\neg P_{1, 3} \vee B_{1, 2})$

Áp dụng Resolution giữa $R_{33}$ và $R_{36}$ ta có:

$$(\neg P_{1, 3} \vee B_{1, 2}) \wedge (\neg B_{1, 2})$$

$R_{37}: \neg P_{1, 3}$

$R_{38}: S_{1, 2} \Leftrightarrow (W_{1, 1} \vee W_{1, 3} \vee W_{2, 2})$

Từ $R_{38}$ áp dụng CNF ta có:
$$(\neg S_{1, 2} \vee W_{1, 1} \vee W_{1, 3} \vee W_{2, 2}) \wedge (\neg W_{1, 1} \vee S_{1, 2}) \wedge (\neg W_{2, 2} \vee S_{1, 2}) \wedge (\neg W_{1, 3} \vee S_{1, 2})$$

$R_{39}: (\neg W_{1, 3} \vee S_{1, 2})$

Áp dụng Resolution giữa $R_{34}: \neg S_{1, 2}$ và $R_{39}$ ta có:

$$(\neg W_{1, 3} \vee S_{1, 2}) \wedge \neg S_{1, 2}$$

$R_{40}: \neg W_{1, 3}$

- Agent di chuyển đến ô (1, 3), cảm nhận được không có Stench và có Breeze.

$R_{41}: B_{1, 3}$

$R_{42}: \neg S_{1, 3}$

$R_{43}: B_{1, 3} \Leftrightarrow (P_{1, 2} \vee P_{1, 4} \vee P_{2, 3})$

Từ $R_{43}$ áp dụng CNF ta có:
$$(\neg B_{1, 3} \vee P_{1, 2} \vee P_{1, 4} \vee P_{2, 3}) \wedge (\neg P_{1, 2} \vee B_{1, 3}) \wedge (\neg P_{1, 4} \vee B_{1, 3}) \wedge (\neg P_{2, 3} \vee B_{1, 3})$$

$$C_3 = (\neg B_{1, 3} \vee P_{1, 2} \vee P_{1, 4} \vee P_{2, 3})$$

Ta có $R_{11}: \neg P_{1, 2}, R_{41}: B_{1, 3}$ Resolution với $C_3$:

$$(\neg B_{1, 3} \vee P_{1, 2} \vee P_{1, 4} \vee P_{2, 3}) \wedge (\neg P_{1, 2}) \wedge (B_{1, 3})$$

$R_{44}: P_{1, 4} \vee P_{2, 3}$

$R_{45}: S_{1, 3} \Leftrightarrow (W_{1, 2} \vee W_{1, 4} \vee W_{2, 3})$

Từ $R_{45}$ áp dụng CNF ta có:
$$(\neg S_{1, 3} \vee W_{1, 2} \vee W_{1, 4} \vee W_{2, 3}) \wedge (\neg W_{1, 2} \vee S_{1, 3}) \wedge (\neg W_{1, 4} \vee S_{1, 3}) \wedge (\neg W_{2, 3} \vee S_{1, 3})$$

$R_{46}: (\neg W_{1, 4} \vee S_{1, 3})$

$R_{47}: (\neg W_{2, 3} \vee S_{1, 3})$

Áp dúng Resolution giữa $R_{42}$ và $R_{46}$ ta có:
$$(\neg W_{1, 4} \vee S_{1, 3}) \wedge (\neg S_{1, 3})$$

$R_{48}: \neg W_{1, 4}$

Áp dụng Resolution giữa $R_{42}$ và $R_{47}$ ta có:
$$(\neg W_{2, 3} \vee S_{1, 3}) \wedge (\neg S_{1, 3})$$

$R_{49}: \neg W_{2, 3}$

Áp dụng Resolution giữa $R_{32}$ và $R_{49}$ ta có:
$$(W_{3, 2} \vee W_{2, 3}) \wedge (\neg W_{2, 3})$$

Suy ra: $R_{51}: W_{3, 2}$

Từ $R_{44}: P_{1, 4} \vee P_{2, 3}$ ta vẫn chưa chắc ở đâu là Pit vẫn không an toàn và ta biết Wumpus ở (3, 2) nên từ ô (1, 3) ta di chuyển đến ô (3, 1) để tìm kiếm tiếp.

- Agent ở ô (3, 1), cảm nhận được có Breeze và có Stench

$R_{52}: B_{3, 1}$

$R_{53}: S_{3, 1}$

$R_{54}: B_{3, 1} \Leftrightarrow (P_{2, 1} \vee P_{3, 2} \vee P_{4, 1})$

Từ $R_{54}$ áp dụng CNF ta có:

$$(\neg B_{3, 1} \vee P_{2, 1} \vee P_{3, 2} \vee P_{4, 1}) \wedge (\neg P_{2, 1} \vee B_{3, 1}) \wedge (\neg P_{3, 2} \vee B_{3, 1}) \wedge (\neg P_{4, 1} \vee B_{3, 1})$$

$$C_4 = (\neg B_{3, 1} \vee P_{2, 1} \vee P_{3, 2} \vee P_{4, 1})$$

Ta có $R_{12}: \neg P_{2, 1}$ và $R_{52}: B_{3, 1}$ Resolution với $C_4$ ta có:
$$(\neg B_{3, 1} \vee P_{2, 1} \vee P_{3, 2} \vee P_{4, 1}) \wedge (\neg P_{2, 1}) \wedge (B_{3, 1})$$

$R_{55}: P_{3, 2} \vee P_{4, 1}$

$R_{56}: S_{3, 1} \Leftrightarrow (W_{2, 1} \vee W_{3, 2} \vee W_{4, 1})$

Từ $R_{56}$ áp dụng CNF ta có:
$$(\neg S_{3, 1} \vee W_{2, 1} \vee W_{3, 2} \vee W_{4, 1}) \wedge (\neg W_{2, 1} \vee S_{3, 1}) \wedge (\neg W_{3, 2} \vee S_{3, 1}) \wedge (\neg W_{4, 1} \vee S_{3, 1})$$

$$C_5 = (\neg S_{3, 1} \vee W_{2, 1} \vee W_{3, 2} \vee W_{4, 1})$$

Ta có $R_{14}: \neg W_{2, 1}$ và $R_{53}: S_{3, 1}$ Resolution với $C_5$ ta có:
$$(\neg S_{3, 1} \vee W_{2, 1} \vee W_{3, 2} \vee W_{4, 1}) \wedge (\neg W_{2, 1}) \wedge (S_{3, 1})$$

$R_{57}: W_{3, 2} \vee W_{4, 1}$

Theo đề ta có $\neg W_{i, j} \vee \neg P_{i, j}$ tức là trong 1 ô chỉ có thể là Wumpus hoặc là Pit không thể cùng 1 lúc vừa là Wumpus vừa là Pit.

Áp dụng cho ô (3, 2) ta có:

$R_{58}: \neg W_{3, 2} \vee \neg P_{3, 2}$ 

Resolution giữa $R_{58}$ với $R_{51}: W_{3, 2}$ ta có:
$$(\neg W_{3, 2} \vee \neg P_{3, 2}) \wedge (W_{3, 2})$$

$R_{59}: \neg P_{3, 2}$

Ta có $R_{30}: P_{3, 2} \vee P_{2, 3}$ và $R_{59}$ áp dụng ReSolution:
$$(P_{3, 2} \vee P_{2, 3}) \wedge \neg P_{3, 2}$$

$R_{60}: P_{2, 3}$

- Agent biết Wumpus ở (3, 2) $W_{3, 2}$ và hiện tại đang ở ô (3, 1) nên thực hiện ShootUp. Wumpus chết:

$R_{61}: \neg W_{3, 2}$

Kết hợp $R_{61}$ với $R_{59}$ Suy ra: $Safe(3, 2)$

- Agent di chuyển đến ô (3, 2), cảm nhận được không có Breeze và có Stench.

$R_{62}: \neg B_{3, 2}$

$R_{63}: S_{3, 2}$

$R_{64}: B_{3, 2} \Leftrightarrow (P_{2, 2} \vee P_{3, 1} \vee P_{4, 2} \vee P_{3, 3})$

Từ $R_{64}$ áp dụng CNF ta có:
$$(\neg B_{3, 2} \vee P_{2, 2} \vee P_{3, 1} \vee P_{4, 2} \vee P_{3, 3}) \wedge (\neg P_{2, 2} \vee B_{3, 2}) \wedge (\neg P_{3, 1} \vee B_{3, 2}) \wedge (\neg P_{4, 2} \vee B_{3, 2}) \wedge (\neg P_{3, 3} \vee B_{3, 2})$$

$R_{65}: (\neg P_{3, 3} \vee B_{3, 2})$

Resolution giữa $R_{65}$ với $R_{62}$ ta có:
$$(\neg P_{3, 3} \vee B_{3, 2}) \wedge \neg B_{3, 2}$$

$R_{66}: \neg P_{3, 3}$

$R_{67}: S_{3, 2} \Leftrightarrow (W_{2, 2} \vee W_{3, 1} \vee W_{4, 2} \vee W_{3, 3})$

Từ $R_{67}$ áp dụng CNF ta có:
$$(\neg S_{3, 2} \vee W_{2, 2} \vee W_{3, 1} \vee W_{4, 2} \vee W_{3, 3}) \wedge (\neg W_{2, 2} \vee S_{3, 2}) \wedge (\neg W_{3, 1} \vee S_{3, 2}) \wedge (\neg W_{4, 2} \vee S_{3, 2}) \wedge (\neg W_{3, 3} \vee S_{3, 2})$$

Vì đã suy ra được $R_{51}: W_{3, 2}$, và trong map chỉ có 1 wumpus nên ta có:

$R_{68}: W_{3, 2} \rightarrow \neg W_{3, 3}$

Từ $R_{68}$ áp dụng CNF ta có:

$R_{69}: \neg W_{3, 2} \vee \neg W_{3, 3}$

Áp dụng Resolution giữa $R_{69}$ với $R_{51}$ ta có:

$$(\neg W_{3, 2} \vee \neg W_{3, 3}) \wedge W_{3, 2}$$

$R_{70}: \neg W_{3, 3}$

Từ $R_{66}: \neg P_{3, 3}$ và $R_{70}: \neg W_{3, 3}$, Suy ra $Safe(3, 3)$

- Agent đến ô (3, 3), cảm nhận được ánh sáng của vàng.

$R_{71}: Glitter_{3, 3}$

Suy ra: $Gold(3, 3)$ Agen thực hiện $Grab(3, 3)$.