'use client'

import { useState } from 'react'
import { FileUpload } from '@/components/FileUpload'
import { MatchVisualizer } from '@/components/MatchVisualizer'
import { ContextPrompt } from '@/components/ContextPrompt'
import { Shortlist } from '@/components/Shortlist'
import { ParticleField } from '@/components/ParticleField'

interface Match {
  role: string
  score: number
  skills: string[]
  matchDetails: {
    technical: number
    experience: number
    education: number
  }
}

export default function Home() {
  const [matches, setMatches] = useState<Match[] | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [context, setContext] = useState('')
  const [selectedFile, setSelectedFile] = useState<File | null>(null)

  const handleFileSelect = (file: File) => {
    setSelectedFile(file)
  }

  const handleContextChange = (newContext: string) => {
    setContext(newContext)
  }

  const handleSubmit = async () => {
    if (!selectedFile) return

    setIsLoading(true)
    const formData = new FormData()
    formData.append('cv', selectedFile)
    formData.append('context', context)

    try {
      const response = await fetch('/api/match', {
        method: 'POST',
        body: formData
      })
      const data = await response.json()
      setMatches(data)
    } catch (error) {
      console.error('Error:', error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="flex h-screen bg-gray-900">
      {/* Sidebar */}
      <div className="w-80 border-r border-gray-800 p-4 flex flex-col relative z-10">
        <h2 className="text-xl font-bold text-white mb-4">Shortlisted Roles</h2>
        {matches && <Shortlist matches={matches} />}
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col relative">
        {/* Particle Background */}
        <div className="absolute inset-0 overflow-hidden">
          <ParticleField />
        </div>

        {/* Content Overlay */}
        <div className="relative z-10 flex-1 flex flex-col">
          {/* Visualization Area */}
          <div className="flex-1 p-8 overflow-hidden">
            {matches ? (
              <MatchVisualizer matches={matches} />
            ) : (
              <div className="h-full flex items-center justify-center">
                <div className="text-white text-center">
                  <p className="text-lg mb-2">Upload your CV and describe your ideal role</p>
                  <p className="text-gray-400">We&apos;ll match you with the perfect opportunities</p>
                </div>
              </div>
            )}
          </div>

          {/* Chat Interface */}
          <div className="border-t border-gray-800 bg-gray-900/80 backdrop-blur-sm p-4">
            <div className="max-w-4xl mx-auto">
              <div className="flex gap-4">
                <div className="flex-1">
                  {!selectedFile ? (
                    <FileUpload onFileSelect={handleFileSelect} />
                  ) : (
                    <div className="text-emerald-400 text-sm mb-2 flex items-center gap-2">
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                      {selectedFile.name}
                    </div>
                  )}
                  <ContextPrompt
                    onSubmit={handleContextChange}
                    disabled={isLoading}
                  />
                </div>
                <button
                  onClick={handleSubmit}
                  disabled={!selectedFile || isLoading}
                  className={`px-6 py-2 rounded-lg self-end transition-colors
                    ${!selectedFile || isLoading
                      ? 'bg-gray-700 text-gray-400 cursor-not-allowed'
                      : 'bg-white text-gray-900 hover:bg-gray-100'
                    }`}
                >
                  {isLoading ? (
                    <div className="flex items-center gap-2">
                      <div className="w-4 h-4 border-2 border-gray-600 border-t-gray-300 rounded-full animate-spin" />
                      Processing
                    </div>
                  ) : (
                    'Submit'
                  )}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
