# Wumpus World ở map 0

<img src="assets/wumpus.png">

- Giả sử Agent đang ở vị trí (3, 2).
    - cột 3 hàng 2.

Agent quyết định đi tiếp như thế nào để đảm bảo không chết và đi đến chiến thắng, chứng minh.

Vì Agent đang ở vị trí (3, 2) trong map 0. ta cảm nhận được _Breeze_ và không có _Stench_.

- Có _Breeze_: $B_{3, 2}$ 

suy ra:

$$P_{2,2} \vee P_{4, 2} \vee P_{3, 1} \vee P_{3, 3} \tag{1.1}$$

- Không có _Stench_: $\neg S_{3, 2}$ 

suy ra:
$$\neg W_{2, 2} \wedge \neg W_{4, 2} \wedge \neg W_{3, 1} \wedge \neg W_{3, 3} \tag{1.2}$$

Từ vị trí (3, 2) các ô lân cận có thể đi là:
- (2, 2)
- (4, 2)
- (3, 1)
- (3, 3)

Nhưng vì có _Breeze_ nên ít nhất một trong 4 ô là Pit. Nhưng ta chưa biết ô nào an toàn, nên ta sử dụng tri thức đã thu được trước đó.

Vì Agent Xuất phát từ (1, 1) Nên theo đề bài ta có ta có:
$$\neg W_{1, 1} \wedge \neg P_{1, 1}$$

1. Tại ô (1, 1) không có _Breeze_ và _Stench_: 

    - Nên $\neg B_{1, 1}, \neg S_{1, 1}$
    
    - suy ra:
$$\neg P_{1, 2} \wedge \neg P_{2, 1} \wedge \neg P_{1, 1} \tag{2.1}$$
$$\neg W_{1, 2} \wedge \neg W_{2, 1} \wedge \neg W_{1, 1} \tag{2.2}$$


2. Tại ô (2, 1) Có _Breeze_ và không có _Stench_: 

    - Nên $B_{2, 1}$ và $\neg S_{2, 1}$

    - suy ra: $P_{1, 1} \vee P_{3, 1} \vee P_{2, 2}$

    - mà $\neg P_{1, 1}$

    - nên 
$$P_{3, 1} \vee P_{2, 2} \tag{3.1}$$
$$\neg W_{3, 1} \wedge \neg W_{2, 2} \tag{3.2}$$

Tại ô (2, 1) ta chỉ có thể đi đến (3, 1) và (2, 2) nhưng từ (3.1) ta có dữ kiện là: $P_{3, 1} \vee P_{2, 2}$ chưa thể chứng minh là an toàn nên ta quay lui về ô (1, 1) để tiếp tục tìm kiếm lên ô (1, 2) vì từ (2.1) và (2.2) ta có $\neg P_{1, 2} \wedge \neg W_{1, 2}$.

3. Tại ô (1, 2) Có _Stench_ và không có _Breeze_.
    - nên $S_{1, 2}$ và $\neg B_{1, 2}$

    - Suy ra: 
$$W_{1, 1} \vee W_{1, 3} \vee W_{2, 2} \tag{4.1}$$
$$\neg P_{1, 1} \wedge \neg P_{1, 3} \wedge \neg P_{2, 2} \tag{4.2}$$

Từ (3.2) và (4. 2) ta có được dữ liệu là $\neg W_{2, 2}$ và $\neg P_{2, 2}$ nên ô (2, 2) an toàn. 

4. Tại ô (2, 2) Không có _Breeze_ và Không có _Stench_:

    - Nên $\neg B_{2, 2}$ và $\neg S_{2, 2}$
    - suy ra: 
$$\neg P_{1, 2} \wedge \neg P_{3, 2} \wedge \neg P_{2, 1} \wedge \neg P_{2, 3} \tag{5.1}$$
$$\neg W_{1, 2} \wedge \neg W_{3, 2} \wedge \neg W_{2, 1} \wedge \neg W_{2, 3} \tag{5.2}$$


Từ (1.1), tại ô (3, 2) Agent biết rằng:
$$P_{2,2} \vee P_{4, 2} \vee P_{3, 1} \vee P_{3, 3}$$

Tuy nhiên từ tri thức thu được trước đó từ các ô $(2, 1), (1, 2)$ và $(2, 2)$ Agent suy ra ô $(2, 2)$ là an toàn, trong khi các ô mới $(4, 2), (3, 1), (3, 3)$ chưa thể chứng minh là an toàn.

Vì vậy lựa chọn an toàn nhất là quay lui về ô (2, 2) để tiếp tục tìm kiếm.

5. Quay lui về ô (2, 2) và từ (5.1) và (5.2) ta có $\neg P_{2, 3} \wedge \neg W_{2, 3}$ Nên ô (2, 3) an toàn.

6. Tại ô (2, 3) Có _Glitter_, _Stench_, _Breeze_:
    - Nên $G_{2, 3}$, $B_{2, 3}$, $S_{2, 3}$

    - Vì đã phát hiện ra _Gold_ nên Agent thực hiện hành động _Grab_ để lấy gold.

sau khi lấy gold, Agent quay lại theo đường cũ $(2, 3) \rightarrow (2, 2) \rightarrow (2,1) \rightarrow (1, 1)$ và thoát khỏi hang.