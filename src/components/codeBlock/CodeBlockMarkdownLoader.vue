<script setup lang="ts" name="CodeBlockMarkdownLoader">
	import { ref, onMounted, nextTick, computed } from 'vue'
	import hljs from 'highlight.js'
	// 主題
	import 'highlight.js/styles/github-dark.css'
	// 載入常用語言
	import 'highlight.js/lib/common'

	
	const props = defineProps<{
		lang?: string;  // 可以鎖定語言
		src: string;    // Markdown 檔案路徑
	}>()

	const code = ref('')
	const detectedLang = ref(props.lang || 'plaintext')
	const loading = ref(true)
	const error = ref('')

	async function loadCode() {
		try {
			const res = await fetch(props.src)
			if (!res.ok) throw new Error(`載入失敗：${props.src}`)
			const text = await res.text()

			// 正則解析 ```lang ... ``` 區塊
			const regex = /``` *(\w+)? *\r?\n([\s\S]*?)```/g
			let match: RegExpExecArray | null
			let found = false

			while ((match = regex.exec(text)) !== null) {
				const lang = match[1] || 'plaintext'
				const content = match[2]!

				// 如果有 props.lang，優先取對應語言
				if (!props.lang || props.lang === lang) {
					code.value = content.trimEnd()
					detectedLang.value = lang
					found = true
					break
				}
			}

			if (!found) {
				code.value = ''
				error.value = '找不到符合語言的程式碼區塊'
			}

		} catch (e) {
			error.value = String(e)
		} finally {
			loading.value = false
		}
	}

	const lines = computed(() => code.value.split('\n'))

	onMounted(async () => {
		await loadCode()
		await nextTick()
		const codeEls = document.querySelectorAll('.code-cell code')
		codeEls.forEach(el => hljs.highlightElement(el as HTMLElement))
	});

	let copyText = ref('Copy')
	let copyTimer: number | null = null

	function copyCode() {
		if (!code.value) return
		navigator.clipboard.writeText(code.value).then(() => {
			copyText.value = 'Copied!'
			// 清除舊的 timer，避免連點 bug
			if (copyTimer) clearTimeout(copyTimer)
			// 3 秒後恢復
			copyTimer = window.setTimeout(() => { copyText.value = 'Copy' }, 3000)
		})
	}
</script>

<template>
	<div class="editor" v-if="!loading && !error">
		<!-- 工具列 -->
		<div class="toolbar">
			<span class="dot red"></span>
			<span class="dot yellow"></span>
			<span class="dot green"></span>
			<span class="code-lang">{{ detectedLang }}</span>
			<button class="copy-btn" @click="copyCode">{{ copyText }}</button>
		</div>
		<!-- 程式碼區 Table 版 -->
		<div class="code-wrapper">
			<table class="code-table">
				<tbody>
					<tr v-for="(line, index) in lines" :key="index">
						<!-- 行號 -->
						<td class="gutter">{{ index + 1 }}</td>
						<!-- 程式碼 -->
						<td class="code-cell">
							<code :class="`language-${detectedLang}`" v-html="line || '&#8203;'"></code>
						</td>
					</tr>
					<tr>
						<td class="gutter"></td>
						<td class="code-cell">&#8203;</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
	<div v-else-if="loading">Loading…</div>
	<div v-else-if="error" style="color:red">{{ error }}</div>
</template>

<style scoped>
	.editor {
		background: #1e1e1e;
		border-radius: 10px;
		overflow: hidden;
		font-family: Menlo, Monaco, Consolas, monospace;
		font-size: 14px;
		margin: 10px;
	}

	/* 工具列 */
	.toolbar {
		display: flex;
		gap: 6px;
		padding: 8px 10px;
		background: #2c2c2c;
		align-items: center;
		position: relative;
	}

	.dot {
		width: 12px;
		height: 12px;
		border-radius: 50%;
	}
	.red { background: #ff5f56; }
	.yellow { background: #ffbd2e; }
	.green { background: #27c93f; }

	.code-lang {
		position: absolute;
		right: 80px; /* Copy 按鈕寬度 + margin */
		color: #c9d1d9;
		font-size: 12px;
		font-weight: bold;
	}

	.copy-btn {
		position: absolute;
		right: 10px;
		background: #21262d;
		color: #fff;
		border: none;
		padding: 2px 8px;
		border-radius: 4px;
		cursor: pointer;
	}
	.copy-btn:hover {
		background: #30363d;
	}

	.code-wrapper {
		overflow-x: auto;
		-webkit-overflow-scrolling: touch; /* 手機滑順滾動 */
	}

	/* Table 行號 + 程式碼 */
	.code-table {
		width: max-content;
		min-width: 100%;
		border-collapse: collapse;
		table-layout: auto;
	}

	.code-table tr {
		vertical-align: top;
	}

	.gutter {
		user-select: none;
		text-align: right;
		padding: 3px 10px;
		color: #6a737d;
		background: #2c2c2c;
		white-space: nowrap;
		box-sizing: border-box;
	}

	.code-cell {
		padding: 3px 10px;
		white-space: pre;
		color: #c9d1d9;
		font-family: Menlo, Monaco, Consolas, monospace;
		tab-size: 4;
		-moz-tab-size: 4;
		-webkit-tab-size: 4;
		word-break: break-all;
		width: 100%;
	}

	.code-cell code.hljs, pre.hljs {
		background-color: #1e1e1e;
		padding: 0;
		display: block; /* 確保 hljs block 正常顯示 */
	}
</style>