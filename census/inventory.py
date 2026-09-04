"""Canonical portfolio inventory for beyond-repair (snapshot 2026-09-04)."""
from __future__ import annotations
from typing import TypedDict

class RepoRecord(TypedDict):
    name: str
    cluster: str
    lifecycle: str
    claim: int
    language: str
    functions: list[str]
    gaps: list[str]

CLUSTERS = (
    "governance",
    "cognitive-substrate",
    "integrity",
    "agent-runtime",
    "physics-cft",
    "simulation-games",
    "security-ops",
    "markets",
    "health",
    "legacy",
)

LIFECYCLES = (
    "ACTIVE",
    "RESEARCH",
    "FROZEN",
    "SUPERSEDED",
    "ARCHIVED",
    "EXPERIMENTAL",
)

INVENTORY: list[RepoRecord] = [
    {"name": "ADL-Governance", "cluster": "governance", "lifecycle": "ACTIVE", "claim": 4, "language": "docs", "functions": ["portfolio constitution", "lifecycle classification", "claim validation 0-5", "SCAN/FORK/SPIKE/ANCHOR/ESCAPE vocabulary"], "gaps": ["no executable census until ADL-Portfolio-Census"]},
    {"name": "ADL-SEEM", "cluster": "governance", "lifecycle": "ACTIVE", "claim": 4, "language": "docs", "functions": ["SEEM response contract v3.0", "cognition claim caps", "canonical pointer to sovereign-clean-room"], "gaps": ["not an executable verifier"]},
    {"name": "sunder", "cluster": "agent-runtime", "lifecycle": "EXPERIMENTAL", "claim": 1, "language": "Python", "functions": ["local-first coding agent", "hyperspherical VSA memory", "constitutional gates", "SCAN SNAP SUNDER loop"], "gaps": ["not wired to forge-aegis proofs", "not registered in a live census"]},
    {"name": "forge-aegis", "cluster": "integrity", "lifecycle": "ACTIVE", "claim": 3, "language": "Python", "functions": ["FLS ontology", "Artifact Graph identity/revision/relationship", "offline host+policy pipeline", "deterministic result_hash"], "gaps": ["no portfolio-wide artifact graph of repos themselves"]},
    {"name": "sovereign-clean-room", "cluster": "cognitive-substrate", "lifecycle": "ACTIVE", "claim": 3, "language": "Python", "functions": ["FHRR VSA engine", "BaNEL", "invertibility gate", "Ed25519 + SHACL skill gates", "offline twin substrate"], "gaps": ["no census export of skills as FLS artifacts"]},
    {"name": "Sovereign-OS", "cluster": "governance", "lifecycle": "RESEARCH", "claim": 1, "language": "docs", "functions": ["constitutional OS concept", "human/company/capital uptime", "default-to-refusal"], "gaps": ["no runtime implementation"]},
    {"name": "SovereignOS", "cluster": "governance", "lifecycle": "SUPERSEDED", "claim": 0, "language": "unknown", "functions": ["earlier SovereignOS naming"], "gaps": ["superseded by Sovereign-OS"]},
    {"name": "SEEM-2.0-Self-Evolving-Emergent-Mind", "cluster": "cognitive-substrate", "lifecycle": "SUPERSEDED", "claim": 1, "language": "Python", "functions": ["offline symbolic AGI-seed claims", "dream-phase metabolism"], "gaps": ["canonical runtime is sovereign-clean-room"]},
    {"name": "SEEM-Cognitive_Microservice", "cluster": "cognitive-substrate", "lifecycle": "SUPERSEDED", "claim": 1, "language": "Python", "functions": ["SEEM 2.0 microservice kernel"], "gaps": ["duplicate of hyphenated sibling"]},
    {"name": "SEEM-Cognitive-Microservice", "cluster": "cognitive-substrate", "lifecycle": "SUPERSEDED", "claim": 1, "language": "Python", "functions": ["SEEM 2.0 microservice kernel"], "gaps": ["duplicate naming"]},
    {"name": "Digital_Double_virtual_workforce", "cluster": "agent-runtime", "lifecycle": "RESEARCH", "claim": 1, "language": "TypeScript", "functions": ["virtual workforce agents"], "gaps": ["description says Python module; language is TypeScript"]},
    {"name": "Digital_Double_Virtual_Workforce_4.", "cluster": "agent-runtime", "lifecycle": "ARCHIVED", "claim": 0, "language": "unknown", "functions": ["earlier workforce iteration"], "gaps": ["empty description"]},
    {"name": "Gia---General-Intelligence-Assistant", "cluster": "agent-runtime", "lifecycle": "ARCHIVED", "claim": 1, "language": "Python", "functions": ["local models", "dynamic tool creation"], "gaps": ["superseded conceptually by sunder + clean-room"]},
    {"name": "coherence-drive", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 2, "language": "docs", "functions": ["master integration of Coherence Drive findings"], "gaps": ["experimental physics; not product"]},
    {"name": "stress-tensor-modification", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 2, "language": "Python", "functions": ["modified Maxwell stress tensor", "Ware constant injection"], "gaps": ["needs independent experimental replication"]},
    {"name": "momentum-closure", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 2, "language": "docs", "functions": ["surface integral + Poynting flux closure"], "gaps": ["proof status is claim-level 2 not 5"]},
    {"name": "ware-constant-phenomenology", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 2, "language": "Python", "functions": ["W ≈ 0.08 coupling study"], "gaps": ["phenomenology not derivation"]},
    {"name": "sierpinski-geometry-045", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 2, "language": "Python", "functions": ["0.45-scaled Sierpinski tetrahedron hardware geometry"], "gaps": ["hardware not fabricated in-repo"]},
    {"name": "CFT-v3.1", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 2, "language": "TeX", "functions": ["CFT white paper", "screened metric vs dark matter"], "gaps": ["not an engine"]},
    {"name": "CFT-v3.0", "cluster": "physics-cft", "lifecycle": "SUPERSEDED", "claim": 1, "language": "Python", "functions": ["volumetric metric solution draft"], "gaps": ["superseded by CFT-v3.1"]},
    {"name": "The-Origin-Point-Hypothesis.", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 1, "language": "TeX", "functions": ["origin-point hypothesis paper"], "gaps": ["empty public description"]},
    {"name": "-Entanglement-and-Emergence", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 1, "language": "docs", "functions": ["emergent gravity from entanglement sketch"], "gaps": ["not connected to CFT master"]},
    {"name": "optimization-limit-conjecture", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 2, "language": "Python", "functions": ["obstruction floors in constrained graphs"], "gaps": ["conjecture not theorem"]},
    {"name": "-text-informational-fork-protocol-", "cluster": "physics-cft", "lifecycle": "RESEARCH", "claim": 1, "language": "Python", "functions": ["informational non-locality protocol"], "gaps": ["naming hygiene", "not wired to census"]},
    {"name": "Project-Cold-Boot", "cluster": "simulation-games", "lifecycle": "ACTIVE", "claim": 2, "language": "GDScript", "functions": ["DLRSE simulation engine", "dual-layer 1994/2026 city", "SCAN SNAP SUNDER gameplay"], "gaps": ["game loop not proven against clean-room gates"]},
    {"name": "blacksite", "cluster": "simulation-games", "lifecycle": "EXPERIMENTAL", "claim": 2, "language": "JavaScript", "functions": ["PvE roguelite", "five operators", "shared facility sim"], "gaps": ["private; no public CI contract"]},
    {"name": "BlockSwarm", "cluster": "markets", "lifecycle": "EXPERIMENTAL", "claim": 0, "language": "Solidity", "functions": ["on-chain swarm contracts (undescribed)"], "gaps": ["empty description"]},
    {"name": "ExoAxis-1", "cluster": "health", "lifecycle": "RESEARCH", "claim": 1, "language": "docs", "functions": ["network pharmacology for longevity/sleep/stress"], "gaps": ["no clinical evidence in-repo"]},
    {"name": "VigilE.S.A.-Enhanced-Security", "cluster": "security-ops", "lifecycle": "RESEARCH", "claim": 1, "language": "Rust", "functions": ["zero trust sketch", "eBPF / enclave / HSM claims", "Wasm plugins"], "gaps": ["scope exceeds demonstrated code; claim must stay ≤1"]},
    {"name": "FortiTrade_Multi-Strategy", "cluster": "markets", "lifecycle": "ARCHIVED", "claim": 0, "language": "Python", "functions": ["multi-strategy trading"], "gaps": ["no description"]},
    {"name": "btc-trading", "cluster": "markets", "lifecycle": "ARCHIVED", "claim": 0, "language": "Python", "functions": ["btc trading scripts"], "gaps": ["no description"]},
    {"name": "fantom-smart-contracts-first-bot", "cluster": "markets", "lifecycle": "ARCHIVED", "claim": 0, "language": "Rust", "functions": ["FTM contract bot"], "gaps": ["no description"]},
    {"name": "ftmA.I.bot", "cluster": "markets", "lifecycle": "ARCHIVED", "claim": 0, "language": "Python", "functions": ["FTM AI bot"], "gaps": ["no description"]},
    {"name": "quantum_A.I._optimization.py", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "Python", "functions": ["quantum circuit + AI agent sketch"], "gaps": ["filename-as-repo"]},
    {"name": "Quantumclustering", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "unknown", "functions": ["placeholder"], "gaps": ["description is 't'"]},
    {"name": "Code_Generation_AI_Program", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "unknown", "functions": ["code generation sketch"], "gaps": ["empty"]},
    {"name": "automate_passive_income", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "unknown", "functions": ["income automation sketch"], "gaps": ["empty"]},
    {"name": "My-mind-A.I.", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "Python", "functions": ["early personal AI"], "gaps": ["superseded by SEEM lineage"]},
    {"name": "new-program-1.01", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "Python", "functions": ["My Mind A.I. successor name"], "gaps": ["naming drift"]},
    {"name": "-Py2APK-main", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "Python", "functions": ["apk packaging utility"], "gaps": ["fork hygiene"]},
    {"name": "test", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "unknown", "functions": ["sandbox"], "gaps": ["should stay private/archived"]},
    {"name": "potential-garbanzo", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 0, "language": "unknown", "functions": ["ai agent placeholder"], "gaps": ["github default name"]},
]

COMPATIBLE_BUILDS: list[dict] = [
    {"name": "ADL-Portfolio-Census", "why": "Governance SCAN/FORK/ANCHOR has no executable implementation.", "compatible_with": ["ADL-Governance", "ADL-SEEM", "forge-aegis", "sovereign-clean-room", "sunder"], "status": "this_repository"},
    {"name": "aegis-repo-graph", "why": "forge-aegis models endpoint artifacts; repos themselves are not yet an Artifact Graph.", "compatible_with": ["forge-aegis", "ADL-Portfolio-Census"], "status": "not_built"},
    {"name": "sunder-aegis-bridge", "why": "sunder gates are local; AEGIS result_hash is not consumed as a merge gate.", "compatible_with": ["sunder", "forge-aegis"], "status": "not_built"},
    {"name": "clean-room-skill-export", "why": "clean-room skills are not exported as signed FLS artifacts.", "compatible_with": ["sovereign-clean-room", "forge-aegis"], "status": "not_built"},
]
