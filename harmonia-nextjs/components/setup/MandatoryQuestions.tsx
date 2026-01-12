'use client';

import { useState } from 'react';
import { QuestionCard } from './QuestionCard';

// The Mandatory Five Questions - Exact specification from design doc
const MANDATORY_QUESTIONS = [
  {
    id: 1,
    text: 'When facing a social gathering, do you typically feel:',
    choiceA: 'Energized by the prospect of meeting new people',
    choiceB: 'Drained and prefer quiet reflection',
    category: 'Social Battery'
  },
  {
    id: 2,
    text: 'In conflict situations, do you tend to:',
    choiceA: 'Address issues directly and immediately',
    choiceB: 'Reflect privately before engaging',
    category: 'Conflict Style'
  },
  {
    id: 3,
    text: 'Your ideal weekend involves:',
    choiceA: 'Pursuing ambitious goals and productivity',
    choiceB: 'Restorative activities and leisure',
    category: 'Ambition'
  },
  {
    id: 4,
    text: 'When making important decisions, you prioritize:',
    choiceA: 'Logic and objective analysis',
    choiceB: 'Intuition and emotional intelligence',
    category: 'Decision Making'
  },
  {
    id: 5,
    text: 'In relationships, you value most:',
    choiceA: 'Deep emotional intimacy and vulnerability',
    choiceB: 'Intellectual connection and shared interests',
    category: 'Connection Type'
  }
];

interface MandatoryQuestionsProps {
  answers: Record<number, string>;
  onAnswer: (questionId: number, choice: string) => void;
}

export function MandatoryQuestions({ answers, onAnswer }: MandatoryQuestionsProps) {
  return (
    <div className="space-y-6">
      {MANDATORY_QUESTIONS.map((question) => (
        <QuestionCard
          key={question.id}
          question={question}
          selectedChoice={answers[question.id]}
          onSelect={(choice) => onAnswer(question.id, choice)}
        />
      ))}
    </div>
  );
}
