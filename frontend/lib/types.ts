import { z } from "zod";

// Response Schemas
export const ErrorDetailSchema = z.object({
    code: z.string(),
    message: z.string(),
    errorId: z.string().optional()
});

export const ApiResponseSchema = z.object({
    success: z.boolean(),
    data: z.record(z.string(), z.unknown()).optional(),
    error: ErrorDetailSchema.nullable(),
    metadata: z.record(z.string(), z.unknown()).nullable()
})

export type ErrorDetail = z.infer<typeof ErrorDetailSchema>
export type ApiResponse = z.infer<typeof ApiResponseSchema>