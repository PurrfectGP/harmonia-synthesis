'use client';

import { useState } from 'react';
import { CardinalDrivers } from '@/components/assessment/CardinalDrivers';
import { VerticalTube } from '@/components/assessment/VerticalTube';
import Link from 'next/link';

export default function AssessmentPage() {
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [isComplete, setIsComplete] = useState(false);

  const handleAnswer = (driverId: string, choice: string) => {
    setAnswers(prev => ({
      ...prev,
      [driverId]: choice
    }));

    // Check if all 7 drivers answered
    const newAnswers = { ...answers, [driverId]: choice };
    if (Object.keys(newAnswers).length === 7) {
      setTimeout(() => {
        setIsComplete(true);
      }, 500);
    }
  };

  const progress = (Object.keys(answers).length / 7) * 100;

  return (
    <main className="min-h-screen bg-parchment-texture p-8 relative">
      {/* Vertical Glass Tube Progress */}
      <VerticalTube progress={progress} />

      {/* Header */}
      <div className="max-w-3xl mx-auto mb-12">
        <div className="text-center mb-8">
          <h1 className="text-5xl font-serif text-mediterranean-500 mb-4">
            Psychometric Assessment
          </h1>
          <p className="text-lg text-parchment-900/80 font-sans">
            Module 3: The Seven Cardinal Drivers
          </p>
          <p className="text-sm text-parchment-900/60 font-sans mt-2">
            Answer honestly to reveal your psychological architecture
          </p>
        </div>

        {/* Progress Text */}
        <div className="text-center mb-8">
          <div className="text-sm font-sans text-parchment-900/60">
            {Object.keys(answers).length} of 7 Drivers Analyzed
          </div>
        </div>
      </div>

      {/* Cardinal Drivers Cards */}
      {!isComplete ? (
        <CardinalDrivers
          answers={answers}
          onAnswer={handleAnswer}
        />
      ) : (
        <div className="max-w-2xl mx-auto text-center">
          <div className="glass-panel p-12 rounded-lg mb-8">
            <div className="text-6xl mb-6">✓</div>
            <h2 className="text-3xl font-serif text-mediterranean-500 mb-4">
              Psychometric Profile Complete
            </h2>
            <p className="text-lg font-sans text-parchment-900/80 mb-2">
              Your personality vector has been mapped
            </p>
            <p className="text-sm font-sans text-parchment-900/60">
              Seven Cardinal Drivers analyzed • 35% match weight configured
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
