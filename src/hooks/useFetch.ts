export async function fetchJSON<T = any>(path: string): Promise<T> {
    const res = await fetch(`${import.meta.env.BASE_URL}${path}`)
    if (!res.ok) throw new Error(`Failed to fetch ${path}: ${res.status}`)
    return await res.json() as Promise<T>
}