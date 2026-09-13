# Erdős #1061 — aliquot-square primitive rays and exact certificate estate

**Author:** Jared Wilder  
**Public extraction:** 2026-09-11  
**Status:** exact standalone construction + independently checkable lower-bound certificate; not a claim to resolve the 2026 parent frontier

Let `sigma(n)` denote the sum of positive divisors of `n`. Erdős #1061 studies ordered positive pairs satisfying

`σ(a)+σ(b)=σ(a+b)`

and their counting function `S(x)` for `a+b<=x`.

This packet records two things recovered from the estate: an explicit primitive-seed generator and a large exact bank of disjoint multiplier rays.

## 1. Aliquot-square primitive-seed generator

Put

`q = σ(a)-a`

and

`b = q^2-a`.

If

- `q` is prime,
- `q` does not divide `a`, and
- `b>0` is prime,

then `(a,b)` is a primitive solution of

`σ(a)+σ(b)=σ(a+b)`.

### Proof

By definition, `σ(a)=a+q`. Since `b` is prime, `σ(b)=b+1`. Also `a+b=q^2`, and since `q` is prime,

`σ(q^2)=q^2+q+1`.

Therefore

`σ(a)+σ(b)=(a+q)+(b+1)=q^2+q+1=σ(q^2)=σ(a+b)`.

Moreover

`gcd(a,b)=gcd(a,q^2-a)=gcd(a,q^2)=1`

because `q` does not divide `a`. Thus the seed is primitive.

A conditional power-of-two subfamily is obtained from

`a=2^m`, `q=2^m-1`, `b=(2^m-1)^2-2^m`

whenever the two required primality conditions hold. The archived exact search found successful exponents including `m=2,3,5,7,13,19`.

One explicit large seed is

`(a,b)=(524288,274876334081)`

with

`a+b=274876858369`.

## 2. Primitive-ray scaling theorem

Let `(a,b)` be a primitive solution with `a<b`, put `s=a+b`, and put

`M=ab(a+b)`.

If `gcd(k,M)=1`, then

`(ka,kb)` and `(kb,ka)`

are again solutions.

Indeed `k` is coprime to each of `a`, `b`, and `s`, so multiplicativity of `σ` gives

`σ(ka)+σ(kb)=σ(k)(σ(a)+σ(b))=σ(k)σ(s)=σ(ks)`.

Distinct primitive seeds with `a<b` generate disjoint ordered rays because the reduced ratio `a:b` is recoverable from any point on a ray.

The asymptotic density contribution of one primitive seed is therefore

`c(a,b)=2 φ(M)/(M(a+b))`.

## 3. 152,803-row exact primitive bank

The recovered certificate file

`ERDOS1061_PRIMITIVE_SEEDS_200K.csv`

contains **152,803 primitive seeds** with `a+b<=200000`.

Its exact byte identity is

- bytes: `17,026,297`
- SHA-256: `343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68`

For every row the release verifier checks, using integer arithmetic only:

- `1<=a<b`;
- `gcd(a,b)=1`;
- `s=a+b<=200000`;
- the three divisor sums;
- `σ(a)+σ(b)=σ(s)`;
- `M=ab s`;
- `φ(M)` via pairwise coprimality of `a,b,s`;
- the exact ray coefficient numerator and denominator;
- the downward-rounded `10^12` coefficient contribution;
- uniqueness of the listed primitive pair.

The verifier rerun on release day returns

```text
PASS
rows=152803
floor_sum=2295492576177
scale=1000000000000
rigorous_base_lower_bound>=2295492576177/1000000000000
```

Hence these listed disjoint rays alone prove

`liminf S(x)/x >= 2.295492576177`.

This lower bound does **not** require the bank to be exhaustive: validity and disjointness of the listed primitive rays suffice.

## 4. Pass-4 aliquot-square upgrade

A separate archived generator pass searched `a<=5,000,000` using the theorem in §1 and produced **43 generator seeds**, 37 outside the `a+b<=200000` bank. Its exact archived receipt reports an additional coefficient of approximately

`4.79586024178362e-6`

and the rigorous combined floor

`liminf S(x)/x > 2.295497372037`.

The exact receipt SHA-256 is

`249e5904035f5df3fcacbf4746ed36be13fd1eb48a3cc3179ba00137c43fc686`.

The 43-row generator payload is being mirrored separately; the stronger decimal is stated here only with its archived exact receipt identity, not as a substitute for the payload.

## 5. Novelty / frontier boundary

The September audit classified the aliquot-square generator as a plausible-original explicit construction after targeted searches failed to locate the same formula, and the 152,803-row bank as an apparently new exact computational artifact. That is a **targeted-search assessment**, not a global historical-priority certificate.

More importantly, stronger 2026 work on the parent problem reportedly gives superlinear growth far beyond this linear lower bound. Therefore this packet is presented as a standalone explicit construction and reproducible certificate estate, **not** as the current resolution or best asymptotic result for Erdős #1061.

## Reproduction

Run

```bash
python verify_base_certificate.py ERDOS1061_PRIMITIVE_SEEDS_200K.csv
```

against the exact CSV bytes named above.

The large CSV payload is tracked by the hash above while byte transport to the public repository is completed; the verifier and theorem packet are public immediately so the mathematics is not buried again.
