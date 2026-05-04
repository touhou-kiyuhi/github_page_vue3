<script setup lang="ts" name="Demo">
    import ljjmk94ProfileCard from '@/assets/ljjmk94ProfileCardByExtricate.gif'
    import CodeBlockFileLoader from '@/components/codeBlock/CodeBlockFileLoader.vue'
    import CodeBlockMarkdownLoader from '@/components/codeBlock/CodeBlockMarkdownLoader.vue'

    import LoadingOverlay from '@/components/LoadingOverlay.vue'
    import { useLoading } from '@/hooks/useLoading'

    const { loading, show, hide } = useLoading()

    const submit = async () => {
        show()
        try {
            await fakeApi()
        } finally {
            hide()
        }
    }

    const fakeApi = () =>
        new Promise(resolve => setTimeout(resolve, 2000))
</script>

<template>
    <main class="demo-main">
        <section class="introduction">
            <h1>Demo</h1>
        </section>
        <button @click="submit">送出</button>

        <LoadingOverlay :visible="loading" />
        <!-- <img :src="ljjmk94ProfileCard" alt="小闇！！" title="窩是隻卯咪！！ 嗷嗷嗷！！"> -->
        <!-- 待調整 -->
        <!-- <CodeBlockFileLoader lang="Python" src="/code/helloWorld.py" />
        <CodeBlockMarkdownLoader src="/markdown/helloWorld/HelloWorld.md" /> -->
    </main>
</template>

<style scoped>
    .demo-main {
        flex: 1;
        padding: 20px;
    }

    .demo-main .introduction p {
        font-size: 18px;
    }
</style>