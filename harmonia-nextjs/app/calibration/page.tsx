'use client';

import { useState, useEffect } from 'react';
import { PortraitGallery } from '@/components/calibration/PortraitGallery';
import Link from 'next/link';

export default function CalibrationPage() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [ratings, setRatings] = useState<Record<number, number>>({});
  const [isComplete, setIsComplete] = useState(false);

  const handleRating = (imageIndex: number, rating: number, dwellTimeMs: number, sliderMovements: number) => {
    setRatings(prev => ({
      ...prev,
      [imageIndex]: rating
    }));

    console.log(`[Calibration] Image ${imageIndex}: Rating ${rating}, Dwell ${dwellTimeMs}ms, Movements ${sliderMovements}`);

    // Move to next image after brief delay
    setTimeout(() => {
      if (currentIndex < 19) { // 20 total images (0-19)
        setCurrentIndex(prev => prev + 1);
      } else {
        setIsComplete(true);
      }
    }, 300);
  };

  const progress = ((currentIndex + 1) / 20) * 100;

  return (
    <main className="min-h-screen bg-parchment-texture p-8">
      {/* Header */}
      <div className="max-w-4xl mx-auto mb-12">
        <div className="text-center mb-8">
          <h1 className="text-5xl font-serif text-mediterranean-500 mb-4">
            Visual Calibration
          </h1>
          <p className="text-lg text-parchment-900/80 font-sans">
            Module 2: Meta FP Vector Training
          </p>
          <p className="text-sm text-parchment-900/60 font-sans mt-2">
            Rate each portrait honestly. We're analyzing your visual preference patterns.
          </p>
        </div>

        {/* Progress Bar */}
        <div className="max-w-md mx-auto mb-8">
          <div className="flex justify-between text-sm font-sans text-parchment-900/60 mb-2">
            <span>Calibration Progress</span>
            <span>{currentIndex + 1} / 20</span>
          </div>
          <div className="h-2 bg-parchment-200 rounded-full overflow-hidden">
            <div
              className="h-full bg-mediterranean-500 transition-all duration-300"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>
      </div>

      {/* Portrait Gallery */}
      {!isComplete ? (
        <PortraitGallery
          imageIndex={currentIndex}
          onRate={handleRating}
        />
      ) : (
        <div className="max-w-2xl mx-auto text-center">
          <div className="glass-panel p-12 rounded-lg mb-8">
            <div className="text-6xl mb-6">✓</div>
            <h2 className="text-3xl font-serif text-mediterranean-500 mb-4">
              Calibration Complete
            </h2>
            <p className="text-lg font-sans text-parchment-900/80 mb-2">
              Your Meta FP vector has been calculated
            </p>
            <p className="text-sm font-sans text-parchment-900/60">
              Analyzed {Object.keys(ratings).length} profiles • 50% match weight configured
            </p>
          </div>

          <Link
            href="/"
            className="inline-block px-8 py-4 bg-mediterranean-500 text-white font-sans rounded-lg hover:bg-mediterranean-600 transition-colors"
            style={{ boxShadow: 'var(--shadow-md)' }}
          >
            Return to Dashboard
          </Link>
        </div>
      )}
    </main>
  );
}
