"""
Similarity Service - Calculate personality similarity between profiles
"""

import numpy as np

class SimilarityService:
    """Service for calculating personality similarity and compatibility."""
    
    def __init__(self):
        """Initialize the similarity service."""
        pass
    
    def calculate_perceived_similarity(self, profile_a: dict, profile_b: dict) -> float:
        """
        Calculate perceived similarity between two personality profiles.

        Args:
            profile_a: First person's traits profile
            profile_b: Second person's traits profile

        Returns:
            Similarity score (0-100)
        """
        # Extract trait scores
        traits = ["drive", "confidence", "passion", "assertiveness", "indulgence", "aspiration", "ease"]

        scores_a = []
        scores_b = []

        for trait in traits:
            if trait in profile_a and trait in profile_b:
                scores_a.append(profile_a[trait]['score'])
                scores_b.append(profile_b[trait]['score'])

        if not scores_a:
            return 50.0  # Default if no data

        # Calculate Euclidean distance
        distance = np.sqrt(sum((a - b) ** 2 for a, b in zip(scores_a, scores_b)))

        # Normalize to 0-100 scale (lower distance = higher similarity)
        # Max distance for traits is ~14 (if all traits differ by 5 or -5)
        max_distance = 14.0
        similarity = 100 * (1 - min(distance / max_distance, 1.0))

        return round(similarity, 1)
