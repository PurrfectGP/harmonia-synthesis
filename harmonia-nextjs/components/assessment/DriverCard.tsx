'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';

interface Driver {
  id: string;
  driver: string;
  theologicalOrigin: string;
  icon: string;
  question: string;
  choiceA: string;
  choiceB: string;
}

interface DriverCardProps {
  driver: Driver;
  selectedChoice?: string;
  onSelect: (choice: 'A' | 'B') => void;
}

export function DriverCard({ driver, selectedChoice, onSelect }: DriverCardProps) {
  const [isAnimating, setIsAnimating] = useState(false);

  const handleChoice = (choice: 'A' | 'B') => {
    setIsAnimating(true);

    // Brief animation before calling onSelect
    setTimeout(() => {
      onSelect(choice);
      setIsAnimating(false);
    }, 150);
  };

  return (
    <motion.div
      className="relative p-8 rounded-lg"
      style={{
        background: 'var(--parchment-50)',
        border: '1px solid rgba(212, 175, 55, 0.3)'
      }}
      animate={{
        scale: isAnimating ? 0.98 : 1,
        boxShadow: selectedChoice
          ? '0 10px 15px -3px rgba(42, 78, 108, 0.15)'
          : '0 4px 6px -1px rgba(42, 78, 108, 0.1)'
      }}
      transition={{
        type: 'spring',
        stiffness: 400,
        damping: 25
      }}
    >
      {/* Icon Watermark - Faint background */}
      <div
        className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-5 pointer-events-none"
        style={{ fontSize: '12rem' }}
      >
        {driver.icon}
      </div>

      {/* Driver Header */}
      <div className="relative mb-6 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="text-4xl">{driver.icon}</div>
          <div>
            <h3 className="text-2xl font-serif text-mediterranean-500">
              {driver.driver}
            </h3>
            <span className="text-xs font-sans uppercase tracking-wider text-champagne-500">
              Cardinal Driver {CARDINAL_DRIVERS.findIndex(d => d.id === driver.id) + 1} of 7
            </span>
          </div>
        </div>

        {selectedChoice && (
          <div className="px-3 py-1 bg-champagne-400/20 rounded-full">
            <span className="text-xs font-sans text-champagne-500 font-medium">
              Answered
            </span>
          </div>
        )}
      </div>

      {/* Question Text */}
      <p className="relative text-xl font-serif text-mediterranean-500 mb-8 leading-relaxed">
        {driver.question}
      </p>

      {/* Choice Buttons */}
      <div className="relative grid grid-cols-1 md:grid-cols-2 gap-4">
        <button
          onClick={() => handleChoice('A')}
          className={`
            p-6 rounded-lg border-2 transition-all duration-300
            font-sans text-left
            ${
              selectedChoice === 'A'
                ? 'border-champagne-400 bg-champagne-400/10 shadow-lg'
                : 'border-parchment-200 hover:border-mediterranean-500/30 hover:bg-parchment-100'
            }
          `}
          style={{
            boxShadow: selectedChoice === 'A' ? 'var(--shadow-md)' : 'none'
          }}
        >
          <div className="text-sm text-champagne-500 font-medium mb-2">Choice A</div>
          <div className="text-base text-parchment-900">{driver.choiceA}</div>
        </button>

        <button
          onClick={() => handleChoice('B')}
          className={`
            p-6 rounded-lg border-2 transition-all duration-300
            font-sans text-left
            ${
              selectedChoice === 'B'
                ? 'border-champagne-400 bg-champagne-400/10 shadow-lg'
                : 'border-parchment-200 hover:border-mediterranean-500/30 hover:bg-parchment-100'
            }
          `}
          style={{
            boxShadow: selectedChoice === 'B' ? 'var(--shadow-md)' : 'none'
          }}
        >
          <div className="text-sm text-champagne-500 font-medium mb-2">Choice B</div>
          <div className="text-base text-parchment-900">{driver.choiceB}</div>
        </button>
      </div>
    </motion.div>
  );
}

// Export for use in watermark
const CARDINAL_DRIVERS = [
  { id: 'passion' },
  { id: 'indulgence' },
  { id: 'ambition' },
  { id: 'serenity' },
  { id: 'conviction' },
  { id: 'yearning' },
  { id: 'dignity' }
];
