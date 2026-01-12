'use client';

interface VerticalTubeProps {
  progress: number; // 0-100
}

export function VerticalTube({ progress }: VerticalTubeProps) {
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
        {/* Royal Blue Ink Fill - Fills from bottom to top */}
        <div
          className="absolute bottom-0 left-0 right-0 transition-all duration-700 ease-out"
          style={{
            height: `${progress}%`,
            background: 'linear-gradient(to top, var(--mediterranean-600), var(--mediterranean-500))',
            boxShadow: progress > 0 ? '0 -4px 12px rgba(42, 78, 108, 0.4)' : 'none'
          }}
        >
          {/* Liquid shine effect */}
          <div
            className="absolute inset-0 opacity-30"
            style={{
              background: 'linear-gradient(to right, transparent 0%, rgba(255,255,255,0.3) 50%, transparent 100%)',
              animation: progress < 100 && progress > 0 ? 'shimmer 3s infinite' : 'none'
            }}
          />
        </div>

        {/* Glass reflection overlay */}
        <div
          className="absolute inset-0 pointer-events-none"
          style={{
            background: 'linear-gradient(to right, rgba(255,255,255,0.1) 0%, transparent 30%, transparent 70%, rgba(255,255,255,0.1) 100%)'
          }}
        />
      </div>

      {/* Progress Label */}
      <div className="mt-3 text-center">
        <div className="text-xs font-sans text-parchment-900/60">
          {Math.round(progress)}%
        </div>
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
