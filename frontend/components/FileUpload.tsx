'use client'

import { useState } from 'react'

interface FileUploadProps {
  onFileSelect: (file: File) => void
}

export function FileUpload({ onFileSelect }: FileUploadProps) {
  const [dragActive, setDragActive] = useState(false)

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true)
    } else if (e.type === "dragleave") {
      setDragActive(false)
    }
  }

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const file = e.dataTransfer.files[0]
      if (file.type === 'application/pdf') {
        onFileSelect(file)
      }
    }
  }

  return (
    <div
      className={`border-2 border-dashed rounded-lg p-4 mb-4 text-center transition-colors
        ${dragActive ? 'border-blue-500 bg-blue-50/5' : 'border-gray-600'}`}
      onDragEnter={handleDrag}
      onDragLeave={handleDrag}
      onDragOver={handleDrag}
      onDrop={handleDrop}
    >
      <input
        type="file"
        id="cv-upload"
        className="hidden"
        accept=".pdf"
        onChange={(e) => {
          const file = e.target.files?.[0]
          if (file) onFileSelect(file)
        }}
      />
      <label
        htmlFor="cv-upload"
        className="cursor-pointer flex items-center justify-center gap-2 text-sm text-gray-400"
      >
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
        </svg>
        Drop your CV here or click to upload (PDF)
      </label>
    </div>
  )
}
