"""
HLA Service - Robust DNA file parser for 23andMe, Ancestry, and MyHeritage
Handles .txt (tab-delimited) and .csv (comma-delimited) formats
"""

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
    
    def parse_hla_input(self, hla_data: str):
        """
        Parse HLA data from CSV (23andMe, Ancestry, MyHeritage) or manual input.
        
        Handles:
        - 23andMe: tab-delimited, 4 columns (rsid, chr, pos, genotype combined)
        - AncestryDNA: tab-delimited, 5 columns (rsid, chr, pos, allele1, allele2)
        - MyHeritage: CSV (comma-delimited), 4 columns (rsid, chr, pos, result)
        - Manual: HLA-A*02:01 format
        
        Returns:
            dict or list of SNPs from chromosome 6 HLA region
        """
        try:
            logger.info("🧬 Parsing HLA data...")
            
            if not hla_data or len(hla_data.strip()) < 10:
                logger.warning("⚠️ No HLA data provided or data too short")
                return []
            
            # Detect format: CSV/TXT vs Manual
            has_chromosome_data = any(x in hla_data for x in ['chromosome', 'chr', 'rsid', 'rs'])
            has_tabs_or_commas = '\t' in hla_data or ',' in hla_data
            has_hla_allele_format = 'HLA-' in hla_data and '*' in hla_data
            
            if has_hla_allele_format and not has_chromosome_data:
                # Manual format: HLA-A*02:01
                return self._parse_manual_input(hla_data)
            elif has_tabs_or_commas and (has_chromosome_data or '6' in hla_data):
                # CSV/TXT format
                return self._parse_csv_format(hla_data)
            else:
                logger.warning(f"⚠️ Unknown HLA data format (length: {len(hla_data)})")
                return []
                
        except Exception as e:
            logger.error(f"❌ Error parsing HLA data: {e}")
            import traceback
            traceback.print_exc()
            return []
    
    def _parse_csv_format(self, csv_data: str):
        """
        Extract chromosome 6 SNPs from CSV/TXT files.
        Supports: 23andMe (.txt, tab), Ancestry (.txt, tab), MyHeritage (.csv, comma)
        """
        hla_snps = []
        lines = csv_data.strip().split('\n')
        
        logger.info(f"📄 Processing {len(lines)} lines from DNA file")
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Skip comment/header lines
            if line.startswith('#') or line.lower().startswith('rsid'):
                continue
            
            try:
                # Auto-detect delimiter
                if '\t' in line:
                    parts = [p.strip() for p in line.split('\t')]
                else:
                    parts = [p.strip() for p in line.split(',')]
                
                # Need at least 4 parts
                if len(parts) < 4:
                    continue
                
                # Extract fields (handle both 4-col and 5-col formats)
                rsid = parts[0]
                chrom_raw = parts[1]
                
                # Chromosome might be numeric or have 'chr' prefix
                chrom = chrom_raw.replace('chr', '').replace('Chr', '').strip()
                
                # Skip non-chromosome-6 entries
                if chrom != '6':
                    continue
                
                # Position (column 2)
                try:
                    position = int(parts[2])
                except (ValueError, IndexError):
                    continue
                
                # Genotype (column 3 or combined from 3+4)
                if len(parts) >= 5:
                    # 5-column format (Ancestry): allele1, allele2 in separate columns
                    allele1 = parts[3].strip()
                    allele2 = parts[4].strip()
                    genotype = allele1 + allele2
                else:
                    # 4-column format (23andMe, MyHeritage): combined genotype
                    genotype = parts[3].strip()
                
                # Validate genotype (should be 2 letters or -- for no-call)
                if len(genotype) < 1 or genotype == '00':
                    continue
                
                # Filter: Only HLA region
                if self.HLA_REGION_START <= position <= self.HLA_REGION_END:
                    locus = self._position_to_locus(position)
                    hla_snps.append({
                        'rsid': rsid,
                        'position': position,
                        'genotype': genotype,
                        'locus': locus
                    })
                    
            except Exception as e:
                # Skip problematic lines without crashing
                if line_num <= 20:  # Only log first 20 errors to avoid spam
                    logger.debug(f"⚠️ Line {line_num} parse error: {e}")
                continue
        
        logger.info(f"✅ Extracted {len(hla_snps)} HLA-region SNPs from chromosome 6")
        
        if len(hla_snps) == 0:
            logger.warning("⚠️ No chromosome 6 SNPs found in HLA region. File may be incorrect format.")
        
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
    
    def calculate_hla_compatibility(self, person_a_hla, person_b_hla) -> dict:
        """Calculate HLA compatibility using SNP dissimilarity or manual alleles."""
        try:
            logger.info("🧬 Calculating HLA compatibility...")
            
            if not person_a_hla or not person_b_hla:
                logger.warning("⚠️ Missing HLA data for one or both people")
                return self._default_compatibility()
            
            # Empty lists/dicts
            if (isinstance(person_a_hla, (list, dict)) and len(person_a_hla) == 0) or \
               (isinstance(person_b_hla, (list, dict)) and len(person_b_hla) == 0):
                logger.warning("⚠️ Empty HLA data structures")
                return self._default_compatibility()
            
            # Check format: manual vs SNP-based
            if isinstance(person_a_hla, dict) and 'manual_alleles' in person_a_hla:
                return self._calculate_from_manual(
                    person_a_hla['manual_alleles'],
                    person_b_hla.get('manual_alleles', {})
                )
            else:
                # SNP-based calculation
                return self._calculate_from_snps(person_a_hla, person_b_hla)
                
        except Exception as e:
            logger.error(f"❌ HLA compatibility calculation error: {e}")
            import traceback
            traceback.print_exc()
            return self._default_compatibility()
    
    def _calculate_from_manual(self, alleles_a: dict, alleles_b: dict) -> dict:
        """Calculate from manually entered HLA alleles."""
        logger.info("🔬 Calculating from manual HLA alleles")
        
        # Simple dissimilarity based on shared vs different alleles
        total_loci = set(alleles_a.keys()) | set(alleles_b.keys())
        if not total_loci:
            return self._default_compatibility()
        
        matches = 0
        comparisons = 0
        
        for locus in total_loci:
            if locus in alleles_a and locus in alleles_b:
                a_alleles = set(alleles_a[locus])
                b_alleles = set(alleles_b[locus])
                shared = len(a_alleles & b_alleles)
                total = len(a_alleles | b_alleles)
                if total > 0:
                    matches += shared
                    comparisons += total
        
        if comparisons == 0:
            return self._default_compatibility()
        
        dissimilarity = 1 - (matches / comparisons)
        score = self._apply_wedekind_curve(dissimilarity)
        
        return {
            'compatibility_score': round(score, 1),
            'dissimilarity': round(dissimilarity, 3),
            'method': 'manual_alleles',
            'comparisons': comparisons
        }
    
    def _calculate_from_snps(self, snps_a, snps_b) -> dict:
        """Calculate from SNP data (list of dicts with rsid, position, genotype)."""
        logger.info("🔬 Calculating from SNP data")
        
        # Handle list format (from CSV parsing)
        if not isinstance(snps_a, list) or not isinstance(snps_b, list):
            logger.warning("⚠️ SNP data not in list format")
            return self._default_compatibility()
        
        if len(snps_a) == 0 or len(snps_b) == 0:
            logger.warning(f"⚠️ Empty SNP lists: A={len(snps_a)}, B={len(snps_b)}")
            return self._default_compatibility()
        
        # Build lookup by rsid for person B
        snps_b_lookup = {snp['rsid']: snp for snp in snps_b}
        
        # Calculate per-locus dissimilarity
        locus_stats = {}
        
        for snp_a in snps_a:
            rsid = snp_a['rsid']
            if rsid not in snps_b_lookup:
                continue
            
            snp_b = snps_b_lookup[rsid]
            locus = snp_a['locus']
            
            if locus not in locus_stats:
                locus_stats[locus] = {'matches': 0, 'mismatches': 0}
            
            # Compare genotypes
            if snp_a['genotype'] == snp_b['genotype']:
                locus_stats[locus]['matches'] += 1
            else:
                locus_stats[locus]['mismatches'] += 1
        
        if not locus_stats:
            logger.warning("⚠️ No shared SNPs found between the two people")
            return self._default_compatibility()
        
        # Calculate weighted dissimilarity
        total_dissim = 0
        total_weight = 0
        
        # Class I (HLA-A, B, C) get 30% weight each
        # Class II (DRB1, DQA1, DQB1) get 20% weight each
        weights = {
            'HLA-A': 0.30,
            'HLA-B': 0.30,
            'HLA-C': 0.30,
            'HLA-DRB1': 0.20,
            'HLA-DQA1': 0.20,
            'HLA-DQB1': 0.20
        }
        
        for locus, stats in locus_stats.items():
            total_snps = stats['matches'] + stats['mismatches']
            if total_snps > 0:
                locus_dissim = stats['mismatches'] / total_snps
                weight = weights.get(locus, 0.10)
                total_dissim += locus_dissim * weight
                total_weight += weight
        
        if total_weight == 0:
            return self._default_compatibility()
        
        overall_dissim = total_dissim / total_weight
        score = self._apply_wedekind_curve(overall_dissim)
        
        shared_snps = sum(stats['matches'] + stats['mismatches'] for stats in locus_stats.values())
        
        logger.info(f"✅ HLA compatibility calculated: {score}% (dissim: {overall_dissim:.3f}, shared SNPs: {shared_snps})")
        
        return {
            'compatibility_score': round(score, 1),
            'dissimilarity': round(overall_dissim, 3),
            'method': 'snp_based',
            'shared_snps': shared_snps,
            'locus_breakdown': locus_stats
        }
    
    def _apply_wedekind_curve(self, dissimilarity: float) -> float:
        """
        Apply Wedekind optimal curve (1995 T-shirt study).
        Optimal dissimilarity is ~55% (0.55).
        Score peaks at optimal, decreases as you move away.
        """
        optimal = 0.55
        distance_from_optimal = abs(dissimilarity - optimal)
        
        # Scale: 0 distance = 100 score, max distance (0.55) = 0 score
        score = 100 * (1 - (distance_from_optimal / optimal))
        
        return max(0, min(100, score))
    
    def _default_compatibility(self) -> dict:
        """Return default score when HLA data unavailable."""
        return {
            'compatibility_score': 50.0,
            'dissimilarity': 0.5,
            'method': 'default',
            'note': 'No genetic data provided. Using neutral baseline.'
        }
    
    def _position_to_locus(self, position: int) -> str:
        """Map chromosome position to HLA locus."""
        for locus, (start, end) in self.LOCUS_RANGES.items():
            if start <= position <= end:
                return locus
        return 'HLA-OTHER'
