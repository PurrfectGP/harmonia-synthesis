'use client';

import { motion } from 'framer-motion';
import { useMemo } from 'react';

interface VerticalTubeProps {
  progress: number; // 0-100
}

export function VerticalTube({ progress }: VerticalTubeProps) {
  // Generate random bubble positions for liquid effect
  const bubbles = useMemo(() => {
    return Array.from({ length: 5 }, (_, i) => ({
      id: i,
      x: 10 + Math.random() * 60, // Random horizontal position (10-70%)
      delay: i * 0.4, // Stagger bubbles
      duration: 2 + Math.random() * 1 // 2-3 seconds to rise
    }));
  }, []);

  return (
    <div className="fixed right-8 top-1/2 -translate-y-1/2 z-40 hidden lg:block">
      {/* Glass Tube Container */}
      <div className="relative w-6 h-96 rounded-full overflow-hidden"
        style={{
          background: 'rgba(245, 240, 230, 0.6)',
          border: '2px solid rgba(212, 175, 55, 0.3)',
          boxShadow: 'inset 0 2px 8px rgba(42, 78, 108, 0.1), 0 4px 12px rgba(42, 78, 108, 0.1)'
        }}
      >
        {/* Royal Blue Ink Fill - Fills from bottom to top with spring physics */}
        <motion.div
          className="absolute bottom-0 left-0 right-0"
          initial={{ height: '0%' }}
          animate={{ height: `${progress}%` }}
          transition={{
            type: 'spring',
            stiffness: 40,
            damping: 12,
            mass: 1.2
          }}
          style={{
            background: 'linear-gradient(to top, var(--mediterranean-600), var(--mediterranean-500))',
            boxShadow: progress > 0 ? '0 -4px 12px rgba(42, 78, 108, 0.4)' : 'none'
          }}
        >
          {/* Liquid surface wave effect */}
          {progress > 0 && progress < 100 && (
            <svg
              className="absolute -top-2 left-0 w-full h-4"
              style={{
                animation: 'liquidWave 2s ease-in-out infinite'
              }}
              preserveAspectRatio="none"
              viewBox="0 0 100 10"
            >
              <path
                d="M0,5 Q25,0 50,5 T100,5 L100,10 L0,10 Z"
                fill="var(--mediterranean-500)"
                opacity="0.6"
              />
            </svg>
          )}

          {/* Rising bubbles in liquid */}
          {progress > 10 && progress < 100 && bubbles.map((bubble) => (
            <motion.div
              key={bubble.id}
              className="absolute w-1 h-1 rounded-full bg-white/40"
              style={{
                left: `${bubble.x}%`,
                bottom: '0%'
              }}
              animate={{
                y: [0, -384], // Rise to top of tube (384px = h-96)
                opacity: [0, 0.6, 0],
                scale: [0.5, 1, 0.5]
              }}
              transition={{
                duration: bubble.duration,
                delay: bubble.delay,
                repeat: Infinity,
                ease: 'easeOut'
              }}
            />
          ))}

          {/* Liquid shine effect with motion */}
          <motion.div
            className="absolute inset-0 opacity-30"
            style={{
              background: 'linear-gradient(to right, transparent 0%, rgba(255,255,255,0.3) 50%, transparent 100%)'
            }}
            animate={{
              x: ['-100%', '100%']
            }}
            transition={{
              duration: 3,
              repeat: progress < 100 && progress > 0 ? Infinity : 0,
              ease: 'linear'
            }}
          />
        </motion.div>

        {/* Glass reflection overlay */}
        <div
          className="absolute inset-0 pointer-events-none"
          style={{
            background: 'linear-gradient(to right, rgba(255,255,255,0.1) 0%, transparent 30%, transparent 70%, rgba(255,255,255,0.1) 100%)'
          }}
        />
      </div>

      {/* Progress Label */}
      <motion.div
        className="mt-3 text-center"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
      >
        <motion.div
          className="text-xs font-sans text-parchment-900/60"
          key={Math.round(progress)}
          initial={{ opacity: 0, y: -5 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3 }}
        >
          {Math.round(progress)}%
        </motion.div>
      </motion.div>

      <style jsx>{`
        @keyframes liquidWave {
          0%, 100% {
            transform: translateY(0) scaleY(1);
          }
          50% {
            transform: translateY(-1px) scaleY(0.95);
          }
        }
      `}</style>
    </div>
  );
}
