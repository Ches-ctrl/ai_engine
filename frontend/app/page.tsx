'use client'

import { useState } from 'react'
import { FileUpload } from '@/components/FileUpload'
import { MatchVisualizer } from '@/components/MatchVisualizer'
import { ContextPrompt } from '@/components/ContextPrompt'
import { Shortlist } from '@/components/Shortlist'

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
      <div className="w-80 border-r border-gray-800 p-4 flex flex-col">
        <h2 className="text-xl font-bold text-white mb-4">Shortlisted Roles</h2>
        {matches && <Shortlist matches={matches} />}
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        {/* Visualization Area */}
        <div className="flex-1 p-8 overflow-hidden">
          {matches ? (
            <MatchVisualizer matches={matches} />
          ) : (
            <div className="h-full flex items-center justify-center">
              <div className="text-gray-500 text-center">
                <p className="text-lg mb-2">Upload your CV and describe your ideal role</p>
                <p>We'll match you with the perfect opportunities</p>
              </div>
            </div>
          )}
        </div>

        {/* Chat Interface */}
        <div className="border-t border-gray-800 p-4 bg-gray-900">
          <div className="max-w-4xl mx-auto">
            <div className="flex gap-4">
              <div className="flex-1">
                {!selectedFile ? (
                  <FileUpload onFileSelect={handleFileSelect} />
                ) : (
                  <div className="text-green-500 text-sm mb-2">
                    ✓ {selectedFile.name} uploaded
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
                    : 'bg-blue-600 hover:bg-blue-700 text-white'
                  }`}
              >
                {isLoading ? (
                  <div className="flex items-center gap-2">
                    <div className="w-4 h-4 border-2 border-gray-400 border-t-white rounded-full animate-spin" />
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
  )
}
