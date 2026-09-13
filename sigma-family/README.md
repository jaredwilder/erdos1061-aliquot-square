# Erdős #1061 — aliquot-square primitive seeds and certified ray lower bounds

**Author:** Jared Wilder  
**Recovered from:** September 2026 full-corpus audit  
**Public extraction:** 2026-09-11

Let `σ(n)` denote the sum of positive divisors of `n`. The frozen equation is

\[
\sigma(a)+\sigma(b)=\sigma(a+b).
\]

This directory records a universal construction theorem, a scaling theorem, and an exact finite
certificate estate. It does **not** claim the surrounding parent problem is at its current frontier:
stronger 2026 work exists for the parent asymptotics.

## Theorem 1 — aliquot-square primitive-seed generator

Let

\[
q=\sigma(a)-a,\qquad b=q^2-a.
\]

If

- `q` is prime;
- `q ∤ a`;
- `b>0` is prime;

then `(a,b)` is a primitive solution of

\[
\boxed{\sigma(a)+\sigma(b)=\sigma(a+b)}.
\]

### Proof

By definition `σ(a)=a+q`. Since `b` is prime, `σ(b)=b+1`. Also

\[
a+b=q^2.
\]

Therefore

\[
\sigma(a)+\sigma(b)=a+q+b+1=q^2+q+1=\sigma(q^2)=\sigma(a+b).
\]

Furthermore

\[
\gcd(a,b)=\gcd(a,q^2-a)=\gcd(a,q^2)=1
\]

because `q∤a`. Thus the seed is primitive.

## Theorem 2 — primitive-ray scaling

Suppose `(a,b)` is a primitive solution and put

\[
M=ab(a+b).
\]

If `gcd(k,M)=1`, then

\[
(ka,kb)
\]

is again a solution. Indeed, pairwise coprimality lets multiplicativity of `σ` give

\[
\sigma(ka)+\sigma(kb)
=\sigma(k)(\sigma(a)+\sigma(b))
=\sigma(k)\sigma(a+b)
=\sigma(k(a+b)).
\]

Reversing the ordered pair gives the second ray. Distinct primitive ratios produce disjoint rays.
The asymptotic ordered-pair coefficient of one primitive seed is

\[
\boxed{\frac{2\varphi(M)}{M(a+b)}}.
\]

## Exact base certificate — 152,803 primitive seeds

The recovered estate contains an exact CSV containing **152,803 primitive seeds with
`a+b<=200000`**. An integer-only verifier checks for every row:

- `1<=a<b` and `a+b=s<=200000`;
- `gcd(a,b)=1`;
- `σ(a)+σ(b)=σ(s)`;
- the stored product `M=abs`;
- the exact Euler-phi value;
- coefficient numerator and denominator;
- the downward-rounded `10^12` coefficient contribution.

The verifier was rerun during this public extraction and returned:

```text
PASS
rows=152803
floor_sum=2295492576177
rigorous_coefficient_lower_bound=2295492576177/1000000000000=2.295492576177
csv_sha256=343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68
```

Hence, under the ordered-pair convention used by the campaign,

\[
\boxed{\liminf_{x\to\infty}\frac{S(x)}x\ge2.295492576177.}
\]

`ERDOS1061_SEED_CERT_VERIFY.py` is the exact recovered verifier. The original certificate is a
17,026,297-byte CSV. The current GitHub connector cannot stream that 17 MB Library artifact into a
repository write, so this public extraction pins its exact SHA-256 and verifier rather than
pretending the large payload was copied when it was not.

## Aliquot-square search certificate

A second exact search through

\[
a\le5,000,000
\]

found **43 generator seeds**, **37 new relative to the `a+b<=200000` base bank**. Its recovered
verifier checks primality, factorization, `σ`, `φ`, gcd, the seed identity and ray coefficient.
Combining those exact contributions with the base certificate gives the rigorous recorded floor

\[
\boxed{\liminf_{x\to\infty}\frac{S(x)}x>2.295497372037.}
\]

Both exact verifiers were rerun in the September canonicalization and recorded `PASS`.

## Mersenne-power specialization

Taking `a=2^m` gives

\[
q=\sigma(2^m)-2^m=2^m-1
\]

and

\[
b=q^2-a=2^{2m}-3\cdot2^m+1.
\]

Therefore

\[
\boxed{
2^m-1\text{ prime and }2^{2m}-3\cdot2^m+1\text{ prime}
\Longrightarrow
(2^m,b)\text{ is a primitive generator seed}.}
\]

The recovered generator certificate contains these exact power-of-two rows:

| m | a | q | b |
|---:|---:|---:|---:|
| 2 | 4 | 3 | 5 |
| 3 | 8 | 7 | 41 |
| 5 | 32 | 31 | 929 |
| 7 | 128 | 127 | 16001 |
| 13 | 8192 | 8191 | 67084289 |
| 19 | 524288 | 524287 | 274876334081 |

No infinitude of such exponents is claimed.

## Novelty boundary

The September prior-art audit found no exact prior occurrence of the aliquot-square generator formula
in its targeted search, while also finding stronger 2026 work on the parent problem by a different
construction. The safe status is therefore:

- universal generator: **no exact prior located in targeted search**;
- 152,803-row and 43-row certificates: **apparently new computational artifacts**;
- historical priority: **not certified globally**;
- parent problem: **not claimed solved here**.

## Reproduce the base certificate check

Place the recovered CSV beside the verifier as
`ERDOS1061_PRIMITIVE_SEEDS_200K.csv`, then run:

```bash
python ERDOS1061_SEED_CERT_VERIFY.py
```

The exact expected SHA-256 and output are pinned in `CERTIFICATE-RECEIPT.md`.

## License

Apache-2.0 for repository-authored material.
