
class SimilarityService:
    """Calculate perceived similarity based on Seven Deadly Sins profiles."""

    # Weights for each sin based on relationship importance
    WEIGHTS = {
        'wrath': 1.5,     # Conflict handling is critical
        'sloth': 1.3,     # Motivation alignment matters
        'pride': 1.2,     # Ego dynamics
        'lust': 1.0,      # Physical compatibility
        'greed': 0.9,     # Resource attitudes
        'gluttony': 0.8,  # Lifestyle habits
        'envy': 0.7       # Security/jealousy
    }

    def calculate_perceived_similarity(self, profile_a: dict, profile_b: dict) -> dict:
        """Calculate compatibility based on POSITIVE OVERLAP.

        Positive Overlap = Both high in same direction (both virtuous OR both vice-leaning)
        This predicts perceived similarity and relationship satisfaction.
        """
        similarity_accumulated = 0.0
        max_possible = sum(self.WEIGHTS.values())
        breakdown = []
        detailed_analysis = {}

        for sin, weight in self.WEIGHTS.items():
            try:
                sa = profile_a['sins'][sin]['score']
                sb = profile_b['sins'][sin]['score']
                ca = profile_a['sins'][sin].get('confidence', 0.8)
                cb = profile_b['sins'][sin].get('confidence', 0.8)
            except (KeyError, TypeError):
                sa, sb, ca, cb = 0, 0, 0.5, 0.5

            # POSITIVE OVERLAP: Both High Vice (>1) OR Both High Virtue (<-1)
            is_same_direction = (sa > 1 and sb > 1) or (sa < -1 and sb < -1)

            if is_same_direction:
                diff = abs(sa - sb)
                trait_similarity = max(0, 1 - (diff / 10.0))
                avg_confidence = (ca + cb) / 2
                weighted_score = trait_similarity * weight * avg_confidence
                similarity_accumulated += weighted_score

                direction = "High Vice" if sa > 0 else "High Virtue"
                breakdown.append(f"{sin.capitalize()} ({direction}): +{weighted_score:.2f}")
                detailed_analysis[sin] = {
                    'direction': direction,
                    'score_a': round(sa, 2),
                    'score_b': round(sb, 2),
                    'contribution': round(weighted_score, 3)
                }
            else:
                detailed_analysis[sin] = {
                    'direction': 'Divergent',
                    'score_a': round(sa, 2),
                    'score_b': round(sb, 2),
                    'contribution': 0
                }

        final_score = similarity_accumulated / max_possible

        return {
            "score": round(final_score, 4),
            "percentage": round(final_score * 100, 1),
            "breakdown": breakdown,
            "detailed": detailed_analysis
        }
