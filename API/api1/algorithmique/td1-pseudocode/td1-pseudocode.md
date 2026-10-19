# (2024-2025) **TD1 Pseudo Code**
- **Exercice 1 :**
  
  1. Le pseudo code 1 :
  ```
  Algorithme Algo1
    A, B, C : ENTIER
  DEBUT
   A <- 5
   B <- 3
   C <- A + B
   A <- 2
   C <- B - A
  FIN
  ```
  Les valeurs des variables A, B et C après l'éxecution de l'algorithme :
  |      | A | B | C |
  | :----:  |    :----:   |    :----:  |  :----:  |
  | A <- 5  | 5 | ? | ? |
  | B <- 3 | 5 | 3 | ? |
  | C <- A + B | 5 | 3 | 8 |
  | A <- 2 | 2 | 3 | 8 |
  | C <- B - A | 2 | 3 | 1 |

   2. Le pseudo code 2 :
  ```
  Algorithme Algo2
    A, B, C : ENTIER
  DEBUT
   A <- 3
   B <- 10
   C <- A + B
   B <- A + B
   A <- C
  FIN
  ```

  Les valeurs des variables A, B et C après l'éxecution de l'algorithme :
  |      | A | B | C |
  | :----:  |    :----:   |    :----:  |  :----:  |
  | A <- 3 | 3 | ? | ? |
  | B <- 10 | 3 | 10 | ? |
  | C <- A + B | 3 | 10 | 13 |
  | B <- A + B | 3 | 13 | 13 |
  | A <- C | 13 | 13 | 13 |

   3. Le pseudo code 3 :
  ```
  Algorithme Algo3
    A, B, C : ENTIER
  DEBUT
   A <- 2
   B <- 1
   C <- (5*(A + 2)*3)*(B + 4)
   B <- C + 8/2
   A <- C%2
  FIN
  ```

  Les valeurs des variables A, B et C après l'éxecution de l'algorithme :
  |      | A | B | C |
  | :----:  |    :----:   |    :----:  |  :----:  |
  | A <- 2 | 2 | ? | ? |
  | B <- 1 | 2 | 1 | ? |
  |C <- (5*(A + 2)*3)*(B + 4) | 2 | 1 | 300 |
  | B <- C + 8/2| 2 | 304 | 300 |
  | A <- C%2 | 0 | 304 | 300 |

   4. Le pseudo code 4 :
  ```
  Algorithme Algo4
    A, B, C : ENTIER
  DEBUT
   A <- B
   B <- A
   C <- A - B
  FIN
  ```

  Les valeurs des variables A, B et C après l'éxecution de l'algorithme :
  |      | A | B | C |
  | :----:  |    :----:   |    :----:  |  :----:  |
  | A <- B | B | ? | ? |
  | B <- A | B | B | ? |
  |C <- A - B | B | B | 0 |

  - **Exercice 2 :**

  ```
  Algorithme : Mystere
    A, B, C, p, d, t : ENTIER
  DEBUT
  /* Lecture des variables*/
  LIRE(A,B,C)
  SI (A<B) ALORS
    SI (C>B) ALORS
      p <- A
      d <- B
      t <- C
    SINON
      SI (A<C) ALORS
        p <- A
        d <- C
        t <- B
      SINON
        p <- C
        d <- A
        t <- B
  SINON
    SI (C>A) ALORS

  ```







  
