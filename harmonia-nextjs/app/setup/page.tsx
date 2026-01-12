'use client';

import { useState } from 'react';
import { MandatoryQuestions } from '@/components/setup/MandatoryQuestions';
import { BiometricSeal } from '@/components/setup/BiometricSeal';
import { InkWellProgress } from '@/components/setup/InkWellProgress';

export default function SetupPage() {
  const [progress, setProgress] = useState(0);
  const [mandatoryAnswers, setMandatoryAnswers] = useState<Record<number, string>>({});
  const [biometricComplete, setBiometricComplete] = useState(false);

  const handleQuestionAnswer = (questionId: number, choice: string) => {
    setMandatoryAnswers(prev => ({
      ...prev,
      [questionId]: choice
    }));
  };

  const allQuestionsAnswered = Object.keys(mandatoryAnswers).length === 5;
  const setupComplete = allQuestionsAnswered && biometricComplete;

  return (
    <main className="min-h-screen bg-parchment-texture p-8">
      {/* Header */}
      <div className="max-w-2xl mx-auto mb-12 text-center">
        <h1 className="text-5xl font-serif text-mediterranean-500 mb-4">
          The Harmonia Protocol
        </h1>
        <p className="text-lg text-parchment-900/80 font-sans">
          Module 1: Biometric Ingestion & Psychological Baseline
        </p>
      </div>

      {/* Progress Indicator */}
      <InkWellProgress progress={(Object.keys(mandatoryAnswers).length / 5) * 100} />

      {/* Mandatory Five Questions */}
      <section className="max-w-3xl mx-auto mb-16">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-serif text-mediterranean-500 mb-2">
            The Mandatory Five
          </h2>
          <p className="text-sm text-parchment-900/60 font-sans">
            Five fundamental questions to establish your baseline personality profile
          </p>
        </div>

        <MandatoryQuestions
          answers={mandatoryAnswers}
          onAnswer={handleQuestionAnswer}
        />
      </section>

      {/* Biometric Ingestion */}
      <section className="max-w-2xl mx-auto mb-16">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-serif text-mediterranean-500 mb-2">
            Biometric Ingestion Port
          </h2>
          <p className="text-sm text-parchment-900/60 font-sans">
            Upload your genetic data (23andMe, Ancestry) or request a testing kit
          </p>
        </div>

        <BiometricSeal onComplete={() => setBiometricComplete(true)} />
      </section>

      {/* Continue Button */}
      {setupComplete && (
        <div className="max-w-2xl mx-auto text-center">
          <button
            className="px-8 py-4 bg-mediterranean-500 text-white font-sans rounded-lg hover:bg-mediterranean-600 transition-colors"
            style={{ boxShadow: 'var(--shadow-md)' }}
          >
            Continue to Calibration →
          </button>
        </div>
      )}
    </main>
  );
}
