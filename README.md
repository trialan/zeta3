# zeta3
Repo with code related to investigation of the zeta-3 problem. The starting point of our research are the following two results:

$$
\sum_{n=2}^{\infty} \text{arctanh}\left(\frac{1}{n^3}\right) = \frac{1}{2} \log\left(\frac{3}{2}\right)
$$


$$
\tanh(a + b) = \frac{\tanh(a) + \tanh(b)}{1 + \tanh(a) \cdot \tanh(b)}
$$

The second is a standard result, and the first follows from investigating the sum (Putnam 1977):

$$\sum_{n=2}^{\infty}\frac{n^3-1}{n^3+1} = \frac{2}{3}$$

Wishful thinking would give the (incorrect) result:


$$
\tanh(a + b + c + ...) = \frac{\tanh(a) + \tanh(b) + \tanh(c) + ... }{1 + \tanh(a) \cdot \tanh(b) \cdot \tanh(c) ...}
$$

Which would immediately yield:

$$
\zeta(3) = 1 + \tanh\left(\frac{1}{2} \log\left(\frac{3}{2}\right)\right) = 1.2
$$

Which is incorrect, as $\zeta(3) \simeq 1.202057$. Incorrect, but interesting.  Can we derive the correct $\tanh$ addition formula?

## Other
### We can also show the (maybe?) related result below.

$$
\sum_{k=1}^{\infty} \frac{\zeta(3k) - 1}{k} = \log\left(3\pi \text{sech}\left(\frac{\pi \sqrt{3}}{2}\right)\right)
$$


### Weierstrass factorisation: extending the original proof
This [AoPS post](https://artofproblemsolving.com/community/c490120h1495301_closed_form_of_the_aperys_constant) has an interesting idea of applying Euler's original method, seems worth digging into a bit more. He gets the [Weierstrass factorisation](https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem) wrong, when you do it correctly you get

$$ \sin(\pi z) = \pi z\prod_{n=1}^{\infty}\left(1-\frac{z^2}{n^2}\right) $$

So a product of sine functions will lead us to find even values of the zeta function, but not odd values. Wishful thinking and bad factorisation would suggest that since the roots of $\sin(ax^2)$ are $\pm\sqrt\frac{n\pi}{a}$ we could write the product of linear factors 

$$\sin(ax^2) = x\left(1-\frac{x}{\sqrt{\pi/a}}\right)\left(1+\frac{x}{\sqrt{\pi/a}}\right)\left(1-\frac{x}{\sqrt{\pi/2a}}\right)\left(1+\frac{x}{\sqrt{\pi/2a}}\right)..$$ 

and then consider $\sin(ax^2)\sin(bx^2)\sin(cx^2)$, and pick values of $a,b,c$ such that 

$$\left(1-\frac{ax^2}{n\pi}\right)\left(1-\frac{bx^2}{n\pi}\right)\left(1-\frac{cx^2}{n\pi}\right) = \left(1-\frac{abcx^6}{n^3\pi^3}\right)$$

and then a lot of l'Hôpital's rule and the tricks in [these lecture notes](https://www.math.cmu.edu/~bwsulliv/basel-problem.pdf) (proof 1) should have been enough.
