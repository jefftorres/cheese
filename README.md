# cheese
This project aims to solve an optimization problem for a cheese supply chain using different optimizations.
The main methods used are bio-inspired optimizations, done by using already implemented libraries.

# Model
The initially proposed model aims to simplify an already established optimization model *(not shown here)* in the framework of this project.

## Schema
The $` n `$ collection centers are represented as a vector, each with a defined quantity $` x `$.
The quantity for the $`i`$th position represents the amount of the total demand $` D `$ that collection center $` j_i `$ is going to supply.

$$
\begin{array} {|r|r|r|r|r|r|}
    \hline x_0 & x_1 & x_2 & x_3 & \cdots & x_n \\
    \hline
\end{array}
\quad \therefore \quad x_i = cacopios_i
$$

## Objective function
Minimize the total costs for the supply chain. 

Having:

$$
\begin{align*}
    Costo_{CA_p} &= k(CA_p) \times Precio(CA_p) + CostoTransp(CA_p) + \\ 
    & \left[ TiempoTransp(CA_p) + TiempoAlistam(CA_p) \right] \\
    p &\in 1,...,N
\end{align*}
$$

and:

$$
\begin{align*}
    Costo_{CA_{apoyo}} = \sum_{i=0, i\neq p}^{N} 
    &\left[ k(CA_i) \times Precio(CA_i) + CostoTransp(CA_i) + \\
    &\left( TiempoTransp(CA_i) + TiempoAlistam(CA_i) \right) \times CostoTiempo \right] \\
    i &= [1,...,N], i \neq p
\end{align*}
$$

then the objective function is:

$$
    min Z = Costo_{CA_p} + Costo_{CA_{apoyo}}
$$

Bound to the following restrictions:

$$
\begin{align*}
    k(CA_p) + \sum_{i=0}^{N} k(CA_i) &= Demanda \\
    k(CA_j) &\leq Stock(CA_j) + Ppotencial(CA_j) \quad &\therefore j \in {1,...,N}
\end{align*}
$$


