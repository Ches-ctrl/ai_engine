import { toCamelCase, toSnakeCase } from "./transform";
import { ApiResponse, ApiResponseSchema } from "./types";

const API_URL = new URL(process.env.NEXT_PUBLIC_API_URL as string);

export async function apiRequest(): Promise<ApiResponse> {
    console.log(API_URL)
    const endpoint = 'abc_route';

    try {
        const response = await fetch(`${API_URL}${endpoint}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            signal: AbortSignal.timeout(20000),
        })

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return ApiResponseSchema.parse(toCamelCase(data))
    } catch (error) {
        if (error instanceof Error) {
            console.error(`Failed to fetch abc_route: ${error.message}`);
        } else {
            console.error('An unknown error occurred while fetching abc_route');
        }
        throw error;
    }
}