# Erdős #1061 — aliquot-square constructions

Let `σ(n)` denote the sum of the positive divisors of `n`. This repository studies solutions of

\[
\sigma(a)+\sigma(b)=\sigma(a+b)
\]

through a primitive-seed construction and a scaling law that turns each primitive seed into an infinite ray of further solutions.

## Primitive-seed theorem

Put

\[
q=\sigma(a)-a,
\qquad
b=q^2-a.
\]

If

- `q` is prime,
- `q\nmid a`, and
- `b>0` is prime,

then `(a,b)` is a primitive solution of

\[
\boxed{\sigma(a)+\sigma(b)=\sigma(a+b).}
\]

The proof is short. Since `σ(a)=a+q`, `σ(b)=b+1`, and `a+b=q^2`,

\[
\sigma(a)+\sigma(b)
=a+q+b+1
=q^2+q+1
=\sigma(q^2)
=\sigma(a+b).
\]

Moreover

\[
\gcd(a,b)=\gcd(a,q^2-a)=1
\]

because `q\nmid a`, so the seed is primitive.

The full statement and proof are in [`sigma-family/README.md`](sigma-family/README.md).

## Primitive rays

If `(a,b)` is a primitive solution and

\[
M=ab(a+b),
\]

then every positive integer `k` with `\gcd(k,M)=1` gives another solution

\[
(ka,kb).
\]

Pairwise coprimality and multiplicativity of `σ` give

\[
\sigma(ka)+\sigma(kb)
=\sigma(k)\bigl(\sigma(a)+\sigma(b)\bigr)
=\sigma(k)\sigma(a+b)
=\sigma(k(a+b)).
\]

Distinct primitive ratios give disjoint rays. Under the ordered-pair convention used in the computation, one primitive seed contributes asymptotic coefficient

\[
\boxed{\frac{2\varphi(M)}{M(a+b)}}.
\]

## Certified lower bound from primitive seeds

An exact certificate contains **152,803 primitive seeds with `a+b\le200000`**. The integer-only verifier checks every row from the defining equation, gcd, factorization, Euler `φ`, and the stored coefficient contribution.

Its exact floor sum is

\[
2295492576177,
\]

which gives the rigorous recorded bound

\[
\boxed{\liminf_{x\to\infty}\frac{S(x)}x\ge 2.295492576177}
\]

under the campaign's ordered-pair counting convention.

A second exact search through `a\le5,000,000` found 43 generator seeds, 37 new relative to the base bank, raising the recorded coefficient floor to

\[
\boxed{\liminf_{x\to\infty}\frac{S(x)}x>2.295497372037.}
\]

The 152,803-row certificate has SHA-256

```text
343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68
```

and is checked by [`sigma-family/ERDOS1061_SEED_CERT_VERIFY.py`](sigma-family/ERDOS1061_SEED_CERT_VERIFY.py).

## A Mersenne specialization

Taking `a=2^m` gives

\[
q=2^m-1,
\qquad
b=2^{2m}-3\cdot2^m+1.
\]

Therefore

\[
\boxed{
2^m-1\text{ prime and }
2^{2m}-3\cdot2^m+1\text{ prime}
\Longrightarrow
(2^m,b)\text{ is a primitive seed}.}
\]

The recovered certificate contains examples at

\[
m=2,3,5,7,13,19.
\]

No infinitude claim is made for those exponents.

## Reading the repository

- [`sigma-family/README.md`](sigma-family/README.md) — primitive-seed theorem, scaling theorem, certified lower bounds, and Mersenne specialization;
- `rays/` — primitive-ray and asymptotic analysis;
- [`CERTIFICATE-RECOVERY.md`](CERTIFICATE-RECOVERY.md) — exact identity and recovery record for the large seed certificate;
- `ore-findings/` — earlier extracted notes and supporting material.

A 2026 preprint by Eric Li gives a stronger asymptotic result for the parent Erdős problem by a different route. This repository is best read as an independent construction theorem, scaling theory, and exact certificate computation.

Author: Jared Wilder.