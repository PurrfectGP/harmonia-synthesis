'use client';

import { useState, useEffect } from 'react';
import { motion, useSpring, useMotionValue } from 'framer-motion';

interface RatingSliderProps {
  value: number | null;
  onChange: (value: number) => void;
}

const FEEDBACK_TEXT = {
  1: 'Indifferent',
  2: 'Indifferent',
  3: 'Potential',
  4: 'Magnetic',
  5: 'Magnetic'
};

const BACKGROUND_COLORS = {
  1: '#e0e5e8', // Cool blue-grey
  2: '#e0e5e8', // Cool blue-grey
  3: '#fbf9f5', // Neutral parchment
  4: '#f5e6d3', // Warm amber
  5: '#f5e6d3'  // Warm amber
};

export function RatingSlider({ value, onChange }: RatingSliderProps) {
  const [isDragging, setIsDragging] = useState(false);
  const [localValue, setLocalValue] = useState<number>(3);

  // Framer Motion spring physics for smooth, weighted movement
  const springValue = useSpring(3, {
    stiffness: 150,
    damping: 20,
    mass: 0.8
  });

  useEffect(() => {
    if (value !== null) {
      setLocalValue(value);
      springValue.set(value);
    } else {
      setLocalValue(3); // Reset to center when value is cleared
      springValue.set(3);
    }
  }, [value, springValue]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newValue = parseInt(e.target.value);
    setLocalValue(newValue);
    springValue.set(newValue); // Animate with spring physics
    onChange(newValue);
  };

  const currentFeedback = FEEDBACK_TEXT[localValue as keyof typeof FEEDBACK_TEXT] || 'Potential';
  const currentBgColor = BACKGROUND_COLORS[localValue as keyof typeof BACKGROUND_COLORS] || BACKGROUND_COLORS[3];

  return (
    <motion.div
      className="p-8 rounded-lg"
      animate={{
        backgroundColor: currentBgColor,
        boxShadow: localValue >= 4 ? '0 0 30px rgba(212, 175, 55, 0.3)' : '0 0 0px rgba(212, 175, 55, 0)'
      }}
      transition={{ duration: 0.5 }}
    >
      {/* Feedback Text */}
      <div className="text-center mb-6">
        <motion.div
          className="text-3xl font-serif text-mediterranean-500 mb-2"
          key={currentFeedback}
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3 }}
        >
          {currentFeedback}
        </motion.div>
        <div className="text-sm font-sans text-parchment-900/60">
          Rate your visual attraction • {localValue} of 5
        </div>
      </div>

      {/* 5-Point Gradient Slider */}
      <div className="relative">
        {/* Track Labels */}
        <div className="flex justify-between mb-3 px-1">
          {[1, 2, 3, 4, 5].map((num) => (
            <button
              key={num}
              onClick={() => {
                setLocalValue(num);
                onChange(num);
              }}
              className={`
                w-8 h-8 rounded-full border-2 font-sans text-sm font-medium transition-all duration-200
                ${localValue === num
                  ? 'border-champagne-400 bg-champagne-400 text-parchment-900'
                  : 'border-mediterranean-500/30 bg-parchment-100 text-mediterranean-500 hover:border-champagne-400/50'
                }
              `}
            >
              {num}
            </button>
          ))}
        </div>

        {/* Slider Input */}
        <div className="relative h-3 mb-2">
          {/* Track */}
          <div
            className="absolute inset-0 rounded-full"
            style={{
              background: 'linear-gradient(to right, #2a4e6c 0%, #2a4e6c 50%, #d4af37 100%)',
              opacity: 0.3
            }}
          />

          {/* Filled Track */}
          <motion.div
            className="absolute inset-y-0 left-0 rounded-full"
            animate={{
              width: `${((localValue - 1) / 4) * 100}%`,
              background: localValue >= 4 ? 'var(--champagne-400)' : 'var(--mediterranean-500)'
            }}
            transition={{ type: 'spring', stiffness: 150, damping: 20 }}
          />

          {/* Slider Input (invisible but functional) */}
          <input
            type="range"
            min="1"
            max="5"
            step="1"
            value={localValue}
            onChange={handleChange}
            onMouseDown={() => setIsDragging(true)}
            onMouseUp={() => setIsDragging(false)}
            onTouchStart={() => setIsDragging(true)}
            onTouchEnd={() => setIsDragging(false)}
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            style={{ zIndex: 10 }}
          />

          {/* Gold Knob/Thumb - Spring Physics */}
          <motion.div
            className="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 w-7 h-7 rounded-full"
            style={{
              left: `${((localValue - 1) / 4) * 100}%`,
              background: 'var(--champagne-400)',
              border: '3px solid var(--champagne-500)',
              zIndex: 5
            }}
            animate={{
              scale: isDragging ? 1.25 : 1,
              boxShadow: isDragging
                ? '0 0 20px rgba(212, 175, 55, 0.6)'
                : '0 2px 8px rgba(42, 78, 108, 0.3)'
            }}
            transition={{
              type: 'spring',
              stiffness: 300,
              damping: 25,
              mass: 0.8
            }}
          />
        </div>

        {/* Scale Labels */}
        <div className="flex justify-between text-xs font-sans text-parchment-900/50 mt-2 px-1">
          <span>Not Attractive</span>
          <span>Highly Attractive</span>
        </div>
      </div>

      {/* Visual Indicators */}
      <div className="mt-6 flex gap-1 justify-center">
        {[1, 2, 3, 4, 5].map((num) => (
          <motion.div
            key={num}
            className="h-1 w-12 rounded-full"
            animate={{
              backgroundColor: localValue >= num
                ? num >= 4
                  ? 'var(--champagne-400)'
                  : 'var(--mediterranean-500)'
                : 'var(--parchment-200)'
            }}
            transition={{ duration: 0.3 }}
          />
        ))}
      </div>
    </motion.div>
  );
}
