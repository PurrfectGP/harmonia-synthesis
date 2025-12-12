import logging
import re

logger = logging.getLogger(__name__)

class HLAService:
    """Calculate HLA genetic compatibility using chromosome 6 SNP data."""
    
    # HLA region on chromosome 6: approximately 29-33.5 megabases (Build 37/GRCh37)
    HLA_REGION_START = 29000000
    HLA_REGION_END = 33500000
    
    # Locus approximate positions (Build 37)
    LOCUS_RANGES = {
        'HLA-A': (29900000, 30000000),
        'HLA-C': (31200000, 31300000),
        'HLA-B': (31300000, 31450000),
        'HLA-DRB1': (32500000, 32650000),
        'HLA-DQA1': (32600000, 32700000),
        'HLA-DQB1': (32700000, 32800000)
    }
    
    def parse_hla_input(self, hla_data: str) -> dict:
        """Parse HLA data from CSV or manual input."""
        logger.info("🧬 Parsing HLA data...")
        
        if not hla_data or len(hla_data.strip()) < 10:
            logger.warning("⚠️ No HLA data provided")
            return {}
        
        # Detect format: CSV (has tabs/commas + chromosome data) vs Manual (HLA-A*02:01 format)
        if '\t' in hla_data or ('6' in hla_data and 'rs' in hla_data):
            return self._parse_csv_format(hla_data)
        else:
            return self._parse_manual_input(hla_data)
    
    def _parse_csv_format(self, csv_data: str) -> dict:
        """Extract chromosome 6 SNPs from CSV (23andMe, Ancestry, MyHeritage)."""
        hla_snps = {}
        lines = csv_data.strip().split('\n')
        
        for line in lines:
            # Skip comments
            if line.startswith('#'):
                continue
            
            # Parse tab or comma delimited
            if '\t' in line:
                parts = line.split('\t')
            else:
                parts = line.split(',')
            
            if len(parts) < 4:
                continue
            
            try:
                rsid = parts[0].strip()
                chrom = parts[1].strip()
                position = int(parts[2].strip())
                genotype = parts[3].strip()
                
                # Filter: Only chromosome 6 in HLA region
                if chrom == '6' and self.HLA_REGION_START <= position <= self.HLA_REGION_END:
                    hla_snps[rsid] = {
                        'position': position,
                        'genotype': genotype,
                        'locus': self._position_to_locus(position)
                    }
                    
            except (ValueError, IndexError):
                continue
        
        logger.info(f"✅ Extracted {len(hla_snps)} HLA-region SNPs from chromosome 6")
        return hla_snps
    
    def _parse_manual_input(self, manual_text: str) -> dict:
        """Parse manually typed HLA alleles: HLA-A*02:01, HLA-B*44:03, etc."""
        hla_alleles = {}
        
        # Pattern: HLA-[LOCUS]*[DIGITS]:[DIGITS]
        pattern = r'HLA-([A-Z0-9]+)\*([0-9]+):([0-9]+)'
        matches = re.findall(pattern, manual_text, re.IGNORECASE)
        
        for locus, allele_group, allele_specific in matches:
            locus = locus.upper()
            allele = f"{allele_group}:{allele_specific}"
            
            key = f'HLA-{locus}'
            if key not in hla_alleles:
                hla_alleles[key] = []
            hla_alleles[key].append(allele)
        
        logger.info(f"✅ Parsed {len(hla_alleles)} HLA loci from manual input: {list(hla_alleles.keys())}")
        return {'manual_alleles': hla_alleles}
    
    def _position_to_locus(self, position: int) -> str:
        """Map chromosome position to HLA locus."""
        for locus, (start, end) in self.LOCUS_RANGES.items():
            if start <= position <= end:
                return locus
        return 'HLA-OTHER'
    
    def calculate_hla_compatibility(self, person_a_hla: dict, person_b_hla: dict) -> dict:
        """Calculate HLA compatibility using SNP dissimilarity or manual alleles."""
        logger.info("🧬 Calculating HLA compatibility...")
        
        if not person_a_hla or not person_b_hla:
            logger.warning("⚠️ Missing HLA data")
            return self._default_compatibility()
        
        # Check format
        if 'manual_alleles' in person_a_hla and 'manual_alleles' in person_b_hla:
            return self._calculate_from_manual(person_a_hla['manual_alleles'], person_b_hla['manual_alleles'])
        else:
            return self._calculate_from_snps(person_a_hla, person_b_hla)
    
    def _calculate_from_manual(self, alleles_a: dict, alleles_b: dict) -> dict:
        """Calculate from manually entered HLA alleles."""
        logger.info("🔬 Calculating from manual HLA alleles")
        
        breakdown = {}
        total_dissimilarity = 0
        loci_compared = 0
        
        for locus in ['HLA-A', 'HLA-B', 'HLA-C', 'HLA-DRB1', 'HLA-DQA1', 'HLA-DQB1']:
            if locus not in alleles_a or locus not in alleles_b:
                breakdown[locus] = {'status': 'no_data', 'dissimilarity': None}
                continue
            
            # Calculate allele dissimilarity
            a_set = set(alleles_a[locus])
            b_set = set(alleles_b[locus])
            
            # Dissimilarity = proportion of non-matching alleles
            all_alleles = a_set | b_set
            matching = a_set & b_set
            dissim = 1.0 - (len(matching) / len(all_alleles)) if all_alleles else 0
            
            # Locus weights: Class I (A,B,C) = 30%, Class II (DR,DQ) = 20%
            weight = 0.30 if locus in ['HLA-A', 'HLA-B', 'HLA-C'] else 0.20
            
            breakdown[locus] = {
                'dissimilarity': round(dissim, 3),
                'contribution': round(weight * 100, 1),
                'status': 'analyzed'
            }
            
            total_dissimilarity += dissim * weight
            loci_compared += weight
        
        if loci_compared == 0:
            return self._default_compatibility()
        
        avg_dissimilarity = total_dissimilarity / loci_compared
        compatibility_score = self._dissimilarity_to_score(avg_dissimilarity)
        
        logger.info(f"✅ HLA compatibility: {compatibility_score:.1f}% (dissim: {avg_dissimilarity:.2f})")
        
        return {
            'compatibility_score': round(compatibility_score, 1),
            'dissimilarity': round(avg_dissimilarity, 3),
            'interpretation': self._interpret_score(compatibility_score, avg_dissimilarity),
            'breakdown': breakdown,
            'method': 'manual_alleles'
        }
    
    def _calculate_from_snps(self, snps_a: dict, snps_b: dict) -> dict:
        """Calculate from SNP data grouped by locus."""
        logger.info("🔬 Calculating from SNP data")
        
        breakdown = {}
        total_dissimilarity = 0
        loci_compared = 0
        
        for locus, (start, end) in self.LOCUS_RANGES.items():
            # Get SNPs for this locus
            a_snps = {rsid: data for rsid, data in snps_a.items() 
                      if start <= data['position'] <= end}
            b_snps = {rsid: data for rsid, data in snps_b.items()
                      if start <= data['position'] <= end}
            
            if not a_snps or not b_snps:
                breakdown[locus] = {'status': 'no_data', 'dissimilarity': None}
                continue
            
            # Calculate dissimilarity for shared SNPs
            shared_rsids = set(a_snps.keys()) & set(b_snps.keys())
            
            if not shared_rsids:
                breakdown[locus] = {'status': 'no_shared_snps', 'dissimilarity': None}
                continue
            
            # Count mismatches
            mismatches = sum(1 for rsid in shared_rsids 
                           if a_snps[rsid]['genotype'] != b_snps[rsid]['genotype'])
            
            dissim = mismatches / len(shared_rsids)
            
            # Locus weights
            weight = 0.30 if 'DR' not in locus and 'DQ' not in locus else 0.20
            
            breakdown[locus] = {
                'dissimilarity': round(dissim, 3),
                'contribution': round(weight * 100, 1),
                'snps_compared': len(shared_rsids),
                'status': 'analyzed'
            }
            
            total_dissimilarity += dissim * weight
            loci_compared += weight
        
        if loci_compared == 0:
            return self._default_compatibility()
        
        avg_dissimilarity = total_dissimilarity / loci_compared
        compatibility_score = self._dissimilarity_to_score(avg_dissimilarity)
        
        logger.info(f"✅ HLA compatibility: {compatibility_score:.1f}% (dissim: {avg_dissimilarity:.2f})")
        
        return {
            'compatibility_score': round(compatibility_score, 1),
            'dissimilarity': round(avg_dissimilarity, 3),
            'interpretation': self._interpret_score(compatibility_score, avg_dissimilarity),
            'breakdown': breakdown,
            'method': 'snp_based'
        }
    
    def _dissimilarity_to_score(self, dissimilarity: float) -> float:
        """Convert dissimilarity to compatibility score using Wedekind optimal curve.
        
        Optimal dissimilarity: ~0.55 (55%)
        Based on Wedekind et al. 1995 - MHC-dependent mate preferences
        """
        optimal = 0.55
        distance_from_optimal = abs(dissimilarity - optimal)
        
        # Inverted parabola: score peaks at optimal, decreases as you move away
        # Max penalty when at 0% or 100% dissimilarity
        max_distance = optimal  # Maximum possible distance from optimal
        score = 100 * (1 - (distance_from_optimal / max_distance))
        
        return max(0, min(100, score))
    
    def _interpret_score(self, score: float, dissim: float) -> str:
        """Interpret compatibility score."""
        if score >= 80:
            return f"Excellent genetic compatibility ({dissim:.0%} dissimilarity, near optimal ~55%)."
        elif score >= 60:
            return f"Good genetic compatibility ({dissim:.0%} dissimilarity, within favorable range)."
        elif score >= 40:
            return f"Moderate genetic compatibility ({dissim:.0%} dissimilarity, some distance from optimal)."
        else:
            return f"Lower genetic diversity ({dissim:.0%} dissimilarity, farther from optimal range)."
    
    def _default_compatibility(self) -> dict:
        """Default when no data available."""
        return {
            'compatibility_score': 50.0,
            'interpretation': 'Insufficient genetic data for detailed analysis.',
            'breakdown': {},
            'method': 'default'
        }
