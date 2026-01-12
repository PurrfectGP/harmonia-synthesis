'use client';

import { useState, useEffect, useRef } from 'react';
import { RatingSlider } from './RatingSlider';
import Image from 'next/image';

// Meta FP Dataset - Stock portrait images (placeholder URLs)
// In production, these would be from Chicago Face Database or professional stock
const META_FP_DATASET = [
  'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1504257432389-52343af06ae3?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1521119989659-a83eee488004?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1491349174775-aaafddd81942?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1502323777036-f29e3972d82f?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1504257432389-52343af06ae3?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1463453091185-61582044d556?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=400&h=500&fit=crop',
  'https://images.unsplash.com/photo-1507081323647-4d250478b919?w=400&h=500&fit=crop'
];

interface PortraitGalleryProps {
  imageIndex: number;
  onRate: (imageIndex: number, rating: number, dwellTimeMs: number, sliderMovements: number) => void;
}

export function PortraitGallery({ imageIndex, onRate }: PortraitGalleryProps) {
  const [rating, setRating] = useState<number | null>(null);
  const [sliderMovements, setSliderMovements] = useState(0);
  const renderTimeRef = useRef<number>(0);

  // Track dwell time - start timer when image loads
  useEffect(() => {
    renderTimeRef.current = Date.now();
    setRating(null);
    setSliderMovements(0);
  }, [imageIndex]);

  const handleRatingChange = (newRating: number) => {
    setRating(newRating);
    setSliderMovements(prev => prev + 1);
  };

  const handleConfirm = () => {
    if (rating === null) return;

    const dwellTimeMs = Date.now() - renderTimeRef.current;
    onRate(imageIndex, rating, dwellTimeMs, sliderMovements);
  };

  const currentImage = META_FP_DATASET[imageIndex] || META_FP_DATASET[0];

  return (
    <div className="max-w-2xl mx-auto">
      {/* Portrait Frame - Gold Leaf Border */}
      <div
        className="relative p-4 rounded-lg mb-8"
        style={{
          border: '4px solid var(--champagne-400)',
          boxShadow: 'var(--shadow-lg)',
          background: 'var(--parchment-100)'
        }}
      >
        {/* Portrait Image */}
        <div className="relative w-full aspect-[4/5] bg-parchment-200 rounded overflow-hidden">
          <Image
            src={currentImage}
            alt={`Calibration Portrait ${imageIndex + 1}`}
            fill
            className="object-cover"
            priority
            unoptimized // For demo with external URLs
          />
        </div>

        {/* Calibration Profile Label */}
        <div className="absolute top-6 left-6 px-3 py-1 glass-panel rounded">
          <span className="text-xs font-sans text-mediterranean-500 font-medium">
            Calibration Profile #{imageIndex + 1}
          </span>
        </div>
      </div>

      {/* Rating Slider */}
      <div className="mb-8">
        <RatingSlider
          value={rating}
          onChange={handleRatingChange}
        />
      </div>

      {/* Confirm Button */}
      <div className="text-center">
        <button
          onClick={handleConfirm}
          disabled={rating === null}
          className={`
            px-8 py-4 rounded-lg font-sans font-medium transition-all duration-300
            ${rating !== null
              ? 'bg-mediterranean-500 text-white hover:bg-mediterranean-600 cursor-pointer'
              : 'bg-parchment-200 text-parchment-900/40 cursor-not-allowed'
            }
          `}
          style={{
            boxShadow: rating !== null ? 'var(--shadow-md)' : 'none'
          }}
        >
          {rating !== null ? 'Confirm Rating →' : 'Move slider to rate'}
        </button>
      </div>
    </div>
  );
}
