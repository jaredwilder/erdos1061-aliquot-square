# Erdős #1061 — the proposed bound `r(N) <= tau(N)` is false

**Author:** Jared Wilder  
**Status:** exact counterexample / killed proof mechanism  
**Parent Erdős #1061 program:** not closed by this note

For positive integer `N`, define

\[
r(N)=\#\{a\in\{1,\ldots,N-1\}:\sigma(a)+\sigma(N-a)=\sigma(N)\}.
\]

Thus `r(N)` counts **ordered** solution pairs `(a,b)` with `a+b=N` for the equation

\[
\sigma(a)+\sigma(b)=\sigma(a+b).
\]

A historical route proposed the load-bearing inequality

\[
r(N)\le \tau(N),
\]

where `tau(N)` is the divisor-counting function. The route requested an exact table but was retracted for another reason before the table was ever run.

The bound is false.

## First failure

The first failure is

\[
\boxed{N=123,\qquad r(123)=6>4=\tau(123).}
\]

The three unordered pairs are

```text
(38,85): sigma(38)+sigma(85) = 60+108 = 168 = sigma(123)
(41,82): sigma(41)+sigma(82) = 42+126 = 168 = sigma(123)
(46,77): sigma(46)+sigma(77) = 72+96  = 168 = sigma(123)
```

and their reversals give the six ordered pairs.

## Complete failures through 400

A fresh exact divisor-sum/divisor-count sieve gives:

| N | r(N) | tau(N) |
|---:|---:|---:|
| 123 | 6 | 4 |
| 141 | 6 | 4 |
| 183 | 8 | 4 |
| 249 | 6 | 4 |
| 279 | 8 | 6 |
| 303 | 6 | 4 |
| 309 | 6 | 4 |
| 393 | 10 | 4 |

So by `N<=400`, the multiplicity has already reached

\[
\boxed{r(393)=10}.
\]

## What this does and does not show

This kills the proposed `r(N)<=tau(N)` upper-bound mechanism independently of the other defect that originally caused the route to be abandoned.

It does **not** give an asymptotic estimate for `r(N)`, and it does not supersede the constructive lower-bound work elsewhere in this repository.

## Verification

The companion script `verify_tau_bound_counterexample.py` recomputes `sigma`, `tau`, every `r(N)` for `3<=N<=400`, the first failure, and the complete failure list above using only integer arithmetic.

## Provenance

Recovered from `erdos-counterexample-queue`, where the exact table was finally run after the original campaign had already stopped. Independently recomputed again before promotion into this subject repository.
