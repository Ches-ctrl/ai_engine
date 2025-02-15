from typing import List, Dict
import asyncio
from concurrent.futures import ThreadPoolExecutor

class JobMatchingAgent:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=10)
        self.base_prompt = """You are an expert HR professional and job matcher with deep experience in talent acquisition.
Your task is to evaluate how well a candidate's profile matches the specific requirements of this role.
Analyze the match considering:
- Required and preferred skills alignment
- Experience level and relevance
- Education fit
- Key achievements and their relevance
- Cultural fit indicators

For this specific role, focus especially on:
{job_specific_requirements}

Score matches objectively on a scale of 0-1 where:
0.0-0.2: Poor match
0.3-0.5: Partial match
0.6-0.8: Good match
0.9-1.0: Excellent match"""

    def _generate_custom_prompt(self, job: Dict) -> str:
        """
        Generate a custom system prompt based on job requirements
        """
        # Extract key aspects from job to focus on
        specific_reqs = []

        if job.get("required_skills"):
            specific_reqs.append(f"- Technical skills: {', '.join(job['required_skills'])}")

        if job.get("experience_years"):
            specific_reqs.append(f"- {job['experience_years']} years of relevant experience")

        if job.get("education"):
            specific_reqs.append(f"- Education background in {job['education']}")

        if job.get("key_responsibilities"):
            specific_reqs.append("- Relevant experience in: " +
                               ", ".join(job['key_responsibilities'][:3]))  # Top 3 responsibilities

        job_specific_section = "\n".join(specific_reqs) or "Standard role requirements"

        return self.base_prompt.format(job_specific_requirements=job_specific_section)

    async def match_cv_to_jobs(self, cv_data: Dict, jobs: List[Dict]) -> List[Dict]:
        """
        Match a CV against multiple jobs in parallel and return scored matches
        """
        tasks = []
        for job in jobs:
            tasks.append(
                asyncio.get_event_loop().run_in_executor(
                    self.executor,
                    self._score_single_match,
                    cv_data,
                    job
                )
            )

        scores = await asyncio.gather(*tasks)

        scored_jobs = [
            {**job, "match_score": score, "system_prompt": self._generate_custom_prompt(job)}
            for job, score in zip(jobs, scores)
        ]

        return sorted(scored_jobs, key=lambda x: x["match_score"], reverse=True)

    def _score_single_match(self, cv_data: Dict, job: Dict) -> float:
        """
        Score how well a single CV matches a job
        Returns a float between 0 and 1
        """
        system_prompt = self._generate_custom_prompt(job)

        # TODO: Use the system_prompt with your preferred LLM to generate the actual score
        # For now, returning a placeholder score
        return 0.5
