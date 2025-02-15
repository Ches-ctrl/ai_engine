'use client'

import { useEffect, useRef } from 'react'
import * as d3 from 'd3'

interface Match extends d3.SimulationNodeDatum {
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
      nodes.attr('transform', d => `translate(${d.x ?? 0}, ${d.y ?? 0})`)
    })

  }, [matches])

  return (
    <div className="bg-gray-800 p-6 rounded-lg">
      <svg ref={svgRef} className="w-full" />
    </div>
  )
}
