<script setup lang="ts" name="Demo">
    import ljjmk94ProfileCard from '@/assets/ljjmk94ProfileCardByExtricate.gif'
    import CodeBlockFileLoader from '@/components/codeBlock/CodeBlockFileLoader.vue'
    import CodeBlockMarkdownLoader from '@/components/codeBlock/CodeBlockMarkdownLoader.vue'
    import BlogGallery from '@/components/blog/BlogGallery.vue'
    import Sudoku from '@/components/Sudoku.vue'
</script>

<template>
    <main class="demo-main">
        <section class="introduction">
            <h1>Demo</h1>
        </section>
        <Sudoku />
        <!-- <BlogGallery /> -->
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