'use client';

import { DriverCard } from './DriverCard';

// The Seven Cardinal Drivers - Rebranded from Seven Deadly Sins
// Specification: Scientific Humanism aesthetic, sophisticated language
const CARDINAL_DRIVERS = [
  {
    id: 'passion',
    driver: 'Passion',
    theologicalOrigin: 'Lust',
    icon: '🔥', // Flame - will be replaced with sketch-style SVG later
    question: 'In intimate connection, do you prioritize:',
    choiceA: 'Intense emotional vulnerability and passion',
    choiceB: 'Steady companionship and mutual respect'
  },
  {
    id: 'indulgence',
    driver: 'Indulgence',
    theologicalOrigin: 'Gluttony',
    icon: '🍷', // Wine Chalice
    question: 'When it comes to life\'s pleasures, you tend to:',
    choiceA: 'Seek rich experiences and sensory indulgence',
    choiceB: 'Practice moderation and mindful restraint'
  },
  {
    id: 'ambition',
    driver: 'Ambition',
    theologicalOrigin: 'Greed',
    icon: '👑', // Crown
    question: 'In your career and personal growth, you value:',
    choiceA: 'Achievement, advancement, and recognition',
    choiceB: 'Work-life balance and contentment with enough'
  },
  {
    id: 'serenity',
    driver: 'Serenity',
    theologicalOrigin: 'Sloth',
    icon: '💧', // Still Water
    question: 'For restoration and well-being, you find yourself drawn to:',
    choiceA: 'Activity, engagement, and purposeful motion',
    choiceB: 'Stillness, silence, and peaceful rest'
  },
  {
    id: 'conviction',
    driver: 'Conviction',
    theologicalOrigin: 'Wrath',
    icon: '⚔️', // Sword
    question: 'When your core principles are challenged, you typically:',
    choiceA: 'Stand firm and defend your values intensely',
    choiceB: 'Seek compromise and maintain harmony'
  },
  {
    id: 'yearning',
    driver: 'Yearning',
    theologicalOrigin: 'Envy',
    icon: '👁️', // Eye
    question: 'In observing others\' success and possessions, you feel:',
    choiceA: 'Inspiration and desire to achieve similar heights',
    choiceB: 'Gratitude for your own unique path and blessings'
  },
  {
    id: 'dignity',
    driver: 'Dignity',
    theologicalOrigin: 'Pride',
    icon: '🪶', // Peacock Feather
    question: 'Regarding your self-worth and identity, you believe in:',
    choiceA: 'Celebrating your strengths and standing proud',
    choiceB: 'Maintaining humility and recognizing limitations'
  }
];

interface CardinalDriversProps {
  answers: Record<string, string>;
  onAnswer: (driverId: string, choice: string) => void;
}

export function CardinalDrivers({ answers, onAnswer }: CardinalDriversProps) {
  return (
    <div className="max-w-3xl mx-auto space-y-6">
      {CARDINAL_DRIVERS.map((driver) => (
        <DriverCard
          key={driver.id}
          driver={driver}
          selectedChoice={answers[driver.id]}
          onSelect={(choice) => onAnswer(driver.id, choice)}
        />
      ))}
    </div>
  );
}
