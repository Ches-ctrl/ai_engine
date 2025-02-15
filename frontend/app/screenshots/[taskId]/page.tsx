'use client';

import { useEffect, useState } from 'react';
import Image from 'next/image';

interface Screenshot {
  step_name: string;
  step_status: string;
  timestamp: string;
  screenshot_url: string;
  step_id: string;
}

export default function TaskScreenshots({ params }: { params: { taskId: string } }) {
  const [screenshots, setScreenshots] = useState<Screenshot[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchScreenshots = async () => {
      try {
        const response = await fetch(`/api/tasks/${params.taskId}/screenshots`);
        if (!response.ok) throw new Error('Failed to fetch screenshots');

        const data = await response.json();
        setScreenshots(data.screenshots);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    fetchScreenshots();
  }, [params.taskId]);

  if (loading) return <div>Loading screenshots...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Task Screenshots</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {screenshots.map((screenshot, index) => (
          <div key={index} className="border rounded-lg p-4">
            <div className="mb-2">
              <h3 className="font-semibold">{screenshot.step_name}</h3>
              <p className="text-sm text-gray-600">
                Status: <span className={`font-medium ${
                  screenshot.step_status === 'completed' ? 'text-green-600' :
                  screenshot.step_status === 'failed' ? 'text-red-600' :
                  'text-yellow-600'
                }`}>{screenshot.step_status}</span>
              </p>
              <p className="text-sm text-gray-600">
                {new Date(screenshot.timestamp).toLocaleString()}
              </p>
            </div>
            <div className="relative h-[300px] w-full">
              <Image
                src={screenshot.screenshot_url}
                alt={`Step ${screenshot.step_name} screenshot`}
                fill
                className="object-contain"
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
