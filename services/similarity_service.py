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
            profile_a: First person's sins profile
            profile_b: Second person's sins profile
            
        Returns:
            Similarity score (0-100)
        """
        # Extract sin scores
        sins = ["greed", "pride", "lust", "wrath", "gluttony", "envy", "sloth"]
        
        scores_a = []
        scores_b = []
        
        for sin in sins:
            if sin in profile_a and sin in profile_b:
                scores_a.append(profile_a[sin]['score'])
                scores_b.append(profile_b[sin]['score'])
        
        if not scores_a:
            return 50.0  # Default if no data
        
        # Calculate Euclidean distance
        distance = np.sqrt(sum((a - b) ** 2 for a, b in zip(scores_a, scores_b)))
        
        # Normalize to 0-100 scale (lower distance = higher similarity)
        # Max distance for sins is ~14 (if all sins differ by 5 or -5)
        max_distance = 14.0
        similarity = 100 * (1 - min(distance / max_distance, 1.0))
        
        return round(similarity, 1)
