import { ref, nextTick } from 'vue'
import { fetchJSON } from '../useFetch'

export function useIntroductionTyping() {
	const displayLines = ref<string[]>([])

	const typingSpeed = 50
	const lineDelay = 500
	const lineBreakDelay = 300

	const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms))
	let scrollContainer: HTMLElement | null = null

	async function startTyping(isMobile: boolean) {
		displayLines.value = [] // 重置

		const data = await fetchJSON('json/about/about.json')
		const lines: string[] = data.introductionLines ?? []

		
		if (isMobile) {
			// mobile 
			scrollContainer = document.querySelector<HTMLElement>('.introduction-text-content')!
		} else {
			// desktop (待確認)
			// scrollContainer = document.querySelector<HTMLElement>('#introduction-animation')!
		}

		for (let i = 0; i < lines.length; i++) {
			const line = lines[i]!

			if (line === '\n') {
				displayLines.value.push('\n')
				if (i < lines.length - 1) await sleep(lineBreakDelay)
				continue
			}

			let current = ''
			displayLines.value.push(current)
			const index = displayLines.value.length - 1

			// desktop 滾動 - 1 (待確認)
			// const lastChild = scrollContainer.lastElementChild
			// if (lastChild) lastChild.scrollIntoView({ behavior: 'smooth' })

			for (const char of line) {
				current += char
				displayLines.value[index] = current

				// mobile 滾動
				if (isMobile && scrollContainer) {
					await nextTick()
					const lastChild = scrollContainer.lastElementChild
					if (lastChild) lastChild.scrollIntoView({ behavior: 'smooth' })
				}
				
				// desktop 滾動 - 2 (待確認)
				// const lastChild = scrollContainer.lastElementChild
				// if (lastChild) {
				// 	lastChild.scrollIntoView({ behavior: 'smooth' })
				// }

				await sleep(typingSpeed)
			}

			// 非最後一行才延遲
			if (i < lines.length - 1) await sleep(lineDelay)
		}
	}

	return { displayLines, startTyping }
}