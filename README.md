# Investigating the $\zeta(3)$ problem
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

So a product of sine functions will lead us to find even values of the zeta function, but not odd values, incidentally, this is exactly why this problem is hard for odd values. Wishful thinking and bad factorisation would suggest that since the roots of $\sin(ax^2)$ are $\pm\sqrt\frac{n\pi}{a}$ we could write the product of linear factors 

$$\sin(ax^2) = x\left(1-\frac{x}{\sqrt{\pi/a}}\right)\left(1+\frac{x}{\sqrt{\pi/a}}\right)\left(1-\frac{x}{\sqrt{\pi/2a}}\right)\left(1+\frac{x}{\sqrt{\pi/2a}}\right)..$$ 

and then consider $\sin(ax^2)\sin(bx^2)\sin(cx^2)$, and pick values of $a,b,c$ such that 

$$\left(1-\frac{ax^2}{n\pi}\right)\left(1-\frac{bx^2}{n\pi}\right)\left(1-\frac{cx^2}{n\pi}\right) = \left(1-\frac{abcx^6}{n^3\pi^3}\right)$$

and then a lot of l'Hôpital's rule and the tricks in [these lecture notes](https://www.math.cmu.edu/~bwsulliv/basel-problem.pdf) (proof 1) should have been enough. 

We can play a similar game with the factorisation of the inverse-Gamma function, and get an expression for $\zeta(3)$ this way, but evaluating the limit as $z$ goes to zero of the LHS seems tricky, simplifying the digamma function with its [Laurent series expansion](https://math.stackexchange.com/questions/4185216/approximating-the-digamma-function-for-small-arguments) doesn't seem to help, instead leading to a blowup to infinity. Here is a more detailed explanation:

The Weierstrass factorisation of interest is:

$$ \frac{1}{\Gamma(z)} = e^{\gamma z}z\prod_{n=1}^{\infty}\left(1+\frac{z}{n}\right)e^{-z/n}$$

Now we can introduce three gamma functions and consider the factorisation of this:

$$ F(z) = \frac{1}{\Gamma(az)\Gamma(bz)\Gamma(cz)} $$

And we have:

$$ F(z) = e^{\gamma (a+b+c) z}z^3\prod_{n=1}^{\infty}\left(1+\frac{az}{n}\right)\left(1+\frac{bz}{n}\right)\left(1+\frac{az}{n}\right)e^{-(a+b+c)z/n} $$

This is interesting because we can set $a,b,c$ to whichever value we please. So we consider the expanded product and choose them such that only the $n^3$ term remains. This gives:

$$ (a b c z^3)/n^3 + (a b z^2)/n^2 + (a c z^2)/n^2 + (a z)/n + (b c z^2)/n^2 + (b z)/n + (c z)/n + 1 $$

So we set $ab+ac+bc=0$ and $a+b+c=0$, this is solved by $b = -\frac{1}{2}i(a\sqrt{3}-ia)$ and $c = \frac{1}{2}i(a\sqrt{3}+ia)$ which conveniently yields $abc=a^3$. So now our W. factorisation is:

$$ F(z) = z^3\prod_{n=1}^{\infty}\left(1+\frac{a^3z^3}{n^3}\right) $$

This is starting to look promising. Now divide by $z^3$ and take the log of both sides:

$$ \log\left(\frac{F(z)}{z^3}\right) = \sum_{n=1}^{\infty}\log\left(\frac{n^3 + a^3z^3}{n^3}\right) $$

and differentiate w.r.t $z$:

$$ \frac{d}{dz}\log\left(\frac{F(z)}{z^3}\right) = 
\sum_{n=1}^{\infty}\left(\frac{3z^2a^3}{n^3 + z^3n^3}\right) $$

finally we reach our expression by dividing by $3a^3z^2$ and taking $\lim_{z \to 0}$

$$ \lim_{z \to 0} \frac{1}{3z^2a^3} \frac{d}{dz}\log\left(\frac{F(z)}{z^3}\right) = \zeta(3) $$

Can we evaluate this limit? 
One confusing thing about this approach is that $a$ is still arbitrary afaik, so when will we get a constraint on $a$?
Might be instructive to evaluate this numerically, but currently limited by missing constraint on $a$. Is the constraint just $a=0$ actually? Because $F(0)$ has to be zero (I think), considering that, as [can be verified with wolfram alpha](https://www.wolframalpha.com/input?i=lim+%281%2FGamma%28z%29%29+as+z+goes+to+0):

$$ \lim_{z \to 0} \frac{1}{\Gamma(z)} = 0$$

[This](https://math.stackexchange.com/questions/1459709/can-this-approximate-closed-form-of-aperys-constant-zeta3-be-improved/) is an interesting approach along similar lines, he gets a good approximation for zeta(3).

Ok maybe that's why this doesn't work... (?)

## Numerical experimentation: beating the record number of digits
The current best approximation to Apéry's constant is good to 21 digits, as quoted on [MathWorld](https://mathworld.wolfram.com/AperysConstantApproximations.html).

The first approximation (accurate to 1 decimal point) that we got from the Putnam product suggests adding log(3/2) to the search vector in [this approach](https://ar5iv.labs.arxiv.org/html/0910.2684), this actually improves distance from $\zeta(3)$ from $1.5 \cdot 10^{-22}$ to $1.2 \cdot 10^{-22}$. This doesn't add a digit though.

However adding $\frac{\pi^2}{7}$ as well does get us to 22 digits. This was tried because of Euler's series expression for zeta(3):

$$ \zeta(3) = \frac{\pi^2}{7} \left(1-4\sum_{k-1}^{
\infty} \frac{\zeta(2k)}{2^{2k}(2k+1)(2k+2)} \right)$$

This is cool, looks like we beat the record, although of course there was no big insight that led to this. But tbf the current record holder also didn't have massive insight either (I guess his insight was to use PSQL?).
