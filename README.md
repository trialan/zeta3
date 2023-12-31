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
We can also show the (maybe?) related result below.

$$
\sum_{k=1}^{\infty} \frac{\zeta(3k) - 1}{k} = \log\left(3\pi \text{sech}\left(\frac{\pi \sqrt{3}}{2}\right)\right)
$$
