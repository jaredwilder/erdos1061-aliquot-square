# Erdős #1061 — Aliquot-Square Constructions

**Jared Wilder**

Explicit constructions, primitive-ray structure, certificates, and lower bounds for Erdős Problem #1061 on the sum-of-divisors function.

The project develops a substantial family of exact solutions beyond the elementary `(a, 2a)` construction. Its main assets are a primitive-seed generator, scaling along primitive rays, exact asymptotic contribution formulas, a large verified seed bank, an independent search, and Mersenne-power specializations.

## Main computational artifact

A recovered certificate contains **152,803 primitive seeds**:

- file: `ERDOS1061_PRIMITIVE_SEEDS_200K.csv`
- bytes: **17,026,297**
- SHA-256: `343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68`
- verifier: **PASS**
- exact floor sum: `2295492576177`
- resulting estate coefficient lower bound: **2.295492576177** under the campaign’s ordered-pair convention

The certificate has been independently rechecked. `CERTIFICATE-RECOVERY.md` records its recovery and transport status.

## Repository map

- `sigma-family/` — core #1061 constructions and identities
- `rays/` — primitive-ray and asymptotic analysis
- `ore-findings/` — released findings from the wider mathematics audit
- `CERTIFICATE-RECOVERY.md` — exact certificate identity and verification record

## External status

A June 2026 preprint by Eric Li, *A resolution of Erdős Problem 1061 on the sum-of-divisors function* (arXiv:2606.25849), states a stronger asymptotic result for the parent problem. This repository preserves Wilder’s independent construction, certificate, and lower-bound program as a separate body of work.

## Verification philosophy

Exact searches, certificate-backed counts, theorem statements, and literature claims are kept as distinct evidence types. The strongest claims in this repository are the ones backed by explicit derivation or reproducible certificates.