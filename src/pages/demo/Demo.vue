<script setup lang="ts" name="Demo">
    import ljjmk94ProfileCard from '@/assets/ljjmk94ProfileCardByExtricate.gif'
    import CodeBlockFileLoader from '@/components/codeBlock/CodeBlockFileLoader.vue'
    import CodeBlockMarkdownLoader from '@/components/codeBlock/CodeBlockMarkdownLoader.vue'
    import VideoPost from '@/components/post/VideoPost.vue'
    


</script>

<template>
    <main class="demo-main">
        <!-- <img :src="ljjmk94ProfileCard" alt="小闇！！" title="窩是隻卯咪！！ 嗷嗷嗷！！"> -->
        <VideoPost src="src/components/post/demo.json"/>
        <!-- 待調整 -->
        <!-- <CodeBlockFileLoader lang="Python" src="/code/helloWorld.py" />
        <CodeBlockMarkdownLoader src="/markdown/helloWorld/HelloWorld.md" /> -->
    </main>
</template>

<style scoped>

</style>