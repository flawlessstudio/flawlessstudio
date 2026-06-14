from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
OFFER = ROOT / "offers" / "ai-product-systems-audit-sprint.md"
INDEX = ROOT / "offers" / "README.md"
PROFILE = ROOT / "README.md"

REQUIRED_HEADINGS = [
    "# AI Product & Systems Audit Sprint",
    "## The problem this solves",
    "## The outcome",
    "## Deliverables",
    "## Method",
    "## Process",
    "## Required inputs",
    "## Boundaries",
    "## Best fit",
    "## Engagement and contact",
]

FORBIDDEN_MARKERS = ["TODO", "TBD", "FIXME", "lorem ipsum", "insert price", "coming soon"]
OFFER_PATH = "offers/ai-product-systems-audit-sprint.md"
EMAIL = "oneflawlessstudio@gmail.com"


def main():
    errors = []
    for path in (OFFER, INDEX, PROFILE):
        if not path.is_file():
            errors.append(f"missing file: {path.relative_to(ROOT)}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1

    offer = OFFER.read_text(encoding="utf-8")
    index = INDEX.read_text(encoding="utf-8")
    profile = PROFILE.read_text(encoding="utf-8")

    for heading in REQUIRED_HEADINGS:
        if heading not in offer:
            errors.append(f"missing offer heading: {heading}")

    lower_offer = offer.lower()
    for marker in FORBIDDEN_MARKERS:
        if marker.lower() in lower_offer:
            errors.append(f"forbidden placeholder: {marker}")

    if EMAIL not in offer or EMAIL not in profile:
        errors.append("contact email is not connected across offer and profile")

    if "./ai-product-systems-audit-sprint.md" not in index:
        errors.append("offer index does not link to the canonical offer")

    if "./offers/ai-product-systems-audit-sprint.md" not in profile:
        errors.append("profile does not link to the canonical offer")

    if "guarantees of revenue" not in lower_offer:
        errors.append("offer does not state outcome-guarantee boundaries")

    if "commercial terms" not in lower_offer:
        errors.append("offer does not define the commercial agreement boundary")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1

    print("Commercial offer structure and publication links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
