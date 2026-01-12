'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import { GoldParticles } from '@/components/effects/GoldParticles';

interface Question {
  id: number;
  text: string;
  choiceA: string;
  choiceB: string;
  category: string;
}

interface QuestionCardProps {
  question: Question;
  selectedChoice?: string;
  onSelect: (choice: 'A' | 'B') => void;
}

export function QuestionCard({ question, selectedChoice, onSelect }: QuestionCardProps) {
  const [isAnimating, setIsAnimating] = useState(false);
  const [showParticles, setShowParticles] = useState(false);

  const handleChoice = (choice: 'A' | 'B') => {
    setIsAnimating(true);
    setShowParticles(true);

    // Brief animation before calling onSelect
    setTimeout(() => {
      onSelect(choice);
      setIsAnimating(false);

      // Hide particles after animation completes
      setTimeout(() => {
        setShowParticles(false);
      }, 1200);
    }, 150);
  };

  return (
    <motion.div
      className="glass-panel p-8 rounded-lg relative overflow-hidden"
      animate={{
        scale: isAnimating ? 0.98 : 1
      }}
      transition={{
        type: 'spring',
        stiffness: 400,
        damping: 25
      }}
    >
      {/* Gold Particle Effect */}
      <GoldParticles isActive={showParticles} particleCount={25} targetY={-120} />
      {/* Category Label */}
      <div className="mb-4">
        <span className="text-xs font-sans uppercase tracking-wider text-champagne-500">
          {question.category}
        </span>
      </div>

      {/* Question Text */}
      <h3 className="text-2xl font-serif text-mediterranean-500 mb-8 leading-relaxed">
        {question.text}
      </h3>

      {/* Choice Buttons */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
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
          <div className="text-base text-parchment-900">{question.choiceA}</div>
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
          <div className="text-base text-parchment-900">{question.choiceB}</div>
        </button>
      </div>
    </motion.div>
  );
}
