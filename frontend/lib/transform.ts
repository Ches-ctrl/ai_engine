// Define a type that represents nested objects and arrays
type NestedObject = {
    [key: string]: NestedValue;
};
type NestedValue = string | number | boolean | null | undefined | NestedObject | NestedValue[];

export function toSnakeCase(obj: NestedValue): NestedValue {
    if (Array.isArray(obj)) {
        return obj.map(item => toSnakeCase(item as NestedValue));
    }
    
    if (obj !== null && typeof obj === 'object') {
        const snakeObj: NestedObject = {};
        
        for (const [key, value] of Object.entries(obj)) {
            const snakeKey = key.replace(/[A-Z]/g, letter => `_${letter.toLowerCase()}`);
            snakeObj[snakeKey] = typeof value === 'object' ? toSnakeCase(value as NestedValue) : value;
        }
        
        return snakeObj;
    }
    
    return obj;
}

export function toCamelCase(obj: NestedValue): NestedValue {
    if (Array.isArray(obj)) {
        return obj.map(item => toCamelCase(item as NestedValue));
    }
    
    if (obj !== null && typeof obj === 'object') {
        const camelObj: NestedObject = {};
        
        for (const [key, value] of Object.entries(obj)) {
            const camelKey = key.replace(/_([a-z])/g, (_, letter) => letter.toUpperCase());
            camelObj[camelKey] = typeof value === 'object' ? toCamelCase(value as NestedValue) : value;
        }
        
        return camelObj;
    }
    
    return obj;
}