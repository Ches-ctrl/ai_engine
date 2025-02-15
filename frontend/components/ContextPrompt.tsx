'use client'

interface ContextPromptProps {
  onSubmit: (context: string) => void
  disabled?: boolean
}

export function ContextPrompt({ onSubmit, disabled }: ContextPromptProps) {
  return (
    <textarea
      className={`w-full p-4 bg-gray-800 rounded-lg border border-gray-700
        focus:border-blue-500 focus:ring-1 focus:ring-blue-500 resize-none
        ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}
      placeholder="Tell us about your ideal role..."
      rows={3}
      onChange={(e) => onSubmit(e.target.value)}
      disabled={disabled}
    />
  )
}
