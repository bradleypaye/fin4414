# Week 1 Notes: Estimating the Population Mean, and the Equity Premium

*First in a series of weekly conceptual notes for the capstone. This week's theme:
almost everything we do this semester eventually reduces to "we have a finite,
noisy sample and we want to say something honest about an unknown population
mean." We'll build that up carefully and self-containedly, using the equity
premium as our running example — every result used below is derived, or at
least sketched, in these notes. The `SampleMeanSimulation.ipynb` and
`SampleVarianceSimulation.ipynb` notebooks in this repo simulate the same
setup and are a great way to *watch* these results play out numerically, but
you shouldn't need either one open to follow the argument.*

## 1. Why this problem is everywhere

The **equity premium** is the average return, per year, that you earn from holding
"the market" (a broad, diversified U.S. equity portfolio) in excess of the
risk-free rate. It's arguably *the* number in asset pricing: it anchors discount
rates for capital budgeting, expected returns for retirement planning, and
countless "is this investment worth it" calculations you'll do in your theses.

And yet — despite being estimated from roughly a century of high-quality return
data — economists still argue about what its value actually is, and how much
uncertainty surrounds it. That's not a data problem. It's a *statistics* problem,
and it's the same problem you already met (in miniature) when you simulated the
sample mean of an i.i.d. Normal variable: **a sample mean computed from a finite
sample is a noisy estimate of an unknown, fixed population quantity.**

If you can precisely state what is and isn't justified about inference on a
sample mean, you can precisely state what is and isn't justified about the
equity premium. That's the goal of this note.

## 2. The classical setup: strong, stylized assumptions

Let $R_t$ denote the market's realized excess return (market return minus the
risk-free rate) in year $t$, for $t = 1, \dots, T$. (We're using $T$ here,
rather than the $N$ from the simulation notebooks, because in finance we're
almost always indexing observations by *time* — but it plays exactly the same
role: it's the sample size.)

The classical, "intro stats" starting point is to assume:

$$R_t \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2), \qquad t = 1, \dots, T$$

Unpacking "i.i.d. Normal" into its three separate, separately violable pieces
will matter a lot in Section 4, so let's name them:

1. **Identically distributed** — $\mu$ and $\sigma^2$ are the *same* in every
   year. The equity premium isn't secretly higher in the 1990s and lower in
   the 2010s; there's one fixed number $\mu$ we're trying to learn.
2. **Independent** — knowing last year's excess return tells you nothing about
   this year's.
3. **Normal** — each $R_t$ individually follows a Normal distribution.

$\mu$ is the equity premium: the object we actually care about. It's unknown.
$\sigma^2$ is also unknown, and is a nuisance parameter we'll have to deal with
along the way.

This is *exactly* the setup simulated in `SampleMeanSimulation.ipynb` (with
$\mu = 5$, $\sigma = 10$ standing in for whatever the "true" equity premium and
return volatility might be).

## 3. Exact inference under the classical assumptions

### 3.1 Three probability facts we're going to lean on

Everything in this section is really just bookkeeping built on top of a
handful of general facts about expectation and variance, stated carefully
enough that it's clear exactly which assumption buys you which result.

**Fact 1: expectation is linear.** Saying the expectation operator $E(\cdot)$
is *linear* means that the expectation of a weighted sum equals the weighted
sum of the expectations:

$$E(aX + bY) = aE(X) + bE(Y)$$

for *any* constants $a, b$ and *any* random variables $X, Y$ — they don't
need to be independent, or Normal, or related to each other at all. This
isn't a probabilistic assumption you need to argue for; it's an algebraic
consequence of the fact that expectation is defined as a sum (or integral),
and sums/integrals are themselves linear. It extends to sums of any number
of terms:

$$E\!\left(\sum_{t=1}^T a_t X_t\right) = \sum_{t=1}^T a_t\, E(X_t)$$

**Fact 2: variance of a sum.** Variance is *not* linear, but it behaves
predictably in two cases we'll use:

- *Scaling*: $\text{Var}(aX) = a^2\,\text{Var}(X)$. (No independence needed —
  this is just one random variable.)
- *Sums of independent (or merely uncorrelated) variables*:
  $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$. Unlike Fact 1, this
  **requires** independence (or at least zero correlation) — in general,
  $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X,Y)$, and
  the cross term only drops out when $X$ and $Y$ are uncorrelated. Flag this
  one mentally: it's exactly the ingredient that fails in Section 4 once we
  admit returns may be autocorrelated.

**Fact 3: Normal random variables are closed under linear combinations.** If
$X$ and $Y$ are (possibly correlated) Normal random variables, then $aX+bY$
is *itself* exactly Normal, for any constants $a, b$. This is a special
property of the Normal family — most distributions don't have it — and it's
what will let us upgrade "each $R_t$ is Normal" to "$\bar R$ is Normal"
below, rather than merely approximately so.

### 3.2 The estimator, and its exact sampling distribution

Our estimator of $\mu$ is the sample mean,
$\bar R = \frac{1}{T}\sum_{t=1}^{T} R_t$. Let's derive its mean and variance
explicitly, one fact at a time.

**Unbiasedness**, using Fact 1 (linearity — note that this step needs
*nothing* about independence):

$$E(\bar R) = E\!\left(\frac{1}{T}\sum_{t=1}^T R_t\right)
\overset{\text{Fact 1}}{=} \frac{1}{T}\sum_{t=1}^T E(R_t)
\overset{\text{ident. dist.}}{=} \frac{1}{T}\sum_{t=1}^T \mu
= \frac{1}{T}(T\mu) = \mu$$

The middle step uses *only* the "identically distributed" assumption
($E(R_t) = \mu$ for every $t$) — independence never enters. That's a genuinely
useful teaching point: **unbiasedness of the sample mean does not require
independence across time**, only that every $R_t$ has the same mean $\mu$.

**Variance**, using Fact 2 — and here independence *does* enter:

$$\text{Var}(\bar R) = \text{Var}\!\left(\frac{1}{T}\sum_{t=1}^T R_t\right)
\overset{\text{scaling}}{=} \frac{1}{T^2}\text{Var}\!\left(\sum_{t=1}^T R_t\right)
\overset{\text{independence}}{=} \frac{1}{T^2}\sum_{t=1}^T \text{Var}(R_t)
\overset{\text{ident. dist.}}{=} \frac{1}{T^2}(T\sigma^2) = \frac{\sigma^2}{T}$$

So $\bar R$ is unbiased, and its spread shrinks at rate $1/\sqrt{T}$ — nothing
new relative to the mean notebook, but now you can see exactly which of the
two assumptions (identical distribution vs. independence) is doing the work
at each step.

Now bring in Fact 3 and full normality. Since each $R_t \sim N(\mu, \sigma^2)$
and $\bar R = \sum_t \frac{1}{T} R_t$ is a linear combination of (independent)
Normal random variables, $\bar R$ is *itself* exactly Normal, by Fact 3 — for
**any** $T$, not just approximately Normal for large $T$. Combined with the
mean and variance just derived (which hold regardless of normality):

$$\bar R \sim N\left(\mu, \frac{\sigma^2}{T}\right) \quad \text{exactly, for every } T.$$

This exactness is a big deal, and it's special: it comes entirely from Fact 3,
which is a property of the Normal distribution specifically, not something
you get for free. Keep that in your back pocket — it's the first thing to go
once we relax normality in Section 5.

### 3.3 The sample variance, and where the chi-squared distribution comes from

Before we can handle the unknown-$\sigma^2$ problem, we need an estimator of
$\sigma^2$ itself, and a way to describe its sampling distribution. That
requires one new distribution — the **chi-squared distribution** — which
shows up constantly whenever *sums of squares* of Normal variables are
involved (it will reappear all semester, e.g. in regression $F$-tests and
$R^2$-based tests).

**Definition.** If $Z_1, \dots, Z_k$ are i.i.d. standard Normal, $N(0,1)$,
random variables, then their sum of squares

$$W = Z_1^2 + Z_2^2 + \cdots + Z_k^2$$

follows a **chi-squared distribution with $k$ degrees of freedom**, written
$W \sim \chi^2_k$. "Degrees of freedom" here just counts how many independent
squared standard-Normal terms went into the sum.

**Properties we'll use** (stated without proof — they follow from the
definition plus standard facts about the Normal distribution):

1. **Support.** $\chi^2_k \geq 0$ always — it's built from squares, so it can
   never be negative. Its distribution is right-skewed, especially for small
   $k$ (it piles up near zero and has a long right tail), and becomes more
   symmetric and bell-shaped as $k$ grows.
2. **Mean.** $E(W) = k$.
3. **Variance.** $\text{Var}(W) = 2k$.
4. **Additivity.** If $W_1 \sim \chi^2_{k_1}$ and $W_2 \sim \chi^2_{k_2}$ are
   *independent*, then $W_1 + W_2 \sim \chi^2_{k_1+k_2}$ — chi-squared degrees
   of freedom add, when you're adding independent chi-squared pieces.

Now define the (unbiased) **sample variance**,

$$s^2 = \frac{1}{T-1}\sum_{t=1}^T (R_t - \bar R)^2$$

the average squared deviation from the *sample* mean, with a $T-1$ (rather
than $T$) divisor. Here's the guiding idea for why the divisor is $T-1$, and
where the stated result

$$\frac{(T-1)s^2}{\sigma^2} \sim \chi^2_{T-1}$$

comes from — a sketch, not a full proof, but enough to see why the pieces fit
together. Start from something we *do* know how to characterize: since each
$R_t \sim N(\mu, \sigma^2)$ i.i.d., the standardized deviations
$(R_t-\mu)/\sigma$ are i.i.d. standard Normal, so by the definition above,
their sum of squares is *exactly* chi-squared with $T$ degrees of freedom —
one for each observation:

$$\sum_{t=1}^T \left(\frac{R_t - \mu}{\sigma}\right)^2 \sim \chi^2_T$$

The problem is that this uses the unknown $\mu$; $s^2$ uses $\bar R$ instead.
The algebraic link between the two comes from a standard "add and subtract
$\bar R$" decomposition. Writing $R_t - \mu = (R_t - \bar R) + (\bar R - \mu)$
and expanding the square, the cross term vanishes when summed over $t$
(because $\sum_t (R_t - \bar R) = 0$ by definition of the sample mean), and
you're left with the identity

$$\sum_{t=1}^T (R_t - \mu)^2 \;=\; \sum_{t=1}^T (R_t - \bar R)^2 \;+\; T(\bar R - \mu)^2$$

i.e., "total squared deviation from the truth" splits exactly into "squared
deviation from the sample mean" plus "squared deviation of the sample mean
from the truth." Dividing through by $\sigma^2$ and relabeling:

$$\underbrace{\sum_{t=1}^T \left(\frac{R_t-\mu}{\sigma}\right)^2}_{\sim\ \chi^2_T \text{ (shown above)}}
\;=\;
\underbrace{\frac{(T-1)s^2}{\sigma^2}}_{\text{what we want}}
\;+\;
\underbrace{\left(\frac{\bar R - \mu}{\sigma/\sqrt{T}}\right)^2}_{\sim\ \chi^2_1}$$

The last term is chi-squared with **1** degree of freedom because it's the
square of a *single* standard Normal: we showed in Section 3.2 that
$\bar R \sim N(\mu, \sigma^2/T)$ exactly, so $(\bar R - \mu)/(\sigma/\sqrt T)$
is itself standard Normal, and squaring one standard Normal is exactly the
$k=1$ case of the definition above.

So we have "$\chi^2_T$ total = (unknown piece) + $\chi^2_1$." A deeper result
called **Cochran's theorem** (named for the statistician William Cochran; we
won't prove it here, but it's worth knowing the name so you can look it up)
guarantees two things in settings like this: (a) the two pieces on the
right-hand side are *independent* of one another, and (b) when a chi-squared
total is split this way into independent orthogonal pieces, their degrees of
freedom add, exactly as in Property 4 above. Since the total has $T$ degrees
of freedom and one piece has $1$, the remaining piece — our piece — must have
$T - 1$:

$$\frac{(T-1)s^2}{\sigma^2} \sim \chi^2_{T-1}$$

which is the stated result. The intuition for *why* it's $T-1$ and not $T$:
the $T$ deviations $R_t - \bar R$ are not free to vary independently — they
are constrained to sum to exactly zero (that's what defines $\bar R$) — so
only $T-1$ of them carry independent information. One degree of freedom is
"spent" estimating $\mu$ by $\bar R$. Cochran's theorem is also, as a bonus,
*why* $\bar R$ and $s^2$ turn out to be **independent** of each other under
these classical assumptions — a special, somewhat surprising fact (the
estimator of the mean carries no information about the estimator of the
spread around it) that we'll use in a moment, and that traces back to exactly
the same orthogonal decomposition above.

**Two quick corollaries**, both one-liners once you have the distributional
result and the chi-squared mean/variance from Properties 2–3:

- *Unbiasedness*: $E\!\left[\frac{(T-1)s^2}{\sigma^2}\right] = T-1$ (chi-squared
  mean, Property 2, with $k=T-1$) $\implies E(s^2) = \sigma^2$.
- *Spread*: $\text{Var}\!\left[\frac{(T-1)s^2}{\sigma^2}\right] = 2(T-1)$
  (chi-squared variance, Property 3) $\implies \text{Var}(s^2) =
  \frac{2\sigma^4}{T-1}$, so $\widehat{\text{SE}}(s^2) = s^2\sqrt{2/(T-1)}$
  once you plug in $s^2$ for the unknown $\sigma^2$ — exactly the recipe
  behind the HW 1 confidence interval for the variance.

### 3.4 The nuisance parameter problem, and the $t$-distribution

The formula in Section 3.2 requires $\sigma^2$, which we don't know. The
natural fix is to plug in the unbiased sample variance $s^2$ from Section
3.3. But once we replace $\sigma^2$ with an *estimate*, we've introduced
extra sampling variability, and the standardized mean is no longer exactly
standard Normal.

Here's where two facts from Section 3.3 combine to give an exact answer:
$\frac{(T-1)s^2}{\sigma^2} \sim \chi^2_{T-1}$, and $\bar R$ and $s^2$ are
*independent* of one another (both facts we obtained above from Cochran's
theorem).

The Student-$t$ distribution with $k$ degrees of freedom is, by definition,
what you get from dividing a standard Normal by an independent
$\sqrt{\chi^2_k / k}$. Plugging in $Z = \frac{\bar R - \mu}{\sigma/\sqrt{T}}$
(standard Normal, from Section 3.2) and $W = \frac{(T-1)s^2}{\sigma^2}$
(chi-squared with $k = T-1$ degrees of freedom, from Section 3.3), the
unknown $\sigma$ cancels algebraically:

$$\frac{Z}{\sqrt{W/(T-1)}}
= \frac{(\bar R - \mu)/(\sigma/\sqrt{T})}{\sqrt{s^2/\sigma^2}}
= \frac{\bar R - \mu}{s/\sqrt{T}}
\; \sim \; t_{T-1}$$

the Student-$t$ distribution with $T-1$ degrees of freedom — the same $T-1$
that shows up as the divisor in the definition of $s^2$ in Section 3.3. This
gives an **exact** confidence interval for the equity premium,

$$\bar R \; \pm \; t_{T-1,\,0.975} \cdot \frac{s}{\sqrt{T}}$$

and an exact hypothesis test (e.g., $H_0: \mu = 0$ — "is there an equity
premium at all?") using the $t_{T-1}$ distribution rather than the Normal.

**Connecting the dots to HW 1:** the confidence interval you built for the
*variance*, using the $\widehat{\text{SE}}(s^2)$ formula derived at the end of
Section 3.3, used the recipe $s^2 \pm 1.96 \times \widehat{\text{SE}}(s^2)$.
That $1.96$ is a Normal-distribution critical value, even though the *exact*
distribution of $s^2$ there is a (rescaled) $\chi^2_{T-1}$, not Normal. That
CI was already quietly leaning on a large-sample Normal approximation, rather
than exact finite-sample theory. Section 5 makes that logic explicit — and
you'll see it's also *why* using $1.96$ instead of a $t_{T-1}$ critical value
for the mean stops mattering once $T$ is reasonably large: the $t_{T-1}$
distribution converges to standard Normal as $T \to \infty$.

## 4. The problem: stock returns are probably not i.i.d. Normal

Everything in Section 3 is mathematically exact — *conditional on* the three
assumptions in Section 2. The trouble is that real equity return data violate
all three, to varying degrees:

- **Not identically distributed.** Volatility clusters — calm periods and
  turbulent periods (2008, 2020) don't have the same $\sigma^2$. Over long
  historical windows there's no guarantee $\mu$ itself has stayed constant
  (structural breaks: regulation, the rise of passive investing, changes in
  the composition of "the market").
- **Not independent.** Volatility clustering also breaks independence
  (today's variance is predictable from yesterday's, even if the *sign* of
  the return isn't). Momentum and reversal effects imply direct
  autocorrelation in returns. Overlapping-horizon returns (e.g., building
  "annual" observations from overlapping monthly windows) mechanically
  induce strong serial correlation.
- **Not Normal.** Return distributions have fatter tails than the Normal
  (large moves happen more often than Normality predicts) and are often
  left-skewed (crashes are sharper than rallies).

None of these are minor technicalities. Each one directly undermines a piece
of Section 3: non-identical distribution undermines the very idea of a single
fixed $\mu$; dependence undermines the $\sigma^2/T$ variance formula (positive
autocorrelation, the empirically relevant case for returns, makes the *true*
uncertainty in $\bar R$ *larger* than $\sigma^2/T$ suggests — so naive
formulas tend to make you overconfident); non-normality undermines the
*exactness* of the $t_{T-1}$ result. This is a big part of why reasonable
people disagree about the equity premium's value and precision: it is
genuinely a hard estimation problem, not a matter of not having "enough"
data.

## 5. Generalizing: large-sample ("asymptotic") inference

The fix is not to throw out everything from Section 3 — it's to ask which
parts of it survive if we replace the strong assumptions with much weaker
ones, accepting that the results now hold only *approximately*, and only once
$T$ is "large enough." Before stating the general result, it's worth working
through two small examples. Each one breaks exactly one piece of the
classical setup and shows you, concretely, what survives and what doesn't —
between them they explain exactly why the CLT is going to matter so much for
the rest of this course.

### 5.1 Two transitional examples

**Example 1: Bernoulli trials — losing normality, keeping i.i.d.**

Suppose that instead of a continuous excess return, we just record *whether*
the market had a positive excess-return year: let $X_t = 1$ if year $t$'s
excess return is positive and $X_t = 0$ otherwise, for $t = 1,\ldots,T$, with
$X_t \overset{\text{i.i.d.}}{\sim} \text{Bernoulli}(p)$. This is i.i.d., but
emphatically not Normal — $X_t$ only ever takes the values 0 or 1. (The same
setup describes, e.g., the win rate of a trading rule: $X_t = 1$ for a
profitable trade.) Here $p = P(X_t = 1)$ is the unknown "population mean"
we're estimating, and directly from the definition of a Bernoulli variable,
$E(X_t) = p$ and $\text{Var}(X_t) = p(1-p)$.

The natural estimator is again a sample mean, $\hat p = \frac{1}{T}\sum_t
X_t$ (the fraction of successes). Facts 1 and 2 from Section 3.1 never
required normality, so they apply completely unchanged:

$$E(\hat p) = p, \qquad \text{Var}(\hat p) = \frac{p(1-p)}{T}$$

$\hat p$ is unbiased, exactly as before. But Fact 3 — the one that delivered
*exact* normality of $\bar R$ back in Section 3.2 — was a special property of
the Normal distribution specifically, and Bernoulli data doesn't have it. In
fact $T\hat p$ (the raw count of successes) is Binomial$(T,p)$, a *discrete*
distribution: for any finite $T$, $\hat p$ simply cannot be Normal (Normal
variables are continuous), and its distribution is visibly lopsided whenever
$p$ is far from $1/2$ or $T$ is small.

And yet — this is, historically, where the whole subject started, roughly a
century before the general CLT was proved (De Moivre, 1733) — as $T$ grows,
the (standardized) Binomial distribution becomes very well approximated by a
Normal:

$$\frac{\hat p - p}{\sqrt{p(1-p)/T}} \; \xrightarrow{d} \; N(0,1)$$

which is exactly the "margin of error" formula behind opinion polling, and
gives an approximate 95% CI, $\hat p \pm 1.96\sqrt{\hat p(1-\hat p)/T}$, for
the win rate $p$. Nothing about the normality of the underlying $X_t$'s was
needed — just i.i.d.-ness and a large enough $T$.

**Example 2: a scale mixture — losing normality via random volatility**

Now go back to continuous returns, but build a mechanism for fat tails
directly into the model. Let

$$R_t = \mu + \sqrt{V_t}\, Z_t, \qquad t = 1,\ldots,T$$

where $Z_t \overset{\text{i.i.d.}}{\sim} N(0,1)$ are idiosyncratic shocks and
$V_t$ are i.i.d. **random** variances — draws representing "how turbulent
year $t$ happens to be" — independent of the $Z_t$'s, with $E(V_t) = \sigma^2
< \infty$. Conditional on $V_t$, $R_t$ is Normal: $R_t \mid V_t \sim N(\mu,
V_t)$. But $V_t$ is unobserved and random, so the *marginal* (unconditional)
distribution of $R_t$ — the one we actually see in the data — is a mixture of
Normals with different scales, not a single Normal.

Pinning down the mean and variance of that marginal distribution takes two
more standard facts about conditional expectation — worth stating explicitly,
since we'll lean on both again once we get to regression later in the
course:

- **Law of total expectation**: $E(X) = E\big[E(X \mid Y)\big]$.
- **Law of total variance**: $\text{Var}(X) = E\big[\text{Var}(X \mid Y)\big]
  + \text{Var}\big[E(X \mid Y)\big]$.

Applying both with $X = R_t$, $Y = V_t$:

$$E(R_t) = E\big[E(R_t \mid V_t)\big] = E[\mu] = \mu$$

$$\text{Var}(R_t) = E\big[\text{Var}(R_t \mid V_t)\big] + \text{Var}\big[E(R_t \mid V_t)\big]
= E[V_t] + \text{Var}[\mu] = \sigma^2 + 0 = \sigma^2$$

So $R_t$ has mean $\mu$ and variance $\sigma^2$, exactly as in the classical
setup — and since the $V_t$'s (hence the $R_t$'s) are i.i.d. across $t$,
Facts 1 and 2 again deliver $E(\bar R) = \mu$ and $\text{Var}(\bar R) =
\sigma^2/T$ exactly, no different from Section 3.2.

But $R_t$ itself is **not** Normal. It's sometimes drawn from a calm,
low-variance Normal and sometimes from a turbulent, high-variance one;
averaged together, the result has *heavier tails* than a single Normal with
the same variance $\sigma^2$ would — this is the standard explanation for the
fat tails and excess kurtosis observed in real return data (Section 4), and
it requires nothing more exotic than variance that varies randomly from
period to period. Fact 3 needed the individual pieces to already be Normal,
so it simply doesn't apply here, and $\bar R$ inherits some of that
non-normality in finite samples too.

Even so — and this is the punch line both examples are building toward — as
$T \to \infty$:

$$\frac{\bar R - \mu}{\sigma/\sqrt{T}} \; \xrightarrow{d} \; N(0,1)$$

exactly as in Example 1, *provided* the variances involved are "well
behaved" (here: $V_t$ i.i.d. with a finite mean, so no single year's draw can
dominate the average). This is a genuine, if stylized, preview of stochastic
volatility: real return volatility isn't just randomly reshuffled year to
year, it's *persistent* — calm years cluster with calm years — which is a
further, separate departure from independence that we come back to below.

### 5.2 The Law of Large Numbers and Central Limit Theorem, in general

Both examples above are special cases of two much more general theorems.

**Law of Large Numbers (LLN).** Under just i.i.d. sampling with a finite mean
(no Normality needed at all), $\bar R \to \mu$ in probability as
$T \to \infty$ — i.e., for any margin of error you name, however small, the
probability that $\bar R$ misses $\mu$ by more than that margin shrinks to
zero as the sample grows. $\bar R$ is a *consistent* estimator of $\mu$ far
more generally than it is an *exactly Normal* one — you can watch this play
out numerically in the mean notebook.

**Central Limit Theorem (CLT).** This is the key upgrade, and it's what made
both examples above work. For i.i.d. data with finite variance $\sigma^2$ —
again, **no normality of $R_t$ required** — it's a remarkable fact that:

$$\sqrt{T}\,(\bar R - \mu) \; \xrightarrow{d} \; N(0, \sigma^2)$$

Informally: for large enough $T$, $\bar R \overset{\text{approx}}{\sim}
N(\mu, \sigma^2/T)$ — the *same* formula as Section 3.2, but now justified as
an approximation that kicks in as $T$ grows, valid under dramatically weaker
assumptions than "the data are Normal." This is arguably the single most
important result in this note: the individual $R_t$'s can be however
non-Normal you like (fat tails, skew), and the *sample mean* still ends up
approximately Normal once you're averaging over enough observations.

Combining the LLN (applied to squared deviations, to argue $s^2$ is still a
consistent estimator of $\sigma^2$ well beyond the Normal case) with a result
called **Slutsky's theorem** (which lets you substitute a consistent estimate
like $s$ for $\sigma$ inside a limit like the one above without changing the
answer) gives you back the practical recipe:

$$\frac{\bar R - \mu}{s/\sqrt{T}} \overset{\text{approx}}{\sim} N(0,1)
\quad \Longrightarrow \quad
\bar R \; \pm \; 1.96 \times \frac{s}{\sqrt{T}} \; \text{ is an approximate 95\% CI}$$

— approximately justified under i.i.d.-with-finite-variance, rather than
exactly justified under i.i.d.-Normal. (And since $t_{T-1} \to N(0,1)$ as
$T \to \infty$, this is consistent with, not a contradiction of, Section 3.4.)

**What about independence?** This is the piece the LLN/CLT story above still
assumes, and it's the piece we flagged as most obviously violated for return
data. The good news is that CLTs still exist for *weakly dependent* stationary
series (the technical conditions go by names like "mixing"), so approximate
normality of $\bar R$ is often still a reasonable thing to lean on. The bad
news is that the simple $\sigma^2/T$ variance formula is no longer right when
returns are autocorrelated — you have to account for the covariances between
different $R_t$'s, not just their individual variances. The standard practical
tool for this is a **heteroskedasticity- and autocorrelation-consistent
(HAC)** standard error, the most common version being **Newey–West**. We
won't derive this now — just file away the name and the reason it exists: it's
the Section 3.4 recipe, repaired for dependence.

One honest caveat: "large enough $T$" is doing a lot of work in this section,
and *how* large depends on how badly the i.i.d.-Normal assumptions are
violated (heavier tails and stronger dependence both slow convergence down).
With roughly a century of *annual* equity premium data, $T$ is not actually
all that large — part of why the confidence intervals economists report for
the equity premium tend to be wide, and why the "how much data do we really
have" question is worth taking seriously rather than assuming CLT magic
rescues everything.

## 6. Where this leaves us, and what's next

- `SampleMeanSimulation.ipynb` and `SampleVarianceSimulation.ipynb` simulate
  exactly the Section 2–3 world: i.i.d. Normal data, exact finite-sample
  results. They're the "ground truth" sandbox for the classical theory above.
- A later notebook will extend those simulations to non-Normal and/or
  dependent data-generating processes, so you can *watch* the CLT-based
  approximate normality of $\bar R$ hold up (or, in bad-enough cases, fail to
  hold up well at the sample sizes we actually have) — the empirical
  counterpart to Section 5.

## Discussion questions

1. If historical annual excess returns are positively autocorrelated (the
   empirically typical finding), is the naive $s/\sqrt{T}$ standard error too
   big or too small relative to the true uncertainty in $\bar R$? What does
   that imply about confidence intervals for the equity premium that don't
   correct for autocorrelation?
2. Why might the average excess return realized over the last 30 years be a
   biased — or at least a very noisy — estimate of the equity premium
   investors *expect* going forward?
3. Suppose someone hands you 100 years of annual data versus 1,200 months of
   monthly data covering the same 100 years. Does the monthly version give
   you 12x the effective information about $\mu$? What would you need to
   assume for that to be true, and why might it fail?
