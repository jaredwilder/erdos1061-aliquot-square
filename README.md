# Erdős #1061 — sigma / aliquot-square program

**Author:** Jared Wilder  
**Estate status:** exact construction / primitive-ray / certificate / lower-bound program.  
**Parent-problem status:** a June 24, 2026 preprint by Eric Li, *A resolution of Erdős Problem 1061 on the sum-of-divisors function* (arXiv:2606.25849), explicitly claims a resolution of the parent problem. This repository does **not** claim priority over that result and has not independently replayed Li's full proof.

This repository is the canonical public home for the estate's #1061 mathematics. The program goes well beyond the compact `(a,2a)` family: it includes a primitive-seed generator for aliquot-square solutions, primitive-ray scaling, exact asymptotic contribution formulas, a large seed certificate bank and verifier, a second exact search, released lower-bound coefficient work, and Mersenne-power specializations.

## Current external status

Li's preprint defines

```text
S(x) = #{(a,b) in N^2 : a+b <= x and sigma(a)+sigma(b)=sigma(a+b)}
```

and states that for every fixed `R>0`,

```text
S(x) / (x (log x)^R) -> +infinity.
```

That is the opposite of the historical linear-asymptotic question `S(x) ~ c x`. As of 2026-09-14 the Erdős Problems registry may still display stale/open metadata; this repository therefore distinguishes the registry label from the existence of the 2026 claimed resolution.

## Exact certificate recovery

The historical `ERDOS1061_PRIMITIVE_SEEDS_200K.csv` has now been recovered from the estate under its exact filename and independently rechecked on 2026-09-14:

- bytes: **17,026,297**;
- rows: **152,803**;
- SHA-256: `343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68`;
- verifier result: **PASS**;
- exact floor sum: `2295492576177`;
- rigorous estate coefficient lower bound: `2.295492576177` under the campaign's ordered-pair convention.

The recovered payload is not yet branch-visible because the current connected GitHub write path cannot transport a 17 MB local file object without serializing its full contents through the tool interface. The recovery debt is therefore now **transport-only**, not source-recovery or verification debt. See `CERTIFICATE-RECOVERY.md`.

## Evidence lanes

The repository keeps theorem statements, exact finite searches, certificate-backed counts, lower-bound derivations, source provenance, and external-priority questions distinct. The 152,803-seed certificate is a finite computational artifact supporting the estate's ray lower bound; it is not the source of Li's much stronger 2026 parent-problem result.

## Source layout

- `sigma-family/` — main #1061 extraction;
- `rays/` — primitive-ray and asymptotic work;
- `ore-findings/` — released #1061 findings from the ore audit;
- `CERTIFICATE-RECOVERY.md` — exact identity and transport state of the recovered 17 MB certificate.
