
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class HLAService:
    """
    HLA/MHC Genetic Compatibility Service.

    Based on research showing MHC dissimilarity correlates with:
    - Body odor attraction (Wedekind et al., 1995)
    - Sexual satisfaction (Garver-Apgar et al., 2006)
    - Partnership quality (Kromer et al., 2016)

    References:
    - https://www.nature.com/articles/srep32550
    - https://pmc.ncbi.nlm.nih.gov/articles/PMC5006172/
    - IPD-IMGT/HLA Database: https://www.ebi.ac.uk/ipd/imgt/hla/

    Key HLA Loci (Class I - most important for mate choice):
    - HLA-A, HLA-B, HLA-C

    Key HLA Loci (Class II):
    - HLA-DRB1, HLA-DQB1, HLA-DPB1
    """

    # Class I has stronger effect on mate preference
    LOCUS_WEIGHTS = {
        'HLA-A': 1.0,
        'HLA-B': 1.5,   # Most important per research
        'HLA-C': 1.2,
        'HLA-DRB1': 0.6,
        'HLA-DQB1': 0.5,
        'HLA-DPB1': 0.4
    }

    def __init__(self):
        logger.info("HLAService initialized")

    def parse_hla_input(self, hla_string: str) -> Dict[str, List[str]]:
        """
        Parse HLA alleles from various input formats.

        Supports:
        - "HLA-A*02:01, HLA-B*07:02" format
        - "A*02:01 B*07:02" format
        - MyHeritage/23andMe export format
        """
        alleles = {locus: [] for locus in self.LOCUS_WEIGHTS}

        if not hla_string or hla_string.strip() == "":
            return alleles

        # Clean and split
        parts = hla_string.upper().replace(',', ' ').replace(';', ' ').split()

        for part in parts:
            part = part.strip()
            if not part:
                continue

            # Handle "HLA-A*02:01" or "A*02:01" format
            for locus in self.LOCUS_WEIGHTS:
                short_locus = locus.replace('HLA-', '')
                if part.startswith(locus) or part.startswith(short_locus):
                    # Extract allele
                    if '*' in part:
                        allele = part.split('*')[1]
                        alleles[locus].append(allele)
                    break

        return alleles

    def calculate_dissimilarity(self, alleles_a: Dict[str, List[str]],
                                 alleles_b: Dict[str, List[str]]) -> dict:
        """
        Calculate HLA dissimilarity score.

        Higher dissimilarity = Higher genetic compatibility
        (MHC-dissimilar partners report higher attraction and satisfaction)
        """
        total_dissimilarity = 0
        total_weight = 0
        breakdown = {}

        for locus, weight in self.LOCUS_WEIGHTS.items():
            set_a = set(alleles_a.get(locus, []))
            set_b = set(alleles_b.get(locus, []))

            if not set_a or not set_b:
                # No data for this locus
                breakdown[locus] = {"status": "no_data", "dissimilarity": None}
                continue

            # Calculate Jaccard dissimilarity
            intersection = len(set_a & set_b)
            union = len(set_a | set_b)

            if union > 0:
                similarity = intersection / union
                dissimilarity = 1 - similarity
            else:
                dissimilarity = 1.0  # Completely different

            weighted_dissim = dissimilarity * weight
            total_dissimilarity += weighted_dissim
            total_weight += weight

            breakdown[locus] = {
                "alleles_a": list(set_a),
                "alleles_b": list(set_b),
                "shared": list(set_a & set_b),
                "dissimilarity": round(dissimilarity, 3),
                "weighted_contribution": round(weighted_dissim, 3)
            }

        if total_weight > 0:
            final_score = (total_dissimilarity / total_weight) * 100
        else:
            final_score = 50  # Neutral if no data

        return {
            "compatibility_score": round(final_score, 1),
            "interpretation": self._interpret_score(final_score),
            "breakdown": breakdown
        }

    def _interpret_score(self, score: float) -> str:
        """Interpret the HLA compatibility score."""
        if score >= 80:
            return "Excellent genetic diversity - strong potential for natural chemistry"
        elif score >= 60:
            return "Good genetic diversity - likely positive olfactory attraction"
        elif score >= 40:
            return "Moderate genetic overlap - neutral chemistry baseline"
        else:
            return "High genetic similarity - chemistry may develop through other factors"

    def get_default_score(self) -> dict:
        """Return default score when no HLA data provided."""
        return {
            "compatibility_score": 50.0,
            "interpretation": "No genetic data provided - using neutral baseline",
            "breakdown": {}
        }
