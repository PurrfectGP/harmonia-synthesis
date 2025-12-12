import logging
import numpy as np

logger = logging.getLogger(__name__)

class VisualService:
    """Visual compatibility analysis with enhanced image features."""
    
    def __init__(self):
        self.partner_ratings = {}  # {user_id: {partner_id: rating}}
        self.image_analyses = {}   # {user_id: detailed_analysis}
    
    def analyze_image(self, image_data: bytes, gemini_service=None) -> dict:
        """Analyze image with basic + enhanced Gemini Vision analysis."""
        # Basic features (placeholder - production would use actual ML model)
        basic_features = {
            'quality_score': float(np.random.uniform(70, 95)),
            'attractiveness_base': float(np.random.uniform(65, 90)),
            'feature_vector': np.random.rand(512).tolist()
        }
        
        # Enhanced analysis using Gemini Vision if available
        enhanced = {}
        if gemini_service and hasattr(gemini_service, 'analyze_image_detailed'):
            try:
                import asyncio
                enhanced = asyncio.run(gemini_service.analyze_image_detailed(image_data))
                logger.info(f"✅ Enhanced analysis: {enhanced.get('facial_expression', 'unknown')}")
            except Exception as e:
                logger.warning(f"⚠️ Enhanced analysis failed: {e}")
        
        result = {**basic_features, **enhanced}
        logger.info(f"✅ Image analyzed (quality: {result['quality_score']:.1f}%)")
        return result
    
    def set_partner_rating(self, user_id: str, partner_id: str, rating: float):
        """Store user's rating of partner's image (1-10 scale)."""
        if user_id not in self.partner_ratings:
            self.partner_ratings[user_id] = {}
        # Ensure rating is in valid range
        rating = max(1.0, min(10.0, float(rating)))
        self.partner_ratings[user_id][partner_id] = rating
        logger.info(f"⭐ {user_id} rated {partner_id}: {rating}/10")
    
    def get_partner_rating(self, user_id: str, partner_id: str) -> float:
        """Get stored rating or default."""
        return self.partner_ratings.get(user_id, {}).get(partner_id, 5.0)
    
    def calculate_mutual_attraction(self, features_a: dict, features_b: dict,
                                    rating_a_to_b: float = None,
                                    rating_b_to_a: float = None) -> dict:
        """Calculate mutual visual attraction using reciprocal scoring.
        
        Uses geometric mean: √(A→B × B→A) to ensure mutual interest.
        """
        # Get ratings (use provided or defaults)
        if rating_a_to_b is None:
            rating_a_to_b = 5.0
        if rating_b_to_a is None:
            rating_b_to_a = 5.0
        
        # Convert 1-10 ratings to percentages
        a_rates_b = (rating_a_to_b / 10) * 100
        b_rates_a = (rating_b_to_a / 10) * 100
        
        # Reciprocal scoring: geometric mean ensures both must be interested
        mutual_score = float(np.sqrt(a_rates_b * b_rates_a))
        
        # Factor in image quality (affects confidence)
        quality_a = features_a.get('quality_score', 80)
        quality_b = features_b.get('quality_score', 80)
        avg_quality = (quality_a + quality_b) / 2
        
        # Confidence based on image quality
        confidence = min(0.95, avg_quality / 100)
        
        logger.info(f"✅ Visual: {mutual_score:.1f}% (A→B: {a_rates_b:.1f}%, B→A: {b_rates_a:.1f}%)")
        
        return {
            'mutual_attraction_score': round(mutual_score, 1),
            'a_rates_b': round(a_rates_b, 1),
            'b_rates_a': round(b_rates_a, 1),
            'quality_a': round(quality_a, 1),
            'quality_b': round(quality_b, 1),
            'confidence': round(confidence, 2),
            'method': 'reciprocal_geometric_mean',
            'note': 'Score represents mutual attraction: √(A→B × B→A). Both must be interested for high score.',
            # Include enhanced features if available
            'facial_expression_a': features_a.get('facial_expression', 'neutral'),
            'facial_expression_b': features_b.get('facial_expression', 'neutral'),
            'body_language_a': features_a.get('body_language', 'relaxed'),
            'body_language_b': features_b.get('body_language', 'relaxed'),
            'style_a': features_a.get('accessories_style', 'casual'),
            'style_b': features_b.get('accessories_style', 'casual')
        }
    
    def get_default_score(self) -> dict:
        """Default when no images provided."""
        return {
            'mutual_attraction_score': 50.0,
            'confidence': 0.5,
            'method': 'default',
            'note': 'No images provided for visual analysis. Using neutral baseline score.'
        }
