'use client';

import { motion } from 'framer-motion';

interface InkWellProgressProps {
  progress: number; // 0-100
}

export function InkWellProgress({ progress }: InkWellProgressProps) {
  return (
    <div className="fixed bottom-0 left-0 right-0 h-3 bg-parchment-200/50 z-50 overflow-hidden">
      {/* Royal Blue Ink Fill with Liquid Wave Effect */}
      <motion.div
        className="relative h-full"
        initial={{ width: '0%' }}
        animate={{ width: `${progress}%` }}
        transition={{
          type: 'spring',
          stiffness: 50,
          damping: 15,
          mass: 1
        }}
      >
        {/* Base liquid fill */}
        <div
          className="absolute inset-0 bg-mediterranean-500"
          style={{
            boxShadow: '0 0 10px rgba(42, 78, 108, 0.4)'
          }}
        />

        {/* Liquid wave effect - SVG wave at top edge */}
        <svg
          className="absolute -top-1 left-0 w-full h-4"
          style={{
            animation: progress > 0 && progress < 100 ? 'wave 3s linear infinite' : 'none'
          }}
          preserveAspectRatio="none"
          viewBox="0 0 1200 10"
        >
          <path
            d="M0,5 Q300,0 600,5 T1200,5 L1200,10 L0,10 Z"
            fill="var(--mediterranean-500)"
            opacity="0.6"
          />
        </svg>

        {/* Second wave for depth */}
        <svg
          className="absolute -top-1 left-0 w-full h-4"
          style={{
            animation: progress > 0 && progress < 100 ? 'wave 2.5s linear infinite reverse' : 'none'
          }}
          preserveAspectRatio="none"
          viewBox="0 0 1200 10"
        >
          <path
            d="M0,5 Q300,8 600,5 T1200,5 L1200,10 L0,10 Z"
            fill="var(--mediterranean-600)"
            opacity="0.4"
          />
        </svg>

        {/* Shimmer effect */}
        <motion.div
          className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent"
          animate={{
            x: ['-100%', '100%']
          }}
          transition={{
            duration: 2,
            repeat: progress < 100 ? Infinity : 0,
            ease: 'linear'
          }}
        />
      </motion.div>

      <style jsx>{`
        @keyframes wave {
          0% {
            transform: translateX(0);
          }
          100% {
            transform: translateX(-50%);
          }
        }
      `}</style>
    </div>
  );
}
