'use client';

import { motion } from 'framer-motion';
import { useMemo } from 'react';

interface GoldParticlesProps {
  isActive: boolean;
  particleCount?: number;
  targetY?: number;
}

export function GoldParticles({ isActive, particleCount = 30, targetY = -100 }: GoldParticlesProps) {
  // Generate random particle configurations
  const particles = useMemo(() => {
    return Array.from({ length: particleCount }, (_, i) => ({
      id: i,
      x: Math.random() * 200 - 100, // Random horizontal spread (-100 to +100)
      y: targetY + Math.random() * -50, // Random vertical variation
      delay: Math.random() * 0.3, // Stagger animation
      duration: 0.8 + Math.random() * 0.4, // Random duration (0.8-1.2s)
      size: 2 + Math.random() * 4, // Random size (2-6px)
      opacity: 0.6 + Math.random() * 0.4 // Random opacity
    }));
  }, [particleCount, targetY]);

  if (!isActive) return null;

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden">
      {particles.map((particle) => (
        <motion.div
          key={particle.id}
          className="absolute rounded-full"
          style={{
            left: '50%',
            top: '50%',
            width: particle.size,
            height: particle.size,
            background: 'radial-gradient(circle, var(--champagne-400) 0%, var(--champagne-500) 100%)',
            boxShadow: '0 0 4px rgba(212, 175, 55, 0.8)'
          }}
          initial={{
            x: 0,
            y: 0,
            opacity: 0,
            scale: 0
          }}
          animate={{
            x: particle.x,
            y: particle.y,
            opacity: [0, particle.opacity, 0],
            scale: [0, 1, 0.5]
          }}
          transition={{
            duration: particle.duration,
            delay: particle.delay,
            ease: [0.4, 0.0, 0.2, 1] // Custom easing for upward float
          }}
        />
      ))}
    </div>
  );
}
