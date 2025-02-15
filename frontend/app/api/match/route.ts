import { NextResponse } from 'next/server'

export async function POST(request: Request) {
  const formData = await request.formData()
  const file = formData.get('cv') as File
  const context = formData.get('context') as string

  // TODO: Implement your CV parsing and matching logic here
  // This is where you'd integrate with your backend AI matching system

  // Dummy response with multiple varied matches
  const matches = [
    {
      role: "Senior Software Engineer",
      score: 0.95,
      skills: ["React", "TypeScript", "Node.js"],
      matchDetails: { technical: 0.95, experience: 0.90, education: 0.85 }
    },
    {
      role: "Frontend Developer",
      score: 0.88,
      skills: ["React", "CSS", "JavaScript"],
      matchDetails: { technical: 0.89, experience: 0.87, education: 0.82 }
    },
    {
      role: "Full Stack Developer",
      score: 0.82,
      skills: ["Python", "React", "PostgreSQL"],
      matchDetails: { technical: 0.84, experience: 0.81, education: 0.80 }
    },
    {
      role: "DevOps Engineer",
      score: 0.78,
      skills: ["Docker", "Kubernetes", "AWS"],
      matchDetails: { technical: 0.80, experience: 0.75, education: 0.78 }
    },
    {
      role: "Technical Lead",
      score: 0.75,
      skills: ["Team Leadership", "Architecture", "Agile"],
      matchDetails: { technical: 0.77, experience: 0.80, education: 0.72 }
    }
  ]

  return NextResponse.json(matches)
}
