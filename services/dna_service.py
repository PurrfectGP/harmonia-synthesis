
import csv
import io
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class DNAService:
    HLA_SNPS = {
        "rs2523393": "HLA-A", "rs2844821": "HLA-A", "rs3823342": "HLA-A",
        "rs2523442": "HLA-B", "rs2596542": "HLA-B", "rs3134792": "HLA-B",
        "rs2524074": "HLA-C", "rs3130867": "HLA-C", "rs9264942": "HLA-C",
        "rs9271366": "HLA-DRB1", "rs6457617": "HLA-DRB1",
        "rs2647050": "HLA-DQB1", "rs9275596": "HLA-DQB1",
        "rs9277535": "HLA-DPB1", "rs3077": "HLA-DPB1"
    }

    GENOTYPE_MAPPINGS = {
        "rs2523393": {"AA": "01", "AG": "02", "GG": "03"},
        "rs2596542": {"TT": "07", "TC": "08", "CC": "15"},
        "rs9264942": {"CC": "04", "CT": "07", "TT": "08"},
    }

    def __init__(self):
        logger.info("DNAService initialized")

    def parse_csv(self, csv_content: str) -> Dict[str, List[str]]:
        logger.info("Parsing DNA CSV file...")
        hla_results = {"HLA-A": [], "HLA-B": [], "HLA-C": [], "HLA-DRB1": [], "HLA-DQB1": [], "HLA-DPB1": []}

        try:
            reader = csv.reader(io.StringIO(csv_content))
            for row in reader:
                if not row or row[0].startswith('#'):
                    continue
                if len(row) >= 4 and row[0].startswith('rs'):
                    rsid = row[0].strip()
                    genotype = row[3].strip().upper() if len(row) == 4 else (row[3]+row[4]).strip().upper()
                    if rsid in self.HLA_SNPS and genotype:
                        locus = self.HLA_SNPS[rsid]
                        if rsid in self.GENOTYPE_MAPPINGS and genotype in self.GENOTYPE_MAPPINGS[rsid]:
                            allele = self.GENOTYPE_MAPPINGS[rsid][genotype]
                            if allele not in hla_results[locus]:
                                hla_results[locus].append(allele)
        except Exception as e:
            logger.error(f"DNA parsing error: {e}")
        return hla_results

    def format_for_display(self, hla_data: Dict[str, List[str]]) -> str:
        parts = [f"{locus}*{a}" for locus, alleles in hla_data.items() for a in alleles]
        return ", ".join(parts) if parts else "No HLA data extracted"

    def estimate_diversity_score(self, hla_data: Dict[str, List[str]]) -> float:
        total = sum(len(a) for a in hla_data.values())
        return min(100, (total / 12) * 100) if total else 50.0
