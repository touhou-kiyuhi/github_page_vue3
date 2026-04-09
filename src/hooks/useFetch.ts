export async function fetchJSON(path: string) {
    const res = await fetch(`${import.meta.env.BASE_URL}${path}`)
    return await res.json()
}