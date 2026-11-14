# Software Supply-Chain Security: Generate and Read an SBOM with Syft

**Code Therapist Knowledge Hub | 14 November 2026 | DevOps & Cybersecurity | Original educational guide**

> An SBOM (software bill of materials) is an inventory of components found in software. It helps you ask *what is included?* It is **not** proof that software is safe and is not, by itself, a vulnerability scan.

## Why developers should care

A project may depend on packages that its author never imported directly. Containers add operating-system packages and libraries. An inventory can support incident response, license review, dependency maintenance and investigations when a vulnerable component is announced. Inventories may be incomplete; always record the source and scan scope.

## Meet Syft

[Anchore Syft](https://github.com/anchore/syft) is an open-source command-line tool and Go library for generating SBOMs from container images, directories and other supported sources. Its documented output formats include CycloneDX JSON, SPDX JSON and Syft JSON. For vulnerability matching, Anchore documents a separate scanner, [Grype](https://github.com/anchore/grype).

## Safe practice lab (Linux, including Kali)

**Prerequisites:** An authorized local sample project; Syft installed using the method documented in its official repository; a terminal. Check the downloaded binary's authenticity and your organization's installation policy. Avoid piping unreviewed installation scripts directly to a privileged shell.

1. Verify installation:

```bash
syft version
```

2. Make a disposable directory with a Python dependency manifest:

```bash
mkdir -p /tmp/ct-sbom-lab
cd /tmp/ct-sbom-lab
printf 'requests==2.32.3\n' > requirements.txt
```

3. Generate a human-readable package inventory from the directory:

```bash
syft dir:. 
```

4. Export a machine-readable SBOM:

```bash
syft dir:. -o cyclonedx-json=sbom.cdx.json
```

5. Inspect its shape without assuming a package was detected:

```bash
python - <<'PY'
import json
from pathlib import Path
data = json.loads(Path("sbom.cdx.json").read_text())
print("SBOM format:", data.get("bomFormat"))
print("Components found:", len(data.get("components", [])))
for item in data.get("components", [])[:10]:
    print(item.get("name"), item.get("version"))
PY
```

**Important:** A requirements file is a declaration, not evidence that a dependency is installed. Syft's package detection varies by ecosystem and artifacts present. For a richer inventory, scan a built container image or an environment containing installed packages. Use a pinned, approved image digest for reproducible team exercises; do not assume that a mutable `latest` tag is fixed.

Example for an image you own or are authorized to inspect:

```bash
syft my-image:my-tag -o spdx-json=sbom.spdx.json
```

## Read and interpret the result

Look for the component name, version, ecosystem/package URL (if available), and relationships or source metadata. Ask whether the inventory reflects the application dependencies, operating-system packages, or both. Compare the result with lockfiles and your build manifest. Missing components are a reason to investigate, not proof of absence.

## SBOM versus vulnerability scanning

- **Syft:** inventories discovered software components.
- **Grype:** matches discovered packages against vulnerability information.
- **Manual review:** checks exploitability, configuration, exposure and whether the advisory applies to your environment.

A package listed in an SBOM is not automatically vulnerable. An empty vulnerability report is not a guarantee of safety.

## Five practical exercises

1. Explain the difference between a dependency manifest and an SBOM.
2. Generate CycloneDX and SPDX JSON for the same authorized target.
3. Count the components reported in each output.
4. Explain how a changing container tag can affect reproducibility.
5. Write a response plan for a newly announced vulnerable dependency: identify affected assets, verify applicability, upgrade, test and regenerate the SBOM.

## Editorial checklist

- Never publish private image names, internal paths, access tokens or proprietary dependency inventories.
- Cite official maintainers; keep source dates distinct from this article's publication date.
- Review package and asset licenses before copying code or images.
- Re-run commands against the installed Syft version because flags and supported formats can change.

## Primary sources and rights

- Anchore, **Syft official repository and usage documentation** (consulted 14 November 2026): https://github.com/anchore/syft
- Anchore, **Grype vulnerability scanner** (consulted 14 November 2026): https://github.com/anchore/grype
- CycloneDX specification: https://github.com/CycloneDX/specification
- SPDX specification: https://spdx.dev/use/specifications/

**Rights:** Explanations, examples and exercises here were independently authored for Code Therapist. External repositories and specifications are linked, not reproduced. Check each project's current license before reusing its code or artwork.

[← DevOps category](./README.md) · [← Knowledge Hub](../../README.md)
