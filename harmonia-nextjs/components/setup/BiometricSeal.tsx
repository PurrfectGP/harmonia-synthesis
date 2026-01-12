'use client';

import { useState, useRef } from 'react';

interface BiometricSealProps {
  onComplete: () => void;
}

// HLA Processing Steps - Labor Illusion text sequence
const HLA_PROCESSING_STEPS = [
  'Detecting File Format (23andMe/Ancestry)...',
  'Parsing Chromosome 6 Region...',
  'Validating 1,000+ SNP Markers...',
  'Imputing HLA-A, B, DRB1 Alleles...',
  'Processing Complete ✓'
];

export function BiometricSeal({ onComplete }: BiometricSealProps) {
  const [isHovering, setIsHovering] = useState(false);
  const [isDragging, setIsDragging] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [processingStep, setProcessingStep] = useState(0);
  const [uploadComplete, setUploadComplete] = useState(false);
  const [showWaitlist, setShowWaitlist] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);

    const files = e.dataTransfer.files;
    if (files.length > 0) {
      processFile(files[0]);
    }
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      processFile(files[0]);
    }
  };

  const processFile = (file: File) => {
    console.log('Processing file:', file.name);
    setIsProcessing(true);
    setProcessingStep(0);

    // Simulate the Labor Illusion - sequential processing steps
    const stepInterval = setInterval(() => {
      setProcessingStep(prev => {
        const next = prev + 1;
        if (next >= HLA_PROCESSING_STEPS.length) {
          clearInterval(stepInterval);
          setTimeout(() => {
            setIsProcessing(false);
            setUploadComplete(true);
            onComplete();
          }, 500);
        }
        return next;
      });
    }, 800); // ~3.2 seconds total (4 steps × 800ms)
  };

  const handleRequestKit = () => {
    // Mock: Check gender quota (in production, this would be API call)
    const maleQuotaFull = true; // Simulating quota full for demo

    if (maleQuotaFull) {
      setShowWaitlist(true);
    } else {
      setUploadComplete(true);
      onComplete();
    }
  };

  return (
    <div className="space-y-6">
      {/* The Biometric Seal */}
      <div
        className={`
          relative w-64 h-64 mx-auto rounded-full
          border-4 border-dashed
          flex items-center justify-center
          cursor-pointer transition-all duration-300
          ${isDragging ? 'border-champagne-400 bg-champagne-400/10 scale-105' : ''}
          ${isHovering && !isDragging ? 'border-champagne-400' : 'border-mediterranean-500'}
          ${uploadComplete ? 'border-solid border-champagne-400 bg-champagne-400/20' : ''}
        `}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onMouseEnter={() => setIsHovering(true)}
        onMouseLeave={() => setIsHovering(false)}
        onClick={() => fileInputRef.current?.click()}
        style={{
          boxShadow: uploadComplete ? 'var(--shadow-spark)' : isHovering ? 'var(--shadow-md)' : 'none'
        }}
      >
        {/* Hidden file input */}
        <input
          ref={fileInputRef}
          type="file"
          className="hidden"
          accept=".txt,.csv,.zip"
          onChange={handleFileSelect}
        />

        {/* DNA Helix Icon (Sketch Style) */}
        {!isProcessing && !uploadComplete && (
          <div className="text-center">
            <svg
              className="w-24 h-24 mx-auto mb-4"
              viewBox="0 0 100 100"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              style={{ color: isHovering ? 'var(--champagne-400)' : 'var(--mediterranean-500)' }}
            >
              {/* Simplified DNA Helix */}
              <path d="M30,20 Q50,30 70,20" />
              <path d="M30,40 Q50,50 70,40" />
              <path d="M30,60 Q50,70 70,60" />
              <path d="M30,80 Q50,90 70,80" />
              <line x1="30" y1="20" x2="30" y2="80" />
              <line x1="70" y1="20" x2="70" y2="80" />
            </svg>
            <p className="text-sm font-sans text-mediterranean-500">
              Drop genome file here
              <br />
              <span className="text-xs text-parchment-900/60">
                (.txt, .csv, .zip)
              </span>
            </p>
          </div>
        )}

        {/* Processing Animation */}
        {isProcessing && (
          <div className="text-center px-8">
            {/* Rotating DNA Helix */}
            <svg
              className="w-16 h-16 mx-auto mb-4 animate-spin"
              viewBox="0 0 100 100"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              style={{ color: 'var(--champagne-400)', animationDuration: '2s' }}
            >
              <path d="M30,20 Q50,30 70,20" />
              <path d="M30,40 Q50,50 70,40" />
              <path d="M30,60 Q50,70 70,60" />
              <path d="M30,80 Q50,90 70,80" />
              <line x1="30" y1="20" x2="30" y2="80" />
              <line x1="70" y1="20" x2="70" y2="80" />
            </svg>
            <p className="text-xs font-sans text-mediterranean-500 min-h-[3rem] flex items-center justify-center">
              {HLA_PROCESSING_STEPS[processingStep] || HLA_PROCESSING_STEPS[HLA_PROCESSING_STEPS.length - 1]}
            </p>
          </div>
        )}

        {/* Upload Complete */}
        {uploadComplete && (
          <div className="text-center">
            <div className="text-6xl mb-4">✓</div>
            <p className="text-sm font-sans text-champagne-500 font-medium">
              Biometric Data Ingested
            </p>
          </div>
        )}
      </div>

      {/* Request Kit Option */}
      {!uploadComplete && !isProcessing && (
        <div className="text-center">
          <p className="text-sm font-sans text-parchment-900/60 mb-4">
            Don't have genetic data?
          </p>
          <button
            onClick={handleRequestKit}
            className="px-6 py-3 bg-parchment-100 text-mediterranean-500 font-sans rounded-lg border border-champagne-400/30 hover:bg-parchment-200 transition-colors"
            style={{ boxShadow: 'var(--shadow-sm)' }}
          >
            Request Testing Kit
          </button>
        </div>
      )}

      {/* Waitlist Modal */}
      {showWaitlist && (
        <div className="fixed inset-0 bg-parchment-900/50 flex items-center justify-center z-50 p-4">
          <div className="glass-panel p-8 max-w-md rounded-lg" style={{ boxShadow: 'var(--shadow-xl)' }}>
            <h3 className="text-2xl font-serif text-mediterranean-500 mb-4">
              Priority Access List
            </h3>
            <p className="text-base font-sans text-parchment-900 mb-6 leading-relaxed">
              Due to strict scientific equilibrium protocols, the Pilot Pool for male testing kits
              is currently at capacity. You have been placed on the Priority Access List.
            </p>
            <p className="text-sm font-sans text-parchment-900/80 mb-6">
              Please proceed with Visual and Psychometric calibration.
            </p>
            <button
              onClick={() => {
                setShowWaitlist(false);
                setUploadComplete(true);
                onComplete();
              }}
              className="w-full px-6 py-3 bg-mediterranean-500 text-white font-sans rounded-lg hover:bg-mediterranean-600 transition-colors"
            >
              Understood
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
