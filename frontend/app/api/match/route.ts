import { NextRequest, NextResponse } from 'next/server'

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData()

    console.log('Sending request to backend...')

    // Send to backend for parsing - updated port to 8080
    const response = await fetch('http://localhost:8080/parse-cv', {
      method: 'POST',
      body: formData,
      // Add headers to handle CORS
      headers: {
        'Accept': 'application/json',
      },
    })

    if (!response.ok) {
      const errorText = await response.text()
      console.error('Backend error:', errorText)
      throw new Error(`Backend error: ${errorText}`)
    }

    const data = await response.json()
    console.log('Received response:', data)

    return NextResponse.json(data)
  } catch (error: any) { // Type assertion to handle the error message
    console.error('API route error:', error)
    return NextResponse.json(
      { error: error.message || 'Failed to process CV' },
      { status: 500 }
    )
  }
}
