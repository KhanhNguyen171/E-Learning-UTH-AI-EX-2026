# Wumpus World ở map 0

<img src="assets/wumpus.png">

- Giả sử Agent đang ở vị trí (3, 2).
    - cột 3 hàng 2.

Agent quyết định đi tiếp như thế nào để đảm bảo không chết và đi đến chiến thắng, chứng minh.

Vì ban đầu Agent phải xuất phát từ vị trí (1, 1) và để đi đến được vị trí (3, 2) thì Agent phải có quá trình tiếp thu các Knowledge Base.

KB:

- Tại ô (1, 1) Agent cảm nhận được không có _Breeze_ và không có _Stench_

    - $R_1: \neg P_{1, 1}$
    - $R_2: \neg W_{1, 1}$

    Định nghĩa Breeze:
    - $R_3: B_{1, 1} \Leftrightarrow (P_{1, 2} \vee P_{2, 1})$

    Định nghĩa Stench
    - $R_4: S_{1, 1} \Leftrightarrow (W_{1, 2} \vee W_{2, 1})$

    - $R_5: \neg B_{1, 1}$
    - $R_6: \neg S_{1, 1}$

    áp dụng luật logic __Biconditional Elimination__ đối với $R_3$
    - $R_7: (P_{1, 2} \vee P_{2, 1}) \Rightarrow B_{1 ,1}$

    áp dụng luật logic __Contrapositive__ đối với $R_7$
    - $R_8: \neg B_{1, 1} \Rightarrow \neg (P_{1, 2} \vee P_{2, 1})$

    áp dụng luật logic __Modus Ponens__ giữa $R_8$ với $R_5$
    - $R_9: \neg (P_{1, 2} \vee P_{2, 1})$

    Áp dụng luật logic __De Morgan__ cho $R_9$
    - $R_{10}: \neg P_{1, 2} \wedge \neg P_{2, 1}$

    áp dụng luật logic __Biconditional Elimination__ đối với $R_4$
    - $R_{11}: (W_{1, 2} \vee W_{2, 1}) \Rightarrow S_{1 ,1}$

    áp dụng luật logic __Contrapositive__ đối với $R_{11}$
    - $R_{12}: \neg S_{1, 1} \Rightarrow \neg (W_{1, 2} \vee W_{2, 1})$

    áp dụng luật logic __Modus Ponens__ giữa $R_{12}$ với $R_6$
    - $R_{13}: \neg (W_{1, 2} \vee W_{2, 1})$

    Áp dụng luật logic __De Morgan__ cho $R_{13}$
    - $R_{14}: \neg W_{1, 2} \wedge \neg W_{2, 1}$

Từ $R_{10}$ và $R_{14}$:
$$Safe(1, 2) \equiv \neg P_{1, 2} \wedge \neg W_{1, 2}$$
$$Safe(2, 1) \equiv \neg P_{2, 1} \wedge \neg W_{2, 1}$$

Lúc này Agent Có thể đi đến 1 trong 2 ô (1, 2) hoặc (2, 1) Giả sử Agent quyết định đi đến ô (2, 1) ta có:

- Tại ô (2, 1) Agent cảm nhận được có _Breeze_ và không có _Stench_.

    Định nghĩa Breeze:
    - $R_{15}: B_{2, 1} \Leftrightarrow (P_{1, 1} \vee P_{2, 2} \vee P_{3, 1})$

    Định nghĩa Stench:
    - $R_{16}: S_{2, 1} \Leftrightarrow (W_{1, 1} \vee W_{2, 2} \vee W_{3, 1})$

    - $R_{17}: B_{2, 1}$
    - $R_{18}: \neg S_{2, 1}$

    Áp dụng luật __Biconditional Elimination__ đối với $R_{15}$
    - $R_{19}: B_{2, 1} \Rightarrow (P_{1, 1} \vee P_{2, 2} \vee P_{3, 1})$

    Áp dụng luật __Modus Ponens__ giữa $R_{19}$ với $R_{17}$
    - $R_{20}: P_{1, 1} \vee P_{2, 2} \vee P_{3, 1}$
    
    Áp dụng __Resolution__ giữa $R_{20}$ và $R_1$:
    - $R_{21}: P_{2, 2} \vee P_{3, 1}$ 

    Áp dụng luật __Biconditional Elimination__ đối với $R_{16}$
    - $R_{22}: (W_{1, 1} \vee W_{2, 2} \vee W_{3, 1}) \Rightarrow S_{2, 1}$

    áp dụng luật logic __Contrapositive__ đối với $R_{22}$
    - $R_{23}: \neg S_{2, 1} \Rightarrow \neg (W_{1, 1} \vee W_{2, 2} \vee W_{3, 1})$

    áp dụng luật logic __Modus Ponens__ giữa $R_{23}$ với $R_{18}$
    - $R_{24}: \neg (W_{1, 1} \vee W_{2, 2} \vee W_{3, 1})$

    Áp dụng luật logic __De Morgan__ cho $R_{24}$
    - $R_{25}: \neg W_{1, 1} \wedge \neg W_{2, 2} \wedge \neg W_{3, 1}$

Từ $R_{21}$ và $R_{25}$:
- ô (2, 2) và (3, 1) đều không chứa Wumpus
- tuy nhiên ít nhất 1 trong 2 ô chứa Pit

Do đó Agent không thể chứng minh được ô nào an toàn.

Vì trước đó đã biết ô (1, 2) là an toàn và chưa kiểm tra. Nên Agent quay lui về ô (1, 1) và tiếp tục khám phá ô (1, 2).

- Tại ô (1, 2), Agent cảm nhận được có _Stench_ và không có _Breeze_.

    Định nghĩa Breeze:
    - $R_{26}: B_{1, 2} \Leftrightarrow (P_{1, 1} \vee P_{2, 2} \vee P_{1, 3})$

    Định nghĩa Stench:
    - $R_{27}: S_{1, 2} \Leftrightarrow (W_{1, 1} \vee W_{2, 2} \vee W_{1, 3})$

    - $R_{28}: \neg B_{1, 2}$
    - $R_{29}: S_{1, 2}$

    Áp dụng luật __Biconditional Elimination__ đối với $R_{26}$
    - $R_{30}: (P_{1, 1} \vee P_{2, 2} \vee P_{1, 3}) \Rightarrow B_{1, 2}$

    áp dụng luật logic __Contrapositive__ đối với $R_{30}$
    - $R_{31}: \neg B_{1, 2} \Rightarrow \neg (P_{1, 1} \vee P_{2, 2} \vee P_{1, 3})$

    áp dụng luật logic __Modus Ponens__ giữa $R_{31}$ với $R_{28}$
    - $R_{32}: \neg (P_{1, 1} \vee P_{2, 2} \vee P_{1, 3})$

    Áp dụng luật logic __De Morgan__ cho $R_{32}$
    - $R_{33}: \neg P_{1, 1} \wedge \neg P_{2, 2} \wedge \neg P_{1, 3}$

    Áp dụng luật __Biconditional Elimination__ đối với $R_{27}$
    - $R_{34}: S_{1, 2} \Rightarrow (W_{1, 1} \vee W_{2, 2} \vee W_{1, 3})$

    Áp dụng luật __Modus Ponens__ giữa $R_{34}$ với $R_{29}$
    - $R_{35}: W_{1, 1} \vee W_{2, 2} \vee W_{1, 3}$
    
    Áp dụng __Resolution__ giữa $R_{35}$ và $R_2$:
    - $R_{36}: W_{2, 2} \vee W_{1, 3}$ 


    Từ $R_{25}: \neg W_{1, 1} \wedge \neg W_{2, 2} \wedge \neg W_{3, 1}$

    Áp dụng luật __And-Elimination__ cho $R_{25}$:
    - $R_{37}: \neg W_{2, 2}$

    Áp dụng __Resolution__ giữa $R_{36}$ và $R_{37}$
    - $R_{38}: W_{1, 3}$

    Áp dụng luật __And-Elimination__ cho $R_{33}$:
    - $R_{39}: \neg P_{2, 2}$

Từ $R_{37}$ và $R_{39}$:
$$Safe(2, 2) \equiv \neg P_{2, 2} \wedge \neg W_{2, 2}$$

Do đó Agent kết luận rằng ô (2, 2) là an toàn và quyết định di chuyển đến ô (2, 2)