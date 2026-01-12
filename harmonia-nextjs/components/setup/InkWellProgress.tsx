'use client';

interface InkWellProgressProps {
  progress: number; // 0-100
}

export function InkWellProgress({ progress }: InkWellProgressProps) {
  return (
    <div className="fixed bottom-0 left-0 right-0 h-2 bg-parchment-200/50 z-50">
      {/* Royal Blue Ink Fill */}
      <div
        className="h-full bg-mediterranean-500 transition-all duration-500 ease-out"
        style={{
          width: `${progress}%`,
          boxShadow: '0 0 10px rgba(42, 78, 108, 0.4)'
        }}
      >
        {/* Animated shine effect */}
        <div
          className="h-full w-full bg-gradient-to-r from-transparent via-white/20 to-transparent"
          style={{
            animation: progress < 100 ? 'shimmer 2s infinite' : 'none'
          }}
        />
      </div>

      <style jsx>{`
        @keyframes shimmer {
          0% {
            transform: translateX(-100%);
          }
          100% {
            transform: translateX(100%);
          }
        }
      `}</style>
    </div>
  );
}
