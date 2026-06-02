# Problem

<img src="assets/Problem1.png">
<img src="assets/Problem2.png">


## Variables

Ta có 5 biến cho mỗi thuộc tính (tổng cộng 25 biến):

- $H_1, H_2, H_3, H_4, H_5$ (Thứ tự nhà từ trái sang phải).
- Mỗi nhà có các thuộc tính: $Color, Nationality, Drink, Tobacco, Pet.$

## Miền giá trị cho mỗi thuộc tính (Domains)

### Color
mỗi nhà:
$$D_{Color} = \{Red, Green, Ivory, Yellow, Blue\}$$

### Nationality
$$D_{Nationality} = \{Brit, Spanish, Ukrainian, Norwegian, Japanese\}$$

### Drink
$$D_{Drink} = \{Coffee, Tea, Milk, OrangeJuice, Water \}$$

### Tobacco
$$D_{Tobacco} = \{OldGold, Kools, Chesterfields, LuckyStrike, Parliaments \}$$

### Pet
$$D_{Pet} = \{Dog, Snails, Fox, Horse, Zebra \}$$

## Unary Constraints
Các ràng buộc trực tiếp.

### Clue 8
```
Milk is drunk in the middle house
```
Nhà số 3

$$Drink_3 = Milk$$

### Clue 9
```
Norwegian lives in first house
```
$$Nationality_1 = Norwegian$$

## Binary Constraints
dạng: 
```
X = value
⇔
Y = value
```

### Clue 1
```
Brit lives in Red house
```
$$Nationality_i = Brit$$

if:
$$Color_i = Red$$

### Clue 2
```
Spanish owns Dog
```
$$Nationality_i = Spanish$$

if:
$$Pet_i = Dog$$

### Clue 3
```
Coffee in Green house
```
$$Color_i = Green$$

if:
$$Drink_i = Coffee$$

### Clue 4
```
Ukrainian drinks Tea
```
$$Nationality_i = Ukrainian$$

if:
$$Drink_i = Tea$$

### Clue 6
```
Old Gold owns Snails
```
$$Tobacco_i = OldGold$$

if:
$$Pet_i = Snails$$

### Clue 7
```
Kools in Yellow house
```
$$Tobacco_i = Kools$$

if:
$$Color_i = Yellow$$

### Clue 12
```
Lucky Strike drinks Orange Juice
```
$$Tobacco_i = LuckyStrike$$

if:
$$Drink_i = OrangeJuice$$

### Clue 13
```
Japanese smokes Parliaments
```
$$Nationality_i = Japanese$$

if:
$$Tobacco_i = Parliaments$$

## Reative Constraints
### Clue 5
Green ngay bên phải Ivory

$$Color_i = Ivory$$
$$Color_{i+1} = Green$$

Với $i \in \{1, 2, 3, 4 \}$

Tức là cặp (Ivory, Green)

### Clue 10
```
Người hút Chesterfields
ở cạnh
người nuôi Fox.
```
$$Tobacco_i = Chesterfields$$

$\Leftrightarrow$

$$Pet_{i-1} = Fox \vee Pet_{i+1} = Fox$$

Nghĩa là Pet nhà bên trái (i-1) hoặc nhà bên phải (i+1) là Fox.

### Clue 11
```
Người hút Kools
ở cạnh
người nuôi Horse.
```

$$Tobacco_i = Kools$$

$\Leftrightarrow$

$$Pet_{i-1} = Horse \vee Pet_{i+1} = Horse$$

### Clue 14
```
The Norwegian lives next to the Blue house.
```
$$Nationality_i = Norwegian$$

$\Leftrightarrow$

$$Color_{i-1} = Blue \vee Color_{i+1} = Blue$$

### Clue 15
```
Người hút Chesterfields
ở cạnh
người uống Water.
```
$$Tobacco_i = Chesterfields$$

$\Leftrightarrow$

$$Drink_{i-1} = Water \vee Drink_{i+1} = Water$$

## Implicit Constraints
Tất cả 5 giá trị trong cùng một hạng mục phải khác nhau.
$$\forall i, j \in \{1, 2, 3, 4, 5 \}, i \ne j$$

# Giải vấn đề

## Bảng CSP ban đầu 
| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |


## Queue ban đầu
```
Q1  Brit → Red
Q2  Red → Brit
Q3  Spaniard → Dog
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q16 Milk → Middle house
Q17 Middle house → Milk
Q18 Norwegian → First house
Q19 First house → Norwegian
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields
```

## Thử giải

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Milk, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |


#### Queue
```
Q16 Milk → Middle house
Q17 Middle house → Milk
Q18 Norwegian → First house
Q19 First house → Norwegian
Q1  Brit → Red
Q2  Red → Brit
Q3  Spaniard → Dog
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields
```

### Step - 1
#### - Xi, Xj
Q16 Milk → Middle house

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |


#### Queue
```
Q17 Middle house → Milk
Q18 Norwegian → First house
Q19 First house → Norwegian
Q1  Brit → Red
Q2  Red → Brit
Q3  Spaniard → Dog
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields
```

### Step - 2
#### - Xi, Xj
Q17 Middle house → Milk

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Norwegian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |


#### Queue
```
Q18 Norwegian → First house
Q19 First house → Norwegian
Q1  Brit → Red
Q2  Red → Brit
Q3  Spaniard → Dog
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields
```

### Step - 3
#### - Xi, Xj
Q18 Norwegian → First house

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Red, Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q19 First house → Norwegian
Q1  Brit → Red
Q2  Red → Brit
Q3  Spaniard → Dog
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields
```

### Step - 4
#### - Xi, Xj
Q19 First house → Norwegian

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Red, Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q1  Brit → Red
Q2  Red → Brit
Q3  Spaniard → Dog
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields
```

### Step - 5
#### - Xi, Xj
Q1  Brit → Red

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q2  Red → Brit
Q3  Spaniard → Dog
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 6
#### - Xi, Xj
Q2  Red → Brit

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q3  Spaniard → Dog
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 7
#### - Xi, Xj
Q3  Spaniard → Dog

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q4  Dog → Spaniard
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))
```

### Step - 8
#### - Xi, Xj
Q4  Dog → Spaniard

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q5  Green → Coffee
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))
```

### Step - 9
#### - Xi, Xj
Q5  Green → Coffee

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q6  Coffee → Green
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

Nationality(H3)
Drink(H3)
Tobacco(H3)
Color(H2)
Color(H4)
```

### Step - 10
#### - Xi, Xj
Q6  Coffee → Green

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q7  Ukrainian → Tea
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))
```

### Step - 11
#### - Xi, Xj
Q7  Ukrainian → Tea

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q8  Tea → Ukrainian
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))
```

### Step - 12
#### - Xi, Xj
Q8  Tea → Ukrainian

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q9  Ivory → Right Green
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))
```

### Step - 13
#### - Xi, Xj
Q9  Ivory → Right Green

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Green, Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q10 Green → Left Ivory
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))
```

### Step - 14
#### - Xi, Xj
Q10 Green → Left Ivory

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q11 Old Gold → Snails
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 15
#### - Xi, Xj
Q11 Old Gold → Snails

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q12 Snails → Old Gold
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 16
#### - Xi, Xj
Q12 Snails → Old Gold

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q13 Kools → Yellow
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 17
#### - Xi, Xj
Q13 Kools → Yellow

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q14 Yellow → Kools
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 18
#### - Xi, Xj
Q14 Yellow → Kools

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q15 Chesterfields → Neighbor Fox
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 19
#### - Xi, Xj
Q15 Chesterfields → Neighbor Fox

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q20 Fox → Neighbor Chesterfields
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 20
#### - Xi, Xj
Q20 Fox → Neighbor Chesterfields

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q21 Kools → Neighbor Horse
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```

### Step - 21
#### - Xi, Xj
Q21 Kools → Neighbor Horse

#### Dx

| House   | Color                             | Nationality                                      | Drink                                    | Tobacco                                                     | Pet                              |
| ------- | --------------------------------- | ------------------------------------------------ | ---------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| House 1 | {Ivory, Yellow, Blue} | {Norwegian} | {Coffee, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Snails, Fox, Horse, Zebra} |
| House 2 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 3 | {Red, Ivory, Yellow, Blue} | {Brit, Spaniard, Japanese} | {Milk} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 4 | {Red, Green, Ivory, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |
| House 5 | {Red, Green, Yellow, Blue} | {Brit, Spaniard, Ukrainian, Japanese} | {Coffee, Tea, Orange Juice, Water} | {Old Gold, Kools, Chesterfields, Lucky Strike, Parliaments} | {Dog, Snails, Fox, Horse, Zebra} |

#### Queue
```
Q22 Horse → Neighbor Kools
Q23 Lucky Strike → Orange Juice
Q24 Orange Juice → Lucky Strike
Q25 Japanese → Parliaments
Q26 Parliaments → Japanese
Q27 Norwegian → Neighbor Blue
Q28 Blue → Neighbor Norwegian
Q29 Chesterfields → Neighbor Water
Q30 Water → Neighbor Chesterfields

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))

(Nationality(H1),Pet(H1))
(Tobacco(H1),Pet(H1))
(Pet(H2),Pet(H1))
(Pet(H3),Pet(H1))
(Pet(H4),Pet(H1))
(Pet(H5),Pet(H1))

(Nationality(H3),Color(H3))
(Drink(H3),Color(H3))
(Tobacco(H3),Color(H3))
(Color(H2),Color(H3))
(Color(H4),Color(H3))

(Color(H1),Drink(H1))
(Nationality(H1),Drink(H1))
(Tobacco(H1),Drink(H1))

(Drink(H2),Drink(H1))
(Drink(H3),Drink(H1))
(Drink(H4),Drink(H1))
(Drink(H5),Drink(H1))

(Color(H3),Nationality(H3))
(Pet(H3),Nationality(H3))
(Drink(H3),Nationality(H3))
(Tobacco(H3),Nationality(H3))

(Nationality(H1),Nationality(H3))
(Nationality(H2),Nationality(H3))
(Nationality(H4),Nationality(H3))
(Nationality(H5),Nationality(H3))

(Nationality(H2),Color(H2))
(Drink(H2),Color(H2))
(Tobacco(H2),Color(H2))
(Color(H1),Color(H2))
(Color(H3),Color(H2))

(Nationality(H5),Color(H5))
(Drink(H5),Color(H5))
(Tobacco(H5),Color(H5))
(Color(H4),Color(H5))

(Nationality(H1),Color(H1))
(Drink(H1),Color(H1))
(Tobacco(H1),Color(H1))
(Color(H2),Color(H1))
```
