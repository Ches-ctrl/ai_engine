'use client'

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

interface ShortlistProps {
  matches: Match[]
}

export function Shortlist({ matches }: ShortlistProps) {
  return (
    <div className="space-y-4">
      {matches.slice(0, 5).map((match, i) => (
        <div
          key={i}
          className="p-4 rounded-lg bg-gray-800 hover:bg-gray-750 transition-colors cursor-pointer"
        >
          <div className="flex justify-between items-start mb-2">
            <h3 className="font-medium text-white">{match.role}</h3>
            <span className="text-sm font-bold text-blue-400">
              {Math.round(match.score * 100)}%
            </span>
          </div>
          <div className="flex flex-wrap gap-1">
            {match.skills.slice(0, 3).map((skill, i) => (
              <span
                key={i}
                className="px-2 py-1 text-xs rounded-full bg-gray-700 text-gray-300"
              >
                {skill}
              </span>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}
