<script setup lang="ts" name="CodeBlockTabs">
    import { ref, onMounted } from "vue";

	interface Method {
		method: string;
		description: string;
	}

	interface ThemeData {
		title: string;
		codePath: string;
		description: {
			node: {
				theme: string;
				description: string;
			};
			dataStructure: {
				theme: string;
				description: string;
				methods: Method[];
			};
		};
	}

	interface TabData {
		title: string;
		description: string;
		data: ThemeData[];
	}

	const props = defineProps<{
		jsonUrl: string;
	}>();

	const tabData = ref<TabData | null>(null);
	const error = ref("");
	const activeTab = ref(0);

	async function loadJSON(url: string) {
		const res = await fetch(url);
		return res.json();
	}

	function formatCode(text: string) {
		return text.replace(/`([^`]+)`/g, "<code>$1</code>");
	}

	function getLastWord(title: string) {
		return title.split(" ").slice(-1)[0];
	}

	onMounted(async () => {
		if (!props.jsonUrl) {
			error.value = "缺少 jsonUrl";
			return;
		}

		try {
			tabData.value = await loadJSON(props.jsonUrl);
		} catch (e) {
			error.value = "載入 JSON 失敗";
		}
	});
</script>

<template>
	<div>
		<p v-if="error" style="color:red;">{{ error }}</p>

		<template v-else>
			<section class="intro">
				<h1>{{ tabData?.title }}</h1>
				<p>{{ tabData?.description }}</p>
			</section>

			<!-- Tabs -->
			<ul class="nav nav-tabs">
				<li
					v-for="(theme, idx) in tabData?.data"
					:key="idx"
					class="nav-item"
				>
					<button
						class="nav-link"
						:class="{ active: activeTab === idx }"
						@click="activeTab = idx"
					>
						{{ getLastWord(theme.title) }}
					</button>
				</li>
			</ul>

			<!-- Content -->
			<div class="tab-content">
				<div
					v-for="(themeData, idx) in tabData?.data"
					:key="idx"
					class="tab-pane fade"
					:class="{ 'show active': activeTab === idx }"
				>
					<br />

					<section>
						<h2>{{ themeData.title }}</h2>

						<h4 v-html="formatCode(themeData.description.node.theme)" />
						<p v-html="formatCode(themeData.description.node.description)" />

						<h4 v-html="formatCode(themeData.description.dataStructure.theme)" />
						<p v-html="formatCode(themeData.description.dataStructure.description)" />

						<code-block :src="themeData.codePath"></code-block>

						<br />

						<div
							v-for="(method, mIdx) in themeData.description.dataStructure.methods"
							:key="mIdx"
						>
							<h5 v-html="formatCode(method.method)" />
							<p v-html="formatCode(method.description)" />
						</div>
					</section>
				</div>
			</div>
		</template>
	</div>
</template>

<style scoped>
	@import "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css";
</style>
