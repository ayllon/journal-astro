$$
f = \sum{{pixel} * {area}} \\
\sigma_{f}^2 = \sum{{\sigma_{pixel}^2} * {area}} \\
f_{err} = \sqrt{\sigma_f^2 + \frac{f}{gain}} \\
M = -2.5 * {{{log}_{10}}(f)} + {M_0} \\
M_{err} = 1.0857 * \frac{f_{err}}{f}
$$

I compare the median of:

$$
\frac{(M - M_{true})^2}{M_{err}^2}
$$