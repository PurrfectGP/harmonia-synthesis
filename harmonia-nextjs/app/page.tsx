export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        {/* Hero Section */}
        <div className="text-center mb-12">
          <h1 className="text-6xl font-serif text-mediterranean-500 mb-4">
            The Harmonia Protocol
          </h1>
          <p className="text-lg text-parchment-900/80 font-sans">
            A scientific approach to meaningful connection.
          </p>
        </div>

        {/* Design System Preview */}
        <div className="glass-panel p-8 mb-8">
          <h2 className="text-3xl font-serif text-mediterranean-500 mb-6">
            Design System Verification
          </h2>

          <div className="space-y-6">
            {/* Color Palette */}
            <div>
              <h3 className="text-xl font-serif mb-3">Color Palette</h3>
              <div className="grid grid-cols-4 gap-4">
                <div className="h-20 bg-parchment-50 rounded-lg border border-parchment-200 flex items-center justify-center text-xs">
                  Parchment 50
                </div>
                <div className="h-20 bg-mediterranean-500 rounded-lg flex items-center justify-center text-xs text-white">
                  Mediterranean
                </div>
                <div className="h-20 bg-champagne-400 rounded-lg flex items-center justify-center text-xs">
                  Champagne
                </div>
                <div className="h-20 bg-danger-500 rounded-lg flex items-center justify-center text-xs text-white">
                  Danger
                </div>
              </div>
            </div>

            {/* Typography */}
            <div>
              <h3 className="text-xl font-serif mb-3">Typography</h3>
              <div className="space-y-2">
                <p className="font-serif text-2xl text-mediterranean-500">
                  Cormorant Garamond Display Font
                </p>
                <p className="font-sans text-base text-parchment-900">
                  DM Sans Body Font - Clean, Modern, Scientific
                </p>
              </div>
            </div>

            {/* Input Example */}
            <div>
              <h3 className="text-xl font-serif mb-3">Input Styles</h3>
              <input
                type="text"
                placeholder="Underlined Input"
                className="input-underline w-full"
              />
            </div>

            {/* Shadow Examples */}
            <div>
              <h3 className="text-xl font-serif mb-3">Blue-Tinted Shadows</h3>
              <div className="grid grid-cols-3 gap-4">
                <div className="p-4 bg-parchment-100 rounded-lg" style={{boxShadow: 'var(--shadow-sm)'}}>
                  Shadow SM
                </div>
                <div className="p-4 bg-parchment-100 rounded-lg" style={{boxShadow: 'var(--shadow-md)'}}>
                  Shadow MD
                </div>
                <div className="p-4 bg-parchment-100 rounded-lg" style={{boxShadow: 'var(--shadow-lg)'}}>
                  Shadow LG
                </div>
              </div>
            </div>

            {/* "The Spark" Glow */}
            <div>
              <h3 className="text-xl font-serif mb-3">The Spark Effect</h3>
              <div
                className="p-6 bg-champagne-400 rounded-lg text-center font-serif text-2xl"
                style={{boxShadow: 'var(--shadow-spark)'}}
              >
                Chemical Spark Detected
              </div>
            </div>
          </div>
        </div>

        {/* Session Status */}
        <div className="text-center space-y-4">
          <div className="inline-block px-6 py-3 bg-mediterranean-500 text-white rounded-lg font-sans">
            ✓ Sessions 1-3 Complete: Design System Foundation
          </div>
          <p className="text-sm text-parchment-900/60">
            Paper grain texture • Blue-tinted shadows • Gold accents • Typography configured
          </p>

          {/* Module Navigation */}
          <div className="pt-8">
            <h3 className="text-2xl font-serif text-mediterranean-500 mb-4">
              Experience Harmonia Modules
            </h3>
            <div className="flex gap-4 justify-center">
              <a
                href="/setup"
                className="px-6 py-3 bg-champagne-400 text-parchment-900 font-sans rounded-lg hover:bg-champagne-500 transition-colors"
                style={{boxShadow: 'var(--shadow-md)'}}
              >
                Module 1: Setup →
              </a>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
