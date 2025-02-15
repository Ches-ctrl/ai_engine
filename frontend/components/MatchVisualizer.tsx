'use client'

import { useEffect, useRef } from 'react'
import * as d3 from 'd3'

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

interface MatchVisualizerProps {
  matches: Match[]
}

export function MatchVisualizer({ matches }: MatchVisualizerProps) {
  const svgRef = useRef<SVGSVGElement>(null)

  useEffect(() => {
    if (!svgRef.current || !matches.length) return

    const width = 800
    const height = 600
    const margin = { top: 20, right: 20, bottom: 30, left: 40 }

    const svg = d3.select(svgRef.current)
      .attr('width', width)
      .attr('height', height)

    // Clear previous content
    svg.selectAll('*').remove()

    // Create force simulation
    const simulation = d3.forceSimulation(matches)
      .force('x', d3.forceX(width / 2))
      .force('y', d3.forceY(height / 2))
      .force('collide', d3.forceCollide().radius(50))

    // Draw circles for each match
    const nodes = svg.selectAll('g')
      .data(matches)
      .enter()
      .append('g')
      .attr('transform', d => `translate(${d.x}, ${d.y})`)

    nodes.append('circle')
      .attr('r', d => d.score * 40)
      .attr('fill', d => d3.interpolateViridis(d.score))
      .attr('opacity', 0.7)

    nodes.append('text')
      .text(d => d.role)
      .attr('text-anchor', 'middle')
      .attr('dy', '.3em')
      .attr('fill', 'white')

    simulation.on('tick', () => {
      nodes.attr('transform', d => `translate(${d.x}, ${d.y})`)
    })

  }, [matches])

  return (
    <div className="space-y-8">
      <div className="bg-gray-800 p-6 rounded-lg">
        <h2 className="text-xl font-bold mb-4">Top Matches</h2>
        <div className="space-y-4">
          {matches.slice(0, 5).map((match, i) => (
            <div key={i} className="flex items-center justify-between p-4 bg-gray-700 rounded-lg">
              <div>
                <h3 className="font-semibold">{match.role}</h3>
                <div className="text-sm text-gray-300 mt-1">
                  {match.skills.join(' • ')}
                </div>
              </div>
              <div className="text-2xl font-bold">{Math.round(match.score * 100)}%</div>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-gray-800 p-6 rounded-lg">
        <svg ref={svgRef} className="w-full" />
      </div>
    </div>
  )
}
